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
