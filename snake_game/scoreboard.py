from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_count = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.pencolor("white")
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score_count} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score_count = 0
        self.update()

    def increase_score(self):
        self.score_count += 1
        self.update()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


