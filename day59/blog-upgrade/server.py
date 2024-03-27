import os
import smtplib
from datetime import datetime

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

MY_BLOG_URL = "https://api.npoint.io/e062d2b05e77cfbfe2a1"
load_dotenv()
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_APP_PASS = os.getenv("SMTP_APP_PASS")
TARGET_EMAIL = os.getenv("TARGET_EMAIL")

current_year = datetime.now().year

app = Flask(__name__)


def get_posts_data():
    response = requests.get(MY_BLOG_URL)
    response.raise_for_status()
    blog_posts = response.json()
    return blog_posts


def send_email(message):
    load_dotenv()
    with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=SMTP_EMAIL, password=SMTP_APP_PASS)
        connection.sendmail(
            # from_addr=f"Smtp Test Mail <{SMTP_EMAIL}>",
            # to_addrs=f"User <{TARGET_EMAIL}>",
            from_addr=SMTP_EMAIL,
            to_addrs=TARGET_EMAIL,
            msg=f"Subject:New Contact\n\n{message}".encode("utf-8")
        )


@app.route("/")
def home():
    blog_posts = get_posts_data()
    return render_template("index.html", year=current_year, posts=blog_posts)


@app.route("/about")
def about():
    return render_template("about.html", year=current_year)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    print(request.method)
    if request.method == "GET":
        heading_message = "Contact Me"
        return render_template("contact.html", heading_message=heading_message, year=current_year)
    elif request.method == "POST":
        heading_message = "Successfully sent your message!"
        form_data = (f"Name: {request.form['name']}\n"
                     f"Email: {request.form['email']}\n"
                     f"Phone: {request.form['phone']}\n"
                     f"Message: {request.form['message']}")
        print(form_data)
        send_email(form_data)
        return render_template("contact.html", heading_message=heading_message, year=current_year)


@app.route("/post/<int:num>")
def get_post(num):
    blog_posts = get_posts_data()
    post = blog_posts[num - 1]
    return render_template("post.html", blog_post=post, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
