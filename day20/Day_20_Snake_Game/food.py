from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("apple.gif")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 220)
        self.goto(random_x, random_y)