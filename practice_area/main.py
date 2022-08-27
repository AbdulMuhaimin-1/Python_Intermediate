import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)

color_list = [(140, 176, 207), (25, 32, 48), (26, 107, 159), (209, 161, 111), (144, 29, 63), (230, 212, 93),
              (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116),
              (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119),
              (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166),
              (153, 205, 220), (184, 185, 210)]


def start_spirograph(gap):
    for _ in range(int(360 / gap)):
        tim.color(random.choice(color_list))
        tim.circle(100)
        tim.left(gap)


start_spirograph(5)
t.done()
