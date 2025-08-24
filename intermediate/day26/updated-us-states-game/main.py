# https://www.sporcle.com/games/g/states

import turtle
import pandas
from map_updates import MapUpdates

map_updater = MapUpdates()
screen = turtle.Screen()

screen.title("US States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data =  pandas.read_csv("./50_states.csv")

game_is_playing = True
score = 0
correct_states = []

while game_is_playing:

    answer_state = screen.textinput(title=f"{score}/50 States Correct]", prompt="What's another States name?").title()
    check_result = data[data.state == answer_state]

    # using list comprehension
    if answer_state == "Exit":
        missed_states = [state for state in data.state if state not in correct_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("./missed_states.csv")
        break

    elif not check_result.empty:
        x = (check_result.x.item())
        y = (check_result.y.item())
        score += 1
        correct_states.append(answer_state)

        new_label = turtle.Turtle()
        new_label.hideturtle()
        new_label.penup()
        new_label.color("black")
        new_label.goto(x, y)
        new_label.write(answer_state)


    




