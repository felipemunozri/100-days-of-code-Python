# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

DEP_CITY_NAME = "Santiago de Chile"  # departure city name Santiago, Chile

# create flight search, data manager and notification manager objects
f_search = FlightSearch()
d_manager = DataManager()
n_manager = NotificationManager()

# ----------------------------- READ CURRENT DATA FROM SPREADSHEET ----------------------------- #

spreadsheet_data = d_manager.get_info_from_spreadsheet()["prices"]
cities_list = [item["city"] for item in spreadsheet_data]
current_prices = [int(item["lowestPrice"]) for item in spreadsheet_data]

# ----------------------------- GET CITY IATA CODES  ----------------------------- #

dep_city_iata_code = f_search.get_city_iata_code(DEP_CITY_NAME)
cities_iata_codes_list = [f_search.get_city_iata_code(item) for item in cities_list]

# ----------------------------- POPULATE SPREADSHEET WITH IATA CODES ----------------------------- #

for index, destination in enumerate(spreadsheet_data):
    data_item = {
        "price": {
            "iataCode": cities_iata_codes_list[index]
        }
    }
    d_manager.update_info_to_spreadsheet(destination["id"], data_item)

# ----------------------------- GET NEW PRICES, COMPARE, UPDATE AND SEND EMAIL ----------------------------- #

# get new flight prices and compare them to see if they are lower than current ones in spreadsheet. If they are, then
# update them and send an email notification to the user
for destination in spreadsheet_data:
    search_result = f_search.search_flights(dep_city_iata_code, destination["iataCode"])
    if search_result is not None:
        if search_result["price"] < destination["lowestPrice"]:
            # format data to update spreadsheet
            data_item = {
                "price": {
                    "lowestPrice": search_result["price"]
                }
            }
            d_manager.update_info_to_spreadsheet(destination["id"], data_item)
            # format data to pass to notification manager
            message_item = {
                "flyFrom": search_result["flyFrom"],
                "cityFrom": search_result["cityFrom"],
                "flyTo": search_result["flyTo"],
                "cityTo": search_result["cityTo"],
                "price": search_result["price"],
                "local_departure": (search_result["local_departure"]).split('T')[0],
                "local_arrival": (search_result["local_arrival"]).split('T')[0]
            }
            n_manager.send_email(message_item)
