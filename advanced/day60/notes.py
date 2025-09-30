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
