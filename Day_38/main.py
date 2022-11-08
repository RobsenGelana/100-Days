import requests

APP_ID = "a8daa4e2"
APP_KEY = "6d1fcdaf606cafdb8ba55a5a036ea703"
GENDER = 'male'
WEIGHT = 68
HEIGHT = 173
AGE = 19

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
print(response.text)