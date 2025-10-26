from turtle import Turtle, Screen
from scoreboard import Scoreboard
from bricks import Bricks
from brickwall import BrickWall
from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

scoreboard = Scoreboard()

wall = BrickWall()
wall.create_bricks()
wall.draw_all_bricks()

ball = Ball()

paddle = Paddle((0, -350))
screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.bounce_x()

    if ball.ycor() > 370:
        ball.bounce_y()

    if ball.ycor() < -320 and ball.distance(paddle) < 50:
        ball.bounce_y()

    if ball.ycor() < -380:
        scoreboard.lose_life()
        if scoreboard.lives == 0:
            scoreboard.game_over(won=False)
            game_is_on = False
        else:
            ball.reset_position()

    for brick in wall.bricks:
        if ball.distance(brick) < 25:
            ball.bounce_y()
            wall.bricks.remove(brick)
            brick.clear()
            
            if brick.colour == "red":
                 scoreboard.add_points(7)
            elif brick.colour == "orange":
                 scoreboard.add_points(5)
            elif brick.colour == "green":
                 scoreboard.add_points(3)
            elif brick.colour == "yellow":
                 scoreboard.add_points(1)
            
            break

    if len(wall.bricks) == 0:
        # Player won!
        scoreboard.game_over(won=True)
        game_is_on = False

screen.exitonclick()