import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


@app.route("/test/<num>")
def get_test(num):
    return f"<p>{num}</p>"


if __name__ == "__main__":
    app.run(debug=True)
