from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

# Player Object
player = Player()

# Screen Setups
screen = Screen()
screen.setup(width=1000, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(key="w", fun=player.move)

# Car Object
carmanager = CarManager()

# Scoreboard Object
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_car()

    # Finish line checker and scorer
    if player.distance_meter():
        scoreboard.level_up()
        carmanager.level_up()

    # Collison detect
    for car in carmanager.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
