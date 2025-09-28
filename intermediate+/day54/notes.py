"""
WebDev with Flask

FE Frameworks = Angular, React
BE Frameworks = Node, Django/Flask
FE Languages = HTML, CSS, JS
BE Languages = JS, Java, Python, Ruby etc

Python BEs = Flask, Django, Bottle, CherryPie, Pyramid


https://pythontutor.com/visualize.html#mode=edit
"""

# run hello.py
# export FLASK_APP=hello.py
# flask run

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()


## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()

"""
Objective Create your own decorator function to measure the amount of seconds that a function takes to execute. 

Expected Output:
    1695050908.1985211
    fast_function run speed: 0.33974480628967285s
    slow_function run speed: 2.9590742588043213s

Calculating Time   

time.time() will return the current time in seconds since January 1, 1970, 00:00:00.

Try running the starting code to see the current time printed. 
If you run the code after a while, you'll see a new time printed.

e.g. first run:  1598524371.736911 
second run:  1598524436.357875 

The time difference = second run - first run  64.62096405029297  (approx 1 minute) 

Given the above information, complete the code exercise by printing out the time it takes to run the fast_function() vs the slow_function().

You will need to complete the speed_calc_decorator() function.  
 """

import time
    
def speed_calc_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result
    return wrapper
    
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
    
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
    
fast_function()
slow_function()

# fast_function run speed: 0.030230998992919922s
# slow_function run speed: 0.3031938076019287s