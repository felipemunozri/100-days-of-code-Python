from turtle import Turtle


class Racquet(Turtle):

    def __init__(self, color, position):
        super().__init__()
        self.score = 0
        self.shape("square")
        self.shapesize(2, 0.5)
        self.penup()
        # self.color("white")
        self.color(color)
        self.speed("fastest")
        self.goto(position)

    def up(self):
        """Moves racquet up on the screen."""
        if self.ycor() < 270:
            self.sety(self.ycor() + 50)

    def down(self):
        """Moves racquet down on the screen."""
        if self.ycor() > -270:
            self.sety(self.ycor() - 50)
