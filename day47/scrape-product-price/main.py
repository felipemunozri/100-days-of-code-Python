import datetime
import requests
import os
import smtplib
import lxml
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_APP_PASSWORD = os.getenv("SMTP_APP_PASSWORD")
TARGET_EMAIL = os.getenv("TARGET_EMAIL")
PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
BUY_PRICE = 100

headers = {
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
                  "Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/"
              "signed-exchange;v=b3;q=0.7"
}

response = requests.get(url=PRODUCT_URL, headers=headers)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "lxml")  # for this site we must use the lxml parser
# print(soup.prettify())

product_title = soup.find(name="h1", id="title").text
product_price = float(
    f"{soup.find(name='span', class_='a-price-whole').text}{soup.find(name='span', class_='a-price-fraction').text}")

print(product_title)
print(product_price)

if product_price < BUY_PRICE:
    message = f"Subject:Amazon Price Alert!\n\n{product_title} is now at ${product_price}\n{PRODUCT_URL}"
    with smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=SMTP_EMAIL, password=SMTP_APP_PASSWORD)
        connection.sendmail(
            from_addr=f"Smtp Test Email <{SMTP_EMAIL}>",
            to_addrs=f"User <{TARGET_EMAIL}>",
            msg=message.encode("utf-8")
        )
