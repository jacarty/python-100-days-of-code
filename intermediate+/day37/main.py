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
