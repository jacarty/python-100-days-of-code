from turtle import Turtle

FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1
        self.starting_cars = 12
        self.new_cars = (self.level)
        self.hideturtle()
        self.color("black")
        self.penup()        
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 280)
        self.write(f"Current Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.new_cars = self.level
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=GAME_OVER_FONT)        
