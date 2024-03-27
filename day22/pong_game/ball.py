from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.penup()
        # self.speed("fastest")

    def move(self, direction):
        """Moves ball 'up' or 'down' according to direction."""
        if direction == "up":
            self.sety(self.ycor() + 1)
        elif direction == "down":
            self.sety(self.ycor() - 1)
