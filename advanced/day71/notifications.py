from dotenv import load_dotenv
import os
import boto3
import requests

class NotificationManager:
    ###########################
    # Send SMS Message with AWS
    ###########################
    
    def __init__(self):
        load_dotenv("../../.env")
        self.AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
        self.AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')
        self.AWS_SENDER_ID= os.getenv('AWS_SENDER_ID')
        self.PHONE_NUMBER = os.getenv('PHONE_NUMBER')
        self.MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN')
        self.MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
        self.RECIPIENT = os.getenv('RECIPIENT')

    def send_sms(self, message):
        """Send SMS via AWS SNS"""      
        # Create SNS client
        sns = boto3.client(
            'sns',
            region_name=self.AWS_DEFAULT_REGION,
            aws_access_key_id=self.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY
        )

        # Create concise SMS message
        sms_message = f"{message}"

        # Send SMS
        response = sns.publish(
            PhoneNumber=self.PHONE_NUMBER,
            MessageAttributes={
                'AWS.SNS.SMS.SenderID': {
                    'DataType': 'String',
                    'StringValue': self.AWS_SENDER_ID
                },
                'AWS.SNS.SMS.SMSType': {
                    'DataType': 'String',
                    'StringValue': 'Transactional'
                }
            },
            Message=sms_message
        )

        return f"Message sent! MessageId: {response['MessageId']}"

    def send_email(self, name, email, phone, message):
        """Send Email via Mailgun"""
            
        email = requests.post(
            f"https://api.eu.mailgun.net/v3/{self.MAILGUN_DOMAIN}/messages",
            auth=("api", self.MAILGUN_API_KEY),
            data={
                "from": f"James <mailgun@{self.MAILGUN_DOMAIN}>",
                "to": [self.RECIPIENT],
                "subject": f"Contact from: {name}",
                "text": f"""
                {name}
                {email}
                {phone}
                {message}
                """
            }
        )

        if email.status_code == 200:
            return f"Email sent successfully!"
        else:
            return f"Error: {email.status_code}"
