"""
Build APIs with RESTful Routing & Flask
"""

# Representative State Transfer
# Different types
# GraphQL
# SOAP & REST
# Falcor

"""
REST (Representational State Transfer) is an architectural pattern for designing web APIs using standard HTTP methods and URL conventions.
Core Principles
RESTful routing maps HTTP verbs to CRUD operations on resources:

- GET - Retrieve/read resources
- POST - Create new resources
- PUT/PATCH - Update existing resources
- DELETE - Remove resources

Standard Route Patterns
For a resource like "articles":

HTTP Verb   Path            Action      Purpose
GET         /articles       index       List all articles
GET         /articles/:id   show        Display one article
GET         /articles/new   new         Show form to create article
POST        /articles       create      Create new article
GET         /articles/:id/  editedit    Show form to edit article
PUT/PATCH   /articles/:id   update      Update specific article
DELETE      /articles/:id   destroy     Delete specific article

Key Conventions

- URLs represent resources (nouns), not actions
- Use plural resource names (/articles, not /article)
- HTTP methods indicate the action being performed
- Keep routes predictable and consistent across your API
- Use nested routes for related resources (e.g., /articles/:id/comments)

This pattern creates clean, intuitive APIs that are easy to understand and maintain.
"""


################################################
# Challenge - RESTful Routing
################################################



"""
Example
https://laptopfriendly.co/london
"""

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):   
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_cafe():
    random_cafe = db.session.execute(
        db.select(Cafe).order_by(func.random()).limit(1)
        ).scalar_one_or_none()

    if random_cafe is None:
        return jsonify(error={"Not Found": "No cafes in the database."}), 404
    
    return jsonify(cafe=random_cafe.to_dict())

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
    #.    "coffee_price": random_cafe.coffee_price,
    # })


@app.route("/all", methods=["GET"])
def all_cafes():
    all_cafes = db.session.execute(
        db.select(Cafe).order_by(Cafe.name)
        ).scalars().all()

    if all_cafes is None:
        return jsonify(error={"Not Found": "No cafes in the database."}), 404
    
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search", methods=["GET"])
def search_cafes():
    query_location = request.args.get("loc")

    matched_cafes = db.session.execute(
        db.select(Cafe).where(Cafe.location == query_location)
        ).scalars().all()

    if matched_cafes is None:
        return jsonify(error={"Not Found": "No cafes in the database."}), 404
    
    return jsonify(cafes=[cafe.to_dict() for cafe in matched_cafes])


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
# http://127.0.0.1:5000/update-price/CAFE_ID?new_price=£5.67
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.get(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    

# HTTP DELETE - Delete Record
# http://127.0.0.1:5000/report-closed/1?api-key=TopSecretAPIKey
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.get(Cafe, cafe_id) 
        if cafe is None:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404     
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
