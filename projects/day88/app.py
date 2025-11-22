from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func

app = Flask(__name__)

#######################################
# CREATE and Connect DB
#######################################
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


#######################################
# Cafe TABLE Configuration
#######################################
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):   
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


#######################################
# Home Page
#######################################
@app.route("/")
def home():
    return render_template("index.html")


#######################################
# Get Random Cafe
#######################################
@app.route("/random", methods=["GET"])
def random_cafe():
    random_cafe = db.session.execute(
        db.select(Cafe).order_by(func.random()).limit(1)
        ).scalar_one_or_none()

    if random_cafe is None:
        return jsonify(error={"Not Found": "No cafes in the database."}), 404
    
    return jsonify(cafe=random_cafe.to_dict())


#######################################
# Get All Cafes
#######################################
@app.route("/cafes")
def cafes():
    all_cafes = db.session.execute(
        db.select(Cafe).order_by(Cafe.name)
    ).scalars().all()
    return render_template("all_cafes.html", cafes=all_cafes)


#######################################
# Cafe Details
#######################################
@app.route("/cafe/<int:cafe_id>")
def cafe_detail(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return "Cafe not found", 404
    return render_template("cafe_detail.html", cafe=cafe)


#######################################
# Search
#######################################
@app.route("/search")
def search():
    location = request.args.get("location", "")
    query = request.args.get("query", "")
    
    # Start with all cafes
    stmt = db.select(Cafe)
    
    # Filter by location if provided
    if location:
        stmt = stmt.where(Cafe.location.ilike(f"%{location}%"))
    
    # Filter by name if query provided
    if query:
        stmt = stmt.where(Cafe.name.ilike(f"%{query}%"))
    
    cafes = db.session.execute(stmt).scalars().all()
    return render_template("all_cafes.html", cafes=cafes, search_term=query, location=location)


#######################################
# Add Cafe
#######################################
@app.route("/add-cafe")
def add_cafe_page():
    """Render the add cafe form page"""
    return render_template("add_cafe.html")


#######################################
# Add Cafe API
#######################################
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


#######################################
# Update Record
# http://127.0.0.1:5000/update-price/CAFE_ID?new_price=£5.67
#######################################
@app.route("/update-cafe/<int:cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    """Update all fields of a cafe"""
    cafe = db.session.get(Cafe, cafe_id)
    
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    
    # Get JSON data from request
    data = request.get_json()
    
    # Update all fields
    if data.get('name'):
        cafe.name = data.get('name')
    if data.get('location'):
        cafe.location = data.get('location')
    if data.get('map_url'):
        cafe.map_url = data.get('map_url')
    if data.get('img_url'):
        cafe.img_url = data.get('img_url')
    if data.get('seats'):
        cafe.seats = data.get('seats')
    if 'coffee_price' in data:  # Allow empty string
        cafe.coffee_price = data.get('coffee_price')
    
    # Update boolean fields
    cafe.has_wifi = bool(data.get('wifi') == '1')
    cafe.has_sockets = bool(data.get('sockets') == '1')
    cafe.has_toilet = bool(data.get('toilet') == '1')
    cafe.can_take_calls = bool(data.get('calls') == '1')
    
    db.session.commit()
    
    return jsonify(response={"success": "Successfully updated the cafe."}), 200
    

#######################################
# Delete Record
# http://127.0.0.1:5000/report-closed/1?api-key=TopSecretAPIKey
#######################################
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


#######################################
# Init App
#######################################
if __name__ == '__main__':
    app.run(debug=True)
