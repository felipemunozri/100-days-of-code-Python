from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 25, "italic")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Linen")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Prints the scoreboard on screen."""
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        """When called increases Scoreboard class self.level variable."""
        self.level += 1
        self.update_scoreboard()
