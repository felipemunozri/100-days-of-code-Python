from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "<p>Bye!</p>"


# We can use variables inside an url path by putting the name of our variable between <> (in this example <name> is our
# variable). Then, we can use that variable inside our code. We could also put more paths after a variable inside a url
# route. For example, we could use something like "/username/<name>/someroute" and it will work Ok.
@app.route("/username/<name>")
def greeting(name):
    return f"<p>Hello {name}!</p>"


# This should give us an error because we are passing the variable <username> instead of <name> to the greeting2()
# function and it is expecting name not username. In this type of cases is vital the use of the debugger.
@app.route("/someroute2/<username>")
def greeting2(name):
    return f"<p>Hello {name}!</p>"


# This should also give us an error because we are trying to concatenate a str to an int. The debugger also warns us
# about this type of errors inside our code
@app.route("/someroute3/<name>")
def greeting3(name):
    return f"<p>Hello {name + 34}!</p>"


# There is another functionality called converter which allow us to specify the type of variable that we are passing.
# By default, when we declare a variable it uses a converter of type string which accepts any text without a slash, as
# the / character is used to separate paths in the url route. If for some reason we need to preserve the / characters in
# our variable we can specify a converter of type <path: > accompanied by the name of our variable. In this example we
# our converter is <path:name>.
@app.route("/someroute4/<path:name>")
def greeting4(name):
    return f"<p>Hello {name} you kept the slash character.</p>"


# Similarly, and as explained before, we can use a converter to specify the type of a variable (int, float, string, path
# or uuid).
@app.route("/someroute5/<name>/<int:age>")
def greeting5(name, age):
    return f"<p>Hello {name}! You are {age} years old.</p>"


if __name__ == "__main__":
    # Here we can set the debug mode for the server to True. This among other useful utilities, allows the server to
    # auto-refresh itself, so we don't need to stop and start the app every time we want to see our changes in the code
    # reflected. All we need to do for the server to detect this changes and automatically reload itself is to save our
    # changes to the file. The debugger also provides us with a PIN number to access an online console directly in the
    # browser. This PIN number appears in the Pycharm console when we run our program.
    app.run(debug=True)
