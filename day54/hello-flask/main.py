from flask import Flask

app = Flask(__name__)


# this decorator ensures that de hello_world() function only gets executed when the app is serving the root (/) url,
# aka. the homepage. This decorators are used by the flask framework
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "<p>Bye</p>"


# In a Python program, the if __name__ == "__main__": construct is used to determine whether the Python script is being
# run as the main program or if it is being imported as a module into another script.
# When a Python script is executed, the special built-in variable __name__ is set to "__main__" if the script is the
# entry point of the program.
# By using if __name__ == "__main__": we can write code that will only execute when the script is run directly and not
# when it's imported as a module.
if __name__ == "__main__":
    app.run()
