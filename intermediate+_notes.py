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