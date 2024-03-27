from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake body of length STARTING_POSITIONS."""
        for position in STARTING_POSITIONS:
            if position == STARTING_POSITIONS[0]:
                self.add_head(position)
            else:
                self.add_segment(position)

    def add_head(self, position):
        """Creates the head of the snake. Appends it to segments list."""
        new_segment = Turtle("square")
        # new_segment.shapesize(0.9, 0.9)
        new_segment.color(105, 93, 2)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def add_segment(self, position):
        """Creates a new segment for the snake body. Appends it to segments list."""
        new_segment = Turtle("square")
        # new_segment.shapesize(0.9, 0.9)
        new_segment.color(105, 93, 2)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """This method is triggered when snake eats some food. Extends the snake body with a new segment. Calls the
        self.add_segment() class method."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Deals with the snake body movement behaviour on the screen. Each segment on self.segments list starting
        from the last one will move to the next segment current position. After that the first segment moves forward
        by a MOVE_DISTANCE distance on the screen."""
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        """Sets the heading of the snakes first segment (head) to go 'north' (90º degrees)."""
        # As a game constraint we cannot make the snake instantly turn in the opposite direction of its current heading
        # (aka. going 'south' or 'down') or 'run on itself'
        # if self.head.heading() != DOWN:
        #     self.head.setheading(UP)
        if self.head.towards(self.segments[1]) != UP:
            self.head.setheading(UP)

    def go_down(self):
        """Sets the heading of the snakes first segment (head) to go 'south' (270º degrees)."""
        # if self.head.heading() != UP:
        #     self.head.setheading(DOWN)
        if self.head.towards(self.segments[1]) != DOWN:
            self.head.setheading(DOWN)

    def go_left(self):
        """Sets the heading of the snakes first segment (head) to go 'left' (180º degrees)."""
        # if self.head.heading() != RIGHT:
        #     self.head.setheading(LEFT)
        if self.head.towards(self.segments[1]) != LEFT:
            self.head.setheading(LEFT)

    def go_right(self):
        """Sets the heading of the snakes first segment (head) to go 'right' (0º degrees)."""
        # if self.head.heading() != LEFT:
        #     self.head.setheading(RIGHT)
        if self.head.towards(self.segments[1]) != RIGHT:
            self.head.setheading(RIGHT)
