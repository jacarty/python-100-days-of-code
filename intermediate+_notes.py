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

##############################################################################
# DAY 47 - Amazon Price Checker
##############################################################################

"""
Amazon Price Tracker

Check Price. Compare to Target. Email if cheaper.

Camel Camel Camel
https://uk.camelcamelcamel.com/product/B000CSCRHY 
average price over 12 months = £28.67 
live price today on Amazon = £51.60
"""

import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from dotenv import load_dotenv
import os
from notification_manager import NotificationManager

load_dotenv("../../.env")

GU_BARS_URL = "https://www.amazon.co.uk/GU-Chocolate-Outrage-Flavour-Energy/dp/B000CSCRHY"
HEADERS = {"User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
TARGET_PRICE = Decimal('28.67')

def fetch_amazon_page(gu_bars_url, headers):
    """Fetch the Amazon Product Page"""

    response = requests.get(gu_bars_url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_price(website_html):
    """Soup Price Extraction"""

    soup = BeautifulSoup(website_html, 'html.parser')

    try:
        gu_price_whole = soup.find("span", class_="a-price-whole").get_text()
        gu_price_fraction = soup.find("span", class_="a-price-fraction").get_text()
    except AttributeError:
        return "Could not find price on page. Amazon may have changed their HTML structure."

    gu_price = Decimal(f"{gu_price_whole}{gu_price_fraction}")
    return gu_price

def check_and_notify(current_price, target_price, gu_bars_url):
    """Price Check and Email"""

    notifications = NotificationManager()

    if current_price < target_price:
        recipient = os.getenv("RECIPIENT")
        subject = "Amazon Price Alert - Gu Buy Time!"
        message = f"Guud news. The price has dropped to {current_price}. Time to stock up.\n{gu_bars_url}"
        send_email = notifications.send_email(recipient, subject, message)
        return send_email
    else:
        return "No Gu Buy"

def main():
    try:
        website_html = fetch_amazon_page(GU_BARS_URL, HEADERS)
        current_price = extract_price(website_html)
        outcome = check_and_notify(current_price, TARGET_PRICE, GU_BARS_URL)
        print(outcome)
    except (requests.RequestException, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

##############################################################################
# DAY 48 - Selenium Webdriver and Game Playing Bot
##############################################################################

"""
Selenium Webdriver and Game Playing Bot

https://selenium-python.readthedocs.io/

"""

##############################
# Example 1 - Amazon
##############################

GU_BARS_URL = "https://www.amazon.co.uk/GU-Chocolate-Outrage-Flavour-Energy/dp/B000CSCRHY"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(GU_BARS_URL)
pound_price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
pence_price = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

print(f"£{pound_price}.{pence_price}")

# closes the active tab
# driver.close()
# closes the entire browser
driver.quit()

##############################
# Example 2 - Python.org
##############################

URL = "https://www.python.org"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# forms typically use name
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

# find by ID
button = driver.find_element(By.ID, value="submit")
print(search_bar.size)

# find by CSS Selector
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# find by XPATH
jobs_link = driver.find_element(By.XPATH, value='/html/body/div/div[3]/div/section/div[1]/div[4]/p[2]/a')
print(jobs_link.text)

# closes the active tab
# driver.close()
# closes the entire browser
driver.quit()

##############################
# Example 3 - Python.org
##############################

URL = "https://www.python.org"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# find by CSS Selector
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# dictionary comprehension with index as key, from the two lists
events = {n: {time.text: name.text} for n, (time, name) in enumerate(zip(event_times, event_names))}
print(events)

# closes the entire browser
driver.quit()

##############################
# Example 4 - Wikipedia
##############################

URL = "https://en.wikipedia.org/wiki/Main_Page"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# find total articles by CSS Selector
article_count = driver.find_elements(By.CSS_SELECTOR, "a[href='/wiki/Special:Statistics']")
print(article_count[1].text)

article_count.click()

# closes the entire browser
driver.quit()

################################
# Example 5 - Click By Link Text
################################

URL = "https://en.wikipedia.org/wiki/Main_Page"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

teahouse = driver.find_element(By.LINK_TEXT, value="Teahouse")
teahouse.click()

# closes the entire browser
driver.quit()

################################
# Example 6 - Input Box Example
################################

URL = "https://en.wikipedia.org/wiki/Main_Page"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# find search box
search = driver.find_element(By.NAME, value="search")
# enter text and retrun
search.send_keys("Python", Keys.ENTER)

# closes the entire browser
driver.quit()

################################
# Example 7 - Webpage Sign Up
################################

URL = "https://secure-retreat-92358.herokuapp.com/"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

fname.send_keys("Rydon")
lname.send_keys("Man")
email.send_keys("rydonman@mailinator.com")

# instructor
# button = driver.find_element(By.CSS_SELECTOR, value="form button")
button = driver.find_element(By.CSS_SELECTOR, value="button.btn.btn-lg.btn-primary.btn-block")
button.click()

# closes the entire browser
driver.quit()

################################
# Challenge - Cookie Clicker
################################

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://ozh.github.io/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, value="bigCookie")

def click_button(duration):
    round_time = time.time()
    while time.time() - round_time < duration:
        cookie.click()
        time.sleep(0.01)

    upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

    if upgrades:
        upgrades[-1].click()
        print("Purchased an upgrade!")

rounds = 0
while rounds <= 20:
    button = click_button(20)
    rounds -= 1
    print(f"Round {rounds}/20 completed!")


##############################################################################
# DAY 49 - Selenium Gym Class Booking Bot
##############################################################################

"""
Selenium to book fake gym classes

"""

import os
import tempfile
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LOGIN_URL = "https://appbrewery.github.io/gym/"
SCHEDULE_URL = "https://appbrewery.github.io/gym/schedule/"
ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""

days = ["tue", "thu"]
timeslot = "1800"
already_on = 0
waitlist = 0
booked = 0
classes = []

# Chrome profile data
user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_py_profile")

# Chrome setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=chrome_options)

def login(driver, url, email, password):
    driver.get(url)
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    wait = WebDriverWait(driver, timeout=5)

    try:
        email_field = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
        email_field.clear()
        email_field.send_keys(email)

        password_field = wait.until(EC.presence_of_element_located((By.ID, "password-input")))
        password_field.clear()
        password_field.send_keys(password)

        submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit-button")))
        submit_button.click()

        wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

        return True

    except Exception as e:
        print(f"Login unsuccessful: {e}")
        return False

def find_day_container(driver, day):

    selectors = [
        f"div[id*='day-group-today-({day},']",      # Today pattern
        f"div[id*='day-group-tomorrow-({day},']",   # Tomorrow pattern
        f"div[id*='day-group-{day}']"               # Regular day pattern
    ]

    for selector in selectors:
        try:
            return driver.find_element(By.CSS_SELECTOR, selector)
        except:
            continue

    raise Exception(f"Could not find container for day: {day}")

def book_class(container, day, time):

    global already_on
    global waitlist
    global booked
    global classes

    try:
        # find card for time (e.g. 1800)
        gym_class = container.find_element(By.CSS_SELECTOR, f"div[id^='class-card-'][id*='{time}']")
        # find the date (of class)
        gym_class_date = container.find_element(By.CLASS_NAME, "Schedule_dayTitle__YBybs")
        # find the class type
        gym_class_type = container.find_element(By.CSS_SELECTOR, "h3[id^='class-name']")
        # find the button
        gym_class_button = gym_class.find_element(By.CSS_SELECTOR, "button")

        # Check if a class is already booked (button reads "Booked")
        if gym_class_button.text == "Booked":
            classes.append(f"Booked: {gym_class_type.text} on {gym_class_date.text} at {time}")
            already_on += 1
            return True

        # Check if you're on the waitlist (button reads "Waitlisted")
        elif gym_class_button.text == "Waitlisted":
            classes.append(f"Waitlisted: {gym_class_type.text} on {gym_class_date.text} at {time}")
            already_on += 1
            return True

        # Join the waitlist if the class is full (button says "Join Waitlist")
        elif gym_class_button.text == "Join Waitlist":
            gym_class_button.click()
            # print(f"✓ Waitlisted: {gym_class_type.text} on {gym_class_date.text} at {time}")
            waitlist +=1
            classes.append(f"Waitlisted: {gym_class_type.text} on {gym_class_date.text} at {time}")
            return True

        else:
            gym_class_button.click()
            # print(f"✓ Booked: {gym_class_type.text} on {gym_class_date.text} at {time}")
            booked += 1
            classes.append(f"New booking: {gym_class_type.text} on {gym_class_date.text} at {time}")
            return True

    except Exception as e:
        print(f"Booking unsuccessful: {e}")
        return False

def verify_bookings(driver):
    my_bookings = driver.find_element(By.ID, "my-bookings-link")
    my_bookings.click()

    wait = WebDriverWait(driver, timeout=5)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".MyBookings_bookingCard__VRdrR")))

    try:
        booked_classes = driver.find_elements(By.CLASS_NAME, "MyBookings_bookingCard__VRdrR")
        print(booked_classes)
        booked_total = len(booked_classes)

        return booked_total

    except NoSuchElementException:
        return 0

def counters(total_booked):

    total_classes = booked + waitlist + already_on

    if total_classes == total_booked:
        result = "✅ SUCCESS: All bookings verified!"
    else:
        result = "❌ MISSING: Booking mismatch!"

    return f"""
    --- BOOKING SUMMARY ---
    Classes booked: {booked}
    Waitlists joined: {waitlist}
    Already booked/waitlisted: {already_on}
    Total 6pm classes processed: {total_classes}

    --- DETAILED CLASS LIST ---
    {'\n    '.join(classes)}

    --- VERIFICATION RESULT ---
    Found: {total_booked} bookings
    {result}
    """

def retry(func, retries=7):

    for _ in range(retries):
        if func():
            return True

    return False

def main(driver, url, email, password, days, timeslot):

    # login
    retry(lambda: login(driver, url, email, password))

    # book classes
    for day in days:
        container = find_day_container(driver, day)
        booking = retry(lambda: book_class(container, day, timeslot))
        print(booking)

    # verify what is booked
    total_booked = verify_bookings(driver)

    # return counters
    summary = counters(total_booked)
    print(summary)

    #driver.quit()

if __name__ == "__main__":
    main(driver,
         LOGIN_URL,
         ACCOUNT_EMAIL,
         ACCOUNT_PASSWORD,
         days,
         timeslot)


##############################################################################
# DAY 50 - Auto Swipe Bot
##############################################################################

"""
Day 50 - Auto Swipe Bot
Instructor code

Fake photos https://www.thispersondoesnotexist.com/

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = YOUR FACEBOOK LOGIN EMAIL
FB_PASSWORD = YOUR FACEBOOK PASSWORD

driver = webdriver.Chrome()

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()


##############################################################################
# DAY 51 - Twitter Complaints Bot
##############################################################################

"""
Twitter Complaints Bot
"""

from dotenv import load_dotenv
import os
import tempfile
import time
from random import uniform
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Constants
load_dotenv("../../.env")
SPEEDTEST_URL = "https://www.speedtest.net/"
SLA_DOWN = 2500
SLA_UP = 250
TWITTER_URL = "https://twitter.com"
TWITTER_U = os.getenv("TWITTER_U")
TWITTER_PW = os.getenv("TWITTER_PW")

class InternetSpeedTwitterBot:

    def __init__(self):
        # Chrome
        user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_py_profile")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--disable-extensions")

        # Selenium
        self.driver = webdriver.Chrome(options=chrome_options)
        self.test_wait = WebDriverWait(self.driver, timeout=60)
        self.standard_wait = WebDriverWait(self.driver, timeout=5)

        # Properties
        self.up = 0
        self.down = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #self.driver.quit()
        pass

    def get_internet_speed(self):
        try:
            self.driver.get(SPEEDTEST_URL)
            test_button = self.standard_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "start-button")))
            test_button.click()

            try:
                close_popup = self.test_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close-btn")))
                close_popup.click()
                print("Closed popup")
            except:
                print("No popup appeared")

            download = self.standard_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-download-status-value].result-data-large")))
            upload = self.standard_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-upload-status-value].result-data-large")))

            self.down = float(download.text)
            self.up = float(upload.text)

            print(f"Download: {self.down} Mbps")
            print(f"Upload: {self.up} Mbps")
            print(f"SLA - Down: {SLA_DOWN} Mbps, Up: {SLA_UP} Mbps")

            if self.down < SLA_DOWN or self.up < SLA_UP:
                print("⚠️  Speed below SLA! Time to tweet at provider!")
                return True
            else:
                print("✅ Speed meets SLA requirements")
                return False

        except Exception as e:
            return f"Start unsuccessful: {e}"


    def human_delay(self, action_type="default"):
        delays = {
            "typing": (4.5, 8.5),      # Shorter for typing
            "clicking": (0.8, 2.2),    # Medium for clicks
            "loading": (3.0, 6.0),     # Longer for page loads
        }
        min_time, max_time = delays.get(action_type, delays["default"])
        time.sleep(uniform(min_time, max_time))

    def tweet_at_provider(self):
        try:
            self.driver.get(TWITTER_URL)
            print("Navigated to Twitter")

            self.human_delay("clicking")

            login_button = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="loginButton"]')))
            login_button.click()
            print("Login button clicked")

            # Wait for the login modal to appear (no iframe needed)
            login_modal = self.standard_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[role="dialog"]')))
            print("Login modal appeared")

            self.human_delay("loading")

            input_area = self.standard_wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Phone, email address, or username']")))
            self.driver.execute_script("arguments[0].click();", input_area)
            print("Clicked on input area using JavaScript")

            # Wait a moment for the input field to be created
            self.human_delay("typing")

            username = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
            username.send_keys(TWITTER_U)
            print("Username entered")

            self.human_delay("clicking")

            next_button = self.standard_wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]')))
            next_button.click()
            print("Next button clicked")

            self.human_delay("loading")

            password = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="current-password"]')))
            password.send_keys(TWITTER_PW)  # Fixed: use password, not username
            print("Password entered")

            self.human_delay("typing")

            final_login_button = self.standard_wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Log in"]')))
            final_login_button.click()
            print("Final login button clicked")

            # Wait a bit for login to complete
            print("Waiting for login to complete...")

            self.human_delay("loading")

            tweet_box = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
            tweet_box.send_keys(f"Hey Internet Provider. Why is my internet {self.down}down/{self.up}up when I pay for {SLA_DOWN}down and {SLA_UP}up?")
            print("Tweet text entered")

            self.human_delay("typing")

            tweet_button = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')))
            tweet_button.click()
            print("Tweet posted!")

            return "Tweet sent successfully"

        except Exception as e:
            print(f"Twitter automation failed at step: {e}")
            return f"Failed to tweet: {e}"

if __name__ == "__main__":
    with InternetSpeedTwitterBot() as app:
        should_tweet = app.get_internet_speed()

        if should_tweet is True:
            tweet_result = app.tweet_at_provider()
            print(f"Tweet result: {tweet_result}")

        elif should_tweet is False:
            print("No need to complain - speeds are good!")

        else:
            print(f"Error: {should_tweet}")


##############################################################################
# DAY 52 - Instagram Bot To Follow Accounts
##############################################################################

"""
Instagram Bot To Follow Accounts
"""

from dotenv import load_dotenv
import os
import tempfile
import time
from random import randint, uniform
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import WebDriverException

# Constants
load_dotenv("../../.env")
URL = "https://instagram.com"
INSTAGRAM_U = os.getenv("INSTAGRAM_U")
INSTAGRAM_PW = os.getenv("INSTAGRAM_PW")
INSTAGRAM_ACC = ""

class InstaFollower:

    def __init__(self):
        # Chrome
        user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_py_profile")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--disable-extensions")

        # Selenium
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=10)

        # Insta
        self.followers_list = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #self.driver.quit()
        pass

    def human_delay(self, action_type="default"):
        delays = {
            "clicking": (0.8, 2.2),
            "default": (0.9, 3.2),
            "typing": (2.5, 8.5)
        }
        min_time, max_time = delays.get(action_type, delays["default"])
        time.sleep(uniform(min_time, max_time))

    def login(self):
        try:
            # Navigate to Page
            self.driver.get(URL)
            print("Navigated to Instagram")

            # Username field
            try:
                self.human_delay("clicking")
                uname_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Phone number, username or email address']")))
                uname_field.clear()
                self.human_delay("typing")
                uname_field.send_keys(INSTAGRAM_U)
                print("Entered Username")
            except Exception as e:
                print(f"Failed to find Username field: {e}")
                return False

            # Password field
            try:
                pword_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Password']")))
                pword_field.clear()
                self.human_delay("typing")
                pword_field.send_keys(INSTAGRAM_PW)
                print("Entered Password")
            except Exception as e:
                print(f"Failed to find Password field: {e}")
                return False

            # Login button
            try:
                self.human_delay("clicking")
                login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and not(@disabled)]")))
                login_button.click()
                print("Clicked Login")
            except Exception as e:
                print(f"Failed to click Login button: {e}")
                return False

            # Click "Not now" to Save Password
            try:
                save_login_prompt = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now')]")))
                save_login_prompt.click()
                print("Dismissed save login prompt")
            except Exception as e:
                print(f"Failed to click Login button: {e}")
                return False

        except WebDriverException as e:
            print(f"WEBDRIVER ERROR: Browser/connection issue - {e}")
            return False
        except Exception as e:
            print(f"UNEXPECTED ERROR: {type(e).__name__} - {e}")
            return False

    def find_followers(self):
        try:
            # Navigate to Page
            self.human_delay("default")
            self.driver.get(f"{URL}/{INSTAGRAM_ACC}")
            print(f"Navigated to {INSTAGRAM_ACC}'s Page")

            # Open Followers
            try:
                followers_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]")))
                self.human_delay("clicking")
                followers_link.click()
                print("Clicked followers link")
            except Exception as e:
                print(f"Failed to find followers link: {e}")
                return False

            # List Followers
            try:
                print("Waiting for followers modal to load...")
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='heading' and contains(text(), 'Followers')]")))
                print("Followers modal loaded")

                time.sleep(2)  # Give content time to load

                self.followers_list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[.//div[text()='Follow']]")))
                print(f"Found {len(self.followers_list)} users to follow")
            except Exception as e:
                print(f"Failed to create followers list: {e}")
                return False

        except WebDriverException as e:
            print(f"WEBDRIVER ERROR: Browser/connection issue - {e}")
            return False
        except Exception as e:
            print(f"UNEXPECTED ERROR: {type(e).__name__} - {e}")
            return False

    def follow(self):
        max_follows = randint(4, 12)

        # Click each button with delays
        for i, button in enumerate(self.followers_list[:max_follows]):
            try:
                # Scroll to button if needed
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                self.human_delay("clicking")
                button.click()
                print(f"Followed user {i+1}")

            except Exception as e:
                print(f"Failed to follow user {i+1}: {e}")

if __name__ == "__main__":
    with InstaFollower() as app:
        login = app.login()

        if login:
            find_followers = app.find_followers()

            if find_followers:
                follow = app.follow()


##############################################################################
# DAY 53 - Zillow Web Scraping and Data Entry
##############################################################################

"""
Zillow = San Fran, Rent, 3K Max, 1 Bedroom
Use this - https://appbrewery.github.io/Zillow-Clone/

Beautful Soup to Scrape
Selenium to Enter Form
"""

from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import tempfile
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import WebDriverException

# Constants
load_dotenv("../../.env")
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GFORM_URL = os.getenv("D53_GFROM_URL")

def scrape_data(url):
    """Get Zillow Reponse"""
    headers = {
        "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
        }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_info(website_html):
    """Soup List Extraction"""

    soup = BeautifulSoup(website_html, 'html.parser')

    try:
        data = soup.find_all("div", class_="StyledPropertyCardDataWrapper")

        addresses = [item.select_one("address[data-test='property-card-addr']").get_text(strip=True).replace(" |", ",")
                for item in data
                if item.select_one("address[data-test='property-card-addr']")]

        prices = [item.select_one("span[data-test='property-card-price']").get_text(strip=True)[:6]
                for item in data
                if item.select_one("span[data-test='property-card-price']")]

        urls = [item.select_one("a[data-test='property-card-link']")['href']
                for item in data
                if item.select_one("a[data-test='property-card-link']")]

        properties = list(zip(addresses, prices, urls))

        return properties

    except Exception as e:
        print(f"Could not create dictionary. Error: {e}")
        return False

def fill_google_form_by_question_text(driver, question_text, answer):
    """Fill form field by locating the question text first"""
    try:
        # Find the question span
        question_xpath = f"//span[contains(text(), '{question_text}')]"
        question_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, question_xpath)))

        # Find the input container for this question
        container = question_element.find_element(By.XPATH, "./ancestor::div[@jscontroller]")

        # Look for textarea or input field
        try:
            input_field = container.find_element(By.TAG_NAME, "textarea")
        except:
            input_field = container.find_element(By.TAG_NAME, "input")

        input_field.clear()
        input_field.send_keys(answer)
        return True

    except Exception as e:
        print(f"Error filling '{question_text}': {e}")
        return False

def submit_form(url, property_list):
    """Submit form fields and loop"""
    # Chrome
    user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_py_profile")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-extensions")

    # Selenium
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    print("Navigated to Form")

    for address, price, url in property_list:
        # Fill each question by its text
        fill_google_form_by_question_text(driver, "address", address)
        fill_google_form_by_question_text(driver, "price", price)
        fill_google_form_by_question_text(driver, "URL", url)

        # Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, "div[role='button'][aria-label*='Submit']")
        submit_button.click()

        time.sleep(1)

        # Wait for success page to load
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Your response has been recorded')]")))

        # Click "Submit another response"
        submit_another_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Submit another response")))
        submit_another_button.click()

        # Wait for form to reload
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))

        print(f"Successfully submitted: {address}")

    # Quit browser
    driver.quit()

if __name__ == "__main__":
    zillow_data = scrape_data(ZILLOW_URL)
    soup_list = extract_info(zillow_data)
    submit_form(GFORM_URL, soup_list)


##############################################################################
# DAY 54 - WebDev with Flask
##############################################################################

"""
WebDev with Flask

FE Frameworks = Angular, React
BE Frameworks = Node, Django/Flask
FE Languages = HTML, CSS, JS
BE Languages = JS, Java, Python, Ruby etc

Python BEs = Flask, Django, Bottle, CherryPie, Pyramid


https://pythontutor.com/visualize.html#mode=edit
"""

# run hello.py
# export FLASK_APP=hello.py
# flask run

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()


## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()

"""
Objective Create your own decorator function to measure the amount of seconds that a function takes to execute.

Expected Output:
    1695050908.1985211
    fast_function run speed: 0.33974480628967285s
    slow_function run speed: 2.9590742588043213s

Calculating Time

time.time() will return the current time in seconds since January 1, 1970, 00:00:00.

Try running the starting code to see the current time printed.
If you run the code after a while, you'll see a new time printed.

e.g. first run:  1598524371.736911
second run:  1598524436.357875

The time difference = second run - first run  64.62096405029297  (approx 1 minute)

Given the above information, complete the code exercise by printing out the time it takes to run the fast_function() vs the slow_function().

You will need to complete the speed_calc_decorator() function.
 """

import time

def speed_calc_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()

# fast_function run speed: 0.030230998992919922s
# slow_function run speed: 0.3031938076019287s


##############################################################################
# DAY 55 - HTML & URL Parsing in Flask
##############################################################################

"""
HTML & URL Parsing in Flask
Higher / Lower Game
"""

# Decorator functions can be used for Routing

# https://www.mysite.com/
# https://www.mysite.com/bye

from flask import Flask

app = Flask(__name__)

# Decorator functions can be used for Routing
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Thanks for coming, goodbye!</p>"

# Decorator functions with Variables can be used for advanced Routing
@app.route("/<name>")
def greet(name):
    return f"Hello, {name}!"

# Decorator functions using Path
@app.route("/username/<path:name>/")
def greeting(name):
    return f"Hello, {name}!"
# http://127.0.0.1:5000/username/james/112/
# Hello, james/112!

# Decorator functions with multiple variables
@app.route("/username/<name>/<int:number>")
def age(name, number):
    return f"Hello, {name}, you are {number} years old!"

# Debug mode autoreloads when file saved
if __name__ == "__main__":
    app.run(debug=True)


"""
Example Decorators
"""

from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        bold = function()
        return f"<b>{bold}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        emphasis = function()
        return f"<i>{emphasis}</i>"
    return wrapper

def make_underline(function):
    def wrapper():
        italic = function()
        return f"<u>{italic}</u>"
    return wrapper

@app.route("/")
@make_bold
@make_emphasis
@make_underline
def hello_world():
    return "Hello, World!"

# Debug mode autoreloads when file saved
if __name__ == "__main__":
    app.run(debug=True)


"""
## Advanced Python Decorator Functions
"""

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("James")
new_user.is_logged_in = True
create_blog_post(new_user)

"""
Advanced Decorators

Create a logging_decorator() which is going to print the name of the function that was called,
the arguments it was given and finally the returned output:
    You called a_function(1,2,3)
    It returned: 6

The value 6 is the return value of the function.

Don't change the body of a_function.
"""

def logging_decorator(func):
    def wrapper(*args):
        result = func(*args)
        print(f"You called {func.__name__}{args}")
        print(f"It returned: {result}")
        return result
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1,2,3)

"""
Final Project - Higher or Lower URLs

Now it's time to complete the final project of the day, the higher lower game that we created in Day 14, but now with a real website.

1. Create a new project in PyCharm called higher-lower, add a server.py file.
2. Create a new Flask application where the home route displays an

<h1> that says "Guess a number between 0 and 9" and display a gif of your choice from giphy.com.

Alternatively use the one I found on Giphy: https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif

3. Generate a random number between 0 and 9 or any range of numbers of your choice.
4. Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9"
and checks that number against the generated random number.
If the number is too low, tell the user it's too low, same with too high or if they found the correct number.
Try to make the <h1> text a different colour for each page.  e.g. If the random number was 5:

    3 is too low:
    7 is too high:
    and 5 is just right:

Here are the GIF URLs I used, but it's way more fun finding your own on giphy.com
High: https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif
Low: https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif
Correct: https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif
"""

from flask import Flask
import random

answer = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <h1>Guess a number between 0 and 9</h1>
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Number guessing game'>
        """

@app.route("/<int:number>")
def guess(number):
    if number > answer:
        return """
            <h1 style='color: red'>You guessed too high</h1>
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='Too high'>
            """
    elif number < answer:
        return """
            <h1 style='color: blue'>You guessed too low</h1>
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='Too low'>
            """
    else:
        return """
            <h1 style='color: green'>You are correct!</h1>
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='Correct'>
            """

if __name__ == "__main__":
    app.run(debug=True)


##############################################################################
# DAY 56 - Static Files, HTML/CSS File Rendering
##############################################################################

"""
Static Files, HTML/CSS File Rendering
Project is Personal Namecard Site

HTML files go in the templates folder
Static files such as media, css etc. go in static folder

In Chrome Dev for real time field editing
Then save the page

document.body.contentEditable=true
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def website():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


##############################################################################
# DAY 57 - URL building and templating with Jinja in Flask
##############################################################################

"""
URL building and templating with Jinja in Flask

Jinja is a templating language

Project is to build a simple blog with posts based on the template
"""

from flask import Flask
from flask import render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def website():
    random_number = random.randint(1, 50)
    current_year = datetime.date.today().strftime("%Y")
    return render_template("index.html", num=random_number, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Jinja Ninja</title>
#     <link rel="stylesheet" href="static/style.css" />
# </head>
# <body>
#     <h1>I am Jinja</h1>
#     <p>This is using Jinja and Python to calculate 5 * 6 = {{ 5 * 6 }}</p>
#     <p>Random number between 1 and 50 generated by randint: {{ num }}</p>
# </body>
# <footer>
#     <p>© {{ year }} - built by James. The year is dynamically generated with the timedate module.</p>
# </footer>
# </html>

from flask import Flask
from flask import render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def website():
    random_number = random.randint(1, 50)
    current_year = datetime.date.today().strftime("%Y")
    return render_template("index.html", num=random_number, year=current_year)

@app.guess("/guess")
def guess()

print(f"Hi James")
gender = "https://api.agify.io?<name>"
print(f"I think you are {gender}")
age = "https://api.genderize.io?<name>"
print(f"And maybe {age} years old")


if __name__ == "__main__":
    app.run(debug=True)


"""
Guess Example
"""

from flask import Flask
from flask import render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def website():
    # number
    random_number = random.randint(1, 50)

    # year
    current_year = datetime.date.today().strftime("%Y")
    return render_template("index.html",
                           num=random_number,
                           year=current_year
                           )

@app.route("/guess/<name>")
def guess(name):
    # name
    upper_name = name.title()

    # gender
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    guessed_gender = gender_response.json()["gender"]

    # age
    age_response = requests.get(f"https://api.agify.io?name={name}")
    guessed_age = age_response.json()["age"]

    # year
    random_number = random.randint(1, 50)
    current_year = datetime.date.today().strftime("%Y")

    return render_template("guess.html",
                           name = upper_name,
                           gender = guessed_gender,
                           age = guessed_age,
                           year = current_year
                           )

@app.route("/blog/<num>")
def get_blog(num):
    #blogs
    blogs_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = blogs_response.json()
    return render_template("blog.html",
                           posts = all_posts
                            )

if __name__ == "__main__":
    app.run(debug=True)

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Jinja Ninja Blog</title>
#     <link rel="stylesheet" href="static/style.css" />
# </head>
# <body>
#     <h1>I am Jinja Blog</h1>
#     {% for blog_post in posts: %}
#         <h2>{{ blog_post["title"] }}</h1>
#         <h3>{{ blog_post["subtitle"] }}</h2>
#     {% endfor %}
# <a href="{{ url_for('get_blog', num=3) }}">Go To Blog</a>
# </body>
# <footer>
# </footer>
# </html>


##############################################################################
# DAY 58 - Bootstrap
##############################################################################

"""
Bootstrap

############################
# Bootstrap Columns Overview
############################

Bootstrap uses a 12-column grid system that's responsive and flexible for creating layouts.
Basic Structure
html<div class="container">
  <div class="row">
    <div class="col-md-6">Half width</div>
    <div class="col-md-6">Half width</div>
  </div>
</div>
Key Classes

Container: .container (fixed width) or .container-fluid (full width)
Row: .row - wraps columns, creates horizontal groups
Columns: .col-{breakpoint}-{size} where size is 1-12

Breakpoints

xs - Extra small (<576px)
sm - Small (≥576px)
md - Medium (≥768px)
lg - Large (≥992px)
xl - Extra large (≥1200px)

Common Patterns
html<!-- Equal width columns -->
<div class="col">Auto width</div>
<div class="col">Auto width</div>

<!-- Specific sizes -->
<div class="col-md-8">8 columns wide</div>
<div class="col-md-4">4 columns wide</div>

<!-- Responsive -->
<div class="col-12 col-md-6 col-lg-4">
  Full on mobile, half on tablet, third on desktop
</div>
Utilities

Offset: .offset-md-2 (push column right)
Order: .order-md-2 (change visual order)
Gutters: .g-0 (no gaps), .gx-3 (horizontal gaps), .gy-2 (vertical gaps)

Remember: Columns must always be inside a .row, and rows should be in a .container.

############################
# Bootstrap Buttons Overview
############################

Basic Button Classes
html<!-- Primary button -->
<button type="button" class="btn btn-primary">Primary</button>

<!-- Other color variants -->
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>
Button Sizes
html<button class="btn btn-primary btn-lg">Large</button>
<button class="btn btn-primary">Default</button>
<button class="btn btn-primary btn-sm">Small</button>
Button States
html<!-- Outline buttons -->
<button class="btn btn-outline-primary">Outline</button>

<!-- Disabled -->
<button class="btn btn-primary" disabled>Disabled</button>

<!-- Active state -->
<button class="btn btn-primary active">Active</button>
Block & Group
html<!-- Full width -->
<button class="btn btn-primary d-grid">Block Button</button>

<!-- Button group -->
<div class="btn-group">
  <button class="btn btn-primary">Left</button>
  <button class="btn btn-primary">Middle</button>
  <button class="btn btn-primary">Right</button>
</div>
Works on <button>, <a>, and <input> elements with .btn class.


############################
# Bootstrap Cards Overview
############################

Basic Card Structure
html<div class="card">
  <div class="card-header">
    Card Header
  </div>
  <div class="card-body">
    <h5 class="card-title">Card Title</h5>
    <p class="card-text">Some quick example text to build on the card title.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
  <div class="card-footer text-muted">
    Card Footer
  </div>
</div>
Card with Image
html<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
Card Grid
html<div class="row">
  <div class="col-md-4">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Card 1</h5>
        <p class="card-text">Content here.</p>
      </div>
    </div>
  </div>
  <div class="col-md-4">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Card 2</h5>
        <p class="card-text">Content here.</p>
      </div>
    </div>
  </div>
</div>
Key Classes

.card - Main container
.card-body - Main content area
.card-title - Card title styling
.card-text - Card text styling
.card-header / .card-footer - Top/bottom sections
.card-img-top / .card-img-bottom - Images

Cards are flexible and can contain headers, footers, images, lists, and any content.


############################
# Bootstrap Navs Overview
############################

Basic Nav (Tabs Style)
html<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled" href="#">Disabled</a>
  </li>
</ul>
Pills Style
html<ul class="nav nav-pills">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
</ul>
Vertical Nav
html<ul class="nav nav-pills flex-column">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
</ul>
Nav with Dropdown
html<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#">Dropdown</a>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Action</a></li>
      <li><a class="dropdown-item" href="#">Another action</a></li>
    </ul>
  </li>
</ul>
Nav Alignment
html<!-- Centered -->
<ul class="nav nav-tabs justify-content-center">
  <!-- nav items -->
</ul>

<!-- Right aligned -->
<ul class="nav nav-tabs justify-content-end">
  <!-- nav items -->
</ul>
Key Classes

.nav - Base nav class
.nav-tabs - Tab style
.nav-pills - Pill style
.nav-item - Nav item wrapper
.nav-link - Nav link styling
.active - Active state
.disabled - Disabled state

############################
# Bootstrap Spacing Overview
############################

Spacing Classes Format
.{property}{sides}-{size} or .{property}{sides}-{breakpoint}-{size}
Properties

m - margin
p - padding

Sides

t - top
b - bottom
s - start (left in LTR)
e - end (right in LTR)
x - horizontal (left & right)
y - vertical (top & bottom)
(no letter) - all sides

Sizes

0 - 0
1 - 0.25rem
2 - 0.5rem
3 - 1rem
4 - 1.5rem
5 - 3rem
auto - auto

Examples
html<!-- Margins -->
<div class="m-3">Margin all sides</div>
<div class="mt-2">Margin top</div>
<div class="mx-auto">Margin horizontal auto (center)</div>
<div class="ms-4">Margin start (left)</div>

<!-- Padding -->
<div class="p-3">Padding all sides</div>
<div class="px-2">Padding horizontal</div>
<div class="py-4">Padding vertical</div>

<!-- Responsive -->
<div class="m-2 m-md-4">Small margin on mobile, larger on medium+</div>

<!-- Remove spacing -->
<div class="m-0">No margin</div>
<div class="p-0">No padding</div>
Common Patterns

mx-auto - Center horizontally
mb-3 - Bottom margin
px-4 py-2 - Horizontal and vertical padding
me-2 - Right margin (between elements)

"""
