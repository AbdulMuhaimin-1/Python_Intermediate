import requests
from pprint import pprint

SHEET_ENDPOINT = "https://api.sheety.co/c12c29a1f07b4968879ea743d993f97b/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,):
        self.destination_data = {} # empty dictionary, to receive all data in the prices key

    def get_data_destination(self):
        response = requests.get(url=SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data # returns all the data under the prices key in the dictionary

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price" : {
                    "iataCode": f"{city['iataCode']}"
                }
            }

            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json = new_data)
            print(response.text)

DataManager()

