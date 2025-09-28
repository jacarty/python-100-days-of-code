from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blogs_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = blogs_response.json()
    return render_template("index.html", posts = all_posts)

@app.route('/post/<int:id>')
def get_post(id):
    blogs_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    article = blogs_response.json()[id-1]
    print(article)
    return render_template("post.html", post = article)

if __name__ == "__main__":
    app.run(debug=True)
