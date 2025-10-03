"""
Requirements:

Create an SQLite database called new-books-collection.db. Remember to initialise the app.

Create a table in this database called books.

The books table should contain 4 fields: id, title, author and rating. The fields should have the same limitations as before e.g. INTEGER/FLOAT/VARCHAR/UNIQUE/NOT NULL etc.

Provide the Flask "app context" and create the schema in the database.

Again, with the flask app context, create a new entry in the books table that consists of the following data:

id: 1
title: "Harry Potter"
author: "J. K. Rowling"
review: 9.3
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float

app = Flask(__name__)

# Create Database
class Base(DeclarativeBase):
  pass

# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)

# Initialise the app with the extension
db.init_app(app)

# Create Table
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250),nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# Note: When creating new records, the primary key fields is optional. The id field will be auto-generated. 
with app.app_context():
        new_book = Book(
            id=1,
            title="Harry Potter",
            author="J. K. Rowling",
            rating="9.3"
        )
        db.session.add(new_book)
        db.session.commit()

"""
Read All Records

    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars()

To read all the records we first need to create a "query" to select things from the database. When we execute a query during a database session we get back the rows in the database (a Result object). We then use scalars() to get the individual elements rather than entire rows. 
"""

"""
Read A Particular Record By Query

    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

To get a single element we can use scalar() instead of scalars(). 
"""


"""
Update A Particular Record By Query

    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
        book_to_update.title = "Harry Potter and the Chamber of Secrets"
        db.session.commit() 
"""


"""
Update A Record By PRIMARY KEY

    book_id = 1
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_update = db.get_or_404(Book, book_id)  
        book_to_update.title = "Harry Potter and the Goblet of Fire"
        db.session.commit()  

Flask-SQLAlchemy also has some handy extra query methods like get_or_404() that we can use. Since Flask-SQLAlchemy version 3.0 the previous query methods like Book.query.get() have been deprecated
"""


"""
Delete A Particular Record By PRIMARY KEY

    book_id = 1
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()

You can also delete by querying for a particular value e.g. by title or one of the other properties. Again, the get_or_404() method is quite handy. 
"""