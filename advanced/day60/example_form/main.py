from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        return f"💪 Success! Form submitted. User: {request.form['username']}, Pass: {request.form['password']}"
    else:
        error = 'Invalid username/password'
        return f"❌ Fail!"
    
if __name__ == "__main__":
    app.run(debug=True)
