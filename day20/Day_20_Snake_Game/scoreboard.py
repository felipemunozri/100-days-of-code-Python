from turtle import Turtle

ALIGNMENT = "center"
FONT = ("ubuntu", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_start(self):
        self.write(f"5 seconds to start", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"GAME OVER | Final Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()