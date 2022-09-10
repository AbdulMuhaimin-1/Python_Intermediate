from turtle import Turtle


class Attempts:

    def __init__(self):
        self.number_of_life = []
        self.new_x = 260
        self.create_life()

    def life_deduct(self):
        self.number_of_life[-1].hideturtle()
        del self.number_of_life[-1]

    def create_life(self):
        for _ in range(3):
            new_life = Turtle("turtle")
            new_life.shapesize(0.8, 0.8)
            new_life.penup()
            new_life.color("red")
            new_life.setheading(90)
            new_life.goto(x=self.new_x, y=270)
            self.new_x -= 20
            self.number_of_life.append(new_life)
