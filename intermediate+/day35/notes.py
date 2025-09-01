"""
API Keys, Authentication, Environment Variables and Sending SMS

Build a rain alert App

Used mailgun and email rather than Twillio

"""
import os
from dotenv import load_dotenv
import requests

load_dotenv("../../.env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
RECIPIENT = os.getenv("RECIPIENT")

latitude = "50.827778" 
longitude = "-0.152778"

# Google Weather APIs
current = "https://weather.googleapis.com/v1/currentConditions:lookup"
hourly = "https://weather.googleapis.com/v1/forecast/hours:lookup" # up to 240 hours
daily = "https://weather.googleapis.com/v1/forecast/days:lookup" # up to 10 days

current_parameters = {
    "key": GOOGLE_API_KEY,
    "location.latitude": latitude,
    "location.longitude": longitude
}

hourly_parameters = {
    "key": GOOGLE_API_KEY,
    "location.latitude": latitude,
    "location.longitude": longitude,
    "hours": "12"   
}

daily_parameters = {
    "key": GOOGLE_API_KEY,
    "location.latitude": latitude,
    "location.longitude": longitude,
    "days": "3"
}

response = requests.get(url=hourly, params=hourly_parameters)
response.raise_for_status()
forecast_hours = response.json()["forecastHours"]
# print(forecast_hours)

rain_probability = [hours["precipitation"]["probability"]["percent"] for hours in forecast_hours]
print(rain_probability)

if any(n > 25 for n in rain_probability):
    print("Umbrella needed")

    response = requests.post(
        f"https://api.eu.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": f"James <mailgun@{MAILGUN_DOMAIN}>",
            "to": [RECIPIENT],
            "subject": "Weather Alert",
            "text": "Don't forget your umbrella today! Rain probability is high."
        }
    )

    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
