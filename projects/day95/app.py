"""
Space Invaders - Classic Arcade Game
Using Python Turtle

Controls:
- Left Arrow: Move left
- Right Arrow: Move right
- Space: Shoot
"""

import turtle
import time

# Game setup
screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Game variables
score = 0
game_over = False
alien_speed = 0.5
alien_move_down = 20

# Player class
class Player:
    def __init__(self):
        self.sprite = turtle.Turtle()
        self.sprite.shape("triangle")
        self.sprite.color("lime")
        self.sprite.setheading(90)
        self.sprite.penup()
        self.sprite.goto(0, -250)
        self.speed = 20
        
    def move_left(self):
        x = self.sprite.xcor()
        if x > -360:
            self.sprite.setx(x - self.speed)
    
    def move_right(self):
        x = self.sprite.xcor()
        if x < 360:
            self.sprite.setx(x + self.speed)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.sprite = turtle.Turtle()
        self.sprite.shape("square")
        self.sprite.color("yellow")
        self.sprite.shapesize(stretch_wid=0.5, stretch_len=0.2)
        self.sprite.penup()
        self.sprite.goto(x, y)
        self.sprite.setheading(90)
        self.speed = 15
        self.active = True
        
    def move(self):
        if self.active:
            y = self.sprite.ycor()
            self.sprite.sety(y + self.speed)
            if y > 300:
                self.active = False
                self.sprite.hideturtle()

# Alien class
class Alien:
    def __init__(self, x, y):
        self.sprite = turtle.Turtle()
        self.sprite.shape("square")
        self.sprite.color("red")
        self.sprite.shapesize(stretch_wid=1, stretch_len=1.5)
        self.sprite.penup()
        self.sprite.goto(x, y)
        self.alive = True
        
    def move(self, dx, dy):
        if self.alive:
            x = self.sprite.xcor()
            y = self.sprite.ycor()
            self.sprite.goto(x + dx, y + dy)

# Barrier block class
class Barrier:
    def __init__(self, x, y):
        self.sprite = turtle.Turtle()
        self.sprite.shape("square")
        self.sprite.color("cyan")
        self.sprite.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.sprite.penup()
        self.sprite.goto(x, y)
        self.health = 3
        self.alive = True
        
    def hit(self):
        self.health -= 1
        if self.health == 2:
            self.sprite.color("blue")
        elif self.health == 1:
            self.sprite.color("darkblue")
        elif self.health <= 0:
            self.alive = False
            self.sprite.hideturtle()

# Score display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "bold"))

# Game over display
game_over_display = turtle.Turtle()
game_over_display.color("red")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)

# Create player
player = Player()

# Create aliens (5 rows x 11 columns)
aliens = []
for row in range(5):
    for col in range(11):
        x = -250 + col * 50
        y = 100 + row * 40  # Start lower to avoid covering score
        alien = Alien(x, y)
        aliens.append(alien)

# Create barriers (4 barriers with multiple blocks each)
barriers = []
barrier_positions = [-250, -100, 100, 250]
for bx in barrier_positions:
    for row in range(3):
        for col in range(5):
            x = bx + col * 15 - 30
            y = -150 + row * 15
            barrier = Barrier(x, y)
            barriers.append(barrier)

# Bullets list
bullets = []

# Alien movement variables
alien_direction = 1  # 1 for right, -1 for left
move_down = False

# Keyboard bindings
def shoot():
    if not game_over:
        bullet = Bullet(player.sprite.xcor(), player.sprite.ycor() + 10)
        bullets.append(bullet)

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(shoot, "space")

# Collision detection
def is_collision(sprite1, sprite2):
    distance = sprite1.distance(sprite2)
    return distance < 20

# Update score
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "bold"))

# Game loop
last_alien_move = time.time()
alien_move_interval = 1.0  # Move aliens every 1 second

while True:
    screen.update()
    time.sleep(0.02)
    
    if game_over:
        continue
    
    # Move bullets
    for bullet in bullets[:]:
        if bullet.active:
            bullet.move()
        else:
            bullets.remove(bullet)
    
    # Move aliens
    current_time = time.time()
    if current_time - last_alien_move > alien_move_interval:
        last_alien_move = current_time
        
        # Check if aliens need to move down
        move_down = False
        for alien in aliens:
            if alien.alive:
                x = alien.sprite.xcor()
                if (alien_direction == 1 and x > 350) or (alien_direction == -1 and x < -350):
                    move_down = True
                    break
        
        if move_down:
            alien_direction *= -1
            for alien in aliens:
                alien.move(0, -alien_move_down)
        else:
            for alien in aliens:
                alien.move(alien_direction * 30, 0)
        
        # Speed up aliens as more are destroyed
        alive_count = sum(1 for alien in aliens if alien.alive)
        alien_move_interval = max(0.2, 1.0 - (55 - alive_count) * 0.015)
    
    # Check bullet-alien collisions
    for bullet in bullets[:]:
        if bullet.active:
            for alien in aliens:
                if alien.alive and is_collision(bullet.sprite, alien.sprite):
                    alien.alive = False
                    alien.sprite.hideturtle()
                    bullet.active = False
                    bullet.sprite.hideturtle()
                    score += 10
                    update_score()
                    break
    
    # Check bullet-barrier collisions
    for bullet in bullets[:]:
        if bullet.active:
            for barrier in barriers:
                if barrier.alive and is_collision(bullet.sprite, barrier.sprite):
                    barrier.hit()
                    bullet.active = False
                    bullet.sprite.hideturtle()
                    break
    
    # Check alien-player collisions
    for alien in aliens:
        if alien.alive:
            # Check if alien reached player
            if alien.sprite.ycor() < -230:
                game_over = True
                game_over_display.write("GAME OVER!", align="center", font=("Courier", 48, "bold"))
                break
            
            # Check direct collision with player
            if is_collision(alien.sprite, player.sprite):
                game_over = True
                game_over_display.write("GAME OVER!", align="center", font=("Courier", 48, "bold"))
                break
    
    # Check if all aliens are destroyed
    if not game_over and all(not alien.alive for alien in aliens):
        game_over = True
        game_over_display.color("lime")
        game_over_display.write("YOU WIN!", align="center", font=("Courier", 48, "bold"))

screen.mainloop()