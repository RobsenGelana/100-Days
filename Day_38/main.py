import requests
from datetime import datetime

APP_ID = "a8daa4e2"
APP_KEY = "6d1fcdaf606cafdb8ba55a5a036ea703"
GENDER = 'male'
WEIGHT = 68
HEIGHT = 173
AGE = 19

sheety_endpoint = "https://api.sheety.co/9b7ed0569a8dbb7098467e7c1f5484dc/myWorkOut/workouts"
page_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
user_input = input("Tell me which exercises you did: ")

http_header = {
    "x-app-id": APP_ID,
    'x-app-key': APP_KEY,
}

json_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=page_endpoint, json=json_params, headers=http_header)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheety_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheety_endpoint, 
                                json=sheety_input,   
                                auth=(
                                        "YOUR NAME", 
                                        " YOUR PASSWORD",
                                    )
                                    )

    print(sheet_response.text)