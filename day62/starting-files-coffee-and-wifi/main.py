import csv

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL

COFFEE_LIST = ["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️", "✘"]
WIFI_LIST = ["️📶", "📶📶", "📶📶📶", "📶📶📶📶", "📶📶📶📶📶", "✘"]
POWER_LIST = ["️🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌", "✘"]

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


def append_to_csv(form):
    csv_data = [
        form.cafe.data,
        form.location.data,
        form.open.data,
        form.close.data,
        form.coffee.data,
        form.wifi.data,
        form.power.data
    ]
    with open('cafe-data.csv', newline='', encoding='utf-8', mode='a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(csv_data)


class CafeForm(FlaskForm):
    cafe = StringField(label="Cafe name", validators=[DataRequired()])
    location = URLField(label="Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField(label="Opening Time e.g 8AM", validators=[DataRequired()])
    close = StringField(label="Closing Time e.g 5:30PM", validators=[DataRequired()])
    coffee = SelectField(label="Coffee Rating", choices=COFFEE_LIST, validators=[DataRequired()])
    wifi = SelectField(label="Wifi Strength Rating", choices=WIFI_LIST, validators=[DataRequired()])
    power = SelectField(label="Power Outlet Availability", choices=POWER_LIST, validators=[DataRequired()])
    submit = SubmitField('Submit', render_kw={"class": "btn-warning"})


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/📶/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        # Exercise:
        # Make the form write a new row into cafe-data.csv
        # with   if form.validate_on_submit()
        append_to_csv(form)

        # below we must use redirect(url_for('cafes')) instead of render_template("cafes.html") because if we use
        # render_template() we end up with an empty 'cafes.html' webpage, as it expect a list of cafes to be rendered.
        # If we use redirect() instead we are redirecting to the cafes() function which renders the template cafes.html
        # and also passes to it the necessary list
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

    # # ALTERNATIVE TO WRITE IN CSV
    #     with open("cafe-data.csv", mode="a", newline="", encoding="utf-8") as csv_file:
    #         csv_file.write(f"{form.cafe.data},"
    #                        f"{form.location.data},"
    #                        f"{form.open.data},"
    #                        f"{form.close.data},"
    #                        f"{form.coffee.data},"
    #                        f"{form.wifi.data},"
    #                        f"{form.power.data}")
    #     return redirect(url_for('cafes'))
    # return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    # print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
