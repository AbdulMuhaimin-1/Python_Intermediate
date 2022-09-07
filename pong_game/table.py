from turtle import Turtle


class Table(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, -190)
        self.color("white")
        self.hideturtle()
        self.setheading(90)
        self.pensize(5)
        self.set_table()

    def set_table(self):
        for _ in range(16):
            self.forward(10)
            self.penup()
            self.forward(15)
            self.pendown()
