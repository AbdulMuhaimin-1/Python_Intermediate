from turtle import Turtle


class RoadManager(Turtle):

    def __init__(self):
        super().__init__()
        self.y_position = -250
        self.penup()
        self.goto(-300, self.y_position)
        self.fillcolor("black")
        self.begin_fill()
        self.create_lanes()
        self.end_fill()

    def create_lanes(self):
        for _ in range(13):
            self.pendown()
            self.move_forward()
            self.setheading(90)
            self.forward(20)
            self.setheading(180)
            self.move_forward()
            self.setheading(270)
            self.forward(20)
            self.penup()
            self.y_position += 40
            self.goto(-300, self.y_position)
            self.setheading(0)

    def move_forward(self):
        self.forward(600)

