from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# NOTE:
#
# turtle.xcor(), turtle.ycor(), turtle.position(), turtle.distance().
# These functions sometimes return relative values (decimals) instead of absolute values (integers)
# which causes errors if we compare two objects for the exact position.

def food_under_snake():
    """Prevents food from appearing under snake body (wip)."""
    while True:
        food.refresh()
        is_conflict = False
        for seg in snake.segments:
            if seg.distance(food.xcor(), food.ycor()) < 10:
                is_conflict = True
                break
        if not is_conflict:
            food.refresh()
            break


def game_over():
    """Validates if user wants to keep playing after losing or close the game."""
    global keep_playing
    global run_game
    while True:
        answer = screen.textinput("GAME OVER", "You lose, want to play again? Type 'Y' or 'N': ")
        # End game
        if answer is None or answer.lower() == "n":
            run_game = False
            keep_playing = False
            break
        # Keep playing
        elif answer.lower() == "y":
            run_game = False
            scoreboard.reset()
            screen.clearscreen()
            break
        # Ask again
        else:
            continue


keep_playing = True

while keep_playing:
    screen = Screen()
    screen.setup(width=600, height=600, startx=None, starty=None)
    screen.title("Snake Game 🐍")
    screen.colormode(255)
    screen.bgcolor(176, 215, 3)
    screen.tracer(0)  # turns off screen animation

    border = Turtle()
    border.shape("square")
    border.shapesize(27, 27, 3)
    border.fillcolor(176, 215, 3)
    border.pencolor(105, 93, 2)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkeypress(fun=snake.go_up, key="Up")
    screen.onkeypress(fun=snake.go_down, key="Down")
    screen.onkeypress(fun=snake.go_left, key="Left")
    screen.onkeypress(fun=snake.go_right, key="Right")

    speed = 0.1
    paused = False
    run_game = True

    while run_game:
        screen.update()  # refreshes the screen after each iteration
        time.sleep(speed)  # delays the screen refresh by speed amount (seconds). Acts as apparent snake speed on screen
        snake.move()

        # Detect collision of snake head with food and refreshes food position
        if snake.head.distance(food) < 15:
            food_under_snake()  # tries to refresh food not under snake
            # After eating food extend snake body, update score and increase snake speed
            snake.extend()
            scoreboard.increase_score()
            speed -= 0.001

        # Detect collision between snake head and tail (must check head against every other segment in snake body)
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_over()

        # Detect collision with screen borders (on testing a value of 281 works best)
        if abs(snake.head.xcor()) > 271 or abs(snake.head.ycor()) > 271:
            game_over()

# screen.exitonclick()
