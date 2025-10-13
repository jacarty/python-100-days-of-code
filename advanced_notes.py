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
# DAY 63 - Flask and SQLite - Book Ranking
##############################################################################

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


##############################################################################
# DAY 64 - Flask and SQLite - Movie Site
##############################################################################

"""
Create a moving raking website with Flask, Jinja, Bootstrap & SQLite

Movie lookup on TMDB with API integration

Dynamic ordering based on rating

Add, edit, delete

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



##############################################################################
# DAY 65 - Web Design & Canva
##############################################################################

"""
Core Web Design Features

Four Pillars of web design: Colour Theory, Typography, UI Design, UX Design

https://www.canva.com/design/DAG02HGC1t0/MUlpL9pSCQhUdtHhfaMLVA/edit?ui=e30

"""

##############################################
# Colour Palette
##############################################


"""
Color Palette Moods for Web Design
Warm Palettes

Reds/Oranges/Yellows: Energetic, passionate, exciting, urgent
Creates feelings of warmth, enthusiasm, and action
Often used for calls-to-action, food brands, entertainment
Can increase heart rate and create sense of urgency

Cool Palettes

Blues/Greens/Purples: Calming, trustworthy, professional, serene
Evokes stability, reliability, and tranquility
Popular for corporate sites, healthcare, finance, tech
Blues especially associated with trust and competence

Neutral Palettes

Grays/Beiges/Whites/Blacks: Sophisticated, minimal, timeless, balanced
Provides clean backdrop and emphasizes content
Common in luxury brands, portfolios, modern design
Creates sense of elegance and simplicity

Vibrant/Saturated

Bold, High-Saturation Colors: Playful, youthful, dynamic, creative
Grabs attention and conveys energy
Effective for brands targeting younger audiences, creative industries
Can feel fun but may overwhelm if overused

Muted/Desaturated

Soft, Low-Saturation Colors: Gentle, sophisticated, vintage, approachable
Creates calm, refined atmosphere
Works well for wellness, lifestyle, artisanal brands
Feels more subtle and easier on the eyes

Monochromatic

Single Hue with Variations: Cohesive, harmonious, focused, elegant
Creates unified look with different shades/tints of one color
Emphasizes hierarchy through lightness/darkness
Professional and visually organized

Key Considerations

Context matters: Same color can feel different depending on saturation, surrounding colors, and cultural context
Accessibility: Ensure sufficient contrast for readability
Brand alignment: Colors should reflect brand personality and values

"""

##############################################
# By Colour
##############################################

"""
Color Moods for Web Design

###############
### Red
###############

Emotions: Passion, energy, urgency, excitement, danger, love, power
Psychological Effects:

Increases heart rate and creates sense of urgency
Grabs attention immediately
Stimulates appetite

Best Used For:

Call-to-action buttons ("Buy Now", "Sale")
Food and restaurant websites
Entertainment and gaming
Emergency or warning messages
Brands wanting bold, energetic presence

Cautions: Can feel aggressive or overwhelming if overused; may signal error or danger

###############
### Yellow
###############
Emotions: Happiness, optimism, warmth, creativity, caution, energy
Psychological Effects:

Most visible color to human eye
Stimulates mental activity and energy
Creates cheerful, welcoming feeling
Can cause eye strain in large amounts

Best Used For:

Highlighting important information
Children's products/websites
Creative or playful brands
Drawing attention to specific elements
Warnings or caution areas

Cautions: Pure bright yellow can be harsh; often works better in softer tones or as accent color

###############
### Green
###############
Emotions: Growth, nature, health, tranquility, freshness, prosperity, harmony
Psychological Effects:

Most restful color for eyes
Associated with balance and stability
Conveys environmental consciousness
Suggests wealth and success

Best Used For:

Environmental/eco-friendly brands
Health and wellness sites
Financial services (money association)
Organic/natural products
Call-to-action buttons (secondary to red)

Variations:

Dark green: wealth, prestige, tradition
Light green: calm, freshness, youth
Olive green: peace, earthiness

###############
### Blue
###############
Emotions: Trust, stability, calm, professionalism, security, intelligence, sadness
Psychological Effects:

Most universally liked color
Lowers heart rate and reduces stress
Creates sense of reliability
Suppresses appetite

Best Used For:

Corporate and professional websites
Technology companies
Healthcare and medical sites
Financial institutions
Social media platforms
Productivity tools

Variations:

Navy blue: authority, confidence, power
Light blue: calm, peace, freedom
Bright blue: energy, clarity, innovation

Cautions: Can feel cold or impersonal; avoid for food brands

###############
### Purple
###############
Emotions: Luxury, creativity, spirituality, mystery, royalty, imagination, wisdom
Psychological Effects:

Historically associated with wealth and royalty
Stimulates creativity and problem-solving
Balances calm (blue) and energy (red)
Rare in nature, feels special

Best Used For:

Luxury and premium brands
Beauty and cosmetics
Creative industries
Spiritual or meditation sites
Youth brands (especially lavender/lighter purples)
Innovation and imagination-focused companies

Variations:

Deep purple: sophistication, luxury, mystery
Light purple/Lavender: feminine, nostalgic, romantic
Violet: creativity, uniqueness

Cautions: Can feel overly feminine or frivolous in some contexts; use carefully in corporate settings

##############################
# Quick Reference for Combinations
##############################
Red + Yellow: Fast food, energy, excitement
Blue + Green: Healthcare, natural tech, trustworthy eco-brands
Purple + Gold: Ultimate luxury
Blue + White: Clean, professional, tech
Green + Brown: Organic, natural, earthy
"""


##############################
# Analogous Colors
##############################

"""
What Are Analogous Colors?

Colors that sit next to each other on the color wheel (typically 2-4 adjacent colors)
Examples:

Blue, blue-green, green
Red, red-orange, orange
Yellow, yellow-green, green


Visual Characteristics
Harmonious & Cohesive

Naturally pleasing to the eye
Low contrast between colors
Creates smooth visual flow

One Dominant Color

Usually choose one color as primary
Others act as supporting/accent colors
Creates clear hierarchy


Mood & Effect
Calming & Unified

Less visual tension than complementary schemes
Feels serene and comfortable
Easy to look at for extended periods

Natural Feel

Often mirrors color combinations found in nature
Sunset: red-orange-yellow
Forest: yellow-green-blue-green
Ocean: blue-green-blue-purple


Best Used For

Backgrounds and sections that need to feel cohesive
Nature/organic brands wanting natural harmony
Calming interfaces (wellness, meditation, healthcare)
Creating depth without harsh contrast
Gradient designs with smooth transitions


Web Design Tips
Pros:

Easy to create visually pleasing designs
Low risk of color clashing
Professional and polished look

Cons:

Can lack visual excitement or punch
May need neutral color (white/gray/black) for contrast
Important elements might not stand out enough

Pro Tip: Use the 60-30-10 rule

60% dominant color
30% supporting color
10% accent color


Common Analogous Combinations

Warm: Red → Orange → Yellow
Cool: Blue → Blue-Purple → Purple
Fresh: Yellow → Yellow-Green → Green
Sunset: Orange → Red-Orange → Red
Ocean: Blue → Blue-Green → Green
"""


##############################
# Complementary Colors
##############################

"""

What Are Complementary Colors?

Colors that sit directly opposite each other on the color wheel
Examples:

Red ↔ Green
Blue ↔ Orange
Yellow ↔ Purple
Red-Orange ↔ Blue-Green


##############
# Visual Characteristics
##############

##############
High Contrast & Vibrant

Maximum color contrast possible
Creates visual tension and energy
Colors make each other appear more intense

##############
Eye-Catching

Instantly grabs attention
Creates strong focal points
Very dynamic when placed side-by-side

##############
# Mood & Effect
###############

##############
Energetic & Bold

Creates excitement and vibrancy
Feels dynamic and active
Can be jarring if not balanced properly

##############
Balanced Opposition

Warm vs Cool contrast
Creates visual equilibrium
Naturally draws the eye


Best Used For

Call-to-action buttons (stand out dramatically)
Sports brands wanting energy and competition
Drawing attention to specific elements
Creating visual pop in designs
Highlighting important information
Brand differentiation (memorable combinations)


##############
# Web Design Tips
##############

Pros:

Maximum visual impact
Excellent for emphasis and hierarchy
Memorable and distinctive
Creates clear focal points

Cons:

Can be overwhelming or chaotic
May feel too intense for long viewing
Requires careful balance
Accessibility concerns if not managed

Pro Tip: Use the 80-20 or 90-10 rule

80-90% one color (dominant)
10-20% complementary color (accent)
Avoid 50-50 splits (too jarring)


##############
# Making It Work
##############

Tone It Down:

Use desaturated/muted versions for softer look
Add neutrals (white, gray, black) to buffer
Use complementary color sparingly as accent only

Increase Readability:

Never place complementary colors directly adjacent for text
Use neutral backgrounds for text
Ensure sufficient contrast ratios for accessibility


##############
# Common Complementary Combinations
###############

Red ↔ Green: Christmas, bold, natural
Blue ↔ Orange: Sports, tech, energetic
Yellow ↔ Purple: Luxury contrast, creative
Teal ↔ Coral: Modern, fresh, vibrant
Navy ↔ Gold: Sophisticated, premium


##############
# Quick Comparison
##############

Analogous       Complementary
Harmonious      High contrast
Calming         Energetic
Subtle          Bold
Easy on eyes    Attention-grabbing
Low risk        High impact
"""

##############################################
# Typography
##############################################

"""
Typography - High Level Overview

Major Typeface Categories

##############
# Serif
##############

Characteristics: Small decorative strokes (serifs) at the ends of letters
Mood: Traditional, trustworthy, authoritative, elegant, established
Best Used For:

Long-form body text (print and digital)
Traditional/established brands
Publishing, news, editorial
Legal, financial, academic sites
Print materials (highly readable)

Examples: Times New Roman, Georgia, Garamond, Merriweather
Digital Note: Works well at larger sizes; ensure good rendering at small sizes on screens

##############
# Sans Serif
##############

Characteristics: Clean lines without decorative strokes; "sans" = without
Mood: Modern, clean, minimal, approachable, friendly, straightforward
Best Used For:

Digital interfaces and UI elements
Body text on screens
Tech and startup brands
Modern, minimalist designs
Mobile applications
Headlines and navigation

Examples: Helvetica, Arial, Open Sans, Roboto, Inter
Digital Note: Generally most readable on screens; dominates web design

##############
# Script
##############

Characteristics: Mimics handwriting or calligraphy; flowing, connected letters
Mood: Elegant, feminine, creative, personal, luxurious, romantic
Best Used For:

Logos and branding (sparingly)
Wedding/event websites
Luxury or boutique brands
Decorative headlines only
Invitations and certificates
Beauty and fashion sites

Examples: Brush Script, Pacifico, Dancing Script, Great Vibes
Cautions:

Never use for body text (illegible)
Use sparingly and at larger sizes
Poor accessibility at small sizes


##############
# Display/Decorative
##############

Characteristics: Highly stylized, unique, attention-grabbing; designed for impact
Mood: Creative, bold, unique, playful, distinctive (varies widely by style)
Best Used For:

Headlines and titles only
Branding and logos
Posters and hero sections
Creative/artistic projects
Making bold statements
Short text that needs impact

Examples: Impact, Bebas Neue, Lobster, Playfair Display
Cautions:

Never for body text
Use very sparingly
Can quickly feel dated or gimmicky


##############
# Monospace
##############

Characteristics: Each character occupies the same horizontal space (fixed-width)
Mood: Technical, precise, retro, code-like, systematic
Best Used For:

Code snippets and technical documentation
Developer/tech brands
Typewriter/retro aesthetics
Data tables and alignment-critical text
Terminal/command-line interfaces

Examples: Courier, Consolas, Monaco, Source Code Pro
Digital Note: Essential for displaying code; rarely used for regular body text

##############
# Quick Selection Guide
##############

For Readability: Sans Serif (digital), Serif (print/long-form)
For Trust/Authority: Serif
For Modern/Clean: Sans Serif
For Luxury/Elegance: Serif or Script (minimal use)
For Tech/Innovation: Sans Serif or Monospace
For Creativity: Display or Script (headlines only)

##############
# Web Design Best Practices
##############

Hierarchy Rule:

Maximum 2-3 typefaces per site
Pair complementary styles (e.g., Serif headline + Sans Serif body)

Readability:

Body text: 16px minimum
Line height: 1.5-1.7 for body text
Line length: 50-75 characters optimal

Pairing Formula:

Contrast: Pair different categories (Serif + Sans Serif)
Harmony: Share similar proportions or mood
Hierarchy: Clear distinction between headline and body

##############
# Common Successful Pairings
##############

Playfair Display (Serif) + Open Sans (Sans Serif): Elegant + Modern
Montserrat (Sans Serif) + Merriweather (Serif): Clean + Readable
Bebas Neue (Display) + Roboto (Sans Serif): Bold + Functional
Lora (Serif) + Lato (Sans Serif): Classic + Contemporary
"""

##############################################
# A Web UI Design Principles & Best Practices
## Reading blocks; typically 40-60 char for easy readability
##############################################

"""
######################
# Core Principles
######################

Clarity & Simplicity
######################

Remove unnecessary elements - every component should serve a purpose
Use clear, concise language and intuitive labels
Avoid overwhelming users with too many choices at once


Consistency
######################

Maintain uniform patterns across the interface (colors, typography, spacing, interactions)
Follow platform conventions and established design systems
Keep navigation predictable throughout the site

Visual Hierarchy
######################

Guide attention with size, color, contrast, and positioning
Most important elements should be most prominent
Use whitespace strategically to create breathing room

Responsive Design
######################

Design mobile-first, then scale up
Ensure functionality across all device sizes
Consider touch targets (minimum 44x44px for mobile)

######################
Best Practices
######################

Navigation
######################

Keep main navigation visible and accessible
Limit top-level menu items (5-7 max)
Show users where they are (breadcrumbs, active states)

Performance
######################

Optimize images and assets for fast loading
Lazy load content when appropriate
Provide loading indicators for slow operations

Accessibility
######################

Use sufficient color contrast (WCAG AA minimum: 4.5:1 for text)
Support keyboard navigation
Include descriptive alt text for images
Don't rely on color alone to convey information

Interaction Design
######################

Provide immediate feedback for user actions
Use familiar UI patterns (buttons look clickable)
Make interactive elements obvious with hover/focus states
Keep forms short and validate in real-time

Typography
######################

Use 2-3 fonts maximum
Maintain readable font sizes (16px+ for body text)
Ensure adequate line height (1.5 for body text)

Call-to-Actions
######################

Make primary actions prominent and obvious
Use action-oriented language ("Get Started" vs "Submit")
Create visual contrast for important buttons

"""

##############################################
# Web UX Design Principles & Best Practices
##############################################

"""
######################
# Core Principles
######################

User-Centered Design
######################

Design for your actual users, not yourself
Base decisions on user research and data, not assumptions
Consider user goals, context, and pain points throughout

Usability
######################

Make interfaces intuitive and easy to learn
Minimize cognitive load - don't make users think unnecessarily
Reduce steps required to complete tasks

Accessibility for All
######################

Design for diverse abilities, ages, and technical skill levels
Consider assistive technologies from the start
Follow WCAG guidelines and inclusive design principles

Feedback & Communication
######################

Always inform users what's happening (loading, errors, success)
Use clear error messages that explain how to fix issues
Provide confirmation for important actions

######################
# Best Practices
######################

Information Architecture
######################

Organize content logically based on user mental models
Use clear categorization and labeling
Implement effective search when content is extensive
Keep important content within 3 clicks

User Research & Testing
######################

Conduct usability testing with real users regularly
Create user personas based on actual data
Map user journeys to identify friction points
A/B test significant design decisions

Content Strategy
######################

Write for scannability (headings, short paragraphs, bullet points)
Front-load important information
Use plain language, avoid jargon
Provide content in the format users expect

Forms & Input
######################

Only ask for essential information
Use appropriate input types (date pickers, dropdowns)
Provide inline validation with helpful error messages
Show progress indicators for multi-step forms
Allow easy error correction

Progressive Disclosure
######################

Show only necessary information initially
Reveal complexity gradually as needed
Use tooltips, expandable sections, and modals strategically

Error Prevention & Recovery
######################

Design to prevent errors before they happen
Provide undo options for destructive actions
Use confirmations for irreversible actions
Make error recovery straightforward

Performance & Speed
######################

Optimize perceived performance (skeleton screens, optimistic UI)
Set user expectations for wait times
Prioritize above-the-fold content loading

Mobile UX Considerations
######################

Design for thumb-friendly zones
Minimize text input requirements
Consider offline functionality
Respect mobile data and battery constraints

Trust & Security
######################

Be transparent about data collection
Provide clear privacy controls
Use secure connections (HTTPS)
Display trust signals (security badges, reviews)

Emotional Design
######################

Create delightful micro-interactions
Use appropriate tone and personality
Design empty states thoughtfully
Celebrate user achievements

######################
# Key Methodologies
######################

Design Thinking Process
######################

Empathize → Define → Ideate → Prototype → Test

Lean UX
######################

Build-Measure-Learn cycles
Focus on outcomes over deliverables
Collaborate cross-functionally

Jobs-to-be-Done Framework
######################

Understand what users are trying to accomplish
Design solutions around user goals, not features


######################
# F-Layout & Z-Layout Patterns
######################

F-Layout Pattern
######################

What It Is
######################

Users scan content in an F-shaped pattern
Based on eye-tracking studies showing how people read web pages
Common on text-heavy pages (blogs, articles, search results)

The Pattern
######################

Horizontal movement across the top (header/navigation)
Second horizontal movement slightly down the page (subheading/intro)
Vertical movement down the left side, scanning for keywords

When to Use
######################

Content-heavy websites (news sites, blogs)
Search engine results pages
List-based content
Text-focused designs

Best Practices
######################

Place most important information in the top-left area
Use compelling headlines at the top
Left-align text and key elements
Front-load paragraphs with important keywords
Use bullet points and subheadings on the left
Place secondary content/ads on the right (less attention)

Structure
[====================] ← Top horizontal bar (logo, nav)
[==========]           ← Second horizontal scan
[===]
[===]                  ← Vertical scan down left
[===]
[==]

######################
# Z-Layout Pattern
######################

What It Is
######################

Users scan in a Z-shaped pattern
Eyes move horizontally across top, diagonally down, then horizontally across bottom
Common on simpler, less text-heavy pages

The Pattern
######################

Top-left to top-right (header, logo to navigation/CTA)
Diagonal down-left (scanning middle content)
Bottom-left to bottom-right (footer, final CTA)

When to Use
######################

Landing pages with minimal text
Simple homepages
Registration/signup pages
Promotional pages
Pages with clear conversion goals

Best Practices
######################

Place logo top-left
Put primary CTA or key navigation top-right
Guide eye with visual hierarchy along the Z-path
Place secondary CTA bottom-right
Use visual elements (images, arrows) to reinforce the Z-flow
Keep content minimal and scannable

Structure
[Logo ============= CTA] ← Horizontal top
       \
         \                ← Diagonal
           \
[Content    \    Image  ]
              \
[Info ========== CTA   ] ← Horizontal bottom

Key Differences
######################
F-Layou                     Z-Layout
Text-heavy content          Minimal content
Multiple sections           Few distinct sections
Blog posts, articles        Landing pages, promos
Slower, detailed reading    Quick scanning
Multiple focal points       2-3 main focal points

Combined Approach
Many modern websites use both patterns strategically:

Z-pattern for hero section/above fold
F-pattern for content sections below

Responsive designs may switch patterns based on screen size

Pro Tip: Don't force these patterns - use them as guidelines. Eye-tracking shows natural reading behavior, but good visual hierarchy and clear CTAs matter more than strict adherence to these layouts.
"""


##############################################################################
# DAY 66 - Flask and APIs with RESTful Routing
##############################################################################

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

##############################################################################
# DAY 67 - Flask, SQLite, CKEditor5, Add, Edit & Delete Posts
##############################################################################

"""
Blog Site with Add, Edit, Delete Posts

Flask
SQLite
CKEditor5

"""

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Create Database
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Configure Table
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# Create New Post Form
class NewPost(FlaskForm):
    title = StringField("Article Title", validators=[DataRequired()])
    subtitle = StringField("Article Subtitle", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    img_url = StringField("Background Image URL", validators=[DataRequired()])
    body = TextAreaField("Body", validators=[DataRequired()])
    submit = SubmitField('Submit')


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = []

    get_all_posts = db.session.execute(
        db.select(BlogPost).order_by(BlogPost.id.desc())
    ).scalars().all()

    if get_all_posts is None:
        return f"No posts found in the database."

    return render_template("index.html", all_posts=get_all_posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    new_post_form = NewPost()

    if new_post_form.validate_on_submit():  
        new_post = BlogPost(
            title = new_post_form.title.data,
            subtitle = new_post_form.subtitle.data,
            author = new_post_form.author.data,
            img_url = new_post_form.img_url.data,
            body = new_post_form.body.data,
            date = date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))
    
    return render_template("make-post.html", form=new_post_form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = NewPost(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data    
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)

@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

##############################################################################
# DAY 68 - Blog
##############################################################################

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Create user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# Create DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create Table with UserMixin
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # Passing True or False if the user is authenticated. 
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        
        hashed_salted_pw =  generate_password_hash(
            request.form['password'], 
            method='pbkdf2:sha256', 
            salt_length=8
        )

        new_user = User(
            name = request.form['name'],
            email = request.form['email'],
            password = hashed_salted_pw
        )
    
        db.session.add(new_user)
        db.session.commit()
    
        # Log in and authenticate user after adding details to DB
        login_user(new_user)

        # Can redirect() and get name from the current_user
        return redirect(url_for("secrets"))
    
    # Passing True or False if the user is authenticated. 
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":

        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email 
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
    
        # Email doesn't exist or password incorrect.
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        
        # Check stored password hash against entered password hashed
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    # Passing True or False if the user is authenticated. 
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    # Passing the name from the current_user
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)

##############################################################################
# DAY 69 - More Forms
##############################################################################

"""
Main
"""

from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm


#############################################################
# Configure App
#############################################################

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


#############################################################
# Configure Web Elements 
#############################################################

ckeditor = CKEditor(app)
Bootstrap5(app)


#############################################################
# Configure Login Elements
#############################################################

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


#############################################################
# Create and Configure Database
#############################################################

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(1000), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")

with app.app_context():
    db.create_all()


#############################################################
# Admin Decorator
#############################################################

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


#############################################################
# Configure Flask Routes
#############################################################

@app.route('/register', methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        email_add = form.email.data
        result = db.session.execute(db.select(User).where(User.email == email_add))
        user = result.scalar()

        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))
           
        else:
            hash_and_salted_password = generate_password_hash(
                form.password.data,
                method = 'pbkdf2:sha256',
                salt_length = 8
            )
            new_user = User(
                email = email_add,
                name = form.name.data,
                password = hash_and_salted_password,
            )
            
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)

            return redirect(url_for("get_all_posts"))
    
    return render_template("register.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        
        # Find user by email 
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        
        # Check stored password hash against entered password hashed
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))

    # Passing True or False if the user is authenticated. 
    return render_template("login.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated)


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):

    requested_post = db.get_or_404(BlogPost, post_id)

    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )

        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('show_post', post_id=post_id))
    
    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


#############################################################
# Init
#############################################################

if __name__ == "__main__":
    app.run(debug=True, port=5000)

"""
Forms
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

#############################################################
# Create Blog Post
#############################################################

class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

#############################################################
# User Registration
#############################################################

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

#############################################################
# Login Form
#############################################################

class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")

#############################################################
# Comment Form
#############################################################

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

##############################################################################
# DAY 70 - Git
##############################################################################

# Good ignore files - https://github.com/github/gitignore

##############################################################################
# DAY 71 - Full Working Blog
# Fully working blog - Python, Flask, Bootstrap, CKEditor, SQLAlchemy, PostgreSQL, Gunicorn, Mailgun
# Note: Final had CKE 4 rather than 5 which I did earlier
##############################################################################

"""
Main.py
"""

from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
# from flask_gravatar import GravatarXx
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import os
from dotenv import load_dotenv
from notifications import NotificationManager


#############################################################
# Configure App
#############################################################

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

ckeditor = CKEditor(app)
Bootstrap5(app)
notifications = NotificationManager()


#############################################################
# Configure Flask Login
#############################################################

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


#############################################################
# Gravatar
#############################################################

# For adding profile images to the comment section
# gravatar = Gravatar(app,
#                     size=100,
#                     rating='g',
#                     default='retro',
#                     force_default=False,
#                     force_lower=False,
#                     use_ssl=False,
#                     base_url=None)


#############################################################
# Configure Database
#############################################################

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    # Create reference to the User object. The "posts" refers to the posts property in the User class.
    author = relationship("User", back_populates="posts")
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    # Parent relationship to the comments
    comments = relationship("Comment", back_populates="parent_post")


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    # This will act like a list of BlogPost objects attached to each User.
    # The "author" refers to the author property in the BlogPost class.
    posts = relationship("BlogPost", back_populates="author")
    # Parent relationship: "comment_author" refers to the comment_author property in the Comment class.
    comments = relationship("Comment", back_populates="comment_author")


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    # Child relationship:"users.id" The users refers to the tablename of the User class.
    # "comments" refers to the comments property in the User class.
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    # Child Relationship to the BlogPosts
    post_id: Mapped[str] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")


with app.app_context():
    db.create_all()


#############################################################
# Admin Decorator
#############################################################

# Create an admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


#############################################################
# Flask Routes
#############################################################

######################
# Register
######################

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # Check if user email is already present in the database.
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        # This line will authenticate the user with Flask-Login
        login_user(new_user)
        return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=form, current_user=current_user)


######################
# Login
######################

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))

    return render_template("login.html", form=form, current_user=current_user)


######################
# Logout
######################

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


######################
# Home Page
######################

@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


######################
# Comments 
######################

# Add a POST method to be able to post comments
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    # Add the CommentForm to the route
    comment_form = CommentForm()
    # Only allow logged-in users to comment on posts
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form)


######################
# New Post
######################

@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


######################
# Edit Post
######################

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


######################
# Delete Post
######################

@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


######################
# About
######################

@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


######################
# Contact Page
######################

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        notifications.send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)    
    return render_template("contact.html", current_user=current_user, msg_sent=False)


#############################################################
# Init
#############################################################

if __name__ == "__main__":
    app.run(debug=True, port=5000)


"""
Forms.py
"""


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Create a form to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


# Create a form to add comments
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
