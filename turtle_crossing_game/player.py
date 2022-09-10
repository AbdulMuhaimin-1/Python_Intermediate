from turtle import Turtle
from scoreboard import Scoreboard

scoreboard = Scoreboard()
BEGIN_POSITION = (0, -280)
DISTANCE = 10
END_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.time_speed = 0.1
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.start_line()
        scoreboard.update()

    def finish_line(self):
        if self.ycor() > END_Y:
            self.start_line()
            self.time_speed *= 0.1
            scoreboard.level_up()

    def start_line(self):
        self.goto(BEGIN_POSITION)

    def up(self):
        self.forward(DISTANCE)
