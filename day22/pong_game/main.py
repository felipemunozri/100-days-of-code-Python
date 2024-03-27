from turtle import Screen, Turtle
from scoreboard import Scoreboard
from player import Player
from ball import Ball
import random
import time

DIRECTION = ["up", "down"]  # keywords list to use later on ball.move() method
HEADING = [0, 180]  # possible headings for ball object (0 = 'right', 180 = 'left')
PLAYER_COLOR = ["Blue", "Red"]  # colors for players
P1_RAC_POS = (-280, 0)  # player1 initial racquet position on screen
P2_RAC_POS = (270, 0)  # player2 initial racquet position on screen
NUM_SETS = 10  # max numbers of sets before game over


def draw_net():
    """Draws the 'tennis court' net on screen."""
    net_segment = Turtle()
    net_segment.penup()
    net_segment.speed("fastest")
    net_segment.shape("square")
    net_segment.shapesize(0.5, 0.2)

    for i in range(-270, 280, 20):
        net_segment.goto(0, i)
        if i % 2 == 0:
            net_segment.color("white")
        else:
            net_segment.color("black")
        net_segment.stamp()


# Flag
play_again = True

while play_again:
    # Init screen canvas
    screen = Screen()
    screen.setup(width=600, height=600, startx=None, starty=None)
    screen.bgcolor("black")
    screen.tracer(0)  # turn off screen animation

    # Call to function
    draw_net()

    # Game objects
    player1 = Player(PLAYER_COLOR[0], P1_RAC_POS)
    player2 = Player(PLAYER_COLOR[1], P2_RAC_POS)
    scoreboard = Scoreboard()
    ball = Ball()

    # Screen onkey events
    screen.listen()
    screen.onkey(fun=player1.racquet.up, key='w')
    screen.onkey(fun=player1.racquet.down, key='s')
    screen.onkey(fun=player2.racquet.up, key='Up')
    screen.onkey(fun=player2.racquet.down, key='Down')

    heading = random.choice(HEADING)
    run_game = True

    while run_game:
        time.sleep(1)  # pause before starting new game set
        game_set = True
        scoreboard.update_scoreboard(player1.score, player2.score)
        player1.reset_racquet(P1_RAC_POS)
        player2.reset_racquet(P2_RAC_POS)
        ball.home()
        direction = random.choice(DIRECTION)  # random direction for ball
        ball.setheading(heading)

        while game_set:
            screen.update()  # refreshes screen, only works if screen.tracer() is off
            time.sleep(0.001)  # delay time between screen updates (lower = faster movement of objects on screen)
            ball.forward(1)
            ball.move(direction)

            # Detect collision with racquets
            if ball.distance(player2.racquet) < 15:
                ball.setheading(HEADING[1])
            elif ball.distance(player1.racquet) < 15:
                ball.setheading(HEADING[0])

            # Detect collision with up/down borders
            if ball.ycor() > 290:
                direction = "down"
            elif ball.ycor() < -290:
                direction = "up"

            # Detect collision with left/right borders
            if ball.xcor() > 290:
                player1.score += 1
                heading = HEADING[0]  # when player1 scores he 'keeps serving'
                game_set = False
            elif ball.xcor() < - 290:
                player2.score += 1
                heading = HEADING[1]  # when player2 scores he 'keeps serving'
                game_set = False

        # Game over when a player score equals NUM_SETS
        if player1.score == NUM_SETS or player2.score == NUM_SETS:
            prompt_text = "wanna play again? Type 'Y' or 'N': "
            if player1.score > player2.score:
                answer = screen.textinput(title="Game over 🏆", prompt=f"{player1.color} player wins! " + prompt_text)
            else:
                answer = screen.textinput(title="Game over 🏆", prompt=f"{player2.color} player wins! " + prompt_text)
            # End game
            if answer is None or answer.lower() == "n":
                run_game = False
                play_again = False
            # Keep playing
            elif answer.lower() == "y" or answer == "":
                screen.clear()
                run_game = False
            # Also keep playing
            else:
                screen.clear()
                run_game = False

# screen.exitonclick()
