'''
Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

from flask import Flask, render_template
# library to integrate Flask and WTForms. Includes functionalities to secure forms with CSRF protection
from flask_wtf import FlaskForm
# library to create html forms but using python instead of writing them with html. Includes validators functionalities
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import os
from flask_bootstrap import Bootstrap5


# first we must create a class which inherits from FlaskForm. Inside we create our input fields specifying their type,
# label and validators (list)
class LoginForm(FlaskForm):
    email = EmailField(label="email", validators=[DataRequired(), Email(check_deliverability=True)])
    password = PasswordField(label="password",
                             # render_kw={"style": "width: 30ch"},  # render_kw allows to pass a dict. of kwargs to render
                             validators=[DataRequired(), Length(min=8, max=16)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
SECRET_KEY = os.urandom(32)  # we pass this secret key to app.secret_key to be able to use csrf protection in forms
app.secret_key = SECRET_KEY
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()  # instance of our class to pass to our login template
    # validate_on_submit() implements our form validations, without this line they will not work. We can use the
    # returned value from validate_on_submit() to redirect to the next webpage, similarly to when we evaluated if
    # request.method == "GET" or if request.method == "POST"
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
