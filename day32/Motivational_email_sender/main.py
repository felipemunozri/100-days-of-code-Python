import datetime as dt
import os
import smtplib
from dotenv import load_dotenv  # must install python-dotenv library
from random import choice

# check current weekday, if friday send email
current_weekday = dt.datetime.now().weekday()

if current_weekday == 0:  # 0 means monday

    # get random quote
    with open("quotes.txt", "r") as f:
        quotes_list = f.readlines()
    rand_quote = choice(quotes_list)

    # send email
    load_dotenv()
    smtp_email = os.getenv("SMTP_EMAIL")
    smtp_app_password = os.getenv("SMTP_APP_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    port = int(os.getenv("PORT"))
    target_email = "felipemunozri@gmail.com"

    with smtplib.SMTP(smtp_server, port) as connection:
        connection.starttls()
        connection.login(user=smtp_email, password=smtp_app_password)
        connection.sendmail(from_addr=smtp_email, to_addrs=target_email,
                            msg=f"Subject:Monday Motivation\n\n{rand_quote}".encode("utf-8"))
