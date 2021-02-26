import requests
from datetime import datetime

GENDER = "YOUR GENDER"
WEIGHT_KG = "YOUR WEIGHT"
HEIGHT_CM = "YOUR HEIGHT"
AGE = "YOUR AGE"

# Nutritionix API
NUTRITIONIX_APP_ID = "YOUR APP_ID"
NUTRITIONIX_API_KEY = "YOUR API_KEY"
# Sheety.co API
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = "https://api.sheety.co/YOUR_SHEETY_WORKSHEET"

exercise_text = input("What exercise did you do: ")

param_header = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

parameters = {
     "query": exercise_text,
     "gender": GENDER,
     "weight_kg": WEIGHT_KG,
     "height_cm": HEIGHT_CM,
     "age": AGE
}

authorization_parameters = {
    "Authorization": "Basic YOUR AUTHORIZATION CODE"
}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=param_header)

time = datetime.now()
date = time.strftime("%d/%m/%Y")
hour = time.strftime("%H:%M:%S")

data = response.json()['exercises']

for exercise in data:
    sheety_parameter = {
        "sheet1": {
            "date": date,
            "time": hour,
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameter, headers=authorization_parameters)
