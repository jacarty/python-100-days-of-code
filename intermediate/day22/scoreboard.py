from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # Create paddle
        self.hideturtle()
        self.color("orange")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 50, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def winner(self):
        self.goto(0, 0)
        if self.left_score > self.right_score:
            self.write("Left Player Wins!", align="center", font=("Courier", 40, "normal"))
        else: 
            self.write("Right Player Wins!", align="center", font=("Courier", 40, "normal"))