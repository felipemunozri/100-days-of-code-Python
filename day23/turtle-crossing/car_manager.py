import random
from turtle import Turtle

COLORS = ["Crimson", "Orange", "Yellow", "Green", "SlateBlue", "Indigo", "Violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.moving_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates a car and appends it to CarManager class self.car_list list."""
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            # x = 300
            x = random.randrange(300, 320, 5)
            y = random.randrange(-250, 250, 20)
            car.goto(x, y)
            self.car_list.append(car)

    def move_car(self):
        """Moves every car on the screen from right to left. Moves every car in CarManager class self.car_list list."""
        [car.goto(car.xcor() - self.moving_distance, car.ycor()) for car in self.car_list]

    def dispose_car(self):
        """After a car gets off the screen hides it from the screen and removes it from CarManager class self.car_list
        list."""
        [(car.hideturtle(), self.car_list.remove(car)) for car in self.car_list if car.xcor() < -320]

    # def increase_movement(self):
    #     """When called increases the distance cars move on the screen by MOVE_INCREMENT amount."""
    #     self.moving_distance += MOVE_INCREMENT
