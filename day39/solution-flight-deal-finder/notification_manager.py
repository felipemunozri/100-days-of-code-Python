# from twilio.rest import Client
#
# TWILIO_SID = YOUR TWILIO ACCOUNT SID
# TWILIO_AUTH_TOKEN = YOUR TWILIO AUTH TOKEN
# TWILIO_VIRTUAL_NUMBER = YOUR TWILIO VIRTUAL NUMBER
# TWILIO_VERIFIED_NUMBER = YOUR TWILIO VERIFIED NUMBER
#
#
# class NotificationManager:
#
#     def __init__(self):
#         self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
#
#     def send_sms(self, message):
#         message = self.client.messages.create(
#             body=message,
#             from_=TWILIO_VIRTUAL_NUMBER,
#             to=TWILIO_VERIFIED_NUMBER,
#         )
#         # Prints if successfully sent.
#         print(message.sid)

import os
import smtplib
from dotenv import load_dotenv


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        load_dotenv()
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT"))
        self.smtp_email = os.getenv("SMTP_EMAIL")
        self.smtp_app_password = os.getenv("SMTP_APP_PASSWORD")
        self.target_email = os.getenv("TARGET_EMAIL")

    def send_email(self, message):
        """Function to send an email message to self.target_email using self.smtp_email. The function receives a
        message_info object with flight deals related info."""
        with smtplib.SMTP(host=self.smtp_server, port=self.smtp_port) as connection:
            connection.starttls()
            connection.login(self.smtp_email, self.smtp_app_password)
            connection.sendmail(
                from_addr=self.smtp_email,
                to_addrs=self.target_email,
                msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
            )
