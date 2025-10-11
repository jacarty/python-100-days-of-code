"""
Flask and SQLite for a Book Ranking Website
Add and Delete record
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float

app = Flask(__name__)

# SQLAlchemy Base class definition
class Base(DeclarativeBase):
  pass

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# ORM Model definition
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250),nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Database table creation
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(
                title = request.form['title'],
                author = request.form['author'],
                rating = request.form['rating']
            )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
      
    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_rating(id):
    book = db.session.get(Book, id)
    if request.method == "POST":
        book.rating = request.form['new_rating']
        db.session.commit()  
        return redirect(url_for('home'))
    return render_template("edit.html", book=book)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    book = db.session.get(Book, id)
    if book:
        db.session.delete(book)
        db.session.commit()  
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
