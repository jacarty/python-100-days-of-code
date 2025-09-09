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
