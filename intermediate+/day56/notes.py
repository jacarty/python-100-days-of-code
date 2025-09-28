"""
Static Files, HTML/CSS File Rendering
Project is Personal Namecard Site

HTML files go in the templates folder
Static files such as media, css etc. go in static folder

In Chrome Dev for real time field editing
Then save the page

document.body.contentEditable=true
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def website():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
