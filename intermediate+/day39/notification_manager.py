from dotenv import load_dotenv
import os
import boto3

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
