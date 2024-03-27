from datetime import datetime

import requests
from flask import Flask, render_template

from post import Post

current_year = datetime.now().year

app = Flask(__name__)


def get_posts():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status()
    blog_posts = response.json()
    return blog_posts


@app.route('/')
def home():
    blog_posts = get_posts()
    return render_template("index.html", posts=blog_posts, year=current_year)


@app.route("/blog/<num>")
def get_blog(num):
    post_number = int(num) - 1
    blog_posts = get_posts()
    post = Post(blog_posts[post_number])
    return render_template("post.html", post=post, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
