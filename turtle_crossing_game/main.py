import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import random


x_position = [-20, -40, -80, -160, -200, -240, 20, 40, 80, 160, 200, 240]
y_position = [0, 20, 40, 80, 160, 200, 240, -20, -40, -80, -160, -200, -240]


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()

car = []
for _ in range(20):
    cars = Cars(random.choice(x_position), random.choice(y_position))
    car.append(cars)

screen.listen()
screen.onkey(fun=player.up, key="Up")

is_game_on = True
while is_game_on:
    time.sleep(player.time_speed)
    screen.update()
    player.finish_line()

    for new_car in car:
        new_car.move()
        if new_car.xcor() < -310:
            new_car.start_position()

        if new_car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
