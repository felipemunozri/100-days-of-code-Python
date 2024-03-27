# My code
from turtle import Screen, Turtle
import random
from tkinter import messagebox


def initialize_screen():
    """Initializes the game canvas with a width of 50% of the total screen size and a height of 60% of the total
    screen size. Modifies the screen.colormode to use rgb values, adds a background color and a screen title. Returns
    the screen object."""
    screen = Screen()
    # screen.setup(width=500, height=400)
    screen.setup(width=0.5, height=0.6, startx=None, starty=None)
    screen.colormode(255)
    screen.bgcolor(135, 220, 246)
    screen.title("Awesome Turtle Race 🏁")
    return screen


def draw_finish_line(a_turtle, x, y, length, first_color, second_color):
    """Takes a turtle object, two int numbers as starting coordinates, a length number (int), and two colors (strings).
    Draws a vertical line of length number of squares in a chessboard pattern alternating between first and second
    color. Each square is 20x20 px in size, the default size of a turtle object."""
    a_turtle.shape("square")
    a_turtle.hideturtle()
    a_turtle.speed("fastest")
    a_turtle.penup()
    a_turtle.goto(x, y)
    for i in range(length):
        if i % 2 == 0:
            a_turtle.color(first_color)
        else:
            a_turtle.color(second_color)
        a_turtle.stamp()  # stamp() prints the current shape of the turtle in the current location
        y += 20  # 20px is the default size of a turtle obj, so we offset the y coordinate by 20 for the next iteration
        a_turtle.sety(y)


def create_race_turtles(x_start, y_start, gap, colors_list):
    """Takes two int numbers as starting coordinates, another number to use as a gap, and a list of colors (lowercase
    strings). Creates a turtle object for each color in the list and positions them starting with the given coordinates
    and separating them on the y-axis by gap. Returns a list of the created turtles."""
    turtles_list = []
    random.shuffle(colors_list)  # shuffles the list before creating the turtles just to give more randomness
    for color in colors_list:
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        y_start += gap
        new_turtle.goto(x_start, y_start)
        turtles_list.append(new_turtle)
    return turtles_list


# def play_again():
#     """Validates with user inputs ('Y', 'y', 'N', 'n', OK button or Cancel button) if the user wants to start a new game
#     or wishes to end the program. Returns a boolean value."""
#     answer = new_screen.textinput(title="Awesome Turtle Race.", prompt="Want to play again? Type 'Y' or 'N': ")
#     if answer is None or answer.lower() == "n":  # answer is None when the Cancel button is pressed
#         new_screen.clearscreen()
#         return False
#     elif answer.lower() == "y" or answer == "":  # answer is "" when the OK button is pressed without writing any text
#         new_screen.clearscreen()
#         return True
#     else:  # if random text was entered and the OK button was pressed we assume to run the game
#         new_screen.clearscreen()
#         return True


run_game = True

while run_game:
    new_screen = initialize_screen()
    turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    donatello = Turtle()

    draw_finish_line(donatello, 210, -180, 20, "Black", "White")
    draw_finish_line(donatello, 230, -180, 20, "White", "Black")

    turtles = create_race_turtles(-230, -172, 50, turtle_colors)

    is_race_on = False
    user_bet = ""

    while True:
        prompt_text = "Which turtle will win the race? Enter a color: "
        user_bet = new_screen.textinput(title="Make your bet:", prompt=prompt_text)
        if user_bet is None:  # Cancel button was pressed and game ends
            run_game = False
            break
        elif user_bet == "":  # OK button was pressed without text
            continue
        elif user_bet.lower() not in turtle_colors:  # entered text doesn't match with any turtle color
            continue
        else:
            user_bet = user_bet.lower()  # convert entered text to lower case
            break

    if user_bet:
        is_race_on = True
        donatello.goto(0, -10)
        donatello.color("Black")
        donatello.write("Go!", align="center", font=("Arial", 14, "bold"))

        while is_race_on:
            for turtle in turtles:
                if turtle.xcor() < 230:
                    rand_distance = random.randint(0, 10)
                    turtle.forward(rand_distance)
                else:
                    is_race_on = False
                    winning_color = turtle.pencolor()

                    result = f"The {winning_color} turtle is the winner!"
                    if winning_color == user_bet:
                        messagebox.showinfo("Race results.", "You've won! " + result)
                    else:
                        messagebox.showinfo("Race results.", "You've lost! " + result)
                    break  # after the condition is met we add a break statement for the for loop

        while True:
            answer = new_screen.textinput(title="Awesome Turtle Race.", prompt="Want another race? Type 'Y' or 'N': ")
            if answer is None or answer.lower() == "n":
                new_screen.clearscreen()  # clears screen before closing the game
                run_game = False
                break
            elif answer.lower() == "y":
                new_screen.clearscreen()
                break
            elif answer == "":
                continue
            else:
                continue
