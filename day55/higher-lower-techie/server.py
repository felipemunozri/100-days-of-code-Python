from flask import Flask, render_template
from random import randint

START_GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

number = randint(0, 9)
print(number)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", color="black", message="Guess a number between 0 and 9",
                           gif_url=START_GIF)


@app.route("/<int:guess>")
def check_guess(guess):
    if guess < number:
        color = "red"
        message = f"Too low, try again!"
        gif_url = LOW
        alt = "too low, gif"
    elif guess > number:
        color = "purple"
        message = f"Too high, try again!"
        gif_url = HIGH
        alt = "too high, gif"
    else:
        color = "green"
        message = f"You found me!"
        gif_url = CORRECT
        alt = "correct, gif"

    return render_template("index.html", color=color, message=message, gif_url=gif_url, alt=alt)


if __name__ == '__main__':
    app.run(debug=True)
