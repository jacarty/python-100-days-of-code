from turtle import Turtle, Screen
import time
import random
from snake import Snake

# Define screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # disable animation

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_playing = True

while game_is_playing:

    screen.update() # update screen to account for disabled animation
    time.sleep(0.1) # sleep in seconds

    snake.move()

screen.exitonclick()