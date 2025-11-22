from dotenv import load_dotenv
import os
import requests

class NotificationManager:

    def __init__(self):
        load_dotenv("../../.env")
        self.MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN')
        self.MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
        self.RECIPIENT = os.getenv('RECIPIENT')

    def send_email(self, name, email, phone, subject, message):
        """Send Email via Mailgun"""
            
        email = requests.post(
            f"https://api.eu.mailgun.net/v3/{self.MAILGUN_DOMAIN}/messages",
            auth=("api", self.MAILGUN_API_KEY),
            data={
                "from": f"James <mailgun@{self.MAILGUN_DOMAIN}>",
                "to": [self.RECIPIENT],
                "subject": f"{subject}",
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
