from turtle import Turtle
POSITION = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.cross()

    def cross(self):
        self.goto(POSITION)

    def up(self):
        self.forward(20)
