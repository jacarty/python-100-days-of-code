from dotenv import load_dotenv
import os
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self):
        load_dotenv("../../.env")
        self.api_url = "https://test.api.amadeus.com/v1"
        self.api_key = os.getenv("FLIGHT_API_KEY")
        self.api_secret = os.getenv("FLIGHT_API_SECRET")

    def flight_login(self):
        """Login to Amadeus and get Bearer"""
        login_url = f"{self.api_url}/security/oauth2/token"

        login_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        login_data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret,
        }

        login = requests.post(url=login_url, headers=login_headers, data=login_data)

        # Check if request was successful
        if login.status_code == 200:
            login_result = login.json()
            self.access_token = login_result.get("access_token")
            
            # Create API Bearer Token
            self.api_bearer = {
                "Authorization": f"Bearer {self.access_token}",
            }

            # print(f"Successfully authenticated! Token expires in {login_result.get('expires_in')} seconds")
            return login_result
        else:
            print(f"Authentication failed: {login.status_code}")
            print(login.text)
            return None
        
    def iata_search(self, city):
        """Return IATA Code for City"""
        city = city
        self.flight_login()
        iata_search_url = f"{self.api_url}/reference-data/locations/cities"
        
        iata_search_data = {
            "keyword": {city},
            "include": "AIRPORTS"
        }

        iata_search = requests.get(url=iata_search_url, headers=self.api_bearer, params=iata_search_data)
        return iata_search.json()["data"][0]["iataCode"]

    def flight_search(self, origin, destination, from_time, to_time, max_price=None, non_stop=True):
        """Return flight prices for round trip"""
        
        search_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        
        search_query = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "currencyCode": "GBP",
            "max": 10,
        }
        
        # Add maxPrice parameter if specified
        if max_price:
            search_query["maxPrice"] = max_price
        if non_stop:
            search_query["nonStop"] = "true"
        
        self.flight_login()
        flight_search = requests.get(url=search_url, headers=self.api_bearer, params=search_query)
        return flight_search.json()
