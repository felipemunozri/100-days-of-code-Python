from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 35, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 250)
        self.hideturtle()
        self.color("White")
        self.penup()
        self.update_scoreboard(None, None)

    def update_scoreboard(self, p1_score, p2_score):
        """Prints players score values on screen."""
        self.clear()
        self.write(f"{p1_score}       {p2_score}", align=ALIGNMENT, font=FONT)
