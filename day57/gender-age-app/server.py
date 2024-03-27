import requests
from flask import Flask, render_template

app = Flask(__name__)

# api endpoint
AGIFY_ENDPOINT = "https://api.agify.io"
GENDERIZE_ENDPOINT = "https://api.genderize.io"


# guess_gender and guess_age functions
def guess_gender(name):
    """This function utilizes the Genderize API (see: https://genderize.io/) to guess the gender of a provided name. The
    function receives a name and returns a gender (both str)."""
    parameters = {"name": name}
    response = requests.get(url=GENDERIZE_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()
    guessed_gender = data["gender"]
    # print(guessed_gender)  # debug only
    return guessed_gender


def guess_age(name):
    """This function utilizes the Agify API (see: https://agify.io/) to guess the gender of a provided name. The
    function receives a name and returns an age (both str)."""
    parameters = {"name": name}
    response = requests.get(url=AGIFY_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()
    guessed_age = data["age"]
    # print(guessed_age)  # debug only
    return guessed_age


# main program
@app.route("/")
def home():
    return ("<h1>Welcome to <u>Name Gender & Age Guesser</u>!</h1><br>"
            "<p>Add <u><b>/guess/yourname</b></u> to the url in your browser to get a guess of your <b>gender</b> and "
            "<b>age</b> based on your name.</p>")


# guess results webpage route
@app.route("/guess/<name>")
def guess(name):
    gender = guess_gender(name)
    age = guess_age(name)
    return render_template("index.html", name=name.title(), gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
