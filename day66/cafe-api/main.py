import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

# connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)


# cafe TABLE configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # Instead of having to create a dictionary on every request response to then pass it to jsonify() we can create a
    # function inside our class definition that returns a dictionary where each property take its values directly from
    # the class attributes
    def to_dict(self):
        # # Method 1 to create the dictionary.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2, using dictionary comprehension
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# db and table creation
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    # random_cafe = db.session.execute(db.select(Cafe).order_by(func.random()).limit(1)).scalar()
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)

    # # To return a json object as the response of our request handler we can use the jsonify() utility built in in Flask,
    # # which serializes the passed argument. In this case, we are passing a dictionary with the properties of the
    # # returned object from our database query.
    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price
    # })
    #
    # # we can even further customize the returned object
    # return jsonify(cafe={
    #         # we can comment out some properties of the object
    #         # "id": random_cafe.id,
    #         "name": random_cafe.name,
    #         "map_url": random_cafe.map_url,
    #         "img_url": random_cafe.img_url,
    #         "location": random_cafe.location,

    #         # or even put some in a sub-category
    #         "amenities": {
    #             "seats": random_cafe.seats,
    #             "has_toilet": random_cafe.has_toilet,
    #             "has_wifi": random_cafe.has_wifi,
    #             "has_sockets": random_cafe.has_sockets,
    #             "can_take_calls": random_cafe.can_take_calls,
    #             "coffee_price": random_cafe.coffee_price
    #         }
    #     })

    return jsonify(random_cafe.to_dict())


# HTTP GET - Read All Records
@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    cafes = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes=cafes)
    # # shorter version
    # return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


# HTTP GET - Search Record
@app.route("/search")
def get_cafe():
    loc = request.args.get("loc")
    all_cafes = db.session.execute(db.select(Cafe).where(Cafe.location.contains(loc))).scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    api_key = request.args.get("api-key")
    if api_key == API_KEY:
        new_cafe = Cafe(name=request.form.get("name"),
                        map_url=request.form.get("map_url"),
                        img_url=request.form.get("img_url"),
                        location=request.form.get("loc"),
                        seats=request.form.get("seats"),
                        has_toilet=bool(request.form.get("toilet")),
                        has_wifi=bool(request.form.get("wifi")),
                        has_sockets=bool(request.form.get("sockets")),
                        can_take_calls=bool(request.form.get("calls")),
                        coffee_price=request.form.get("coffee_price"))
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


# HTTP PUT/PATCH - Update Record
@app.route("/update_price/<int:cafe_id>", methods=["PATCH"])
def patch_coffee_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    cafe_to_update.coffee_price = new_price
    if cafe_to_update:
        db.session.add(cafe_to_update)
        db.session.commit()
        return jsonify(success="Successfully updated the price.")
    else:
        # this code is never reached because of the get_or_404() flask-sqlalchemy method, but if instead we use a
        # db.session.execute() query or the sqlalchemy session.get() and check in an if statement if the returned value
        # is None, then we can return this custom JSON message
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == API_KEY:
        cafe = db.get_or_404(Cafe, cafe_id, description="Sorry a cafe with that id was not found in the database.")
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            # again, this code is never reached unless we change get_or_404() for a db.session.execute() query instead
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


# OPTIONAL: this route handler allows to overwrite the returned 404 errors and instead of returning a 404 Webpage as is
# the intended behaviour of the flask-sqlalchemy get_or_404(), we can return a JSON object with our desired error
# message
@app.errorhandler(404)
def invalid_route(e):
    return jsonify(error={'Not found': 'Sorry a cafe with that id was not found in the database.'})


if __name__ == '__main__':
    app.run(debug=True)

# After digging, I've found that if we use the get_or_404() as suggested in the solution we never reach the custom error
# message because, as the flask-sqlalchemy says in the docs, this query is intended for VIEWS, so we are immediately
# aborting and returning html, and not our intended JSON object.
#
# We could customize the error message of this view if we use the description parameter like this:
#
# db.get_or_404(Cafe, cafe_id, description="Sorry a cafe with that id was not found in the database.")
#
# But I believe returning html is not the correct way to respond to API consumers. If we want to return the JSON we can
# either use the SQLAlchemy session.get() or a normal db.session.execute() query and then compare if the result is None
# and return the JSON if True.Or as suggested by @Ken we can create a custom route to return api error as JSON.
#
# Hope this helps.

# Cafe & Wifi API provides information about a collection of cafe places and the perks of each one like wifi, sockets
# and toilet availability, number of seats, location in Google Maps, average coffee price, etc.
# It allows users to retrieve information about random cafes, search cafes by location, update average coffe prices of
# specific cafes and, for authenticated user, it allows to add and delete cafes to the collection.

# When you send your requests in Postman there is an option to save the response as an example. It is then added to the
# documentation.
