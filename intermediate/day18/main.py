"""
Create a painting of 10 x 10 rows of dots
Dots 20 in size
Space between dots 50
Always creates new dots left to right
"""

from turtle import Turtle, Screen
import random

# colours generate off "The Prodigy - Fat Of The Land" Album Cover

colors = [
    (15, 82, 186),    # Deep ocean blue
    (45, 125, 210),   # Bright sky blue
    (220, 95, 45),    # Orange crab shell
    (180, 65, 25),    # Dark orange/rust
    (25, 55, 95),     # Dark blue water
    (255, 140, 60),   # Bright orange highlights
    (10, 45, 75),     # Deep navy blue
    (200, 85, 40),    # Medium orange-red
    (65, 145, 225),   # Light blue water
    (140, 45, 20)     # Dark red-brown
]

dave = Turtle()
screen = Screen()
screen.colormode(255)

dave.shape("turtle")
dave.speed("fastest")

def random_colour():
    turtle_colour = colors[random.randint(0,9)]
    return turtle_colour

def draw_line_of_dots(num_dots, dot_size, space):
    for i in range(num_dots):
        colour = random_colour()
        dave.color(colour)
        dave.dot(dot_size)
        dave.penup()
        dave.forward(space)
        dave.pendown()

def new_line_of_dots(num_dots, space):
    dave.penup()
    dave.backward(num_dots * space)
    dave.left(90)
    dave.forward(space)
    dave.right(90)
    dave.pendown()
    
def draw_painting(dot_size, space, num_dots, num_rows):
    dave.penup()
    start_x = 22.5 * num_dots
    start_y = 22.5 * num_dots
    dave.setposition(-start_x, -start_y)
    dave.pendown()

    for i in range(num_rows):
        draw_line_of_dots(num_dots, dot_size, space)
        new_line_of_dots(num_dots, space)

draw_painting(dot_size=20, space=50, num_dots=10, num_rows=10)

screen.exitonclick()
