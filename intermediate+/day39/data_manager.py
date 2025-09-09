import pandas as pd

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.df = pd.read_csv("./location_data.csv")

    def read_cities(self):
        """Create a list of all Cities in the CSV file"""
        self.cities = [city for city in self.df["City"]]
        self.city_code = [city for city in self.df["IATA_Code"]]
        return self.city_code
    
    def update_iata_code(self, city, iata_code):
        """Update the CSV IATA_Code for given City"""
        city = city.title()
        iata_code = iata_code.upper()
    
        mask = self.df['City'] == city

        if mask.any():
            self.df.loc[mask, 'IATA_Code'] = iata_code
            self.df.to_csv("./location_data.csv", index=False)
            return self.df
        else:
            return False

    def cheaper_flight(self, city, flights):
        """
        Compare the flight data supplied with Target Price.
        If the price is cheaper return the details.
        """

        # Trim to get data
        flight_list = flights.get('data', [])
    
        # If no flights, return no flights
        if not flight_list:
            return "No flights found"

        cheapest_flight = min(flight_list, key=lambda x: float(x['price']['total']))

        # Set lookup to City IATA Code         
        mask = self.df['IATA_Code'] == city  
        
        if not mask.any():
            return f"City code {city} not found in DataFrame"
    
        # Get target price from data
        target_price = self.df.loc[mask, 'Lowest_Price'].values[0]

        if float(cheapest_flight['price']['total']) < float(target_price):

            price = cheapest_flight['price']['total']
            departure_airport_code = cheapest_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
            arrival_airport_code = cheapest_flight['itineraries'][0]['segments'][-1]['arrival']['iataCode']
            outbound_date = cheapest_flight['itineraries'][0]['segments'][0]['departure']['at']
            inbound_date = cheapest_flight['itineraries'][1]['segments'][-1]['arrival']['at']

            return f"""
            Price: {price}
            Departure Airport: {departure_airport_code}
            Arrival Airport: {arrival_airport_code}
            Outbound Date: {outbound_date}
            Inbound Date: {inbound_date}
            """
        
        else:
            return "No cheaper flights found"
