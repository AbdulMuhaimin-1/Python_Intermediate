import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("/home/abdul-muhaimin/Desktop/EnvVar/ENVVAR.env")

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

exercise_config = {
    "query" : exercise_text,
    "gender" : "male",
    "weight_kg" : 49.7,
    "height_cm" : 167.14,
    "age" : 28
}

header = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=header)
result = response.json()

sheet_endpoint = os.getenv("SHEET_ENDPOINT")
today = datetime.now()

sheet_body = {
    "workout": {
        "date": f"{today.strftime('%d/%m/%Y')}",
        "time": f"{today.strftime('%H:%M:%S')}",
        "exercise": f"{result['exercises'][0]['user_input']}".title(),
        "duration": f"{result['exercises'][0]['duration_min']}",
        "calories": f"{result['exercises'][0]['nf_calories']}"
    }
}

headers = {
    "Authorization" : f"Bearer {os.getenv('AUTH_TOKEN')}"
}

sheet_response = requests.post(url=sheet_endpoint, json=sheet_body, headers=headers)
print(sheet_response.text)