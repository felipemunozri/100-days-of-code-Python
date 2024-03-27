from pprint import pprint
import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.sheety_headers = {"Authorization": SHEETY_BEARER_TOKEN}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=self.sheety_headers,
                json=new_data
            )
            print(response.text)
