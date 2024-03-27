import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

# # Draw a square
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)

# # Draw a dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# # Draw from a triangle to a decagon changing to a random color with each figure
# def change_color():
#     R = random.random()
#     B = random.random()
#     G = random.random()
#
#     timmy.color(R, G, B)
#
#
# for i in range(3, 11):
#     change_color()
#     angle = 360 / i
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(angle)

# # Official answer to draw from triangle to decagon changing colors. Same as above
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3, 10):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side_n)
#

# # Random walk with random colors
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def random_move():
#     timmy.pensize(10)
#     timmy.speed(10)
#     timmy.color(random.choice(colours))
#     direction = random.choice(['forward', 'back', 'left', 'right'])
#     if direction == 'forward':
#         timmy.forward(20)
#     elif direction == 'back':
#         timmy.backward(20)
#     elif direction == 'left':
#         # timmy.left(random.random() * 360)
#         timmy.left(90)
#     else:
#         # timmy.right(random.random() * 360)
#         timmy.right(90)
#
# for _ in range(500):
#     random_move()

# # Answer to random walk, same as code above
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# we modify the colormode() directly into the turtle module to make it accept int values between 0 and 255
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     # we return a tuple with the three values
#     rand_color = (r, g, b)
#     return rand_color
#
#
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fastest")
#
# for _ in range(200):
#     # timmy.color(random.choice(colours))
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# # Draw a spirograph
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # we return a tuple with the three values
    color = (r, g, b)
    return color


timmy.speed("fastest")

# for i in range(72):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.left(5)

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(7)

screen = Screen()
screen.exitonclick()
