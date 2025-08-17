from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, x_start, y_start):
        super().__init__()
        
        self.random_colour = COLORS[random.randint(0, 5)]

        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(self.random_colour)
        self.penup()
        self.setheading(180)
        self.goto(x_start, y_start)
        
        self.y = y_start
        self.x_move = MOVE_INCREMENT
        self.move_speed = 0.1

    def move_car(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.y)
