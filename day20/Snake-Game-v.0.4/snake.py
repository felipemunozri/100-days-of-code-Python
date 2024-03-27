# NOTE:
#
# turtle.xcor(), turtle.ycor(), turtle.position(), turtle.distance().
# These functions sometimes return relative values (decimals) instead of absolute values (integers)
# which causes errors if we compare two objects for the exact position.

from turtle import Turtle
BODY_SIZE = 20
STARTING_POS = [(20, 0), (0, 0), (-20, 0)]
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
BORDER = 290


class Snake:

    def __init__(self):
        self.body = []
        for position in STARTING_POS:
            self.add_segment(position)

        self.head = self.body[0]
        self.__prev_heading = self.head.heading()  # Block simultaneous movement causing conflict

    def add_segment(self, position: tuple):
        t = Turtle(shape='square')
        t.color('white')
        t.penup()
        t.goto(position)
        self.body.append(t)

    def up(self, is_paused=False):
        if self.__prev_heading != DOWN and not is_paused:
            self.head.setheading(UP)

    def down(self, is_paused=False):
        if self.__prev_heading != UP and not is_paused:
            self.head.setheading(DOWN)

    def left(self, is_paused=False):
        if self.__prev_heading != RIGHT and not is_paused:
            self.head.setheading(LEFT)

    def right(self, is_paused=False):
        if self.__prev_heading != LEFT and not is_paused:
            self.head.setheading(RIGHT)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].position())
            # self.body[i].setheading(self.body[i - 1].heading())

        self.head.forward(BODY_SIZE)
        self.__prev_heading = self.head.heading()

    def grow(self):
        self.add_segment(self.body[-1].position())

    def is_out_of_bound(self):
        return abs(self.head.xcor()) > BORDER or abs(self.head.ycor()) > BORDER

    def is_hit(self):
        for fragment in self.body[1:]:
            if self.head.distance(fragment) < 10:
                return True

        return False
