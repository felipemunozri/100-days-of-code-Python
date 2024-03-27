from flask import Flask

app = Flask(__name__)


def make_bold(f):
    def wrapper():
        rv = f()
        text = f'<b>{rv}</b>'
        return text
    return wrapper


def make_emphasis(f):
    def wrapper():
        rv = f()
        text = f'<em>{rv}</em>'
        return text
    return wrapper


def make_underlined(f):
    def wrapper():
        rv = f()
        text = f'<u>{rv}</u>'
        return text
    return wrapper

# # Alternative declaration for the style decorators
# def make_bold(function):
#     def wrapper():
#         return "<b>" + function() + "</b>"
#     return wrapper
#
# def make_emphasis(function):
#     def wrapper():
#         return "<em>" + function() + "</em>"
#     return wrapper
#
# def make_underlined(function):
#     def wrapper():
#         return "<u>" + function() + "</u>"
#     return wrapper


# We can render html code by simply returning it from our function in our desired route.
@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media3.giphy.com/media/1d99GLB20hS0OwYyqj/giphy.gif?cid'
            '=ecf05e47vxrh51gyer2hkw62efmcpyya77k6ggvh51sbmbj8&ep=v1_gifs_gifId&rid=giphy.gif&ct=g" width=200px>')


# We can also style our html code by applying decorators to the function that returns the html code. It's important to
# note that the style decorators must be applied below the @app.route() decorator but above the function we wish to
# decorate.
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "<h1>Bye!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
