import requests

sheety_endpoint = "https://api.sheety.co/9b7ed0569a8dbb7098467e7c1f5484dc/copyOfFlightDeals/prices"

class DataManager:
    def __init__(self):
        self.initial = {}
    #This class is responsible for talking to the Google Sheet.
    def get_initial_data(self):
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.initial = data['prices']
        return self.initial



