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

###############
# Pixela Signup
###############

import requests
from dotenv import load_dotenv
import os

load_dotenv("../../.env")
PIXELA_API = os.getenv("PIXELA_API")
USERNAME = "j1m"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_API, 
    "username": USERNAME, 
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)