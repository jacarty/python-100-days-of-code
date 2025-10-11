import json
from main import app, db, Cafe

with open('cafes.json', 'r') as file:
    data = json.load(file)

with app.app_context():
    # Optional: Clear existing data
    # db.session.query(Cafe).delete()
    
    for cafe_data in data['cafes']:
        # Check if cafe already exists to avoid duplicates
        existing_cafe = db.session.execute(
            db.select(Cafe).where(Cafe.id == cafe_data['id'])
        ).scalar_one_or_none()
        
        if existing_cafe is None:
            cafe = Cafe(
                id=cafe_data['id'],
                name=cafe_data['name'],
                map_url=cafe_data['map_url'],
                img_url=cafe_data['img_url'],
                location=cafe_data['location'],
                seats=cafe_data['seats'],
                has_toilet=cafe_data['has_toilet'],
                has_wifi=cafe_data['has_wifi'],
                has_sockets=cafe_data['has_sockets'],
                can_take_calls=cafe_data['can_take_calls'],
                coffee_price=cafe_data['coffee_price']
            )
            db.session.add(cafe)
    
    db.session.commit()
    print(f"Successfully added {len(data['cafes'])} cafes!")