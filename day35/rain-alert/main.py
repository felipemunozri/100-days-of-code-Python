import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from twilio.rest import Client  # must install first


# Santiago latitude an longitude
MY_LAT = -33.448891
MY_LON = -70.669266

# Chiloe (almost always rainy) latitude and longitude
# MY_LAT = -42.727032
# MY_LON = -73.942703

# Open Weather API keys
load_dotenv()  # first load .env file to be able to read environmental variables
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
# DR_ANGELA_API_KEY = "69f04e4613056b159c2761a9d9e664d2"


# ------------------------------- Weekday Name Function ------------------------------- #
def get_weekday_name(days_from_today: int):
    """This functions receives an integer number as a number of days from today and returns the equivalent weekday
    name."""
    today = datetime.now()
    target_date = today + timedelta(days=days_from_today)  # adds the specified number of days to the current date
    weekday_name = target_date.strftime("%A")  # strftime("%A") formats the date as name of the weekday
    return weekday_name


# ------------------------------- Send Function ------------------------------- #
def send_telegram_message(message):
    """Function to send a notification message through a Telegram chat with a bot. It requeries to have created a
    Telegram bot and have access to its token and the chat ID number. See
    https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e and
    https://stackoverflow.com/questions/29003305/sending-telegram-message-from-python."""
    load_dotenv()
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot_chat_id = os.getenv("TELEGRAM_BOT_CHAT_ID")

    parameters = {
        "chat_id": bot_chat_id,
        "parse_mode": "Markdown",
        "text": message
    }

    response = requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage", params=parameters)
    print(response.json())


def send_twilio_sms():
    """Function to send an SMS message through the Twilio SMS Messaging API service. Not working at the moment due to
    Twilio restrictions with my account, bastards!"""
    # Find your Account SID and Auth Token at twilio.com/console and set the environment variables. See
    # http://twil.io/secure
    load_dotenv()
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_virtual_phone = os.getenv("TWILIO_VIRTUAL_PHONE")  # twilio virtual phone number is the message sender
    recipient_phone = os.getenv("RECIPIENT_PHONE")  # recipient phone number
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain today. Remember to bring an ☂",
                                     from_=twilio_virtual_phone,  # twilio virtual phone number is the message sender
                                     to=recipient_phone)  # my phone number is the recipient
    print(message.status)


# ------------------------------- OpenWeather Test API Call ------------------------------- #

# Tests call to the 'Current Weather by City Name' (deprecated but working) api from Open Weather. Just a test not used
# in this project
# parameters = {
#     "q": "Santiago",
#     "appid": API_KEY
# }
#
# res = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
# data = res.json()
# print(data)


# ------------------------------- Hourly Notifications Code ------------------------------- #

# # Call to the 'One Call 2.8' (current version 3.0 is paid) api from Open Weather. We use this one to get weather
# # information based on a specific location (lat, lon). This api service returns weather information regarding the
# # current weather conditions and minutely (1 hr), hourly (48 hours) and daily (8 days) weather predictions. We are
# # interested just in the hourly info
# parameters = {
#     "lat": MY_LAT,
#     "lon": MY_LON,
#     "exclude": "current,minutely,daily",  # optional parameter, used to exclude data from the api call
#     "appid": API_KEY
# }
#
# resp = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=parameters)
# resp.raise_for_status()
# weather_data = resp.json()
# next12 = weather_data["hourly"][:12]  # we slice the data to get weather predictions just for the next 12 hours
# # each hourly weather report has a weather list and within them there is one or more objects containing an 'id' key.
# # These 'weather ids' are codes ranging from 2xx up to 800 (see
# # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2). We are interested in weather ids below 700
# # which mean rainy conditions (or worst). If we found a rainy code within the next 12 hours report we will send an SMS
# # notification using Twilio
# if any(item["weather"][0]["id"] < 700 for item in next12):
#     # print("It's going to rain today. Remember to bring an ☂")
#     # send_twilio_sms()
#     message = "It's going to rain today. Remember to bring an ☂"
#     send_telegram_message(message)


# ------------------------------- Daily Notifications Code ------------------------------- #

# Call to the 'One Call 2.8' (current version 3.0 is paid) api from Open Weather. We use this one to get weather
# information based on a specific location (lat, lon). This api service returns weather information regarding the
# current weather conditions and minutely (1 hr), hourly (48 hours) and daily (8 days) weather predictions. We are
# interested just in the daily info
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,hourly",  # optional parameter, used to exclude data from the api call
    "appid": API_KEY
}

resp = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=parameters)
resp.raise_for_status()
weather_data = resp.json()
daily8 = weather_data["daily"]
# We are interested in weather ids below 700 which mean rainy conditions (or worst). If we found a rainy code within the
# next 8 days report we will send a chat notification using Telegram indicating the weekday and a brief description of
# the weather conditions for that day
going_to_rain = False
weekday = ""
weather_description = ""
for index, item in enumerate(daily8):
    if item["weather"][0]["id"] < 700:
        going_to_rain = True
        weekday = get_weekday_name(index)
        weather_description = item["weather"][0]["description"].title()
        break

# if true we send the message, else we do nothing
if going_to_rain:
    message = f"{weather_description} is forecasted for next {weekday}. Be sure to have an ☂ with you."
    send_telegram_message(message)
