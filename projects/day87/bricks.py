from turtle import Turtle

class Bricks(Turtle):

    def __init__(self, x, y, colour):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.x_cor = x
        self.y_cor = y
        self.colour = colour

    def draw_brick(self):
        self.setheading(0)
        self.goto(self.x_cor, self.y_cor)
        self.fillcolor(self.colour)
        self.begin_fill()
        
        self.forward(38)
        self.right(90)

        self.forward(20)
        self.right(90)

        self.forward(38)
        self.right(90)
        
        self.forward(20)
        self.right(90)

        self.end_fill()
