"""
Create a moving raking website with Flask, Jinja, Bootstrap & SQLite
"""

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os


#################################################
# Setup App
#################################################

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")
Bootstrap5(app)


#################################################
# Config Database
#################################################

class Base(DeclarativeBase):
  pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()


#################################################
# Create Forms
#################################################

class EditForm(FlaskForm):
    rating = IntegerField("Your Rating - 0 to 10", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField('Add Movie')


#################################################
# TMDB Movie Search
#################################################

TMDB_TOKEN = os.getenv("TMDB_TOKEN")

def search_movie(film):
    url = "https://api.themoviedb.org/3/search/movie"

    headers = {
        "Authorization": f"Bearer {TMDB_TOKEN}"
    } 

    params = {
        "query": film,
        "include_adult": "true"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    movies = data['results']
    return movies


#################################################
# Flask
#################################################

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.asc()))
    all_movies = result.scalars().all()
    return render_template("index.html", all_movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    id = request.args.get("id")
    movie = db.get_or_404(Movie, id)
    if form.validate_on_submit():
        movie.rating = int(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))  
    return render_template("edit.html", form=form)


@app.route("/delete", methods=["GET"])
def delete():
    id = request.args.get("id")
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit() 
    return redirect(url_for('home'))  


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        film = add_form.title.data
        search_results = search_movie(film)
        return render_template("select.html", results=search_results)
    return render_template("add.html", form=add_form)


@app.route("/select", methods=["GET", "POST"])
def select():
    id = request.args.get("id")
    url = f"https://api.themoviedb.org/3/movie/{id}"
    response = requests.get(url, headers={"Authorization": f"Bearer {TMDB_TOKEN}"})
    data = response.json()

    new_movie = Movie(
        title=data['title'],
        year=data['release_date'][:4],
        description=data['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        rating=0,
        review="placeholder"
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", id=new_movie.id))


#################################################
# Application Entry Point
#################################################

if __name__ == '__main__':
    app.run(debug=True)
