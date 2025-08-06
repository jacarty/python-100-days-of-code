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

