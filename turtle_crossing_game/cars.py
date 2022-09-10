from turtle import Turtle
import random
COLORS = ["red", "blue", "yellow", "orange", "purple", "green"]
X_COR = 310
Y_COR = [0, 20, 40, 80, 160, 200, 240, -20, -40, -80, -160, -200, -240]


class Cars(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.goto(x_pos, y_pos)

    def start_position(self):
        self.goto(X_COR, random.choice(Y_COR))

    def move(self):
        self.forward(5)





    #     self.x_position = [-20, -40, -80, -160, -200, -240, 20, 40, 80, 160, 200, 240]
    #     self.y_position = [0, 20, 40, 80, 160, 200, 240, -20, -40, -80, -160, -200, -240]
    #     self.cars = []
    #     self.rand_position()
    #
    # def rand_position(self):
    #     for _ in range(30):
    #         new_car = shape("square")
    #         new_car.shapesize(stretch_wid=1, stretch_len=2)
    #         new_car.color(random.choice(COLORS))
    #         new_car.penup()
    #         new_car.setheading(180)
    #         new_x = random.choice(self.x_position)
    #         new_y = random.choice(self.y_position)
    #         new_car.goto(new_x, new_y)
    #         self.cars.append(new_car)
    #
    # def start_position(self):
    #     for car in self.cars:
    #         # if car.xcor() < -290:
    #         car.goto(X_COR, Y_COR)
    #
    # def move(self):
    #     for car in self.cars:
    #         car.forward(1)
