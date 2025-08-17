from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Define screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_start_position = (350, 0)
left_start_position = (-350, 0)

right_paddle = Paddle(right_start_position)
left_paddle = Paddle(left_start_position)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "a")
screen.onkey(left_paddle.down, "z")

game_is_playing = True
number_of_games = 5

while number_of_games > 0:

    screen.update() # update screen to account for disabled animation
    time.sleep(ball.move_speed) # sleep in seconds
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with right paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50:
        ball.hit()
    
    # detect collision with left paddle
    if ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.hit()

    # left player scores
    if ball.xcor() > 360:
        number_of_games -= 1
        ball.reset_position()
        scoreboard.left_point()

    # right player scores
    if ball.xcor() < -360:
        number_of_games -= 1
        ball.reset_position()
        scoreboard.right_point()

scoreboard.winner()

screen.exitonclick()