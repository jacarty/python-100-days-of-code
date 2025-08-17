import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

danny = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(danny.move, "Up")

starting_cars = scoreboard.starting_cars
car_inventory = []
last_execution = time.time()
game_is_on = True

for i in range(0, starting_cars):
    x_start = random.randint(-200, 350)
    y_start = random.randint(-250, 250)
    car_inventory.append(CarManager(x_start, y_start))

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars_to_keep = []
    
    for car in car_inventory:
        car.move_car()

        # remove from list when off screen
        if car.xcor() >= -320:
            cars_to_keep.append(car)

        # check for collision
        if danny.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False
    
    car_inventory = cars_to_keep

    # add cars
    current_time = time.time()
    if current_time - last_execution >= 1:
        add_cars = random.randint(1, scoreboard.new_cars)
        for i in range(add_cars):
            y_start = random.randint(-250, 250)
            car_inventory.append(CarManager(280, y_start))
        last_execution = current_time

    # level up
    if danny.ycor() > 280:
        danny.level_up()
        scoreboard.level_up()

screen.exitonclick()
