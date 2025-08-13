from turtle import Turtle, Screen
import time
import random

# Define screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # disable animation

# Create snakes
# starting_snake_size = 3
starting_coords = [(0, 0), (-20, 0), (-40, 0)]
snake_list = []

for i in starting_coords:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(i)
    snake_list.append(snake)

game_is_playing = True

while game_is_playing:

    screen.update() # update screen to account for disabled animation
    time.sleep(0.2) # sleep in seconds

    for snake in range(len(snake_list) - 1, 0, -1): # start, stop, step
        new_x = snake_list[snake - 1].xcor()
        new_y = snake_list[snake - 1].ycor()
        snake_list[snake].goto(new_x, new_y)

    snake_list[0].forward(20)

screen.exitonclick()