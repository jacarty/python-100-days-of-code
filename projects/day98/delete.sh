#!/bin/bash

# Load environment variables from .env file
if [ -f ../../.env ]; then
    export $(cat ../../.env | grep -v '^#' | xargs)
else
    echo "Error: .env file not found"
    exit 1
fi

if [ -z "$AWS_DEFAULT_REGION" ]; then
    echo "Error: AWS_DEFAULT_REGION not found in .env file"
    exit 1
fi

# Configuration
LAMBDA_FUNCTION_NAME="stock-price-tracker"
LAMBDA_ROLE_NAME="stock-tracker-lambda-role"
SECRET_NAME="stock-tracker/secrets"
SSM_PARAM_NAME="/stock-tracker/targets"
CLOUDWATCH_RULE_NAME="stock-tracker-schedule"
POLICY_NAME="stock-tracker-policy"

echo "================================================"
echo "Cleaning up Stock Price Tracker from AWS"
echo "================================================"
echo ""
echo "This will delete:"
echo "  - Lambda Function: $LAMBDA_FUNCTION_NAME"
echo "  - CloudWatch Rule: $CLOUDWATCH_RULE_NAME"
echo "  - Secret: $SECRET_NAME"
echo "  - SSM Parameter: $SSM_PARAM_NAME"
echo "  - IAM Role: $LAMBDA_ROLE_NAME"
echo "  - IAM Policy: $POLICY_NAME"
echo ""
read -p "Are you sure you want to continue? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "Cleanup cancelled."
    exit 0
fi

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Step 1: Remove CloudWatch Events target
echo ""
echo "Step 1: Removing CloudWatch Events target..."
aws events remove-targets \
    --rule $CLOUDWATCH_RULE_NAME \
    --ids "1" \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "Target already removed or doesn't exist"

# Step 2: Delete CloudWatch Events rule
echo "Step 2: Deleting CloudWatch Events rule..."
aws events delete-rule \
    --name $CLOUDWATCH_RULE_NAME \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "Rule already deleted or doesn't exist"

# Step 3: Remove Lambda permission
echo "Step 3: Removing Lambda permission..."
aws lambda remove-permission \
    --function-name $LAMBDA_FUNCTION_NAME \
    --statement-id stock-tracker-event \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "Permission already removed or doesn't exist"

# Step 4: Delete Lambda function
echo "Step 4: Deleting Lambda function..."
aws lambda delete-function \
    --function-name $LAMBDA_FUNCTION_NAME \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "Lambda function already deleted or doesn't exist"

# Step 5: Delete secret from Secrets Manager
echo "Step 5: Deleting secret from Secrets Manager..."
aws secretsmanager delete-secret \
    --secret-id $SECRET_NAME \
    --force-delete-without-recovery \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "Secret already deleted or doesn't exist"

# Step 6: Delete SSM parameter
echo "Step 6: Deleting SSM parameter..."
aws ssm delete-parameter \
    --name $SSM_PARAM_NAME \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "SSM parameter already deleted or doesn't exist"

# Step 7: Detach policies from IAM role
echo "Step 7: Detaching policies from IAM role..."

# Detach AWS managed policy
aws iam detach-role-policy \
    --role-name $LAMBDA_ROLE_NAME \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "AWS managed policy already detached or doesn't exist"

# Detach custom policy
POLICY_ARN="arn:aws:iam::${ACCOUNT_ID}:policy/${POLICY_NAME}"
aws iam detach-role-policy \
    --role-name $LAMBDA_ROLE_NAME \
    --policy-arn $POLICY_ARN \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "Custom policy already detached or doesn't exist"

# Step 8: Delete IAM role
echo "Step 8: Deleting IAM role..."
aws iam delete-role \
    --role-name $LAMBDA_ROLE_NAME \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "IAM role already deleted or doesn't exist"

# Step 9: Delete custom IAM policy
echo "Step 9: Deleting custom IAM policy..."
aws iam delete-policy \
    --policy-arn $POLICY_ARN \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "IAM policy already deleted or doesn't exist"

# Step 10: Clean up local files
echo "Step 10: Cleaning up local files..."
rm -f lambda-function.zip output.json

echo ""
echo "================================================"
echo "✅ Cleanup complete!"
echo "================================================"
echo ""
echo "All resources have been deleted."
echo ""
echo "Note: Secrets in Secrets Manager are permanently deleted."
echo "If you need to restore, you'll need to recreate everything."