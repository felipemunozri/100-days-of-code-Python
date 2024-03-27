import turtle
import random
from snake import BODY_SIZE
FOOD_ICONS = [
    'gfx/apple.gif',
    'gfx/banana.gif',
    'gfx/blueberry.gif',
    'gfx/candy.gif',
    'gfx/cherry.gif',
    'gfx/chocolate.gif',
    'gfx/cupcake.gif',
    'gfx/grape.gif',
    'gfx/kiwi.gif',
    'gfx/orange.gif',
    'gfx/pear.gif',
    'gfx/pie.gif',
    'gfx/strawberry.gif',
    'gfx/watermelon.gif'
]
for icon in FOOD_ICONS:
    turtle.addshape(icon)


class SnakeFood(turtle.Turtle):

    def __init__(self, snake_body: list):
        super().__init__()
        self.shape(random.choice(FOOD_ICONS))
        self.penup()
        self.shapesize()
        self.speed("fastest")
        self.refresh(snake_body)

    def refresh(self, snake_body: list):
        while True:
            x = random.randint(-14, 14) * BODY_SIZE
            y = random.randint(-14, 14) * BODY_SIZE

            # Avoid putting food at the position of snake's body
            is_conflict = False
            for fragment in snake_body:
                if fragment.distance(x, y) < 10:
                    is_conflict = True
                    break

            if not is_conflict:
                self.shape(random.choice(FOOD_ICONS))
                self.goto(x, y)
                break
