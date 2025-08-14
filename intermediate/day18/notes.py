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
