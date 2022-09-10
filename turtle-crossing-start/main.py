import time
from turtle import Screen
from attempts import Attempts
from road_manager import RoadManager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)
#
attempts = Attempts()
road_manager = RoadManager()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
#
screen.listen()
screen.onkey(player.go_up, "Up")
#
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
#
    car_manager.create_car()
    car_manager.move_cars()

    if len(attempts.number_of_life) == 0:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            attempts.life_deduct()
            player.go_to_start()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
