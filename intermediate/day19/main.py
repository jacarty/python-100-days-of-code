from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turle will win the race? Enter a colour: ")
print(user_bet)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
height = -125

for turtle in range(0, 6):
    colour = colours[turtle]
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour)
    new_turtle.penup() 
    new_turtle.goto(x=-200, y=height)
    turtle_list.append(new_turtle)
    height += 50


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("You win")
            else:
                print(f"You've lost. The winning turtle was {winning_colour}.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick() 
