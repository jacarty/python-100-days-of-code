"""
INTERMEDIATE+ NOTES CONSOLIDATION
Contains all notes from intermediate+ section (Days 32-58)
"""

##############################################################################
# DAY 32 - SMTP and Datetime module
##############################################################################

"""
STMP and Datetime module
"""

###############
# Sending email
###############

import smtplib

email_add = "test@test.com"
password = "pass"

with smtplib.SMTP("smtp.live.com") as connection:
    connection.starttls()
    connection.login(user=email_add, password=password)
    connection.sendmail(
        from_addr=email_add, 
        to_addrs="test2@test.com",
        msg="Subject:Hello\n\nThis is the email body."
    )

###############
# Date and Time
###############

import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)

month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year= 2000, month= 1, day= 1)

"""
Monday motivational email
"""

import datetime as dt
import random
import smtplib

EMAIL_ADDR = "test@test.com"
EMAIL_PASS = "pass"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("./quotes.txt") as file:
        list_of_quotes = file.readlines()
        random_quote = random.choice(list_of_quotes)

    print(random_quote)

    with smtplib.SMTP("smtp.live.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDR, password=EMAIL_PASS)
        connection.sendmail(
            from_addr=EMAIL_ADDR, 
            to_addrs=EMAIL_ADDR,
            msg=f"Subject:Happy Monday!\n\n{random_quote}"
        )

"""
Birthday Email
"""

#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


##############################################################################
# DAY 33 - API Endpoints
##############################################################################

"""
API Endpoints

The projects is to build an ISS Tracker

An Application Programming Interface is a set of commands, functions, protocols, and objects
that programmers can use to create software or interact with external systems.

                API Request
Your Program ---------------> External System                      
            <----------------
                API Response
                
"""


##########################################################
#
# ISS Location API
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
#
##########################################################

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
# returns <Response [200]>

########################################################################################
# There are five classes defined by the standard:
#    1xx informational response – the request was received, continuing process
#    2xx successful – the request was successfully received, understood, and accepted
#    3xx redirection – further action needs to be taken in order to complete the request
#    4xx client error – the request contains bad syntax or cannot be fulfilled
#    5xx server error – the server failed to fulfil an apparently valid request
########################################################################################

print(response.status_code)
# returns 200

print(response.json())
# returns the JSON reponse

print(response.raise_for_status())
# will tell you the status code returned (for error handling)

######################################################
# Return ISS location
# 
# https://www.latlong.net/Show-Latitude-Longitude.html
#
######################################################

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_location = (longitude, latitude)
print(iss_location)

################################
# Sunrise & Sunset for Location
# https://sunrise-sunset.org/api
################################

import requests
from datetime import datetime

# London
#LAT = 51.507351
#LNG = -0.127758

# Hove 
LAT = 50.827930
LNG = -0.168749

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hour = sunrise.split("T")[1].split(":")[0]
print(sunrise_hour)
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunset_hour)

time_now = datetime.now()
hour_now = time_now.hour
print(hour_now)


######################################
# Check if ISS overhead and dark
######################################

import requests
from datetime import datetime

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    print(sunrise)
    print(sunset)
    print(hour_now)

    if not sunrise < hour_now < sunset:
        return True

if is_iss_overhead and is_night:
    print("ISS is overhead and you can see it")


##############################################
# Instructor
#
# Check every 60 sec if ISS overhead and dark
#
# Email you
##############################################

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )


##############################################################################
# DAY 34 - Trivia API and GUI Quiz App
##############################################################################

"""
Trivia API and The Quizzler App

"""

##################################################
# HTML Entities
# https://www.w3schools.com/html/html_entities.asp
##################################################

import html

text = html.unescape("Q.1: Valve&#039;s &quot;Portal&quot; and &quot;Half-Life&quot; " \
                    "franchises exist within the same in-game universe.")
print(text)

# Q.1: Valve&#039;s &quot;Portal&quot; and &quot;Half-Life&quot; franchises exist within the same in-game universe. (True/False): 
# Q.1: Valve's "Portal" and "Half-Life" franchises exist within the same in-game universe.

###################
# Type Hints
###################

# sets what the input type should be, and also what the returned data type will be

def greeting(name: str) -> str:
    return 'Hello ' + name


###########################
# Quiz Game Updates
#
# Uses API to get questions
#
# Has GUI to display quiz
#
# Read UI.py 
# Read Data.py
# Read Quiz_Brain.py
###########################


##############################################################################
# DAY 35 - API Keys, Authentication, Environment Variables and SMS
##############################################################################

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


##############################################################################
# DAY 36 - Stock Trading News Alert
##############################################################################

"""
Stock News Monitoring Project

Skipped Twilio; will use AWS later

"""

from dotenv import load_dotenv
import os
import requests
import boto3

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


##############################################################################
# DAY 37 - Advanced Authentication with POST/PUT/DELETE
##############################################################################

"""
Advanced Authentication and POST / PUT / DELETE Requests

Build a Habit Tracker with Pixela
"""

import requests

# requests.get() - Fetching/Reading data
"""
     CLIENT                    SERVER
        │                         │
        │  GET /api/users ────────>
        │                         │
        │<──────── 200 OK         │
        │   [{"id":1,"name":..}]  │
        │                         │
    📥 GETTING                 📚 DATA
"""

# requests.post() - Creating new data
"""
     CLIENT                    SERVER
        │                         │
        │  POST /api/users ──────>
        │  {"name":"John"}        │
        │                         │
        │<──────── 201 Created    │
        │   {"id":2,"name":"John"}│
        │                         │
    📤 SENDING                 ➕ CREATING
"""

# requests.put() - Updating/Replacing data
"""
     CLIENT                    SERVER
        │                         │
        │  PUT /api/users/2 ─────>
        │  {"name":"Jane"}        │
        │                         │
        │<──────── 200 OK         │
        │   {"id":2,"name":"Jane"}│
        │                         │
    ✏️ UPDATING               🔄 REPLACING
"""

# requests.delete() - Removing data
"""
     CLIENT                    SERVER
        │                         │
        │  DELETE /api/users/2 ──>
        │                         │
        │<──────── 204 No Content │
        │                         │
        │                         │
    🗑️ DELETING               ❌ REMOVED
"""

import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv("../../.env")
PIXELA_API = os.getenv("PIXELA_API")
USERNAME = "j1m"
GRAPH_ID = "g1"

#####################
# Create User
#####################

# user endpoint
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_API, 
    "username": USERNAME, 
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#####################
# Create Graph
#####################

# graph endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# send token in header
headers = {
    "X-USER-TOKEN": PIXELA_API
}

# new graph config
graph_config = {
    "id": GRAPH_ID,
    "name": "Pages Read",
    "unit": "Pages",
    "type": "int",
    "color": "sora"
}

# response = requests.post(headers=headers, url=graph_endpoint, json=graph_config)
# print(response.text)

# result
# https://pixe.la/v1/users/j1m/graphs/g1.html

#####################
# Post Pixel
#####################

# Get todays date
today = datetime.now()
# Format date with strftime
today_formatted = today.strftime("%Y%m%d")

pixel_create_url = f"{graph_endpoint}/{GRAPH_ID}"

# new graph config
post_pixel = {
    "id": GRAPH_ID,
    "date": today_formatted,
    "quantity": "5"
}

# response = requests.post(headers=headers, url=pixel_create_url, json=post_pixel)
# print(response.text)

#####################
# Update Pixel
#####################

DATE = "20250904"
pixel_update_url = f"{graph_endpoint}/{GRAPH_ID}/{DATE}"

# new graph config
update_pixel = {
    "quantity": "25"
}

# response = requests.put(headers=headers, url=pixel_update_url, json=update_pixel)
# print(response.text)

#####################
# Delete Pixel
#####################

DATE = "20250904"
pixel_update_url = f"{graph_endpoint}/{GRAPH_ID}/{DATE}"

# response = requests.delete(headers=headers, url=pixel_update_url, json=update_pixel)
# print(response.text)


#####################
# Delete User
#####################

# user endpoint
pixela_endpoint = f"https://pixe.la/v1/users/{USERNAME}"

user_params = {
    "token": PIXELA_API,
}

response = requests.delete(url=pixela_endpoint, json=user_params)
print(response.text)


##############################################################################
# DAY 38 - Exercise Tracking with Python
##############################################################################

"""
Exercise energy tracking with Python

I didnt want to sign up to Sheetly and provide access to Google
"""

######################
# Imports
######################

from dotenv import load_dotenv
import os
import requests

######################
# Load local ENVs
######################

load_dotenv("../../.env")
NUTRITIONIX_APP_ID= os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY= os.getenv("NUTRITIONIX_API_KEY")

######################
# URLs
######################

exercise_api = "https://trackapi.nutritionix.com/v2/natural/exercise"

######################
# Exercise Auth Header
######################

exercise_headers = {
    "x-app-id": NUTRITIONIX_APP_ID, 
    "x-app-key": NUTRITIONIX_API_KEY
}

######################
# Exercise Query
######################

exercise_query = str(input("What exercise did you do?: "))
weight = int(input("What is your weight in kg?: "))
height = float(input("What is your height in cm?: "))
age= str(input("How old are you?: "))

exercise_params = {
    "query": exercise_query,
    "gender": "male",
	"weight_kg": weight,
	"height_cm": height,
    "age": age	
}

response = requests.post(headers=exercise_headers, url=exercise_api, json=exercise_params)
result = response.json()
print(result)