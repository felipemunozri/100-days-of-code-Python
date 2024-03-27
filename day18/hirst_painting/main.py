# import colorgram

# # Extract colors from an image using cologram module
# extraction = colorgram.extract("mm_spot_painting.jpg", 15)
# colors = []
# print(extraction)
# # for item in extraction:
# #     colors.append(item.rgb[slice(3)])
# for c in extraction:
#     colors.append(c.rgb[:3])

# # Answer for extract colors from an image, same as code above
# rgb_colors = []
# colors = colorgram.extract('mm_spot_painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# My code
import random
import turtle as turtle_module

# modify native turtle module colormode to accept integers tuples as rgb colors
turtle_module.colormode(255)

# CHALLENGE CONSTRAINTS:
# Draw a 10 x 10 square of random colored dots
# Each dot (circle) should be 20 in size, and they should be spaced by 50 passes

turtle = turtle_module.Turtle()
turtle.hideturtle()
turtle.speed('fastest')
turtle.penup()


def draw_spots_painting(row, col, colors):
    """Draws a row x col size spots-painting à la Damien Hirst. Takes two integers numbers and a list of tuples of
    rgb values (0-255) as inputs."""
    start_position = [float(row - row * 25), float(col - col * 25)]
    turtle.setposition(tuple(start_position))

    for i in range(col):
        for j in range(row):
            # turtle.pendown()  # not needed
            turtle.dot(20, random.choice(colors))  # draw a dot of size 20 and a random color from colors list
            turtle.penup()
            turtle.forward(50)
        # after completing drawing a line of dots we reset the position of the turtle to the starting position in the
        # x-axis but 50 passes upwards in the y-axis
        start_position[1] += 50
        turtle.setposition(tuple(start_position))


# list of colors extracted from mm_spot_painting.jpg image. see commented code above
color_list = [(234, 241, 247), (141, 163, 182), (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62),
              (220, 156, 97), (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31), (204, 67, 26),
              (226, 170, 199), (242, 80, 27), (16, 172, 189), (34, 176, 93), (2, 114, 63), (247, 214, 2),
              (114, 188, 142), (181, 95, 111), (188, 182, 211), (40, 39, 46), (157, 207, 217), (229, 173, 162),
              (162, 208, 181), (118, 117, 163)]

draw_spots_painting(10, 10, color_list)

screen = turtle_module.Screen()
screen.exitonclick()

# # Other solution
# from turtle import Turtle, Screen, colormode
# import random
#
# color_list = [(230, 238, 246), (235, 245, 240), (200, 157, 115), (43, 110, 146), (134, 172, 193), (226, 208, 113),
#               (134, 84, 67), (148, 65, 85), (198, 140, 153), (193, 83, 102), (182, 159, 51), (150, 178, 164),
#               (191, 98, 83), (68, 114, 94), (227, 170, 182), (36, 51, 68), (225, 177, 168), (45, 157, 186),
#               (60, 47, 41), (155, 205, 218), (49, 56, 94), (22, 90, 76), (129, 38, 59), (58, 44, 52), (33, 60, 53),
#               (97, 146, 125), (173, 203, 189), (178, 188, 212)]
#
# tim = Turtle()
# colormode(255)
# tim.speed(0)
# tim.penup()
# tim.hideturtle()
#
# for y in range(-250, 250, 50):
#     for x in range(-250, 250, 50):
#         tim.goto(x, y)
#         tim.dot(20, random.choice(color_list))
#
# screen = Screen()
# screen.exitonclick()
