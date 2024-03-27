from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
IMPORTANT:
If we upgrade to Flask version 3.0.0 there will be an error with the flask_ckeditor module as it uses Flask to import 
the Markup functionality, but Markup was removed from Flask 3.0.0.

As a solution we can downgrade Flask to a version where it still uses Markup or alternatively, we can edit the 
__init__.py file from the flask_ckeditor module an replace the import of Markup from Flask to import from the MarkupSafe 
module instead.

As for 10-10-2023 it is an active issue with the flask_ckeditor module.  
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# app.config['CKEDITOR_SERVE_LOCAL'] = True  # whether to load ckeditor resources from CDN or locally
app.config['CKEDITOR_HEIGHT'] = 400  # changes the size of the ckeditor text-area
Bootstrap5(app)
ckeditor = CKEditor(app)  # initialize app with ckeditor

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


# CREATE FORM
class CreatePostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = URLField(label="Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


# @app.route('/', methods=["GET", "POST"])
@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.id)).scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/show_post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new_post", methods=["GET", "POST"])
def add_new_post():
    post_form = CreatePostForm()
    if post_form.validate_on_submit():
        new_blog_post = BlogPost(title=post_form.title.data,
                                 subtitle=post_form.subtitle.data,
                                 date=date.today().strftime("%B %d, %Y"),
                                 body=post_form.body.data,
                                 author=post_form.author.data,
                                 img_url=post_form.img_url.data)
        db.session.add(new_blog_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=post_form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit_post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post_to_edit = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(title=post_to_edit.title,
                               subtitle=post_to_edit.subtitle,
                               author=post_to_edit.author,
                               img_url=post_to_edit.img_url,
                               body=post_to_edit.body)
    if edit_form.validate_on_submit():
        post_to_edit.title = edit_form.title.data
        post_to_edit.subtitle = edit_form.subtitle.data
        post_to_edit.author = edit_form.author.data
        post_to_edit.img_url = edit_form.img_url.data
        post_to_edit.body = edit_form.body.data
        db.session.add(post_to_edit)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_to_edit.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
