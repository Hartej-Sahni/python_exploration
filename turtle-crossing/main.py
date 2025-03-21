import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

def collision():
    for car in car_manager.cars:
        if player.distance(car) < 20:
            return True
    return False

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    if player.hit_top():
        time.sleep(0.5)
        player.reset()
        scoreboard.increment_level()
        car_manager.level_up()
    if collision():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()