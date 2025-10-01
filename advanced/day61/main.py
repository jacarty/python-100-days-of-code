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
