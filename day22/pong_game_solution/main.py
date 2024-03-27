# create screen
# create and move paddle
# create another paddle
# create ball and make it move
# detect collision with wall and bounce
# detect collision with paddle
# detect when paddle misses the ball
# keep score
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600, startx=None, starty=None)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
amount = -10

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # ball.forward(1)
    # ball.move("down")

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 and ball.x_move > 0:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340 and ball.x_move < 0:
        ball.bounce_x()

    # Detect collision with borders
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect collision with borders
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
