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

    def send_email(self, message_info):
        """Function to send an email message to self.target_email using self.smtp_email. The function receives a
        message_info object with flight deals related info."""
        message = f"Low price alert! Only {message_info['price']} to fly from {message_info['cityFrom']}-"
        f"{message_info['flyFrom']} to {message_info['cityTo']}-{message_info['flyTo']}, from "
        f"{message_info['local_departure']} to {message_info['local_arrival']}"

        f"Subject:New Low Price Flight!\n\n{message}"
        
        with smtplib.SMTP(host=self.smtp_server, port=self.smtp_port) as connection:
            connection.starttls()
            connection.login(self.smtp_email, self.smtp_app_password)
            connection.sendmail(
                from_addr=self.smtp_email,
                to_addrs=self.target_email,
                msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
            )
