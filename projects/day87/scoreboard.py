from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(150, 375)
        self.write(f"Score: {self.score} // Lives: {self.lives}", align="center", font=("Courier", 15, "normal"))

    def add_points(self, points):
        self.score += points
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self, won):
        self.goto(0, 0)
        if won:
            self.write("YOU WIN!", align="center", font=("Courier", 30, "bold"))
        else:
            self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))