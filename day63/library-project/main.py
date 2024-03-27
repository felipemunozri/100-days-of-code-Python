from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # we must use .all() after the query result as it returns all the ScalarResults inside a list
    with app.app_context():
        all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    # print(all_books)
    return render_template("index.html", books_list=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(title=request.form["title"], author=request.form["author"],
                            rating=float(request.form["rating"]))
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get("id")
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    if request.method == "POST":
        new_rating = request.form["rating"]
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_rating.html", book=book_to_update)


# ALTERNATIVE TO EDIT
# @app.route("/edit/<int:id>", methods=["GET", "POST"])
# def edit(id):
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
#     if request.method == "POST":
#         new_rating = request.form["rating"]
#         book_to_update.rating = new_rating
#         db.session.commit()
#         return redirect(url_for("home"))
#     return render_template("edit_rating.html", book=book_to_update)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    book_id = request.args.get("id")
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
