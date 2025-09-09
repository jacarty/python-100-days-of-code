"""
Exercise energy tracking with Python

I didnt want to sign up to Sheetly and provide access to Google
"""

######################
# Imports
######################

from dotenv import load_dotenv
import os
import requests

######################
# Load local ENVs
######################

load_dotenv("../../.env")
NUTRITIONIX_APP_ID= os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY= os.getenv("NUTRITIONIX_API_KEY")

######################
# URLs
######################

exercise_api = "https://trackapi.nutritionix.com/v2/natural/exercise"

######################
# Exercise Auth Header
######################

exercise_headers = {
    "x-app-id": NUTRITIONIX_APP_ID, 
    "x-app-key": NUTRITIONIX_API_KEY
}

######################
# Exercise Query
######################

exercise_query = str(input("What exercise did you do?: "))
weight = int(input("What is your weight in kg?: "))
height = float(input("What is your height in cm?: "))
age= str(input("How old are you?: "))

exercise_params = {
    "query": exercise_query,
    "gender": "male",
	"weight_kg": weight,
	"height_cm": height,
    "age": age	
}

response = requests.post(headers=exercise_headers, url=exercise_api, json=exercise_params)
result = response.json()
print(result)
