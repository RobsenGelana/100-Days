import requests

OPEN_WEATHER = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "310fe326d50b57e36ecf5172fa769264"
LAT = 9.145000
LON = 40.489674

weather = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key
}

response = requests.get(OPEN_WEATHER, params=weather)
response.raise_for_status()
print(response.json())
