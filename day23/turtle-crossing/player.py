from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#c4e581")
        self.penup()
        self.setheading(90)
        self.reset_position()
        self.move_distance = MOVE_DISTANCE

    def go_up(self):
        """Moves the player turtle up on the screen."""
        new_y = self.ycor() + self.move_distance
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the player turtle down on the screen."""
        if self.ycor() > -280:
            new_y = self.ycor() - self.move_distance
            self.goto(self.xcor(), new_y)

    def go_left(self):
        """Moves the player turtle left on the screen."""
        if self.xcor() > -290:
            new_x = self.xcor() - self.move_distance
            self.goto(new_x, self.ycor())

    def go_right(self):
        """Moves the player turtle right on the screen."""
        if self.xcor() < 280:
            new_x = self.xcor() + self.move_distance
            self.goto(new_x, self.ycor())

    def at_upper_border(self):
        """Evaluates if player turtle is at the upper border of the screen."""
        if self.ycor() > FINISH_LINE_Y:
            return True

    def reset_position(self):
        """Reset the player turtle to its starting position at STARTING_POSITION."""
        self.goto(STARTING_POSITION)
