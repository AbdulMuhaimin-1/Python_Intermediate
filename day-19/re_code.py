import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=800, height=600)
user_bet = turtle.textinput(title="Make a bet!", prompt="Choose a turtle, Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_pos = [-250, -150, -50, 50, 150, 250]
all_turtles = []

for turtles in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtles])
    new_turtle.penup()
    new_turtle.goto(x=-380, y=turtle_pos[turtles])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winner = turtle.pencolor()
            # screen.reset()
            tim = Turtle(shape="turtle")
            tim.penup()
            if winner == user_bet:
                tim.write(f"You've won!, the {winner} turtle was the winner.", True, align="center",
                          font=("Elephant", 12, "normal"))
                tim.left(90)
            else:
                tim.write(f"You've lost!, the {winner} turtle was the winner.", True, align="center",
                          font=("Elephant", 12, "normal"))
                tim.left(90)
        rand_pos = random.randint(0, 10)
        turtle.forward(rand_pos)
screen.exitonclick()