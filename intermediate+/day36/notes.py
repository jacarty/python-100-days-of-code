"""
Stock News Monitoring Project

Skipped Twilio; will use AWS later

"""

from dotenv import load_dotenv
import os
import requests

###########################
# Read API Keys
###########################

load_dotenv("../../.env")
ALPHA_API_KEY = os.getenv("ALPHA_API_KEY")
NEWS_API = os.getenv("NEWS_API")

###########################
# Global Vars
###########################

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

###########################
# Get Stock Data & Trim
###########################

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHA_API_KEY
}

# Get API data
data = requests.get(url=ALPHA_URL, params=alpha_parameters)
# Check for error response
data.raise_for_status()
# Trim data for Daily information
tsla_stock_data = data.json()["Time Series (Daily)"]
print(tsla_stock_data)

# List comporehension to just get values by day
values = [value for (key, value) in tsla_stock_data.items()]
print(values)

# Trim to get the Closing prices as float
close = float(values[0]["4. close"])   # 333.87
previous_close = float(values[1]["4. close"])  # 345.98
percentage_change = ((close - previous_close) / previous_close) * 100

###########################
# Get News If Needed
# Return First 3 Articles
###########################

if abs(percentage_change) > 1: # If + or - 1%
    up_down = "🔺" if percentage_change > 0 else "🔻"
    print(f"Get News - Stock moved {percentage_change:+.1f}%")

    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API
    }

    news = requests.get(url=NEWS_URL, params=news_parameters)
    news.raise_for_status()
    news_articles = news.json()["articles"][:3]
    print(news_articles)

formatted_articles = [f"""Headline: {article['title'][:50]}{'...' if len(article['title']) > 50 else ''}
                      \nLink: {article['url']}""" 
                      for article in news_articles]
print(formatted_articles)

###########################
# Send SMS Message with AWS
###########################

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')
AWS_SENDER_ID= os.getenv('AWS_SENDER_ID')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')

# Create SNS client
sns = boto3.client(
    'sns',
    region_name=AWS_DEFAULT_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Create concise SMS message
sms_message = f"{STOCK}: {up_down}{percentage_change}%\n\n" + "\n---\n".join(formatted_articles[:3])

# Send SMS
response = sns.publish(
    PhoneNumber=PHONE_NUMBER,
    MessageAttributes={
        'AWS.SNS.SMS.SenderID': {
            'DataType': 'String',
            'StringValue': AWS_SENDER_ID
        },
        'AWS.SNS.SMS.SMSType': {
            'DataType': 'String',
            'StringValue': 'Transactional'
        }
    },
    Message=sms_message
)

print(f"Message sent! MessageId: {response['MessageId']}")
