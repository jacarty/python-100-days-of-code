"""
Consolidated Notes from Intermediate Section (Days 16-26)
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


# =============================================================================
# DAY 22 - Making Pong
# =============================================================================

"""
Making Pong

1. Set up the Main Screen

2. Create a Paddle that responds to Key Presses

3. Write the Paddle Class and Create the Second Paddle

4. Write the Ball Class and Make the Ball Move

5. Add the Ball Bouncing Logic

6. How to Detect Collisions with the Paddle

7. How to Detect when the Ball goes Out of Bounds

8. Score Keeping and Changing the Ball Speed

"""


# =============================================================================
# DAY 24 - Working with local files and directories
# =============================================================================

"""
Working with local files and directories
"""

# Open, read and close a file
# You need to rememeber to close to free up memory
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Using with method closes files when you've finished with it
with open("my_file.txt") as f:
    contents = f.read()
    print(contents)

# Writing to a file; w overwrites the content
with open("my_file.txt", mode="w") as f:
    contents = f.write("My text.")

# Writing to a file; a appends
with open("my_file.txt", mode="a") as f:
    contents = f.write("\nAdditional text.")
    print(contents)

# Writing to a file that doesn't exist, creates it.
with open("new_file.txt", mode="a") as f:
    contents = f.write("Hello, this is a new file with text.")
    print(contents)

# Related to files
# import OS
import os
# Show current working directory
print("Current working directory:", os.getcwd())
# List files in current directory
print("Files in current directory:", os.listdir())


"""
Instructor Mail Merge
"""

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


# =============================================================================
# DAY 25 - Working with CSV files and analysing data with Pandas
# =============================================================================

"""
Working with CSV files and analysing data with Pandas
"""

# open CSV and add to list
# results in a a messy list though

with open("./weather_data.csv") as file:
    data = file.readlines()
    print(data)
    # ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

######
# use the python csv module
######

import csv

with open("./weather_data.csv") as file:
    data = csv.reader(file)
    print(data)
    # create object
    # <_csv.reader object at 0x10510d2a0> 
    for row in data:
        print(row)
        """
        ['day', 'temp', 'condition']
        ['Monday', '12', 'Sunny']
        ['Tuesday', '14', 'Rain']
        ['Wednesday', '15', 'Rain']
        ['Thursday', '14', 'Cloudy']
        ['Friday', '21', 'Sunny']
        ['Saturday', '22', 'Sunny']
        ['Sunday', '24', 'Sunny']
        """

# add just the temperatures to the list temp
# no heading
# add as integer
import csv

with open("./weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
print(data)
"""
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
"""

data = pandas.read_csv("./weather_data.csv")
print(data["temp"])

"""
0    12
1    14
2    15
3    14
4    21
5    22
6    24
"""

######
# Check data type
######
data = pandas.read_csv("./weather_data.csv")
print(type(data))
# <class 'pandas.core.frame.DataFrame'>

######
# Check data type
######
data = pandas.read_csv("./weather_data.csv")
print(type(data["temp"]))
# <class 'pandas.core.series.Series'>

"""
The two primary data structures of pandas, Series (1-dimensional) and DataFrame (2-dimensional), handle the vast majority of typical use cases in finance, statistics, social science, and many areas of engineering. For R users, DataFrame provides everything that R's data.frame provides and much more. pandas is built on top of NumPy and is intended to integrate well within a scientific computing environment with many other 3rd party libraries.
"""

######
# Open Data
######
data = pandas.read_csv("./weather_data.csv")

######
# Pandas DataFrame (workbook) To_Dictionary
######
data_dict = data.to_dict()
print(data_dict)

######
# # Pandas Series (column) To_List
######
temp_list = data["temp"].to_list()
print(temp_list)


######
# calculate the average temperature
# manual way
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

total = 0 

# Pandas Series (column) To_List
for temperature in data["temp"].to_list():
    total += temperature

average = total / len(data["temp"].to_list())
print(average)

######
# calculate the average temperature
# with statistics
######

import pandas
import statistics

# Open Data
data = pandas.read_csv("./weather_data.csv")

temperatures = data["temp"].to_list()
statistics.mean(temperatures)

######
# calculate the average temperature
# with pandas
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

print(data["temp"].mean())

######
# find the maximum temperature
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

print(data["temp"].max())

"""
Get temp column
data["temp"]

Another way to call a column is simply
data.temp
"""

print(data.temp)

######
# return a row of data, e.g. Monday
######

print(data[data.day == "Monday"])

######
# return the row with highest temp of week
######

max_temp = data.temp.max()
print(data[data.temp == max_temp])

######
# alternative
######

print(data[data.temp == data.temp.max()])

######
# tapping in to a row
######

monday = data[data.day == "Monday"]
print(monday.condition)

monday = data[data.day == "Monday"]
print(monday.temp)


######
# get temp and convert to Fahrenheit
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

monday = data[data.day == "Monday"]
fahrenheit = (monday.temp[0] * (9/5)) + 32
print(fahrenheit)

"""
Create a Dataframe
"""

import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

#####
# output to CSV
#####

data.to_csv("new_data.csv")


"""
https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data

Count Squirrels By Fur Colour

Gray
Cinnamon
Black
"""

import pandas
data = pandas.read_csv("./squirrel_data.csv")
# print(data["Primary Fur Color"])

values = data["Primary Fur Color"].value_counts()
print(values)
values.to_csv("squirrel_count.csv")


########
# Instructor making dataframe and exporting
# Central Park Squirrel Data Analysis
########
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


# =============================================================================
# DAY 26 - Lists and Dictionary Comprehensions
# =============================================================================

"""
Lists and Dictionary Comprehensions
"""


# =============================================================================
# DAY 27 - GUI with Tkinter and Functional Arguments
# =============================================================================

"""
GUI with Tkinter and Functional Arguments
"""
# import
import tkinter

#### Windows

# create a window
window = tkinter.Tk()

# title window
window.title("My GUI Program")
# minimum size (autoscales by default)
window.minsize(width=500, height=300)

#### Labels
my_label = tkinter.Label(text="I am a label", font=("courier", 11, "bold"))
my_label.pack(side="left")

# keep window on screen; has to be at the bottom of program
window.mainloop()

"""
##### Keyword arguments
"""

def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    pass

my_function(a=1, b=2, c=2)    

#### Arguments with default values
def my_function(a=1, b=2, c=3):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    pass

my_function()    

#### Overwrite one value
def my_function(a=1, b=2, c=3):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    pass

my_function(b=4)    

"""
##### Unlimited positional arguments

They get passed in as a Tuple

"""

#print them
def add(*args):
    for n in args:
        print(n)

add(1, 2, 6, 10)

### add them
def add(*args):
    return(sum(args))

print(add(1, 2, 6, 10))

# get one value
def add(*args):
    print(args[1])

add(1, 2, 6, 10)

"""
##### Unlimited positional keyword arguments

They get passed in as a Dictionary

"""
### kwargs
def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    
    print(kwargs["add"])

calculate(add=3, multiply=8)

### with a value and kwargs
def calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply=8)

### create Class with kwargs (kw)
class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Bugait", model="Veyron")
print(my_car.model)

### using get is the way for Classes with optional inputs
### if the value is empty it just returns none
### the key lookup would cause an error if not passed
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")

my_car = Car(make="Bugait", model="Veyron")
print(my_car.colour)


### you can mix all three
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
    # 4 (7, 3, 0) {'x': 10, 'y': 64}
    
all_aboard(4, 7, 3, 0, x=10, y=64)


"""
Examples of widgets

"""

from tkinter import *

def center_window(window, min_width=500, min_height=500):
    """Center window with minimum size but allow growth for content"""
    
    # Get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    
    # Use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    
    # Get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

my_window = Tk()
# show all available methods
# print(dir(my_window))
# give window a title
my_window.title("Distance Converter")
# function to set size and centre on screen
center_window(my_window)



# on screen label
my_label = Label(text="I am a label")
# lots of element can be configured with .config or individually
my_label.config(font=("courier", 12))
# pack always needed to position on screen
my_label.pack()


def button_clicked():
    print("I got clicked")
    # update the label text
    # my_label.config(text="Button was clicked")
    # use the input window text
    my_label.config(text=my_entry.get())

# on screen button
# command defines what happens when clicked; it calls the name of a function
my_button = Button(text="Click me", command=button_clicked)
# pack always needed to position on screen
my_button.pack()


# on screen Entry box
my_entry = Entry()
my_entry.pack()
my_entry.config(width=20)
# default text
my_entry.insert(END, string="enter email")


# multi line Text entry
my_text_entry = Text()
# box size
my_text_entry.config(width=30, height=10)
# start cursor in this box
my_text_entry.focus()
my_text_entry.insert(END, "Some starting text in the box")
print(my_text_entry.get(1.0, END))
my_text_entry.pack()


# spinbox 
def spinbox_used():
    print(my_spinbox.get())

my_spinbox = Spinbox()
my_spinbox.config(from_=0, to=10, width=5, command=spinbox_used)
my_spinbox.pack()


# scale / scroll to set number
def scale_used(value):
    print(value)

# scale / scroll to set number
my_scale = Scale()
my_scale.config(from_=0, to=100, command=scale_used)
my_scale.pack()

# checkbutton
def checkbutton_used():
    # prints 1 in clicked otherwise 0
    print(checked_state.get())

checked_state = IntVar()
my_checkbutton = Checkbutton()
my_checkbutton.config(text="Is On?", variable=checked_state, command=checkbutton_used)
my_checkbutton.pack()

# radio button 
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
my_radiobutton1 = Radiobutton()
my_radiobutton2 = Radiobutton()
my_radiobutton1.config(text="Option1", value=1, variable=radio_state, command=radio_used)
my_radiobutton2.config(text="Option2", value=2, variable=radio_state, command=radio_used)
my_radiobutton1.pack()
my_radiobutton2.pack()

# listbox
def listbox_used(event):
    # gets current selection from listbox
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
my_listbox.config(height=4)
fruits = ["Apple", "Orange", "Pineapple", "Strawberry"]
for item in fruits:
    my_listbox.insert(fruits.index(item), item)
my_listbox.bind("<<ListboxSelect>>", listbox_used)
my_listbox.pack()

# keep window open; last line
my_window.mainloop()


"""
can't mix pack and grid in same program

let Tk order and place on window
my_label.pack()

specific places on window
my_label.place(x=50, y=50)

using grid to divide the window and place
my_label.grid(column=0, row=0)
"""

from tkinter import *

def center_window(window, min_width=0, min_height=0):
    """Center window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

def button_clicked():
    """Create a button"""
    print("I got clicked")
    label.config(text=entry.get())

# create Window and centre in screen
window = Tk()
window.title("Distance Converter")
center_window(window)

# label
label = Label(text="I am a label")
#label.config(font=("courier", 12), padx=20, pady=20)
label.grid(column=0, row=0)

# button one
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# button two
button_2 = Button(text="Button 2")
button_2.grid(column=2, row=0)

# entry box
entry = Entry()
entry.config(width=20)
entry.insert(END, string="enter email")
entry.grid(column=3, row=3)

# centre window
center_window(window, min_width=0, min_height=0)
# keep alive
window.mainloop()

#######################
# miles to KM converter
#######################

from tkinter import *

def center_window(window, min_width=0, min_height=0):
    """Center window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

def button_clicked():
    """Create a button"""
    print("I got clicked")
    calc = round((float(miles_entry.get()) * 1.609), 2)
    calc_label.config(text=calc)

# create Window and centre in screen
window = Tk()
window.title("Distance Converter")
center_window(window)
window.config(padx=10, pady=10)

# entry box
miles_entry = Entry()
miles_entry.config(width=10)
miles_entry.insert(END,string="0")
miles_entry.grid(column=1, row=0)

# miles label
miles_label = Label(text="Miles")
miles_label.config(font=("courier", 12))
miles_label.grid(column=2, row=0)

# equals to label
equals_label = Label(text="Is equal to")
equals_label.config(font=("courier", 12))
equals_label.grid(column=0, row=1)

# km label
calc_label = Label(text="0")
calc_label.config(font=("courier", 12))
calc_label.grid(column=1, row=1)

# label4
km_label = Label(text="KM")
km_label.config(font=("courier", 12))
km_label.grid(column=2, row=1)

# button
calc_button = Button(text="Calculate", command=button_clicked)
calc_button.config(font=("courier", 12))
calc_button.grid(column=1, row=2)

# centre window
center_window(window)
# keep alive
window.mainloop()


# =============================================================================
# DAY 28 - Building a Pomodoro App with Tkinter
# =============================================================================

"""
Building a Pomodoro App with Tkinter

The Pomodoro Technique
A time management method that breaks work into focused intervals, traditionally 25 minutes long, separated by short breaks.

Basic Flow:
Work (25 min) → Break (5 min) → Work (25 min) → Break (5 min) → 
Work (25 min) → Break (5 min) → Work (25 min) → Long Break (15-30 min)

Key Steps:
-- Choose a task to work on
-- Set timer for 25 minutes
-- Work with full focus until timer rings
-- Take a short break (5 minutes)

Repeat - After 4 pomodoros, take a longer break

The technique helps maintain focus, prevents burnout, and makes large tasks feel more manageable by breaking them into smaller, timed chunks.

"""

# https://colorhunt.co/


#######################################################################
#
# Dynamic Datatyping
# We're changing the Variable from Int to Str
# This isn't possible in all languages 
#
# https://stackoverflow.com/questions/11328920/is-python-strongly-typed
#
#######################################################################

def count_down(count):
    # timer function; 1s (1000ms)

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec == f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)



"""

Pomodoro Application

"""

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps

    reps += 1

    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    work_min = WORK_MIN * 60

    # 8th round
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    # 2nd, 4th and 6th round
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)
    # 1st, 3rd, 5th, 7th round
    else:
        count_down(work_min)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    # timer function; 1s (1000ms)

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

def center_window(window, min_width=200, min_height=200):
    """Center window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, fg=GREEN, font=("FONT_NAME", 30, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.config(
    bg=YELLOW, 
    activebackground=YELLOW,
    highlightbackground=YELLOW,
    highlightcolor=YELLOW
)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(
    bg=YELLOW, 
    activebackground=YELLOW,
    highlightbackground=YELLOW,
    highlightcolor=YELLOW
)
reset_button.grid(column=2, row=2)

checkmarks = Label()
checkmarks.config(bg=YELLOW, fg=GREEN, font=("FONT_NAME", 16, "bold"))
checkmarks.grid(column=1, row=3)

canvas = Canvas(width=220, height=250, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="tomato.png")
canvas.create_image(110, 125, image=bg_image)
timer_text = canvas.create_text(110, 140, text="00:00", fill="white", font=("FONT_NAME", 16, "bold"))
canvas.grid(column=1, row=1)

center_window(window)
window.mainloop()


# =============================================================================
# DAY 29 - Building a Password Generator with Tkinter
# =============================================================================

"""

Building a Password Generator with Tkinter

File output format
website | email | password

"""

from tkinter import *
from tkinter import messagebox # need to import message box
import string # used to get letters, digits and punctuation
import pyperclip
import random

FONT = "courier"
FONT_SIZE = 11

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(16))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy()

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"""These are the details entered: \n
                                Website: {website}\n
                                Email: {email}\n
                                Password: {password}\n
                                Is it okay to save?""")

        if is_ok:
            with open("./passwords.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

def centre_window(window, min_width=0, min_height=0):
    """Centre window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(127, 100, image=bg_image)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website:", font=(FONT, FONT_SIZE))
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.config(width=42)
website_entry.focus() # default cursor to this box
website_entry.grid(column=1, columnspan=2, row=1)

email_label = Label()
email_label.config(text="Email/Username:", font=(FONT, FONT_SIZE))
email_label.grid(column=0, row=2)

email_entry = Entry()
email_entry.config(width=42)
email_entry.insert(0, "test@email.com") # default text
email_entry.grid(column=1, columnspan=2, row=2)

password_label = Label()
password_label.config(text="Password:", font=(FONT, FONT_SIZE))
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(command=generate_password)
password_button.config(text="Generate Password", font=(FONT, FONT_SIZE))
password_button.grid(column=2, row=3)

add_button = Button(command=save_password)
add_button.config(text="Add", width=40, font=(FONT, FONT_SIZE))
add_button.grid(column=1, columnspan=2, row=4)

#centre_window(window)
window.mainloop()


# =============================================================================
# DAY 30 - Errors, Exceptions and Saving JSON Data
# =============================================================================

"""
Errors, Exceptions and Saving JSON Data

try:

except:

else:

finallly:

"""

######
# File Example
######

# would fail if file doesn't exist
# with open("a_file.txt") as f:
#     f.read()

# try this
try:
    f = open("a_file.txt")
    a_dict = {"key" : "value"}
    print(a_dict["ads"])
# error specific
except FileNotFoundError:
    print("There was an error opening, creating file")
    f = open("a_file.txt", "w")
    f.write("Hello")
# error specific that's captured
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist.")
# run if the try succeeds
else:
    content = f.read()
    print(content)
# happens regardless if the code succeeds or fails
finally:
    f.close()
    print("The file was closed.")

    # allows you to raise an error and message
    raise TypeError("This is an error I made up.")

######
# Realk Example
# Valid code but nonsense result
######

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)

"""
IndexError Handling

Issue 

We've got some buggy code. Try running the code. The code will crash and give you an IndexError.
This is because we're looking through the list of fruits for an index that is out of range. 


Objective 

Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie". 


IMPORTANT: The exception handling should NOT allow each fruit to be printed when there is an exception. e.g. it should not print out Apple pie, Pear pie and Orange pie, when there is an exception it should only print "Fruit pie".  
"""

fruits = ["Apple", "Pear", "Orange"]
     
# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")
     
make_pie(4)



"""
KeyError Handling

We've got some buggy code, try running the code. The code will crash and give you a KeyError.
This is because some of the posts in the facebook_posts don't have any "Likes". 

Objective 
Use what you've learnt about exception handling to prevent the program from crashing.
"""

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
 
    total_likes = 0
    for post in posts:
      try:
        total_likes = total_likes + post['Likes']
      except KeyError:
        pass 
    
    return total_likes
 
 
count_likes(facebook_posts)



############
# Mine
############

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

while True:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, please only enter letters of the alphabet.")
        continue
    else:
        print(output_list)
        break

""""
JSON
"""

########
# JSON file to read
########
# dict = dictionary to pass in (serialise)
# file_name is output
# indent=4 is number spaces to add (for readability)
json.dump(dict, file_names, indent=4)

########
# JSON file name to load
########
# outputs back to dictionary (deserialise)
json.load(file_name)

########
# update a JSON file
########
# read old data from file
data = json.load(data_file)
# update old data with new data
json.update(dict)
# write file back
json.dump(data, file_name, indent=4)

"""

Update Password Generator

File output format JSON

"""

from tkinter import *
from tkinter import messagebox # need to import message box
import string # used to get letters, digits and punctuation
import pyperclip
import random
import json

FONT = "courier"
FONT_SIZE = 11

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(16))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"""These are the details entered: \n
                                       Website: {website}\n
                                       Email: {email}\n
                                       Password: {password}\n
                                       Is it okay to save?""")

####################
# we could avoid except / else repitition with a function
# being left like this for future readability
####################

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # read data file
                    data = json.load(file)

            except FileNotFoundError:
                print("File not found. Needs to be created.")
                with open("data.json", "w") as file:
                    # saving updated data
                    json.dump(new_data, file, indent=4)

            else:
                # update old data with new data
                data.update(new_data)

                with open("data.json", "w") as file:
                    # saving updated data
                    json.dump(data, file, indent=4)
                
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    # print("search")
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        email_lookup = data[website]["email"]
        pw_lookup = data[website]["password"]

    except FileNotFoundError:
        messagebox.showinfo(title=f"{website}", message="No data file found.")

    except KeyError:
        messagebox.showinfo(title=f"{website}", message="No details exist for the website.")

    else:
        messagebox.showinfo(title=f"{website}", message=f"""Email: {email_lookup}\n
                                                        Password: {pw_lookup}""")

# ---------------------------- UI SETUP ------------------------------- #

def centre_window(window, min_width=0, min_height=0):
    """Centre window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(127, 100, image=bg_image)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website:", font=(FONT, FONT_SIZE))
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.config(width=21)
website_entry.focus() # default cursor to this box
website_entry.grid(column=1, row=1)

search_button = Button(command=search_password)
search_button.config(text="Search Password", width=17, font=(FONT, FONT_SIZE))
search_button.grid(column=2, row=1)

email_label = Label()
email_label.config(text="Email/Username:", font=(FONT, FONT_SIZE))
email_label.grid(column=0, row=2)

email_entry = Entry()
email_entry.config(width=42)
email_entry.insert(0, "test@email.com") # default text
email_entry.grid(column=1, columnspan=2, row=2)

password_label = Label()
password_label.config(text="Password:", font=(FONT, FONT_SIZE))
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(command=generate_password)
password_button.config(text="Generate Password", font=(FONT, FONT_SIZE))
password_button.grid(column=2, row=3)

add_button = Button(command=save_password)
add_button.config(text="Add", width=40, font=(FONT, FONT_SIZE))
add_button.grid(column=1, columnspan=2, row=4)

#centre_window(window)
window.mainloop()


# =============================================================================
# DAY 31 - Flashcard Capstone Project
# =============================================================================

"""
Flashcard Project

https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists

https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish

https://github.com/hermitdave/FrequencyWords/tree/master/content/2018

"""


from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("./data/spanish_words_to_learn.csv")
    spanish_list = df.to_dict('records')
except:
    df = pd.read_csv("./data/spanish_words_1k.csv")
    spanish_list = df.to_dict('records')

random_word = {}
flip_timer = None

def known_word():
    global random_word
    spanish_list.remove(random_word)
    
    df = pd.DataFrame(spanish_list)
    df.to_csv("./data/spanish_words_to_learn.csv", index=False)
    generate_card()


def generate_card():
    global random_word, flip_timer
    random_word = random.choice(spanish_list)

    canvas.itemconfig(canvas_image, image=spanish_image)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=random_word["word"], fill="black")

    # cancel any running timer when a new card is generated
    if flip_timer:
        window.after_cancel(flip_timer)

    # set timer
    flip_timer = window.after(3000, flip_card)


def flip_card():
    english_word = random_word['translation']

    canvas.itemconfig(canvas_image, image=english_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")


def centre_window(window, min_width=0, min_height=0):
    """Centre window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
spanish_image = PhotoImage(file="./images/card_front.png")
english_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(410, 263, image=spanish_image)
card_title = canvas.create_text(400, 120, font=("ariel", 35, "italic"))
card_word = canvas.create_text(400, 263, font=("ariel", 60, "italic"))
canvas.grid(column=0, columnspan=2, row=0)

cross_button = Button(command=generate_card)
cross_image = PhotoImage(file="./images/wrong.png")
cross_button.config(image=cross_image, highlightthickness=0, bd=0)
cross_button.grid(column=0, row=1)

check_button = Button(command=known_word)
check_image = PhotoImage(file="./images/right.png")
check_button.config(image=check_image, highlightthickness=0, bd=0)
check_button.grid(column=1, row=1)

centre_window(window)
generate_card()
window.mainloop()