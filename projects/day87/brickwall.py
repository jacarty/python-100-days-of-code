from bricks import Bricks

class BrickWall():

    def __init__(self):
        self.bricks = []
        self.rows = 8
        self.columns = 14
        self.colours = ["red", "orange", "green", "yellow"]

    def create_bricks(self):
        for row in range(self.rows):
            for col in range(self.columns):
                x = -280 + (col * 40)
                y = 350 - (row * 23)
                num = row // 2 
                colour = self.colours[num]
                
                brick = Bricks(x, y, colour)
                self.bricks.append(brick)

    def draw_all_bricks(self):
        for brick in self.bricks:
            brick.draw_brick()