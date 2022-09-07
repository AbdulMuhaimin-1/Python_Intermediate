from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(50, 130)
        self.write(self.r_score, align="center", font=("courier", 30, "bold"))
        self.goto(-50, 130)
        self.write(self.l_score, align="center", font=("courier", 30, "bold"))

    def r_point(self):
        self.r_score += 1
        self.score_update()

    def l_point(self):
        self.l_score += 1
        self.score_update()

