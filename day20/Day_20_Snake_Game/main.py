from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("background.gif")
screen.title("Snake Game")
screen.tracer(0)
screen.register_shape("apple.gif")
screen.register_shape("snake.gif")
screen.register_shape("snake_head.gif")
screen.register_shape("snake_head_right.gif")
screen.register_shape("snake_head_up.gif")
screen.register_shape("snake_head_down.gif")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")


def snake_game():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.new_food()
            snake.grow_snake()
            scoreboard.increase_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 230 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()


snake_game()
screen.exitonclick()
