##############################################################################
# DAY 59 - Flask and Bootstrap
##############################################################################

"""
Flask Templates with a Bootstrap Template

Blog
Dynamic Posts
Bootstrap
"""

############################################################
# Website Template
# https://startbootstrap.com/previews/clean-blog
############################################################

from flask import Flask, render_template
import requests

app = Flask(__name__)

blogs_api = "https://api.npoint.io/e9d9c46c7277cb7135c7"
blog_data = requests.get(blogs_api).json()

@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html", all_posts = blog_data)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = next((post for post in blog_data if post['id'] == index), None)
    return render_template("post.html", post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)


##############################################################################
# DAY 60 - Capturing Input
##############################################################################

"""
Flask - Capturing Input; e.g. Contact Forms
"""

############################################################
# Website Template
# https://startbootstrap.com/previews/clean-blog
############################################################

from flask import Flask, render_template, request
import requests
from notification_manager import NotificationManager

blogs_api = "https://api.npoint.io/e9d9c46c7277cb7135c7"
blog_data = requests.get(blogs_api).json()

app = Flask(__name__)
notifications = NotificationManager()

@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html", all_posts = blog_data)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        notifications.send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)    
    return render_template("contact.html", msg_sent=False)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = next((post for post in blog_data if post['id'] == index), None)
    return render_template("post.html", post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)


##############################################################################
# DAY 61 - Bootstrap & Flask
##############################################################################

"""
Using WTForms for Username & Password.

We're using template inheritance from Base.html to Success.html and Denied.html.

You can override inherited elements by using Super Blocks (super.init()).

Using flask_bootstrap too.
"""

from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import random
import string
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
app.secret_key = random_string

demo_user = ""
demo_pass = ""

class ContactForm(FlaskForm):
    email = EmailField(
        label='Email', 
        validators=[
            DataRequired(),
            Email(message='Please enter a valid email address')
        ]
    )
    password = PasswordField(
        label='Password', 
        validators=[
            DataRequired(),
            Length(min=8, message='Password must be at least 8 characters long')
        ]
    )
    login = SubmitField('Login')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    form = ContactForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == demo_user and password == demo_pass:
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template('login.html', form=form)

@app.route('/success', methods=["GET", "POST"])
def login_success():
    return render_template('success.html')
    
@app.route('/denied', methods=["GET", "POST"])
def login_denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)

##############################################################################
# DAY 62 - Flask, WTForms, Bootstrap and CSV
##############################################################################

"""
Flask, WTForms, Bootstrap and CSV
"""

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

##############################################################################
# DAY 63 - Flask and SQLite
##############################################################################
