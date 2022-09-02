from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.pencolor("white")
        self.update()

    def increase_score(self):
        self.clear()
        self.score_count += 1
        self.update()

    def update(self):
        self.write(f"Score: {self.score_count}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


