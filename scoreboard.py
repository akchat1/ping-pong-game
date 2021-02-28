from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.display()

    def score_right(self):
        self.r_score += 1
        self.display()

    def score_left(self):
        self.l_score += 1
        self.display()

    def display(self):
        self.clear()
        self.goto(-100, 200)
        self.write(align="center", arg=f"{self.l_score}", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(align="center", arg=f"{self.r_score}", font=("Courier", 80, "normal"))

    def game_end(self):
        if self.l_score == 10 or self.r_score == 10:
            return False
        else:
            return True
