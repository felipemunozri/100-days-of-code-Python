# ------------------ Extra Hard Starting Project ------------------ #
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import os
import random
import pandas as pd
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# get current day
current_day = dt.datetime.now().day
current_month = dt.datetime.now().month

# read .csv data
try:
    df = pd.read_csv("birthdays.csv")
except FileNotFoundError as error_message:
    print(error_message)
else:
    person_name = ""
    person_email = ""
    for index, item in df.iterrows():  # this will work for more than one person if they share the same birthday date
        # if current_day and current_month are equal to day and month in data then return the person's name and email
        if item["day"] == current_day and item["month"] == current_month:
            person_name = item["name"]
            person_email = item["email"]

        # get a copy of random letter and edit it by adding person_name
        rand_num = str(random.randint(1, 3))
        try:
            with open(f"./letter_templates/letter_{rand_num}.txt", "r") as letter:
                new_letter = letter.read().replace("[NAME]", person_name)
        except FileNotFoundError as error_message:
            print(error_message)
        else:
            # read mail data from .env file
            if not load_dotenv():
                print(".env file not found")
            else:
                smtp_email = os.getenv("SMTP_EMAIL")
                smtp_app_password = os.getenv("SMTP_APP_PASSWORD")
                smtp_server = os.getenv("SMTP_SERVER")
                port = os.getenv("PORT")

                # Create a MIMEText object for the message
                message = MIMEMultipart()
                message['From'] = f"Smtp Test Mail <{smtp_email}>"
                message['To'] = f"{person_name} <{person_email}>"
                message['Subject'] = "Happy Birthday!"

                # Attach the message content
                message.attach(MIMEText(new_letter, 'plain'))

                # send email
                with smtplib.SMTP(smtp_server, int(port)) as connection:
                    connection.starttls()
                    connection.login(smtp_email, smtp_app_password)
                    connection.sendmail(from_addr=smtp_email, to_addrs=person_email,
                                        # msg=f"Subject:Happy Birthday!\n\n{new_letter}".encode("utf-8"))
                                        msg=message.as_string())
