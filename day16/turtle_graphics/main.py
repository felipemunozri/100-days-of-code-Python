# import turtle
# timmy = turtle.Turtle()

# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# # timmy.color("DarkSeaGreen")
# timmy.color("DarkOliveGreen4")
# timmy.forward(100)

# when we print an object what we see is its location in memory at that particular moment like this
# <turtle.Turtle object at 0x0000021E5158F7D0>
# print(timmy)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
