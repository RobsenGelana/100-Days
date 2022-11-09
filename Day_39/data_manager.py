import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    sheety_endpoint = "https://api.sheety.co/9b7ed0569a8dbb7098467e7c1f5484dc/copyOfFlightDeals/prices"

    response = requests.get(url=sheety_endpoint)
    print(response.text)

