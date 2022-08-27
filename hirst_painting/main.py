import turtle as t
import random


tim = t.Turtle()
sc = t.Screen()
color_list = [(140, 176, 207), (25, 32, 48), (26, 107, 159), (209, 161, 111), (144, 29, 63), (230, 212, 93),
              (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116),
              (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119),
              (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166),
              (153, 205, 220), (184, 185, 210)]


def draw_dots():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


coordinates = [-300, -250]
x_axis = coordinates[0]
y_axis = coordinates[1]
t.colormode(255)
tim.hideturtle()
tim.speed(0)
tim.penup()
tim.setposition(x_axis, y_axis)
for _ in range(10):
    y_axis += 50
    draw_dots()
    tim.setposition(x_axis, y_axis)

t.done()    # hold the screen
# sc.exitonclick()
