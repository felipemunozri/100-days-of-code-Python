from turtle import Turtle
import random

# TODO: 1. Add some colors to the food and have different effects like speeding up/down the snake, add or subtract
#  segments from the snake's body (this food elements could begin to appear after a certain score level), etc.
color = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
         "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.tilt(45)
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # self.color("Red")
        self.color(105, 93, 2)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Generates a random position on the screen for a food object."""
        # rand_x = random.randrange(-280, 300, 20)  # the stop number is exclusive, so we must put stop at 300 to get 280
        # rand_y = random.randrange(-280, 280, 20)  # we use 280 on top limit to prevent food from appearing over score
        rand_x = random.randrange(-260, 260, 20)  # the stop number is exclusive, so we must put stop at 300 to get 280
        rand_y = random.randrange(-260, 260, 20)  # we use 280 on top limit to prevent food from appearing over score
        self.goto(rand_x, rand_y)
