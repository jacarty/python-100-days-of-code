"""
Guess Example
"""

from flask import Flask
from flask import render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def website():
    random_number = random.randint(1, 50)
    current_year = datetime.date.today().strftime("%Y")
    return render_template("index.html", 
                           num=random_number, 
                           year=current_year
                           )

@app.route("/guess/<name>")
def guess(name):

    upper_name = name.title()

    # gender
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    guessed_gender = gender_response.json()["gender"]

    # age
    age_response = requests.get(f"https://api.agify.io?name={name}")
    guessed_age = age_response.json()["age"]

    # year
    random_number = random.randint(1, 50)
    current_year = datetime.date.today().strftime("%Y")

    return render_template("guess.html", 
                           name = upper_name, 
                           gender = guessed_gender, 
                           age = guessed_age, 
                           year = current_year
                           )

@app.route("/blog/<num>")
def get_blog(num):
    #blogs
    blogs_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = blogs_response.json()
    return render_template("blog.html", 
                           posts = all_posts
                            )

if __name__ == "__main__":
    app.run(debug=True)