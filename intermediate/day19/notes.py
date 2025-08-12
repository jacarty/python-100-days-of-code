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