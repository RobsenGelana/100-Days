#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
sheety_endpoint = "https://api.sheety.co/9b7ed0569a8dbb7098467e7c1f5484dc/copyOfFlightDeals/prices"

response = requests.get(url=sheety_endpoint)
pprint(response.text)