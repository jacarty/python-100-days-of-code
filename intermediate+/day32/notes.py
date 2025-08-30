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
 