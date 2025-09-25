"""
HTML & URL Parsing in Flask
Higher / Lower Game
"""

# Decorator functions can be used for Routing

# https://www.mysite.com/
# https://www.mysite.com/bye

from flask import Flask

app = Flask(__name__)

# Decorator functions can be used for Routing
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye(): 
    return "<p>Thanks for coming, goodbye!</p>"

# Decorator functions with Variables can be used for advanced Routing
@app.route("/<name>")
def greet(name):
    return f"Hello, {name}!"

# Decorator functions using Path
@app.route("/username/<path:name>/")
def greeting(name):
    return f"Hello, {name}!"
# http://127.0.0.1:5000/username/james/112/
# Hello, james/112!

# Decorator functions with multiple variables
@app.route("/username/<name>/<int:number>")
def age(name, number):
    return f"Hello, {name}, you are {number} years old!"

# Debug mode autoreloads when file saved
if __name__ == "__main__":
    app.run(debug=True)


"""
Example Decorators
"""

from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        bold = function()
        return f"<b>{bold}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        emphasis = function()
        return f"<i>{emphasis}</i>"
    return wrapper

def make_underline(function):
    def wrapper():
        italic = function()
        return f"<u>{italic}</u>"
    return wrapper

@app.route("/")
@make_bold
@make_emphasis
@make_underline
def hello_world():
    return "Hello, World!"

# Debug mode autoreloads when file saved
if __name__ == "__main__":
    app.run(debug=True)


"""
## Advanced Python Decorator Functions
"""

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("James")
new_user.is_logged_in = True
create_blog_post(new_user)

"""
Advanced Decorators

Create a logging_decorator() which is going to print the name of the function that was called, 
the arguments it was given and finally the returned output: 
    You called a_function(1,2,3) 
    It returned: 6 

The value 6 is the return value of the function.

Don't change the body of a_function. 
"""

def logging_decorator(func):
    def wrapper(*args):
        result = func(*args)
        print(f"You called {func.__name__}{args}")
        print(f"It returned: {result}")
        return result
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1,2,3)

"""
Final Project - Higher or Lower URLs

Now it's time to complete the final project of the day, the higher lower game that we created in Day 14, but now with a real website.

1. Create a new project in PyCharm called higher-lower, add a server.py file.
2. Create a new Flask application where the home route displays an 

<h1> that says "Guess a number between 0 and 9" and display a gif of your choice from giphy.com.

Alternatively use the one I found on Giphy: https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif

3. Generate a random number between 0 and 9 or any range of numbers of your choice.
4. Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" 
and checks that number against the generated random number. 
If the number is too low, tell the user it's too low, same with too high or if they found the correct number. 
Try to make the <h1> text a different colour for each page.  e.g. If the random number was 5:

    3 is too low:
    7 is too high:
    and 5 is just right:

Here are the GIF URLs I used, but it's way more fun finding your own on giphy.com
High: https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif
Low: https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif
Correct: https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif
"""

from flask import Flask
import random

answer = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <h1>Guess a number between 0 and 9</h1>
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Number guessing game'>
        """

@app.route("/<int:number>")
def guess(number):
    if number > answer:
        return """
            <h1 style='color: red'>You guessed too high</h1>
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='Too high'>
            """
    elif number < answer:
        return """
            <h1 style='color: blue'>You guessed too low</h1>
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='Too low'>
            """             
    else:
        return """
            <h1 style='color: green'>You are correct!</h1>
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='Correct'>
            """   

if __name__ == "__main__":
    app.run(debug=True)
    