from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, start_position):
        super().__init__()
        self.move_distance = 20
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.color("white")
        self.penup()
        self.goto(start_position)

    def left(self):
        new_x = self.xcor() - self.move_distance
        if new_x > -275:  # Check boundary
            self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + self.move_distance
        if new_x < 275:  # Check boundary
            self.goto(new_x, self.ycor())
