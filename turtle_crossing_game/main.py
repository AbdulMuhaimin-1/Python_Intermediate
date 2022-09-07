import time
from turtle import Screen
from player import Player
from cars import Cars

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
cars = Cars()

screen.listen()
screen.onkey(fun=player.up, key="Up")


is_game_on = True
while is_game_on:
    time.sleep(0.01)
    screen.update()
    cars.move()

    if player.ycor() > 280:
        player.cross()


screen.exitonclick()
