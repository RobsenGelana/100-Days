import requests

import os
from twilio.rest import Client

#using open weather map api to get access for the weather conditions
OPEN_WEATHER = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "YOUR API"
LAT = 51.507351
LON = -0.127758

#GETTING THIS FROM TWILIO
account_sid = os.environ['Your Account SID']
auth_token = os.environ['YOUR AUTH TOKEN']

weather = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OPEN_WEATHER, params=weather)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_data:
    condition = hour_data['weather'][0]['id']

    if int(condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              body='It is going to rain to day so get your umbrella',
                              from_='+13023054130',
                              to='Your verified Phone number'
                          )

    print(message.status)
