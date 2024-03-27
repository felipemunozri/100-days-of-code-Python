from itertools import tee

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///library.db"
db = SQLAlchemy()
Bootstrap5(app)
db.init_app(app)


class AddForm(FlaskForm):
    book = StringField(label='Book Name', validators=[DataRequired()])
    author = StringField(label='Book Author', validators=[DataRequired()])
    rating = StringField(label='Rating', validators=[DataRequired()])
    notes = TextAreaField(label='Notes')
    submit = SubmitField('Submit', render_kw={"class": "btn-warning"})


class EditForm(FlaskForm):
    rating = StringField(label='Rating', validators=[DataRequired()])
    submit = SubmitField('Submit', render_kw={"class": "btn-warning"})


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String, nullable=False)
    notes = db.Column(db.String(500))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        new_book = Book(title=form.book.data,
                        author=form.author.data,
                        rating=form.rating.data,
                        notes=form.notes.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


@app.route("/edit/<book_id>", methods=['GET', 'POST'])
def edit(book_id):
    form = EditForm()
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    if form.validate_on_submit():
        book_to_update.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit_rating.html", book=book_to_update, form=form)


@app.route("/delete/<book_id>", methods=['GET', 'POST'])
def delete(book_id):
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
