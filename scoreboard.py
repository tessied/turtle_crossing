from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.level = 0
        self.goto(-270, 260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

