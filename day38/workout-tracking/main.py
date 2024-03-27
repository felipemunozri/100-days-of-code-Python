import os
import requests
from datetime import datetime
from dotenv import load_dotenv

GENDER = "male"
WEIGHT_KG = 75  # float
HEIGHT_CM = 176  # float
AGE = 34  # int


# ------------------------------- NUTRITIONIX NATURAL EXERCISE API ------------------------------- #

# The Nutritionix API (Natural Exercise) (see
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.aqn9u960gf9i) allows to
# pass exercise related data as text in natural language and returns information regarding an estimate of the calories
# burned for each exercise activity it detects. The only required key in the http post request body is the 'query',
# which is the text describing the exercise activities. Optionally we can pass information regarding age, sex, weight
# and height to obtain more accurate calories estimates
def get_nutritionix_exercise_info(user_input):
    """This function utilizes the Nutritionix API (Natural Exercise) (see
    https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.aqn9u960gf9i). This
    function receives a sting input describing exercises activities in natural language, gets the related info from the
    Nutritionix API endpoint, and then formats it to pass it to the add_exercises_to_spreadsheet() function."""
    load_dotenv()
    nutritionix_app_id = os.getenv("NUTRITIONIX_APP_ID")
    nutritionix_api_key = os.getenv("NUTRITIONIX_API_KEY")

    nat_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

    headers = {
        "x-app-id": nutritionix_app_id,
        "x-app-key": nutritionix_api_key,
        "Content-Type": "application/json"
    }

    exercise_data = {
        "query": user_input,  # required, description of the types of exercise the user performed
        "gender": GENDER,  # optional
        "weight_kg": WEIGHT_KG,  # optional
        "height_cm": HEIGHT_CM,  # optional
        "age": AGE
    }

    response = requests.post(url=nat_exercise_endpoint, headers=headers, json=exercise_data)
    response.raise_for_status()
    exercises_data = response.json()["exercises"]  # from the response we get the info inside the 'exercises' section

    # we will create a list to store a formatted dictionary for each of the exercise activities the api detected
    formatted_list = []
    for item in exercises_data:
        sheet_inputs = {  # sheety expect the inputs to be JSON payloads in the request body, so we create a dictionary
            # sheety also expects the records to be nested in a singular root property named after our spreadsheet, so,
            # for example, if our Google Spreadsheet is called 'Workouts' then the property name should be 'workout'
            "workout": {
                "date": datetime.now().strftime("%d/%m/%Y"),  # date as dd/mm/yy
                "time": datetime.now().strftime("%X"),  # time as our local time format
                "exercise": item["name"].title(),
                "duration": item["duration_min"],
                "calories": item["nf_calories"]
            }
        }
        formatted_list.append(sheet_inputs)  # append dict to list

    # call to add_exercises_to_spreadsheet() function passing the formatted_list
    add_exercises_to_spreadsheet(formatted_list)


# ------------------------------- SHEETY API ------------------------------- #

# The Sheety API (see https://sheety.co/docs/requests) allows to turn Google Spreadsheets into a Restful JSON API,
# meaning we can get data in and out of a spreadsheet using HTTP requests and URLs. To make it work first we need to
# manually create a Google Spreadsheet, give it a name, and add in the first row some column names. After that, we can
# create a 'new project' in Sheety passing the Google Spreadsheet url. Then we can manually select which operations are
# allowed (get, post, put, delete)
def get_info_from_spreadsheet():
    """This function utilizes the Sheety API (see https://sheety.co/docs/requests) to get info from a Google
    Spreadsheet."""
    load_dotenv()
    sheety_bearer_token = os.getenv("SHEETY_BEARER_TOKEN")
    sheety_endpoint = "https://api.sheety.co/cada709713ded3510e95bb2e5ff32f77/myWorkouts/workouts"

    headers = {
        "Authorization": sheety_bearer_token
    }

    response = requests.get(url=sheety_endpoint, headers=headers)
    response.raise_for_status()
    print(response.json())


def add_exercises_to_spreadsheet(formatted_data):
    """This function utilizes the Sheety API (see https://sheety.co/docs/requests) to write info into a Google
    Spreadsheet. It receives a list of dictionaries and for each item on this list it makes a post http request to the
    api endpoint passing the dictionary as the request body."""
    load_dotenv()
    sheety_bearer_token = os.getenv("SHEETY_BEARER_TOKEN")
    sheety_endpoint = "https://api.sheety.co/cada709713ded3510e95bb2e5ff32f77/myWorkouts/workouts"

    headers = {
        "Authorization": sheety_bearer_token
    }

    for item in formatted_data:
        response = requests.post(url=sheety_endpoint, headers=headers, json=item)
        response.raise_for_status()
        print(response.json())  # response contains de 'id' parameter which is equivalent to the row number in the sheet


# ------------------------------- MAIN PROGRAM ------------------------------- #

# get input from user
user_input = input("Tell me which exercises you did: ")

# call to get_nutri_exercise_info() function passing the user_input
get_nutritionix_exercise_info(user_input)
