from turtle import Turtle

ALIGNMENT = "left"
FONT = ('Courier', 15, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        # self.color("White")
        self.color(105, 93, 2)
        self.penup()
        self.goto(-270, 272)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Prints the self.score value on the screen."""
        self.clear()
        self.goto(250, 272)
        self.write("🐍", align=ALIGNMENT, font=FONT)
        self.goto(-270, 272)
        # self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.write(f"Score: {self.score} High_Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increments the self.score value. Triggered when snake eats some food."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
