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
