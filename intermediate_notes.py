"""
Consolidated Notes from Intermediate Section (Days 16-21)
This file contains a copy of all notes.py files from the intermediate folder.
"""

# =============================================================================
# DAY 16 - Object Oriented Programming
# =============================================================================

"""
Day 16 Content - Object Oriented Programming

The challenge will be a building the Coffee Machine with OOP.
"""

"""
Objects - consider two things:

What it has (attributes)
What it does (methods)

Can call / run multiple versions of the same object; we treat them as blueprints

Class (bluprint) & Ojects (created from the blueprint)

Example
Class = Car
Object = Car instance

# Pascal case used to capitalise the first letter of class to differentiate from variables, functions etc. which use underscores
car = CarBlueprint (class) 

"""

# example import of module
# import module
# fetch the variable from the module
import another_module
print(another_module.another_variable)


"""
Similar to above. In simple terms:
Import the Module turtle
Fetch the class Turtle and construct object from that blueprint with ()
Assigned to an object named Dan """

import turtle
dan = turtle.Turtle()

"""
Alternate is to just import the Class 
"""

from turtle import Turtle, Screen
dan = Turtle()
print(dan)

"""
To access the objects attributes

car.speed
car.fuel
"""

from turtle import Turtle, Screen

dan = Turtle()
print(dan)

my_screen = Screen()
print(my_screen.canvheight)

"""
To access the objects methods (things it does)

car.move()
car.stop()

Turtle documentation
https://docs.python.org/3/library/turtle.html 
"""

from turtle import Turtle, Screen

# create object dan from Class Turtle
dan = Turtle()
print(dan)
# call the method and set shape to Turtle
dan.shape("turtle")
# set colour of Dan using method color
dan.color("blue")
# move forward 100 paces
dan.forward(100)

# create object my_screen from Class Screen 
my_screen = Screen()
# set attribute
print(my_screen.canvheight)
# set attribute
my_screen.exitonclick()

"""
Python Packages

Collections of premade files that are packed together for a goal or purpose

e.g. To create an ascii table manually would be painful

print("| Pokemon Name | Type |")
print("-----------------------")

Python Package Index - pypi.org

use venv to isolate to this repo
pip install PrettyTable 

"""

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

"""
I added this to demonstrate a way to use a dictionary for the data
"""

from prettytable import PrettyTable

table = PrettyTable()
# change attribute to centre align (it already did but don't like right or left)
table.align = "c"

# create dictionary that fits the input requirements
data = {
    "Pokemon Name": ["Pikachu", "Squirtle", "Charmander"],
    "Type": ["Electric", "Water", "Fire"]
}

# loop dictionary to add colums and data
for column_name, column_data in data.items():
    table.add_column(column_name, column_data)

print(table)


# =============================================================================
# DAY 17 - Building Classes
# =============================================================================

"""
Day 17 Content - Building Classes

The challenge will be a building a Quiz Game with OOP.
"""

"""
Simply defined by class Name:
Then code follows.

Classes should have each letter of the first word Capitilised
Reminder it's called: PascalCase 

vs camelCase which has the first word lower, and the rest first char upper

vs snake_case which is lower case and separated by _ (variables, py files etc.)

camelCase - commonly used for variable and function names in languages like JavaScript and Java

PascalCase - often used for class names and type names in languages like Python, C# and .NET

class Car:
"""
# Pass simply used to avoid the formatting error of expecting code after the :
class User: # define class
    pass

user1 = User() # create object from Class

"""
How to create an attribute for your class

An attribute is a variable associated with an object

Examples:

But notice, unless defined in the Class you can create any attributes, 
and it's also errorprone/potentially inconsitent

The notion of a Class is to specify these pieces of information 
when creating the object from the Class in the form of Constructors
"""

class User: # define class
    pass

user1 = User() # create object from Class
user1.id = "001"
user1.username = "alan"

print(user1.username)

user2 = User()
user1.id = "002"
user1.name = "steve"

"""
Constructor
A part of the blueprint that specifies what should happen when the object is being constructed

When the object is being initialised from the Class
you set the variables, counters, switches to their starting values 

You create the Constructor by using the init function - it's a special method

class Car:
    def __init__(self):
    #intialise attributes

Self is the Object being created
"""

class User: # define class
    
    # this is where we create or intialise the starting values for our attributes
    # the __init__ function is called ever time you create a new object from this Class
    def __init__(self):
        print("new user being created")

user1 = User() # create object from Class
user1.id = "001"
user1.username = "alan"
print(user1.username)

user2 = User()
user2.id = "002"
user2.name = "steve"
print(user2.name)

"""
Will result in:

new user being created
alan
new user being created
steve

Reminder:
Attributes - things a Class has
Methods - things a Class does

Example on setting attributes
E.g. a car has 5 seats
You pass in the parameter alongside the Object being created (initialised)
The parameter gets passed in when the Object is constructed from the Class
You can pass in as many parameters as you want
When you recieve that data you can use it to set that Objects attributes
"""

# sets the numher of seats to 5
class Car:
    def __init__(self, seats):
        self.seats = seats
        print(seats)

my_car = Car(5)

# which is effectively the same result as

my_car.seats = 5

"""
/\ /\ /\ The key Point on above
The __init__ method is convenient, automated way to set attributes when an object is created. 
But the actual mechanism of setting self.seats = seats inside __init__ 
is the same as setting my_car.seats = 5 outside of it.
"""

class User: 

    def __init__(self):
        pass

user1 = User() # create object from Class
user1.id = "001"
user1.username = "alan"
print(user1.username)

#returns alan

""" we're creating attributes at the time of constuction 
typical convention is for the name of parameter to match name of attribute (doesnt have to)
"""

class User: # define class

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user1 = User("001", "alan") 
print(user1.username)

"""Because we've now set the parameters in the constructor, 
you have to use them when creating the object from the Class

If not you will receive an error:
TypeError: __init__() missing 2 required positional arguments: 'user_id' and 'username'
See below
"""
user2 = User()
user2.id = "002"
user2.name = "steve"
print(user2.name)

"""
You can also set default values that done have to be passed as parameters
"""

class User: # define class

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 

user1 = User("001", "alan") 
print(user1.followers)

# returns 0

"""
methods = things the Class does

e.g attribute = has 5 seats
method = change to 2 seats

example
"""

class User: # define class

    def enter_race_mode(): # method
        self.seats = 2 # gets seats attribute and changes to 2

my_car.enter_race_mode()


"""
in practice - instagram followers
"""
class User: # define class

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 
        self.following = 0

    # you always use 'self' as first parameter in a method so the function knows the Ojnect that called it
    # assume we follow a user (instagram)
    def follow(self, user):
        user.followers += 1     # the user we're following goes up by 1
        self.following += 1     # the user count we're following goes up by 1

user1 = User("001", "alan") 
user2 = User("002", "dan") 

user1.follow(user2)

print(f" user 1 followers: {user1.followers}")
print(f" user 1 following: {user1.following}")

print(f" user 2 followers: {user2.followers}")
print(f" user 2 following: {user2.following}")

 """
 returns
 user 1 followers: 0
 user 1 following: 1
 user 2 followers: 1
 user 2 following: 0
 """


# =============================================================================
# DAY 18 - Turtle Graphics, Tuples and Importing Modules
# =============================================================================

"""
Day 18 Content - Turtle Graphics, Tuples and Importing Modules

The challenge will be a building a Drawing.
"""

from turtle import Turtle, Screen

dave = Turtle()
dave.shape("turtle")
dave.color("orange")
dave.pencolor("orange")

for move in range(4):
    dave.forward(50)
    dave.left(90)

screen = Screen()
screen.exitonclick()

"""
Importing Modules

Basic = import ModuleName
e.g. 
import turle
dave = turtle.Turtle()

Specific
e.g usefule when calling a lot
from turtle import Turtle
dave = Turtle()
steve = Turtle()
alan = Turtle()

Import everything (it's not good practice to do this)
from turtle import *
BUT it;s less obvious where things come from
i.e. where does the method come from? which Class?

forward(100)
vs dave.forward(100) when you import a specific Module
"""

"""
Import method as.... ALIAS

import turtle as t
dave = t.Turtle()
"""

"""
Dashed drawing
"""

from turtle import Turtle, Screen

dave = Turtle()
dave.shape("turtle")
dave.color("orange")
dave.pencolor("orange")

for move in range(4):
    dave.forward(50)
    dave.penup()
    dave.forward(50)
    dave.pendown()
    dave.left(90)

screen = Screen()
screen.exitonclick()

"""
Drawing shapes continuosly (in sequence)
Triangle, Square, Pentagon, Hexagon, Heptagon, Octogon, Nonogon and Decacon
Lenght of all = 100
Random colours

Maths:
360 / num_of_sides = angle
"""

from turtle import Turtle, Screen

dave = Turtle()
dave.shape("turtle")
dave.color("orange")
dave.pencolor("orange")

number_of_sides = 4

while number_of_sides < 11:
    angle = 360/number_of_sides
    for sides in range(number_of_sides):
        dave.forward(100)
        dave.right(angle)

    number_of_sides +=1
    
screen = Screen()
screen.exitonclick()


"""
Instructor
They created a function over loop (didnt suggest function in course)
"""

import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

"""
Random Walk
Move Faster
Thicker lines

"""

from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

dave = Turtle()
dave.shape("turtle")

def draw_shape(move,rotate):
    dave.forward(move)
    dave.setheading(rotate)
    dave.color(random.choice(colours))

turn = [0, 90, 180, 270]
dave.width(5)
dave.speed(8)

for moves in range(50):
    rotation = random.choice(turn)
    move = random.randint(10, 50)
    draw_shape(move, rotation)

screen = Screen()
screen.exitonclick()

"""
Tuples
Ordered Data type (1, 3, 4)
my_tuple = (1, 3, 9)
my_tuple[0] = 1

You can't change or remove items in a Tuple
Once created it is immutable
You can convert to list by list(my_tuple)
"""

from turtle import Turtle, Screen
import random

dave = Turtle()
screen = Screen()
screen.colormode(255)

dave.shape("turtle")
dave.width(5)
dave.speed(8)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_colour = (r, g, b)
    return turtle_colour

def draw_shape(move, rotate, colour):
    dave.forward(move)
    dave.right(rotate)
    dave.color(colour)

turn = [90, 180, 270]

for moves in range(50):
    rotation = random.choice(turn)
    move = random.randint(10, 50)
    colour = random_colour()
    draw_shape(move, rotation, colour)

screen.exitonclick()

"""
Create Spirograph
"""

from turtle import Turtle, Screen
import random

dave = Turtle()
screen = Screen()
screen.colormode(255)

dave.shape("turtle")
dave.width(3)
dave.speed("fastest")

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_colour = (r, g, b)
    return turtle_colour

def draw_shape(move, rotate, colour):
    dave.circle(move)
    dave.left(rotate)
    dave.color(colour)

def draw_spirograph(num_circles, size):
    rotate = 360 / num_circles
    for moves in range(num_circles):
        circle_size = size
        colour = random_colour()
        draw_shape(circle_size, rotate, colour)

draw_spirograph(num_circles=70, size=125)

screen.exitonclick()


"""
Instructor version
"""

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()


# =============================================================================
# DAY 19 - More Turtle Graphics, Event Listeners, State and Multiple Instances
# =============================================================================

"""
More Turtle Graphics, Event Listeners, State and Multiple Instances

The Challenge is Turtle Coordinate System Quiz
"""

"""
Event listeners allow you to tap into key strokes etc.
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen() # set focus on TurtleScreen (in order to collect key-events)
# reminder, when you pass a function as an input, you only pass the name
screen.onkey(key="space", fun=move_forwards) # this function is used to bind fun to the key-release event of the key
screen.exitonclick() 

"""
Example higher order function.
Frequently used when needing to listen for events then trigger a function

def apply_operation(func, x, y):
    '''Higher-order function that applies any function to two numbers'''
    return func(x, y)

# Define basic operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

# Usage
print(apply_operation(add, 8, 3))       # Output: 11
print(apply_operation(multiply, 4, 7))  # Output: 28
print(apply_operation(divide, 15, 3))   # Output: 5.0

"""

"""
Etch a Sketch

Mine
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(5)

def move_backwards():
    tim.backward(5)

def counter_clockwise():
    tim.left(5)

def clockwise():
    tim.right(5)

def clear_and_centre():
    screen.reset()


screen.listen() # set focus on TurtleScreen (in order to collect key-events)
# reminder, when you pass a function as an input, you only pass the name
screen.onkey(fun=move_forwards, key="Up") 
screen.onkey(fun=move_backwards, key="Down") 
screen.onkey(fun=counter_clockwise, key="Left")
screen.onkey(fun=clockwise, key="Right")
screen.onkey(fun=clear_and_centre, key="c")
screen.exitonclick() 


"""
Instructor
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()

"""
Turtle Race Game
"""

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turle will win the race? Enter a colour: ")
print(user_bet)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
height = -125

for turtle in range(0, 6):
    colour = colours[turtle]
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour)
    new_turtle.penup() 
    new_turtle.goto(x=-200, y=height)
    turtle_list.append(new_turtle)
    height += 50


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("You win")
            else:
                print(f"You've lost. The winning turtle was {winning_colour}.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick() 


# =============================================================================
# DAY 21 - Inheritance & Slicing
# =============================================================================

"""
Inheritance & Slicing

class Fish():
    def __init__(self):

    
class Fish(Animal):
    def __init__(self):
        super().__init__()

"""

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe() # this does everything the breathe method above does
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()
nemo.swim()
print(nemo.num_eyes)

"""

slicing works on lists and tuples
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

piano_keys[2:5]
returns c, d, e
2, 3 and 4

piano_keys[2:5:2]
returns c, e
every other one

piano_keys[::-1]
returns, g, f, e, d, c, b, a

"""

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[1:])

# returns 're', 'mi', 'fa', 'so', 'la', 'ti'

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[:5])

# returns 'do', 're', 'mi', 'fa', 'so'