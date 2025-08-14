from turtle import Turtle

STARTING_COORDS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        # Create snakes
        # starting_snake_size = 3
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for i in STARTING_COORDS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(i)
            self.snake_list.append(snake)

    def move(self):
        for snake in range(len(self.snake_list) - 1, 0, -1): # start, stop, step
            new_x = self.snake_list[snake - 1].xcor()
            new_y = self.snake_list[snake - 1].ycor()
            self.snake_list[snake].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)