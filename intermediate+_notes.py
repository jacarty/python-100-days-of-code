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

##############################################################################
# DAY 39 - Flight Deal Finder Part 1
##############################################################################

"""
Flight tracker part one

Handy JSON tool https://jsonformatter.curiousconcept.com/#

Lots more code in Classes
"""

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

############################
# Create Instances
############################
data_manager = DataManager()
flight_search = FlightSearch()
notifications = NotificationManager()

############################
# Update CSV with Iata Codes
############################
city_code = data_manager.read_cities()
print(f"Searching the following: {city_code}")
# for city in cities:
#     iata_code = flight_search.iata_search(city)
#     print(iata_code)
#     data_manager.update_iata_code(city, iata_code)

############################
# Search Flights
############################

cheap_flights_found = []

for city in city_code:
    origin = "LON"
    destination = city
    today = datetime.now()
    tomorrow = today + timedelta(weeks=1)
    six_months = today + timedelta(weeks=4)

    flights = flight_search.flight_search(origin, destination, tomorrow, six_months)
    # print(flights)
    cheap_flight = data_manager.cheaper_flight(city, flights)

    if cheap_flight and cheap_flight not in ["No flights found", "No cheaper flights found", False]:
        cheap_flights_found.append(f"{city}: {cheap_flight}")
        print(f"Found cheap flight to {city}")
        # print(cheap_flight)
    else:
        print(f"No cheap flights to {city}")

############################
# Send SMS
############################
if cheap_flights_found:
    message = "Low price alerts!\n" + "\n".join(cheap_flights_found)
    sms = notifications.send_sms(message)
    print(f"SMS sent with {len(cheap_flights_found)} flight deals")
else:
    print("No cheap flights found for any destination")


##############################################################################
# DAY 40 - Flight Deal Finder Part 2
##############################################################################

"""
Flight tracker part two

Handy JSON tool https://jsonformatter.curiousconcept.com/#
"""

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from users import UserManagement

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

############################
# Create Instances
############################
data_manager = DataManager()
flight_search = FlightSearch()
notifications = NotificationManager()
user = UserManagement()

############################
# Check / Create User
############################
while True:
    new_user = input("Do you want to create a New User? Y or N: ").lower()
    
    if new_user == "y":
        user.signup_user()
        break
    elif new_user == "n":
        print("Skipping user creation")
        break
    else:
        print("Please try again. Enter Y or N")

############################
# Update CSV with Iata Codes
############################
city_code = data_manager.read_cities()
print(f"Searching the following: {city_code}")
for city in city_code:
    iata_code = flight_search.iata_search(city)
    print(iata_code)
    data_manager.update_iata_code(city, iata_code)

############################
# Search Flights
############################

cheap_flights_found = []

for city in city_code:
    origin = "LON"
    destination = city
    today = datetime.now()
    tomorrow = today + timedelta(weeks=1)
    six_months = today + timedelta(weeks=4)

    flights = flight_search.flight_search(origin, destination, tomorrow, six_months)
    # print(flights)
    cheap_flight = data_manager.cheaper_flight(city, flights)

    if cheap_flight == "No flights found":
        # Try indirect flights
        print(f"No direct flights to {city}, trying indirect...")
        flights = flight_search.flight_search(origin, destination, tomorrow, six_months, non_stop=False)
        cheap_flight = data_manager.cheaper_flight(city, flights)
        
        if cheap_flight and cheap_flight not in ["No flights found", "No cheaper flights found", False]:
            cheap_flights_found.append(f"{city} (indirect): {cheap_flight}")
            print(f"Found indirect cheap flight to {city}")
        else:
            print(f"No indirect flights to {city} either")
            
    elif cheap_flight == "No cheaper flights found":
        print(f"No cheap flights to {city}")
        
    elif cheap_flight and cheap_flight not in [False, "City code not found"]:
        cheap_flights_found.append(f"{city} (direct): {cheap_flight}")
        print(f"Found direct cheap flight to {city}")
        

############################
# Send SMS
############################
if cheap_flights_found:
    message = "Low price alerts!\n" + "\n".join(cheap_flights_found)
    sms = notifications.send_sms(message)
    print(f"SMS sent with {len(cheap_flights_found)} flight deals")
else:
    print("No cheap flights found for any destination")

############################
# Send Email To Mailing List
############################

emails = user.return_emails()

if cheap_flights_found:
    message = "Low price alerts!\n" + "\n".join(cheap_flights_found)
    for subscriber in emails:
        notifications.send_email(subscriber, message)
        print(f"Email sent with {len(cheap_flights_found)} flight deals")
else:
    print("No cheap flights found for any destination")


##############################################################################
# DAY 41 - Introduction to HTML
##############################################################################

"""
Websites - HTML, CSS and JavaScript

HTML = Structure
CSS = Sytle
JavaScript = Functionaility/Behaviour


🔧 1. Basic HTML Structure Tags
Tag 	Description 	Example
<html> 	Root of the HTML document 	<html> ... </html>
<head> 	Metadata container 	<head> ... </head>
<body> 	Main document content 	<body> ... </body>
<title> 	Page title (in browser tab) 	<title>My Page</title>
<!DOCTYPE> 	Declares document type 	<!DOCTYPE html>

📝 2. Text Formatting Tags
Tag 	Description 	Example
<p> 	Paragraph 	<p>This is a paragraph.</p>
<br> 	Line break 	Hello<br>World
<hr> 	Horizontal line 	<hr>
<h1> to <h6> 	Headings 	<h1>Heading 1</h1>
<strong> 	Bold (semantic) 	<strong>Important</strong>
<b> 	Bold (visual only) 	<b>Bold Text</b>
<i> 	Italic (visual only) 	<i>Italic Text</i>
<em> 	Emphasis (semantic italic) 	<em>Emphasized</em>
<mark> 	Highlighted text 	<mark>Highlight</mark>
<small> 	Smaller text 	<small>Note</small>
<sub> 	Subscript 	H<sub>2</sub>O
<sup> 	Superscript 	E = mc<sup>2</sup>
<u> 	Underline 	<u>Underlined</u>
<del> 	Deleted text 	<del>Old</del>
<ins> 	Inserted text 	<ins>New</ins>

🔗 3. Links & Anchors
Tag 	Description 	Example
<a> 	Hyperlink 	<a href="https://example.com">Visit</a>
<link> 	External resources (e.g., CSS) 	<link rel="stylesheet" href="style.css">
<nav> 	Navigation block 	<nav><a href="#home">Home</a></nav>

🖼️ 4. Media Tags
Tag 	Description 	Example
<img> 	Image 	<img src="img.jpg" alt="Image">
<video> 	Video 	<video controls><source src="video.mp4"></video>
<audio> 	Audio 	<audio controls><source src="audio.mp3"></audio>
<source> 	Media source 	<source src="movie.mp4" type="video/mp4">
<track> 	Captions/subtitles 	<track src="subs.vtt" kind="subtitles">
<embed> 	External resource (e.g., PDF) 	<embed src="file.pdf">

📋 5. Lists
Tag 	Description 	Example
<ul> 	Unordered list 	<ul><li>Item</li></ul>
<ol> 	Ordered list 	<ol><li>First</li></ol>
<li> 	List item 	<li>Element</li>
<dl> 	Description list 	<dl><dt>HTML</dt><dd>Markup</dd></dl>
<dt> 	Term in <dl> 	<dt>Term</dt>
<dd> 	Description in <dl> 	<dd>Definition</dd>

📦 6. Table Tags
Tag 	Description 	Example
<table> 	Table container 	<table> ... </table>
<tr> 	Table row 	<tr> ... </tr>
<td> 	Table data cell 	<td>Data</td>
<th> 	Table header cell 	<th>Header</th>
<thead> 	Table header section 	<thead><tr><th>Col</th></tr></thead>
<tbody> 	Table body section 	<tbody><tr><td>Row</td></tr></tbody>
<tfoot> 	Table footer section 	<tfoot><tr><td>Foot</td></tr></tfoot>
<caption> 	Table caption/title 	<caption>Sales Data</caption>
<col> 	Column formatting 	<col span="2">
<colgroup> 	Group of columns 	<colgroup><col></colgroup>

🧩 7. Form & Input Tags
Tag 	Description 	Example
<form> 	Form container 	<form> ... </form>
<input> 	User input 	<input type="text">
<textarea> 	Multi-line input 	<textarea></textarea>
<label> 	Form label 	<label for="name">Name</label>
<select> 	Dropdown 	<select><option>One</option></select>
<option> 	Dropdown item 	<option value="1">One</option>
<button> 	Button 	<button>Click</button>
<fieldset> 	Group form fields 	<fieldset><legend>Info</legend></fieldset>
<legend> 	Caption for <fieldset> 	<legend>User Info</legend>
<datalist> 	Predefined input list 	<datalist id="browsers"><option>Chrome</option></datalist>
<output> 	Output result 	<output>Result</output>

📁 8. Semantic Layout Tags
Tag 	Description 	Example
<header> 	Page or section header 	<header> ... </header>
<footer> 	Page or section footer 	<footer> ... </footer>
<section> 	Generic section 	<section> ... </section>
<article> 	Independent content 	<article> ... </article>
<aside> 	Sidebar content 	<aside> ... </aside>
<main> 	Main content 	<main> ... </main>
<div> 	Generic container 	<div> ... </div>
<span> 	Inline container 	<span> ... </span>

🧠 9. Scripting & Meta Tags
Tag 	Description 	Example
<script> 	JavaScript code 	<script>alert('Hi')</script>
<noscript> 	Shown if JS disabled 	<noscript>No JS</noscript>
<meta> 	Metadata 	<meta charset="UTF-8">
<style> 	Internal CSS 	<style>p{color:red}</style>

🔎 10. Interactive Tags
Tag 	Description 	Example
<details> 	Toggle details 	<details><summary>Click</summary>Info</details>
<summary> 	Visible heading in <details> 	<summary>More</summary>
<dialog> 	Dialog box 	<dialog open>Hi</dialog>

🔄 11. Deprecated/Obsolete Tags (for reference only)
Tag 	Description 	Example
<center> 	Center align 	<center>Centered</center>
<font> 	Font formatting 	<font color="red">Text</font>
<marquee> 	Scrolling text 	<marquee>Scroll</marquee>

✅ 12. Miscellaneous Tags
Tag 	Description 	Example
<iframe> 	Inline frame (embed) 	<iframe src="page.html"></iframe>
<base> 	Base URL for links 	<base href="https://example.com/">
<time> 	Time value 	<time datetime="2025-07-30">Today</time>
<code> 	Code snippet 	<code>print()</code>
<kbd> 	Keyboard input 	<kbd>Ctrl</kbd>
<samp> 	Sample output 	<samp>Hello</samp>
<var> 	Variable name 	<var>x</var>
<bdi> 	Isolate bidirectional text 	<bdi>abc</bdi>
<bdo> 	Override text direction 	<bdo dir="rtl">Text</bdo>

"""

#############################
# Tags vs Element
#############################

# The Element is the entire thing
# Tags and Content

# <h1>content</>
# opening tag -- content -- closing tag

# Example
# <h1>Book</h1>
#   <h2>Chapter 1</h2>
#     <h3>Section 1</h3>
#     <h3>Section 2</h3>
#   <h2>Chapter 2</h2>
#     <h3>Section 1</h3>
#       <h4>Diagram 1</h4>
#   <h2>Chapter 3</h2>
#     <h3>Section 1</h3>
#     <h3>Section 2</h3>

#############################
# Paragraph
#############################

# <p>paragraph of text</p>

#############################
# Void Elements
#############################

# Horizontal Rule
# <hr />

# Break Rule (new line in Poem or address)
# <br /> 

#############################
# Challenge
#############################

# <!DOCTYPE html>
# <h1>James' Top TV Shows</h1>
# <h2>In no particular order - 5 of my favourite TV series!</h2>
# <hr />
# <h3>Bron ||| Broen</h3>
# <p>
#     When a body is found on the bridge between Denmark and Sweden, right on the border, Danish inspector Martin Rohde and
#     Swedish Saga Norén have to share jurisdiction and work together to find the killer.
# </p>
# <h3>Ted Lasso</h2>
# <p>
#     American college football coach Ted Lasso heads to London to manage AFC Richmond, a struggling English Premier League
#     soccer team.
# </p>
# <h3>The Sorpanos</h3>
# <p>
#     New Jersey mob boss Tony Soprano deals with personal and professional issues in his home and business life that affect
#     his mental state, leading him to seek professional psychiatric counseling.
# </p>
# <h3>Breaking Bad</h3>
# <p>
#     A chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine with a
#     former student to secure his family's future.
# </p>
# <h3>Taskmaster</h3>
# <p>
#     Five comedians are set tasks challenging their creativity and wit. The tasks are supervised by Alex Horne but the
#     Taskmaster, Greg Davies, always has the final word.
# </p>


##############################################################################
# DAY 42 - HTML Intermediate
##############################################################################

"""
The HTML Boilderplate

Understanding HTML Structure
"""

###########################
# Boilderplate
###########################

# <!-- Set to HTML5 -->
# <!DOCTYPE html>
# <!-- Specify language; useful for screen readers -->
# <html lang="en">
    
#     <!-- Page data for browser -->
#      <head>
#         <!-- Specify page is using UTF-8 characters-->
#         <meta charset="UTF-8">
#         <!-- Specify Page Title -->
#         <title>Page Title</title>
#     </head>

#     <!-- Page content -->
#     <body>
#         <h1>Hello World!</h1>
#     </body>
# </html>

###########################
# Lists
###########################

# <h2>Unordered List...</h2>
# <ul>
#     <li>milk</li>
#     <li>bread</li>
#     <li>cheese</li>
#     <li>bacon</li>
# </ul>
# <h2>Ordered List...</h2>
# <ol>
#     <li>milk</li>
#     <li>bread</li>
#     <li>cheese</li>
#     <li>bacon</li>
# </ol>

###########################
# Nested Lists
###########################

# <ul>
#     <li>milk</li>
#     <li>bread</li>
#     <li>brown sauce</li>
#     <li>bacon</li>
#     <li>cheeses:
#         <ul>
#             <li>cheddar</li>
#             <li>jarlsberg</li>
#             <li>port salut</li>
#         </ul>
#     </li>
# </ul>

###########################
# Anchor Tags
###########################

# URL
# <a href="https://www.google.com/">Google Link</a>

# Draggable
# <a draggable="true" href="https://www.google.com/">Google Link</a>

# Image
# <!-- Random Image Website-->
# <img src="https://picsum.photos/400" alt="Random photo via picsum.photos"/><br>


###########################
# Birthday Site Example
###########################

# <!-- This is one possible solution -->
# <h1>It's My Birthday!</h1>
# <h2>On the 12th May</h2>

# <img src="https://raw.githubusercontent.com/appbrewery/webdev/main/birthday-cake3.4.jpeg"
#   alt="purple birthday cake with candles" />

# <h3>What to bring:</h3>
# <ul>
#   <li>Baloons (I love baloons)</li>
#   <li>Cake (I'm really good at eating)</li>
#   <li>An appetite (There will be lots of food)</li>
# </ul>

# <h3>This is where you need to go:</h3>
# <a
#   href="https://www.google.com/maps/@35.7040744,139.5577317,3a,75y,289.6h,87.01t,0.72r/data=!3m6!1e1!3m4!1sgT28ssf0BB2LxZ63JNcL1w!2e0!7i13312!8i6656">Google
#   map link</a>


##############################################################################
# DAY 43 - CSS Introduction
##############################################################################

"""
Cascading Style Sheets
CSS - Why Do We Need It?

https://appbrewery.github.io/just-add-css/

You can add in three ways:

-- Inline 
-- Was used for a particular Element
<tag style="css"/>

-- Internal
-- Was used for an individual Page
<style>css</style>

-- External
-- Used for an entire site
<link 
    rel="stylesheet" 
    href="./style.css"
/>

"""
# Should be Unique within HTML
# #ID-Selector
# #main{
# color: red;
# }

# Many elements
# .Class-Selector
# .red-text{
# color: red;
# }

# Attiribute selector
# p[draggable]{
# color: red;
# }

# Universal selector
# *{
# color: red;
# }


##############################################################################
# DAY 44 - CSS Properties
##############################################################################

"""
CSS Properties

colorhunt.co
fonts.google.com
"""

############################
# Colour
############################

# html {
# background-color: blue
# }
#
# h1 {
# color: blue
# }
#
# h2 {
# color: 0D1164
# }

############################
# Font Property Examples
############################

# 1 px = 1/96th Inch
# 1 px = 0.26 mm

# 1 pt = 1/72nd Inch
# 1 pt = 0.35 mm

# 1 em = 100% of parent
# 1 rem = 100% of root

# #color {
#     color: coral;
#     font-size: 2rem; # 2x parent size
#     font-weight: 900;
#     font-family: 'Caveat', cursive;
#     text-align: right;
# }

############################
# Margin, Padding & Border
############################

# borders expand out; they dont reduce the box
# border: thickness style colour
# border-top: value
# border-width: top right bottom left
# border-width: top-bottom right-left
#
# padding pushes out border by value; box stays same size
# padding: value
#
# margin is the bit outside the border
# margin: value

# ┌─────────────────────────────────────────────────────────────────┐
# │                           MARGIN                                │
# │  ┌───────────────────────────────────────────────────────────┐  │
# │  │                        BORDER                             │  │
# │  │  ┌─────────────────────────────────────────────────────┐  │  │
# │  │  │                    PADDING                          │  │  │
# │  │  │  ┌───────────────────────────────────────────────┐  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  │                 CONTENT                       │  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  │            (Your actual element               │  │  │  │
# │  │  │  │             text, images, etc.)               │  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  └───────────────────────────────────────────────┘  │  │  │
# │  │  │                                                     │  │  │
# │  │  └─────────────────────────────────────────────────────┘  │  │
# │  │                                                           │  │
# │  └───────────────────────────────────────────────────────────┘  │
# │                                                                 │
# └─────────────────────────────────────────────────────────────────┘

#                         Box Model Layers:
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 1. CONTENT   - The actual content (text, images, etc.)
# 2. PADDING   - Space between content and border (inside border)
# 3. BORDER    - The border surrounding padding and content
# 4. MARGIN    - Space outside the border (between elements)

# Example CSS:
# ───────────
# .box {
#     margin: 20px;      /* Outermost spacing */
#     border: 5px solid; /* Border thickness & style */
#     padding: 15px;     /* Inner spacing */
#     width: 200px;      /* Content width */
#     height: 100px;     /* Content height */
# }

# Total Width  = margin + border + padding + content + padding + border + margin
# Total Height = margin + border + padding + content + padding + border + margin

############################
# HTML Div
############################

# A <div> (division) is a generic HTML container element that groups content together. 
# By itself, it's invisible and has no visual styling—it's like an empty box waiting to be decorated.

# Class Selector example

# <div class="my-box">Content here</div>

# .my-box {
#     background-color: lightgray;
#     padding: 20px;
#     border: 2px solid black;
# }

##############################################################################
# DAY 45 - Webscraping with Beatiful Soup
##############################################################################

"""
 Web Scraping With Beautiful Soup

 https://www.crummy.com/software/BeautifulSoup/bs4/doc/

"""

# Beautiful Soup
from bs4 import BeautifulSoup
# import lxml

with open("./index.html") as file:
    html_content = file.read()
    print(html_content)

# if html doesnt work try lxml
soup = BeautifulSoup(html_content, 'html.parser')

# print title tag
print(soup.title)
# print title name
print(soup.title.name)
# print title text
print(soup.title.string)
# formats the output
print(soup.prettify())

# print first anchor tag it finds
print(soup.a)
# print first list it finds
print(soup.li)
# print first paragraph it finds
print(soup.p)

# find all instances of X
all_paragraphs = soup.find_all("p")
print(all_paragraphs)

# find all instances of X
all_anchor_tags = soup.find_all("a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

# search by tag or heading
heading = soup.find(name="h1", id="heading")

# search by class, note _ at end of class
section_heading = soup.find(name="h3", class_="TV")
print(section_heading)

# search by CSS selector
selector = soup.select_one(selector="#name")

# search by CSS class
headings = soup.select(".heading")


######################################################
# Hackernew 
# Aim is to get the most upvoted article in the top 30
######################################################

from bs4 import BeautifulSoup
import requests

site = "https://news.ycombinator.com/news"
response = requests.get(site)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# return articles from first page
articles = soup.find_all("span", class_="titleline")

# generate two lists
articles_text = [] 
articles_url = []

# add Article Header and URL to lists
for article in articles:

    text = article.get_text()
    articles_text.append(text)

    url = article.find("a").get("href")
    articles_url.append(url)

# list comprehension to get the scores per article
article_upvotes = [int(votes.get_text().split()[0]) for votes in soup.find_all("span", class_="score")]

# print(articles_text)
# print(articles_url)
# print(article_upvotes)

# return index of highest score
max_score_index = article_upvotes.index(max(article_upvotes))

# print the list items corresponding to score
print(f"This article with the most votes is: {articles_text[max_score_index]} -> {articles_url[max_score_index]}")

######################################################
# Webscraping
# 
# Legal Rules for Web Scraping (via Claude)
#
# 1. Check the robots.txt File
# Before scraping any website, always check website.com/robots.txt. This file tells you:
# Which parts of the site you can scrape
# Which parts are off-limits
# Crawl delay requirements
# Example:
# Always check: https://example.com/robots.txt
# # It might contain:
#   User-agent: *
#   Disallow: /private/
#   Crawl-delay: 1
#
# 2. Review the Terms of Service (ToS)
# Many websites explicitly prohibit scraping in their Terms of Service. Violating ToS can lead to:
#   IP bans
#   Legal action
#   Account termination (if logged in)
#
# 3. Respect Rate Limits
#   Add delays between requests (typically 1-3 seconds)
#   Don't overwhelm servers with rapid requests
#   This is both ethical and helps avoid getting blocked
#       pythonimport time
#       time.sleep(2)  # Wait 2 seconds between requests
#
# 4. Copyright and Data Ownership
#   Factual data generally can't be copyrighted
#   Creative content (articles, images) is usually protected
#   Database compilations may have protection
#   Always consider fair use, but it's complex
# 
# Best Practices for Legal Scraping
# 
#   1. Use APIs When Available
#       Many sites offer APIs specifically for data access - always prefer these over scraping.
#   2. Identify Yourself
#       Set a proper User-Agent header:
#       pythonheaders = {
#           'User-Agent': 'Your Bot Name (your-email@example.com)'
#       }
#
#   3. Handle Personal Data Carefully
#
#       GDPR (Europe) and CCPA (California) have strict rules about personal data
#       Avoid scraping personal information when possible
#       If you must, ensure compliance with privacy laws
#
#   4. Respect "No Scraping" Signs
#
#   If you see:
#       Meta tags like <meta name="robots" content="noindex,nofollow">
#       Explicit "no scraping" notices
#       CAPTCHA challenges
#       These are clear signals to stop.
#
# Common Legal Pitfalls to Avoid
#
#   Don't bypass security measures (login walls, CAPTCHAs)
#   Don't scrape copyrighted content for commercial use
#   Don't violate Computer Fraud and Abuse Act (CFAA) - unauthorized access
#   Don't ignore cease and desist letters
#   Don't resell or redistribute scraped data without permission
#
# Gray Areas and Recent Cases
#
#   LinkedIn vs. HiQ Labs (2019): Publicly available data may be fair game
#   Facebook vs. Power Ventures: Logged-in scraping is riskier
# 
#   The legal landscape is evolving - what's okay today might not be tomorrow
######################################################

"""
Challenge

Empire 
Return the Top 100 Movies and output to txt file
"""

from bs4 import BeautifulSoup
import requests

site = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(site)
website_html = response.text
# print(response.text)

soup = BeautifulSoup(website_html, 'html.parser')
# print(soup.prettify())

# list comprehensin for movie names; 100 to 1
movies = [movie.text for movie in soup.find_all("h3", class_="title")]

# reverse list and appeend each to file
with open("./movies.txt", "a") as f:
    for movie in reversed(movies):
        f.write(f"{movie}\n")

##############################################################################
# DAY 46 - Billboard 100 Scraping and Spotify Playlist creatiom
##############################################################################

from billboard import BillboardSoup
from spotify_api import Spotify
from my_spotipy import MySpotipy
from datetime import datetime, timedelta
import sys

def main(date):
    ##############################################
    # Find previous Saturday to get Billboard Date
    ##############################################

    # Parse the input date
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Get day of week (0=Monday, 5=Saturday, 6=Sunday)
    days_since_saturday = (date.weekday() + 1) % 7
    
    # If it's already Saturday, use it; otherwise go to previous Saturday
    if days_since_saturday == 0:
        billboard_date = date
    else:
        billboard_date = date - timedelta(days=days_since_saturday)
    
    billboard_date_str = billboard_date.strftime("%Y-%m-%d")

    ##############################################
    # Billboard Soup - Get Top100 for Week
    ##############################################

    # date = "2000-08-19"
    soup = BillboardSoup()
    top_100 = soup.get_chart(date=billboard_date_str)
    # print(top_100)

    ##############################################
    # Spotify - Lookup Top 100
    ##############################################

    spotify = Spotify()
    track_uris = []

    for title, artist in top_100.items():
        uri = spotify.search_track(artist_name=artist, track_name=title)
        if uri:
            track_uris.append(uri.split(":")[2])
            print(f"✓ Found: {title} - {artist}")
        else:
            print(f"✗ Not found: {title} - {artist}")
    # print(track_uris)

    ##############################################
    # Spotipy - Create Playlist for Top 100
    ##############################################

    playlist_name = f"Billboard 100 - {billboard_date_str}"
    spotipy = MySpotipy()
    spotipy.create_playlist(playlist_name, f"Playlist for the week {billboard_date_str}")
    spotipy.add_to_playlist(playlist_name, track_uris)

    ##############################################
    # Results
    ##############################################

    print(f"\n📊 Playlist Statistics:")
    print(f"   Date: {billboard_date_str}")
    print(f"   Found: {len(track_uris)}/{len(top_100)} tracks")
    print(f"   Success rate: {len(track_uris)/len(top_100)*100:.1f}%")
    print(f"   Playlist: {playlist_name}")


if __name__ == "__main__":
    default_date = "2000-08-19"
    
    if len(sys.argv) > 1:
        date = sys.argv[1]
    else:
        user_input = input(f"Enter date (YYYY-MM-DD) [default: {default_date}]: ")
        date_str = user_input if user_input else default_date
    
    main(date_str)
