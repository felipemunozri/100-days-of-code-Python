import pandas
from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ('Arial', 8, 'normal')

# Initialize screen
screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

# Writer turtle instance
writer = Turtle()
writer.hideturtle()
writer.penup()

# Read data from csv file
data = pandas.read_csv("50_states.csv")
state_names = list(data["state"])

# Game start
score = 0
while score < 50:
    while True:
        answer = screen.textinput(f"{score}/50 States Correct", "What's another state's name?")
        if answer is None or answer == "Exit":
            score = 100  # just to get out of the outer loop
            df = pandas.DataFrame(state_names)
            df.columns = ["state"]
            df.to_csv("states_to_study.csv")
            break
        elif answer.title() in state_names:
            answer = answer.title()
            score += 1
            state_names.remove(answer)
            item = data[data["state"] == answer]
            writer.goto(int(item["x"]), int(item["y"]))
            writer.write(answer, align=ALIGNMENT, font=FONT)
            print(state_names)  # debug only
            break
        else:
            continue
# Game end
if score != 50:
    screen.textinput("Game Over", "A list with states was generated for you to study.")
else:
    screen.textinput(f"{score}/50 States Correct👍", "Congratulations! You guessed all the states.")

screen.exitonclick()
