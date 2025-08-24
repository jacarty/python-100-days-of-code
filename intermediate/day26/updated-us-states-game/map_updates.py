from turtle import Turtle

class MapUpdates:

    def __init__(self):
        pass

    def map_label(self, anwser_state, x_coor, y_coor):
        new_label = Turtle()
        new_label.hideturtle()
        new_label.penup()
        new_label.color("black")
        new_label.goto(x_coor, y_coor)
        new_label.write(anwser_state)
