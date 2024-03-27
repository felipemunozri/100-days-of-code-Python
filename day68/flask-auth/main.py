from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

'''
IMPORTANT: Most of the werkzeug functionalities used in this project are NOT available in the latest version of the 
werkzeug module (3.0.0), so we must use the 2.3.7 version instead. For this reason we also must use Flask version 2.3.3 
instead of the latest 3.0.0 because as per its requirement the latest version of Flask requires werkzeug >= 3.0.0.  
'''

app = Flask(__name__)
# The flask SECRET_KEY is necessary for users Session management, among other security related tasks. To properly
# generate an application SECRET_KEY we must use this python command in the terminal and copy its output
# python -c 'import secrets; print(secrets.token_hex())'
app.config['SECRET_KEY'] = '81e6bb11fdc2fe2eb769398a5792dd16a8d466bcdc4cfabca5fce4bbbe2a5782'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# INSTANCE OF LOGIN MANAGER
login_manager = LoginManager(app)


# USER LOADER IMPLEMENTATION
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# USER TABLE. We are using multiple inheritance as we will be using the UserMixin class too, which provides methods used
# for flask_login. The proper syntax for this inheritance is e.g. class MyClass(MixinClassB, MixinClassA, BaseClass),
# being db.Model our BaseClass
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))


# CREATE TABLE IN DB
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        # Check if mail already exist in database
        mail_exist = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if mail_exist:
            error = "You've already signed up with that email, log in instead."
            return redirect(url_for("login", error=error))
        else:
            # We take the user's password, salt it, and hash it with the pbkdf2:sha256 method. For this we use the
            # generate_password_hash() function. In the database the password is stored with this format
            # method$salt$hash
            hashed_password = generate_password_hash(password=password, method='pbkdf2:sha256', salt_length=8)
            new_user = User(email=email, password=hashed_password, name=name)
            db.session.add(new_user)
            db.session.commit()
            # Log in and authenticate user after adding details to database.
            login_user(new_user)
            return redirect(url_for("secrets", name=new_user.name))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    error = request.args.get("error")
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if not user:
            error = "That email does not exist, please try again."
        # We now use the check_password_hash() function to securely compare the stored hashed password in the database
        # against the inputted password
        elif not check_password_hash(pwhash=user.password, password=password):
            error = "Password incorrect, please try again."
        else:
            login_user(user)
            flash(message="Logged in successfully.", category="success")
            return redirect(url_for("secrets"))
    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required  # Protect this route, only accessible to logged-in users
def secrets():
    # Once a user is logged-in it is stored in a variable called 'current_user'. We then can tap in its properties, like
    # in this case we are passing its name to be rendered in the secrets.html template
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(message="Logged out successfully.", category="success")
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    # with send_from_directory() first we must put the name of the directory relative to root where the path to the file
    # is located, and then we put the path to the file
    return send_from_directory(directory="static", path="files/cheat_sheet.pdf")
    # return send_from_directory("static", 'files/cheat_sheet.pdf', as_attachment=True)  # we can send as attachment too


if __name__ == "__main__":
    app.run(debug=True)
