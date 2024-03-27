import requests
from flask import Flask, render_template

app = Flask(__name__)


def query_api(url, name):
    query = {'name': name}
    response = requests.get(url=url, params=query)
    response.raise_for_status()
    return response.json()


@app.route("/")
def home():
    return ("<h1>Welcome to <u>Name Gender & Age Guesser</u>!</h1><br>"
            "<p>Add <u><b>/guess/yourname</b></u> to the url in your browser to get a guess of your <b>gender</b> and "
            "<b>age</b> based on your name.</p>")

 
@app.route('/guess/<name>')
def guess(name: str):
    name = name.title()
    age = query_api(url='https://api.agify.io', name=name)["age"]
    gender = query_api(url='https://api.genderize.io', name=name)["gender"]
    return render_template('guess.html', name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)
    