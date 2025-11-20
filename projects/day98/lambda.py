"""
The Lambda Code that will run in AWS
It polls Finnhub to get prices
It will SMS if a price goes below/above the targets
"""

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
            send_alert(alerts, phone_number)
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

def send_alert(alerts, phone_number):
    """Send SMS alert via SNS"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"🚨 Stock Alert - {timestamp}\n\n" + "\n".join(alerts)
    
    sns.publish(
        PhoneNumber=phone_number,
        Message=message
    )
    print(f"Alert sent: {message}")