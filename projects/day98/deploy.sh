#!/bin/bash

# Load environment variables from .env file
if [ -f ../../.env ]; then
    export $(cat ../../.env | grep -v '^#' | xargs)
else
    echo "Error: .env file not found"
    exit 1
fi

# Check for required env variables
if [ -z "$FINNHUB_API_KEY" ]; then
    echo "Error: FINNHUB_API_KEY not found in .env file"
    exit 1
fi

if [ -z "$PHONE_NUMBER" ]; then
    echo "Error: PHONE_NUMBER not found in .env file"
    exit 1
fi

if [ -z "$AWS_DEFAULT_REGION" ]; then
    echo "Error: AWS_DEFAULT_REGION not found in .env file"
    exit 1
fi

if [ -z "$AWS_SENDER_ID" ]; then
    echo "Error: AWS_SENDER_ID not found in .env file"
    exit 1
fi

# Configuration
LAMBDA_FUNCTION_NAME="stock-price-tracker"
LAMBDA_ROLE_NAME="stock-tracker-lambda-role"
SECRET_NAME="stock-tracker/secrets"
SSM_PARAM_NAME="/stock-tracker/targets"
CLOUDWATCH_RULE_NAME="stock-tracker-schedule"

echo "================================================"
echo "Setting up Stock Price Tracker on AWS"
echo "Using Finnhub API"
echo "================================================"

# Step 1: Create IAM role for Lambda
echo "Step 1: Creating IAM role for Lambda..."

TRUST_POLICY='{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'

aws iam create-role \
    --role-name $LAMBDA_ROLE_NAME \
    --assume-role-policy-document "$TRUST_POLICY" \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "Role already exists, continuing..."

# Attach basic Lambda execution policy
aws iam attach-role-policy \
    --role-name $LAMBDA_ROLE_NAME \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole \
    --region $AWS_DEFAULT_REGION

# Step 2: Create custom policy for Lambda
echo "Step 2: Creating custom IAM policy..."

LAMBDA_POLICY='{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "arn:aws:secretsmanager:'$AWS_DEFAULT_REGION':*:secret:'$SECRET_NAME'-*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:GetParameter"
      ],
      "Resource": "arn:aws:ssm:'$AWS_DEFAULT_REGION':*:parameter'$SSM_PARAM_NAME'"
    },
    {
      "Effect": "Allow",
      "Action": [
        "sns:Publish"
      ],
      "Resource": "*"
    }
  ]
}'

POLICY_ARN=$(aws iam create-policy \
    --policy-name stock-tracker-policy \
    --policy-document "$LAMBDA_POLICY" \
    --region $AWS_DEFAULT_REGION \
    --query 'Policy.Arn' \
    --output text 2>/dev/null)

if [ -z "$POLICY_ARN" ]; then
    # Policy already exists, get its ARN
    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    POLICY_ARN="arn:aws:iam::${ACCOUNT_ID}:policy/stock-tracker-policy"
fi

aws iam attach-role-policy \
    --role-name $LAMBDA_ROLE_NAME \
    --policy-arn $POLICY_ARN \
    --region $AWS_DEFAULT_REGION

# Also attach SNS Full Access
aws iam attach-role-policy \
    --role-name $LAMBDA_ROLE_NAME \
    --policy-arn arn:aws:iam::aws:policy/AmazonSNSFullAccess \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "SNS policy already attached"

echo "Waiting 10 seconds for IAM role to propagate..."
sleep 10

# Step 3: Store secrets in Secrets Manager
echo "Step 3: Storing secrets in AWS Secrets Manager..."

SECRET_VALUE='{
  "finnhub_api_key": "'$FINNHUB_API_KEY'",
  "phone_number": "'$PHONE_NUMBER'",
  "sender_id": "'$AWS_SENDER_ID'"
}'

aws secretsmanager create-secret \
    --name $SECRET_NAME \
    --secret-string "$SECRET_VALUE" \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || \
aws secretsmanager update-secret \
    --secret-id $SECRET_NAME \
    --secret-string "$SECRET_VALUE" \
    --region $AWS_DEFAULT_REGION

# Step 4: Store price targets in SSM Parameter Store
echo "Step 4: Storing price targets in SSM Parameter Store..."

TARGETS='{
  "AAPL": {"target_low": 150, "target_high": 200},
  "TSLA": {"target_low": 200, "target_high": 300},
  "GOOGL": {"target_low": 100, "target_high": 150}
}'

aws ssm put-parameter \
    --name $SSM_PARAM_NAME \
    --value "$TARGETS" \
    --type String \
    --region $AWS_DEFAULT_REGION \
    --overwrite

# Step 5: Create Lambda deployment package
echo "Step 5: Creating Lambda deployment package..."

mkdir -p lambda-package
cat > lambda-package/lambda_function.py << 'EOF'
import boto3
import json
import urllib3
from datetime import datetime

ssm = boto3.client('ssm')
secrets = boto3.client('secretsmanager')
sns = boto3.client('sns')
http = urllib3.PoolManager()

def lambda_handler(event, context):
    try:
        # Get secrets from Secrets Manager
        secret_data = get_secret('stock-tracker/secrets')
        api_key = secret_data['finnhub_api_key']
        phone_number = secret_data['phone_number']
        sender_id = secret_data.get('sender_id', 'StockAlert')
        
        # Get price targets from SSM
        targets = json.loads(
            ssm.get_parameter(Name='/stock-tracker/targets')['Parameter']['Value']
        )
        
        alerts = []
        
        # Check each stock
        for symbol, thresholds in targets.items():
            try:
                current_price = get_stock_price(symbol, api_key)
                
                if current_price <= thresholds['target_low']:
                    alerts.append(f"{symbol}: ${current_price:.2f} ≤ ${thresholds['target_low']:.2f} (LOW)")
                elif current_price >= thresholds['target_high']:
                    alerts.append(f"{symbol}: ${current_price:.2f} ≥ ${thresholds['target_high']:.2f} (HIGH)")
                else:
                    print(f"{symbol}: ${current_price:.2f} (within range)")
                    
            except Exception as e:
                print(f"Error checking {symbol}: {str(e)}")
        
        # Send alert if any triggers
        if alerts:
            send_alert(alerts, phone_number, sender_id)
        else:
            print("No alerts triggered")
            
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Checked {len(targets)} stocks, {len(alerts)} alerts sent',
                'alerts': alerts
            })
        }
        
    except Exception as e:
        print(f"Error in lambda_handler: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def get_secret(secret_name):
    """Retrieve secret from AWS Secrets Manager"""
    response = secrets.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

def get_stock_price(symbol, api_key):
    """Fetch current stock price from Finnhub"""
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
    
    response = http.request('GET', url)
    data = json.loads(response.data.decode('utf-8'))
    
    # Finnhub returns 'c' for current price
    if 'c' not in data or data['c'] == 0:
        raise ValueError(f"Invalid response for {symbol}: {data}")
    
    return float(data['c'])

def send_alert(alerts, phone_number, sender_id):
    """Send SMS alert via SNS with message attributes"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"🚨 Stock Alert - {timestamp}\n\n" + "\n".join(alerts)
    
    # Send with MessageAttributes for better delivery
    response = sns.publish(
        PhoneNumber=phone_number,
        Message=message,
        MessageAttributes={
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': sender_id
            },
            'AWS.SNS.SMS.SMSType': {
                'DataType': 'String',
                'StringValue': 'Transactional'
            }
        }
    )
    print(f"Alert sent: {message}")
    print(f"SNS Response: MessageId={response['MessageId']}")
EOF

# Create deployment package
cd lambda-package
zip -q ../lambda-function.zip lambda_function.py
cd ..
rm -rf lambda-package

# Step 6: Create Lambda function
echo "Step 6: Creating Lambda function..."

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ROLE_ARN="arn:aws:iam::${ACCOUNT_ID}:role/${LAMBDA_ROLE_NAME}"

aws lambda create-function \
    --function-name $LAMBDA_FUNCTION_NAME \
    --runtime python3.12 \
    --role $ROLE_ARN \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://lambda-function.zip \
    --timeout 30 \
    --memory-size 128 \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || \
aws lambda update-function-code \
    --function-name $LAMBDA_FUNCTION_NAME \
    --zip-file fileb://lambda-function.zip \
    --region $AWS_DEFAULT_REGION

echo "Setting CloudWatch Logs retention..."
aws logs put-retention-policy \
    --log-group-name /aws/lambda/$LAMBDA_FUNCTION_NAME \
    --retention-in-days 7 \
    --region $AWS_DEFAULT_REGION

# Step 7: Create CloudWatch Events rule (runs every 30 minutes)
echo "Step 7: Creating CloudWatch Events rule..."

aws events put-rule \
    --name $CLOUDWATCH_RULE_NAME \
    --schedule-expression 'rate(30 minutes)' \
    --region $AWS_DEFAULT_REGION

# Get Lambda ARN
LAMBDA_ARN=$(aws lambda get-function \
    --function-name $LAMBDA_FUNCTION_NAME \
    --region $AWS_DEFAULT_REGION \
    --query 'Configuration.FunctionArn' \
    --output text)

# Add Lambda as target
aws events put-targets \
    --rule $CLOUDWATCH_RULE_NAME \
    --targets "Id"="1","Arn"="$LAMBDA_ARN" \
    --region $AWS_DEFAULT_REGION

# Add permission for CloudWatch to invoke Lambda
aws lambda add-permission \
    --function-name $LAMBDA_FUNCTION_NAME \
    --statement-id stock-tracker-event \
    --action 'lambda:InvokeFunction' \
    --principal events.amazonaws.com \
    --source-arn "arn:aws:events:${AWS_DEFAULT_REGION}:${ACCOUNT_ID}:rule/${CLOUDWATCH_RULE_NAME}" \
    --region $AWS_DEFAULT_REGION \
    2>/dev/null || echo "Permission already exists"

# Cleanup
rm lambda-function.zip

echo "================================================"
echo "✅ Setup complete!"
echo "================================================"
echo ""
echo "Resources created:"
echo "  - IAM Role: $LAMBDA_ROLE_NAME"
echo "  - Secret: $SECRET_NAME (includes sender_id)"
echo "  - SSM Parameter: $SSM_PARAM_NAME"
echo "  - Lambda Function: $LAMBDA_FUNCTION_NAME"
echo "  - CloudWatch Rule: $CLOUDWATCH_RULE_NAME (every 30 min)"
echo ""
echo "Your stock tracker is now active! 🚀"
echo ""
echo "Finnhub API limits: 60 calls/minute (free tier)"
echo ""
echo "To update price targets, run:"
echo "  aws ssm put-parameter --name $SSM_PARAM_NAME --value '{...}' --overwrite --region $AWS_DEFAULT_REGION"
echo ""
echo "To test manually:"
echo "  aws lambda invoke --function-name $LAMBDA_FUNCTION_NAME --region $AWS_DEFAULT_REGION output.json && cat output.json"
echo ""
echo "To view logs:"
echo "  aws logs tail /aws/lambda/$LAMBDA_FUNCTION_NAME --follow --region $AWS_DEFAULT_REGION"