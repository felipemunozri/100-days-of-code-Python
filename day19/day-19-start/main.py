from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


# CHALLENGE CONSTRAINTS:
# make and Etch-A-Sketch app to draw on screen using the keyboard
# use 'w' key to move forwards
# use 's' key to move backwards
# use 'a' key to move counter-clockwise
# use 'd' key to move clockwise
# use 'c' key to clear the screen and put cursor on the center

def move_forwards():
    tim.forward(10)


def turn_cont_clockwise():
    tim.left(10)


def turn_clockwise():
    tim.right(10)


def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()
    # tim.reset()


def pen_up():
    tim.penup()


def pen_down():
    tim.pendown()


screen.listen()
screen.onkeypress(fun=move_forwards, key="d")  # we use keyword arguments instead of positional arguments
screen.onkeypress(fun=move_forwards, key="a")
screen.onkey(fun=turn_cont_clockwise, key="w")
screen.onkey(fun=turn_clockwise, key="s")
screen.onkey(fun=clear_screen, key="c")
screen.onkey(fun=pen_up, key="f")
screen.onkey(fun=pen_down, key="e")

screen.exitonclick()
