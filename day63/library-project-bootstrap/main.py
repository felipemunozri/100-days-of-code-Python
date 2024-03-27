from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

RATING_LIST = ["🏆", "🏆🏆", "🏆🏆🏆", "🏆🏆🏆🏆", "🏆🏆🏆🏆🏆"]

app = Flask(__name__)
app.secret_key = "MySuperSecretKey"
Bootstrap5(app)

# Database definition.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db = SQLAlchemy(app)


# Book table definition.
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


# Add book form definition.
class AddBookForm(FlaskForm):
    title = StringField(label="Book Title:", validators=[DataRequired()])
    author = StringField(label="Book Author:", validators=[DataRequired()])
    rating = SelectField(label="Book Rating:", choices=RATING_LIST, validators=[DataRequired()])
    submit = SubmitField(label="Submit", render_kw={"class": "btn-info btn-lg px-4 me-sm-3 fw-bold"})


# Edit book form definition.
class EditBookForm(FlaskForm):
    rating = SelectField(label="New Rating:", choices=RATING_LIST, validators=[DataRequired()])
    submit = SubmitField(label="Submit", render_kw={"class": "btn-info btn-lg px-4 me-sm-3 fw-bold"})


# Create database and table.
with app.app_context():
    db.create_all()


# Flask route handlers.
@app.route("/")
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template("index.html", books_list=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddBookForm()
    if add_form.validate_on_submit():
        new_book = Book(title=add_form.title.data, author=add_form.author.data, rating=add_form.rating.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=add_form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_form = EditBookForm()
    book_id = request.args.get("id")
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    if edit_form.validate_on_submit():
        book_to_update.rating = edit_form.rating.data
        db.session.add(book_to_update)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form, book=book_to_update)


@app.route("/delete", methods=["GET"])
def delete():
    book_id = request.args.get("id")
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
