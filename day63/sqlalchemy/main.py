# ----------------------------------- DB CREATION (OLD SYNTAX) ----------------------------------- #
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Create database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy()
# Initialise the app with the extension
db.init_app(app)


# Create table. The class must inherit from db.Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed. Its good practice to write
    # a repr for any class you build and give it an output which is the exact code you would use to create the object
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# ----------------------------------- CRUD OPERATIONS (NEW SYNTAX) ----------------------------------- #

# Create record
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

# Read all records
with app.app_context():
    # this query returns a result object with all the rows in it
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # to access the individual elements rather than the entire rows we use scalars()
    all_books = result.scalars()
    # once we get the individual element we can iterate over them to tap into the objects and its properties
    for book in all_books:
        print(book.rating)

# Read a particular record
with app.app_context():
    # we must use scalar() (SINGULAR!) to get a single element
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    print(book)

# Update a particular record
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# Update a record by primary key
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()
    # there are some extra query methods in Flask-SQLAlchemy designed for views that return a 404 Not Found error for
    # missing entries. These methods are:
    #    .get_or_404() will raise a 404 if the row with the given id doesn’t exist, otherwise it will return the
    #    instance
    #    .first_or_404() will raise a 404 if the query does not return any results, otherwise it will return the first
    #    result
    #    .one_or_404() will raise a 404 if the query does not return exactly one result, otherwise it will return the
    #    result
    # usage example:
    #     book_to_update = db.get_or_404(Book, book_id)

# Delete a particular record
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

# ----------------------------------- DB CREATION (NEW SYNTAX) ----------------------------------- #
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Integer, String, Float
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# db = SQLAlchemy(model_class=Base)
#
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# db.init_app(app)
#
#
# class Book(db.Model):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
#     author: Mapped[str] = mapped_column(String, nullable=False)
#     rating: Mapped[float] = mapped_column(Float, nullable=False)
#
#     def __repr__(self):
#         return f'<Book {self.title}>'
#
#
# with app.app_context():
#     db.create_all()
#
# with app.app_context():
#     new_book = Book(id=1, title = "Harry Potter", author = "J. K. Rowling", rating = 2.0)
#     db.session.add(new_book)
#     db.session.commit()
