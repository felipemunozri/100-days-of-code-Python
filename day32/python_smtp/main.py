# ------------------------------- USING GMAIL AS SMTP ------------------------------- #
# import smtplib
#
# smtp_email = "flpmnzsmtptestmail@gmail.com"
# smtp_app_password = "ohddiuzvmwvsvzrw"
# target_email = "felipemunozri@gmail.com"
#
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=smtp_email, password=smtp_app_password)
#     connection.sendmail(from_addr=smtp_email, to_addrs=target_email,
#                         # we must use Subject: to add an email subject and then add \n\n for the body of the email
#                         msg="Subject:TEST MAIL\n\nThis is a test mail from flpmnzsmtptestmail@gmail.com.")
#     # connection.close()  # we avoid using close() by using with

# ------------------------------- READING CREDENTIALS FROM A .ENV FILE ------------------------------- #
import os
import smtplib
from dotenv import load_dotenv  # must install python-dotenv library

# load_dotenv() loads all the variables found on an .env file as environmental variables. In this case .env file is in
# the root of the project, but we can pass an absolute path to the file's location
load_dotenv()

# we then read the environmental variables using os.getenv() and passing the name of the variable
smtp_email = os.getenv("SMTP_EMAIL")
smtp_app_password = os.getenv("SMTP_APP_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER")
port = int(os.getenv("PORT"))
target_email = "felipemunozri@gmail.com"

with smtplib.SMTP(smtp_server, port) as connection:
    connection.starttls()
    connection.login(user=smtp_email, password=smtp_app_password)
    connection.sendmail(from_addr=smtp_email, to_addrs=target_email,
                        msg="Subject:TEST MAIL\n\nThis is a test mail from flpmnzsmtptestmail@gmail.com.")
