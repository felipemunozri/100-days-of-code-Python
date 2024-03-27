import os
import requests
from datetime import date, timedelta
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"  # Tesla Inc
# STOCK_NAME = "UPTD"
# COMPANY_NAME = "TradeUP"
ARROWS = ["🔺", "🔻"]


# ------------------------------- Get Stock Values ------------------------------- #

# We are going to use the Alpha Vantage (TIME_SERIES_DAILY) API which returns a daily values (date, daily open, daily
# high, daily low, daily close, daily volume) of the equity (STOCK) specified. We are interested just in the closing
# values of yesterday and the day before yesterday. When STOCK price increase/decreases by 5% between those days then we
# execute the next function to get the latest news regarding this company
def get_stock_values(stock_name):
    """This function utilizes de Alpha Vintage API (see https://www.alphavantage.co/documentation/) to get the closing
    values of yesterday and the day before yesterday for the specified STOCK equity. Compares both values and if it
    detects a difference greater than a specified percentage, then it will trigger a function to get the latest news for
    that company."""
    load_dotenv()
    alpha_vantage_key = os.getenv("ALPHA_VANTAGE_KEY")
    ytd = str(date.today() - timedelta(days=1))  # yesterday date
    db_ytd = str(date.today() - timedelta(days=2))  # day before yesterday date

    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_name,
        "apikey": alpha_vantage_key
    }

    response = requests.get("https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    daily_data = response.json()["Time Series (Daily)"]
    ytd_close = float(daily_data[ytd]["4. close"])  # yesterday close value
    db_ytd_close = float(daily_data[db_ytd]["4. close"])  # day before yesterday close value
    print(ytd_close)  # debug only
    print(db_ytd_close)  # debug only

    diff = ytd_close - db_ytd_close
    percent = round((diff / ytd_close) * 100, 2)
    print(f"diff: {diff}")  # debug only
    print(f"percent: {percent}")  # debug only

    # percent = 3  # debug only

    if percent > 4:  # if percent was greater than 4 and positive then pass the percentage and the 🔺 icon
        print("pass")  # debug only
        get_news(abs(percent), ARROWS[0])
    elif percent < -4:  # if percent was greater than 4 but negative then pass the 🔻 icon
        get_news(abs(percent), ARROWS[1])
        print("pass")  # debug only


# ------------------------------- Get Latest News ------------------------------- #

# We'll be using the NewsAPI API (everything) to get the latest top headlines regarding the company owner of the
# stocks we are monitoring. Once we get the headlines, we'll be formatting them as messages to pass them to the
# send_telegram_message() function

def get_news(percentage, icon):
    """This function utilizes the NewsAPI (everything) API (see https://newsapi.org/docs) to get the top headlines
    from different news sources regarding the company owner of the stocks we are monitoring. It receives a percentage
    value and an icon to concatenate to the retrieved headlines and format a list of messages to pass to the
    send_telegram_message() function."""
    load_dotenv()
    parameters = {
        "q": COMPANY_NAME,
        "searchIn": "title,description",
        "language": "en",
        "pageSize": 3,
        "apiKey": os.getenv("NEWSAPI_KEY")
    }

    res = requests.get("https://newsapi.org/v2/everything", params=parameters)
    res.raise_for_status()
    articles = res.json()["articles"]
    # print(articles)  # debug only

    # USING TELEGRAM MESSAGES
    messages = []
    for article in articles:
        if article["title"] is not None:  # check if the retrieved headline actually has info in it
            message = f"{STOCK_NAME}: {icon}{percentage}% \nHeadline: {article['title']}\nUrl: {article['url']}"
            messages.append(message)
        else:
            print("no news")  # debug only
    send_telegram_message(messages)

    # USING EMAIL MESSAGES
    # email_messages = []
    # for article in articles:
    #     subject = f"{STOCK_NAME}:{icon}{percentage}% ,{article['title']}"
    #     body = f"{article['description']}\n\n{article['url']}"
    #     message = EmailMessage()
    #     message.add_header("From", f"Smtp Test Mail <{os.getenv('SMTP_EMAIL')}>")
    #     message.add_header("To", f"Subscriber <{os.getenv('TARGET_EMAIL')}>")
    #     message.add_header("Subject", subject)
    #     message.set_payload(body, "utf-8")
    #     email_messages.append(message)
    # send_email_message(email_messages)


# ------------------------------- Send Messages ------------------------------- #

# We'll send separate messages with the percentage change and each article's title and url through a Telegram bot
def send_telegram_message(messages):
    """Function to send a notification message through a Telegram chat with a bot. It requeries to have created a
    Telegram bot and have access to its token and the chat ID number. See
    https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e and
    https://stackoverflow.com/questions/29003305/sending-telegram-message-from-python."""
    load_dotenv()
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot_chat_id = os.getenv("TELEGRAM_BOT_CHAT_ID")

    for message in messages:
        parameters = {
            "chat_id": bot_chat_id,
            "parse_mode": "Markdown",
            "text": message
        }
        response = requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage", params=parameters)
        print(response.json())


def send_email_message(email_messages):
    load_dotenv()
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))
    smtp_email = os.getenv("SMTP_EMAIL")
    target_email = os.getenv("TARGET_EMAIL")
    for message in email_messages:
        with smtplib.SMTP(host=smtp_server, port=smtp_port) as connection:
            connection.starttls()
            connection.login(user=smtp_email, password=os.getenv("SMTP_APP_PASSWORD"))
            connection.send_message(message, from_addr=smtp_email, to_addrs=target_email)


# call to get_stock_values() function. Could use a list of stocks and for each element call the function
get_stock_values(STOCK_NAME)
