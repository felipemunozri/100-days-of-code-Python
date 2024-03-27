from random import randint
from flask import Flask

START_GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

number = randint(0, 9)
print(number)

app = Flask(__name__)


@app.route("/")
def main():
    return (f'<h1>Guess a number between 0 and 9</h1>'
            f'<img src={START_GIF}>')


@app.route("/<int:guess>")
def check_answer(guess):
    if guess < number:
        return (f'<h1 style="color: red">Too low, try again</h1>'
                f'<img src={LOW}>')
    elif guess > number:
        return (f'<h1 style="color: purple">Too high, try again</h1>'
                f'<img src={HIGH}>')
    else:
        return (f'<h1 style="color: green">You found me!</h1>'
                f'<img src={CORRECT}>')


if __name__ == "__main__":
    app.run(debug=True)

# ---------------------------------- Alternative Solution ---------------------------------- #

# from flask import Flask
# from random import randint
#
# app = Flask(__name__)
#
# START_GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
# HIGH = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
# LOW = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
# CORRECT = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
#
#
# def style_decorator(function):
#     def wrapper(**kwargs):
#         text = function(**kwargs)
#         if function.__name__ == 'guess_number':
#             if 'low' in text:
#                 text_color = 'red'
#                 gif_link = LOW
#             elif 'high' in text:
#                 text_color = 'purple'
#                 gif_link = HIGH
#             else:
#                 text_color = 'green'
#                 gif_link = CORRECT
#         else:
#             text_color = 'black'
#             gif_link = START_GIF
#         return (f'<h1 style="color:{text_color}">{text}</h1>'
#                 f'<img src="{gif_link}">')
#
#     return wrapper
#
#
# @app.route('/', endpoint='start_game')
# @style_decorator
# def start_game():
#     return 'Guess a number between 0 and 9'
#
#
# @app.route('/<int:n>', endpoint='guess_number')
# @style_decorator
# def guess_number(n):
#     if n < number:
#         text = 'Too low, try again!'
#     elif n > number:
#         text = 'Too high, try again!'
#     else:
#         text = 'You found me!'
#     return text
#
#
# if __name__ == '__main__':
#     number = randint(0, 9)
#     print(number)
#     app.run(debug=True)
