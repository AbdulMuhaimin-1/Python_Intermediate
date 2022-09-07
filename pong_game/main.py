from turtle import Screen
from table import Table
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=400)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

table = Table()
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.start_move()

    # Detect collision with wall.
    if ball.ycor() > 180 or ball.ycor() < -180:
        ball.bounce_y()

    # Detect collision with paddle.
    if ball.distance(r_paddle) < 30 or ball.distance(l_paddle) < 30:
        ball.bounce_x()

    # Detect collision with right miss.
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect collision with left miss.
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
