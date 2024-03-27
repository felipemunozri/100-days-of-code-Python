from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


# we can pass key-pair arguments to the render_template to be able to render variable values inside our html docs
@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template("index.html", year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
