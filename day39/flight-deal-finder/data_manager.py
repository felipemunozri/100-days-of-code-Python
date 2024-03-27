import os
import requests
from dotenv import load_dotenv


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.sheety_endpoint = "https://api.sheety.co/cada709713ded3510e95bb2e5ff32f77/flightDeals/prices"
        self.sheety_bearer_token = os.getenv("SHEETY_BEARER_TOKEN")
        self.sheety_headers = {"Authorization": self.sheety_bearer_token}

    def get_info_from_spreadsheet(self):
        """This function utilizes the Sheety API (see https://sheety.co/docs/requests) to get info from a Google
        Spreadsheet."""
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        response.raise_for_status()
        data = response.json()
        print(data)
        return data

    def add_info_to_spreadsheet(self, content):
        """This function utilizes the Sheety API (see https://sheety.co/docs/requests) to add info to a Google
        Spreadsheet."""
        response = requests.post(url=self.sheety_endpoint, headers=self.sheety_headers, json=content)
        response.raise_for_status()
        print(response.json())

    def update_info_to_spreadsheet(self, object_id, content):
        """This function utilizes the Sheety API (see https://sheety.co/docs/requests) to update info to a Google
        Spreadsheet. It requires the object_id as it is used at the endpoint url to be able to locate which element must
        be updated."""
        update_endpoint = f"{self.sheety_endpoint}/{object_id}"
        response = requests.put(url=update_endpoint, headers=self.sheety_headers, json=content)
        response.raise_for_status()
        print(response.json())
