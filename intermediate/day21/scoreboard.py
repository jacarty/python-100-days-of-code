from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")

class Scoreboard(Turtle):
        
        def __init__(self):
            super().__init__()

            self.score = 0
            self.color("orange")
            self.hideturtle()
            self.penup()
            self.goto(0, 280)
            self.speed("fastest")
            self.update_scoreboard()
            
        def update_scoreboard(self):
            self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

        def increase_score(self):
              self.score += 1
              self.clear()
              self.update_scoreboard()

        def game_over(self):
              self.goto(0, 0)
              self.write(f"Game Over", align=ALIGNMENT, font=FONT)