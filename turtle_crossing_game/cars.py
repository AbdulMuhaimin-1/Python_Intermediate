from turtle import Turtle
import random
COLORS = ["red", "blue", "yellow", "orange", "purple"]
X_POSITI0N = 310
Y_POSITION = [0, 10, 20, 30, 40, 50, 60]


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        # self.goto(x=X_POSITI0N, y=Y_POSITION[0])
        # self.multiple_cars()
        self.setheading(180)

    def multiple_cars(self):
        for car in range(10, 101, 10):
            new_y = car
            self.goto(X_POSITI0N, new_y)

    def move(self):
        self.multiple_cars()
        self.forward(10)

