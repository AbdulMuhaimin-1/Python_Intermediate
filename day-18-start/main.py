from turtle import Screen
import turtle as t
import random


tim = t.Turtle()
screen = Screen()
t.colormode(255)
tim.pensize(2)
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(0)
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen.exitonclick()
