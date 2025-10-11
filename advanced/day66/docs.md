Cafe API Documentation
Base URL: http://127.0.0.1:5000

1. Get Random Cafe
Returns a random cafe from the database.
Endpoint: GET /random
Parameters: None
Response:
Success (200):
json{
  "cafe": {
    "id": 1,
    "name": "Science Gallery London",
    "map_url": "https://g.page/scigallerylon?share",
    "img_url": "https://atlondonbridge.com/...",
    "location": "London Bridge",
    "seats": "50+",
    "has_toilet": true,
    "has_wifi": false,
    "has_sockets": true,
    "can_take_calls": true,
    "coffee_price": "£2.40"
  }
}
Not Found (404):
json{
  "error": {
    "Not Found": "No cafes in the database."
  }
}

2. Get All Cafes
Returns all cafes in the database, ordered by name.
Endpoint: GET /all
Parameters: None
Response:
Success (200):
json{
  "cafes": [
    {
      "id": 1,
      "name": "Ace Hotel Shoreditch",
      "map_url": "https://g.page/acehotellondon?share",
      "img_url": "https://...",
      "location": "Shoreditch",
      "seats": "50+",
      "has_toilet": true,
      "has_wifi": true,
      "has_sockets": true,
      "can_take_calls": false,
      "coffee_price": "£3.00"
    },
    {
      "id": 2,
      "name": "Another Cafe",
      "...": "..."
    }
  ]
}

3. Search Cafes by Location
Search for cafes in a specific location.
Endpoint: GET /search
Query Parameters:

loc (string, required) - The location to search for (e.g., "Peckham", "Shoreditch")

Example Request:
GET /search?loc=Peckham
Response:
Success (200):
json{
  "cafes": [
    {
      "id": 2,
      "name": "Social - Copeland Road",
      "map_url": "https://g.page/CopelandSocial?share",
      "img_url": "https://...",
      "location": "Peckham",
      "seats": "20-30",
      "has_toilet": true,
      "has_wifi": true,
      "has_sockets": true,
      "can_take_calls": false,
      "coffee_price": "£2.75"
    }
  ]
}
Not Found (404):
json{
  "error": {
    "Not Found": "No cafes in the database."
  }
}

4. Add New Cafe
Add a new cafe to the database.
Endpoint: POST /add
Content-Type: application/x-www-form-urlencoded
Form Data Parameters:

name (string, required) - Cafe name
map_url (string, required) - Google Maps URL
img_url (string, required) - Image URL
location (string, required) - Location/neighborhood
seats (string, required) - Number of seats (e.g., "20-30", "50+")
sockets (boolean, optional) - Has power sockets
toilet (boolean, optional) - Has toilet
wifi (boolean, optional) - Has WiFi
calls (boolean, optional) - Can take calls
coffee_price (string, optional) - Price of coffee (e.g., "£2.50")

Example Request:
POST /add
Content-Type: application/x-www-form-urlencoded

name=New Cafe&map_url=https://maps.google.com&img_url=https://example.com/image.jpg&location=Shoreditch&seats=30-40&sockets=true&toilet=true&wifi=true&calls=false&coffee_price=£3.50
Response:
Success (200):
json{
  "response": {
    "success": "Successfully added the new cafe."
  }
}

5. Update Cafe Coffee Price
Update the coffee price for a specific cafe.
Endpoint: PATCH /update-price/<cafe_id>
URL Parameters:

cafe_id (integer, required) - The ID of the cafe to update

Query Parameters:

new_price (string, required) - The new coffee price (e.g., "£5.67")

Example Request:
PATCH /update-price/1?new_price=£5.67
Response:
Success (200):
json{
  "response": {
    "success": "Successfully updated the price."
  }
}
Not Found (404):
json{
  "error": {
    "Not Found": "Sorry a cafe with that id was not found in the database."
  }
}

6. Delete Cafe (Report Closed)
Delete a cafe from the database. Requires API key authentication.
Endpoint: DELETE /report-closed/<cafe_id>
URL Parameters:

cafe_id (integer, required) - The ID of the cafe to delete

Query Parameters:

api-key (string, required) - API key for authentication (value: "TopSecretAPIKey")

Example Request:
DELETE /report-closed/1?api-key=TopSecretAPIKey
Response:
Success (200):
json{
  "response": {
    "success": "Successfully deleted the cafe from the database."
  }
}
Not Found (404):
json{
  "error": {
    "Not Found": "Sorry a cafe with that id was not found in the database."
  }
}
Forbidden (403):
json{
  "error": {
    "Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."
  }
}

Testing with cURL
Get Random Cafe
bashcurl http://127.0.0.1:5000/random
Get All Cafes
bashcurl http://127.0.0.1:5000/all
Search Cafes
bashcurl "http://127.0.0.1:5000/search?loc=Peckham"
Add New Cafe
bashcurl -X POST http://127.0.0.1:5000/add \
  -d "name=Test Cafe" \
  -d "map_url=https://maps.google.com" \
  -d "img_url=https://example.com/image.jpg" \
  -d "location=Shoreditch" \
  -d "seats=20-30" \
  -d "sockets=true" \
  -d "toilet=true" \
  -d "wifi=true" \
  -d "calls=false" \
  -d "coffee_price=£2.80"
Update Price
bashcurl -X PATCH "http://127.0.0.1:5000/update-price/1?new_price=£5.67"
Delete Cafe
bashcurl -X DELETE "http://127.0.0.1:5000/report-closed/1?api-key=TopSecretAPIKey"

Notes

All boolean fields in POST requests should be sent as strings ("true" or omitted)
The search endpoint currently only returns exact location matches (case-sensitive)
The API key for deletion is hardcoded as "TopSecretAPIKey" (should be changed in production)