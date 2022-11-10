import requests

sheety_endpoint = "https://api.sheety.co/9b7ed0569a8dbb7098467e7c1f5484dc/copyOfFlightDeals/prices"

class DataManager:
    def __init__(self):
        pass
    #This class is responsible for talking to the Google Sheet.
    def get_initial_data(self):
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        print(data)

DataManager()

