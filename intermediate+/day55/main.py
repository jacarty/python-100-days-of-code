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