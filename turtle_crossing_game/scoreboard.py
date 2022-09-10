from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()

    def update(self):
        self.clear()
        self.goto(-270, 270)
        self.write(f"Level: {self.level}", align='left', font=("courier", 12, "bold"))

    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))
