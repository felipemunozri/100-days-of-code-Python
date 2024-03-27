import requests
import smtplib
from datetime import datetime
import config as cf
import time

MY_LAT = -33.448891  # Your latitude
MY_LONG = -70.669266  # Your longitude
LOCAL_UTC_OFFSET = datetime.utcnow().hour - datetime.now().hour


def send_email():
    """Function to send an email notification. It gets the smtp and recipients configuration values from the config.py
    file."""
    with smtplib.SMTP(cf.smpt_server, cf.smtp_port) as connection:
        connection.starttls()
        connection.login(cf.smpt_email, cf.smtp_app_password)
        connection.sendmail(from_addr=cf.smpt_email,
                            to_addrs=cf.target_email,
                            msg="Subject: ISS Overhead 🛰\n\nHey, go outside and look up! The ISS is passing over your "
                                "location right now.".encode("utf-8"))


def utc_to_local(utc_hour):
    """This function receives a UTC hour value and returns the hour at local time. A LOCAL_UTC_OFFSET constant must be
    created."""
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


def is_iss_overhead():
    """This function checks if the current ISS location is closer to our local location and if it is, then returns true.
    It utilizes the iss-now API to get the current ISS location."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Our position is within +5 or -5 degrees of the ISS position.
    # if iss_latitude in range(round(MY_LAT) - 5, round(MY_LAT) + 5) and iss_longitude in range(round(MY_LONG) - 5,
    #                                                                                           round(MY_LONG) + 5):
    #     return True
    # if MY_LAT-5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    #     return True
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True


def is_night():
    """This function checks if the current time is between the local sunset and sunrise hours, and if it is then returns
    true. It utilizes the sunrise-sunset.org API to get the local sunset and sunrise hours. We must provide the local
    latitude and longitude values as they are mandatory parameters for the api to work properly."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    lt_sunrise = utc_to_local(sunrise)
    lt_sunset = utc_to_local(sunset)
    time_now = int(datetime.now().hour)

    if time_now >= lt_sunset or time_now <= lt_sunrise:
        return True


while True:
    # If the ISS is close to my current position, and it is currently dark, then email me to tell me to look up.
    # BONUS: run the code every 1 hour.
    time.sleep(3600)
    if is_iss_overhead() and is_night():
        send_email()
