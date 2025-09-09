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
