import pandas
from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ('Arial', 8, 'normal')

# Initialize screen
screen = Screen()
screen.setup(width=500, height=600, startx=None, starty=None)
screen.bgpic("chile_blank_regions.gif")
screen.title("Chile Regions Game")

# Writer turtle instance
writer = Turtle()
writer.hideturtle()
writer.penup()

# Read data from csv file
data = pandas.read_csv("chile_regions.csv")
region_names = list(data["region"])

# Game start
score = 0
while score < 16:
    while True:
        answer = screen.textinput(f"{score}/16 Regions Correct", "What's another region's name?")
        if answer is None:
            break
        elif answer.title() in region_names:
            break
        else:
            continue
    score += 1
    answer = answer.title()
    region_names.remove(answer)
    x = int(data[data["region"] == answer]["x"])
    y = int(data[data["region"] == answer]["y"])
    writer.goto(x, y)
    writer.write(answer, align=ALIGNMENT, font=FONT)
    # print(region_names)  # debug only

# Game end
    screen.textinput(f"{score}/16 Regions Correct👍", "Congratulations! You guessed all the regions.")
screen.exitonclick()
