from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
import requests

load_dotenv()
TMDB_KEY = os.getenv('TMDB_KEY')
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(30)
Bootstrap5(app)

# ----------------------------------------- DATABASE ----------------------------------------- #
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
db = SQLAlchemy(app)


# ------------------------------------ API SEARCH FUNCTION ------------------------------------ #
def search_movies_by_name(movie_title):
    # tmdb search endpoint
    url = "https://api.themoviedb.org/3/search/movie"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    parameters = {
        "query": movie_title,  # required
        "include_adult": "false",
        "language": "en-US",
        "page": 1,
        # "primary_release_year": "some string",
        # "region": "some string",
        # "year": "some string"
    }
    response = requests.get(url, headers=headers, params=parameters)
    response.raise_for_status()
    results = response.json()["results"]
    return results


# ------------------------------------- API FIND FUNCTION ------------------------------------- #
def find_movie_by_id(movie_id):
    base_url = 'https://image.tmdb.org/t/p/'
    file_size = 'w500'  # poster aspect ratio is 2:3

    # tmdb find endpoint
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    parameters = {
        "append_to_response": "images",  # comma separated list of endpoints to append to the same request (e.g. videos)
        "language": "en-US",
        # "include_image_language": "en"
    }
    response = requests.get(url, headers=headers, params=parameters)
    response.raise_for_status()
    movie_data = response.json()
    new_movie = Movie(title=movie_data["original_title"],
                      year=movie_data["release_date"].split("-")[0],
                      description=movie_data["overview"],
                      img_url=f"{base_url}{file_size}/{movie_data['poster_path']}"
                      )
    return new_movie


# ----------------------------------------- TABLE ----------------------------------------- #
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<Movie {self.title}>"


# -------------------------------------- TEST MOVIE DATA  -------------------------------------- #
first_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's "
                "sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to "
                "a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake,"
                " Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe,"
                " the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)

# ---------------------------- DB & TABLE CREATION + TEST MOVIE DATA INSERTION --------------------------- #
with app.app_context():
    db.create_all()
    # db.session.add(first_movie)
    # db.session.add(second_movie)
    # db.session.commit()


# --------------------------------------- ADD MOVIE FORM --------------------------------------- #
class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie", render_kw={"class": "btn-light"})


# --------------------------------------- EDIT MOVIE FORM --------------------------------------- #
class RateMovieForm(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()],
                        render_kw={"type": "number", "min": "1.0", "max": "10.0", "step": "0.1"})
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done", render_kw={"class": "btn-light"})


# ---------------------------------------- FLASK ROUTES ---------------------------------------- #
@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
    rank = 1
    for movie in all_movies:
        movie.ranking = rank
        rank += 1
    db.session.commit()
    all_movies.reverse()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=['GET', 'POST'])
def add():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        results = search_movies_by_name(add_form.title.data)
        return render_template("select.html", movies_list=results)
    return render_template("add.html", form=add_form)


@app.route("/find")
def find():
    movie_id = request.args.get("id")
    new_movie = find_movie_by_id(movie_id)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    movie_id = request.args.get("id")
    edit_form = RateMovieForm()
    movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    if edit_form.validate_on_submit():
        movie_to_update.rating = edit_form.rating.data
        movie_to_update.review = edit_form.review.data
        db.session.add(movie_to_update)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form, movie=movie_to_update)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    # app.run(debug=True, use_reloader=False)
    app.run(debug=True)
