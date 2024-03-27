import requests
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv


class FlightSearch:

    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv()
        self.kiwi_api_key = os.getenv("KIWI_API_KEY")
        self.current_date = datetime.now()
        self.six_months = self.current_date + relativedelta(months=+6)

    def get_city_iata_code(self, search_term):
        """This function utilizes the Tequila API (Locations) to search iata codes for a specific location, for example,
        city names. Receives a search_term (a city name, string) and returns the corresponding iata city code."""
        locations_api_endpoint = "https://api.tequila.kiwi.com/locations/query"

        headers = {
            "accept": "application/json",
            "apikey": self.kiwi_api_key
        }

        parameters = {
            "term": search_term,  # can search by iata, id, name or code of the location
            "locale": "en-US",  # language of the results
            # location_types accepted values: station, airport, bus_station, city, autonomous_territory, subdivision,
            # country, region, continent.To use more than one location_types, use multiple location_types
            "location_types": "airport",
            "limit": 3,  # number of results in output
            "active_only": "true",  # displays all active locations
            # "sort": "name"  # order of the output. For A->Z use 'sort: name', for Z->A use 'sort: -name'
        }

        response = requests.get(url=locations_api_endpoint, headers=headers, params=parameters)
        response.raise_for_status()
        # print(response.json())
        data = response.json()
        city_iata_code = data["locations"][0]["city"]["code"]
        return city_iata_code

    def search_flights(self, dep_city_iata_code, des_city_data_code):
        """This function utilizes the Tequila API (Search) to search flight itineraries from and to specific locations
        (see https://tequila.kiwi.com/portal/docs/tequila_api/search_api). The API accepts various parameters to
        customize search results. The parameters used here are the ones related to: departure location, arrival location
        , departure date, arrival date, price limit, type of currency and limit of search results. The function receives
        a departure city iata code and a destiny city iata code (both string), it then uses the current date and up to
        six months from current date to filter search results. The function filters the results even further to return
        the flight itinerary with the lowest price."""
        search_api_endpoint = "https://api.tequila.kiwi.com/v2/search"

        headers = {
            "accept": "application/json",
            "apikey": self.kiwi_api_key
        }

        parameters = {
            "fly_from": dep_city_iata_code,
            "fly_to": des_city_data_code,
            "date_from": self.current_date.strftime("%d/%m/%Y"),
            "date_to": self.six_months.strftime("%d/%m/%Y"),
            # "price_from": ,
            "price_to": 600,
            # "sort": "price",
            "limit": 3,
            "curr": "USD",
            # "locale": "en",
            # "vehicle_type": "aircraft",
            # "return_from": ,
            # "return_to": ,
            # "nights_in_dst_from": ,
            # "nights_in_dst_to": ,
            # "max_fly_duration": ,
            # "ret_from_diff_city": ,
            # "ret_to_diff_city": ,
            # "one_for_city": ,
            # "one_per_date": ,
            # "adults": ,
            # "children": ,
            # "infants": ,
            # "selected_cabins": ,
            # "mix_with_cabins": ,
            # "adult_hold_bag": ,
            # "adult_hand_bag": ,
            # "child_hold_bag": ,
            # "child_hand_bag": ,
            # "fly_days": ,
            # "fly_days_type": ,
            # "ret_fly_days": ,
            # "ret_fly_days_type": ,
            # "only_working_days": ,
            # "only_weekends": ,
            # "partner_market": ,
            # "dtime_from": ,
            # "dtime_to": ,
            # "atime_from": ,
            # "atime_to": ,
            # "ret_dtime_from": ,
            # "ret_dtime_to": ,
            # "ret_atime_from": ,
            # "ret_atime_to": ,
            # "stopover_from": ,
            # "stopover_to": ,
            # "max_stopovers": ,
            # "max_sector_stopovers": ,
            # "conn_on_diff_airport": ,
            # "ret_from_diff_airport": ,
            # "ret_to_diff_airport": ,
            # "select_airlines": ,
            # "select_airlines_exclude": ,
            # "select_stop_airport": ,
            # "select_stop_airport_exclude": ,
            # "enable_vi":
        }

        response = requests.get(url=search_api_endpoint, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()["data"]
        # prices_list = [item["price"] for item in data]
        # return prices_list

        # first we check if the returned list of flights is not empty. If it is not, then we obtain the min value among
        # them and return that item. If the list is empty we return None
        if data:
            min_price_flight = data[0]
            for item in data:
                if item["price"] < min_price_flight["price"]:
                    min_price_flight = item
            return min_price_flight
        else:
            return None
