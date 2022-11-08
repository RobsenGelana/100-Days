import requests

APP_ID = "a8daa4e2"
APP_KEY = "6d1fcdaf606cafdb8ba55a5a036ea703"


page_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

http_header = {
    "x-app-id": APP_ID,
    'x-app-key': APP_KEY,
}

