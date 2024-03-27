from snake import Snake
from food import SnakeFood
from turtle import Turtle, Screen
import time
FORMAT = {'align': 'center', 'font': ("Courier", 20, "normal")}


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.goto(0, 310)

        self.score = 0

        try:
            with open('pp.dat', 'r') as f:
                self.high_score = int(f.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0

    def display_score(self):
        self.write(f'Score: {self.score} - High score: {self.high_score}', **FORMAT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()


class SnakeGame:

    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=700, height=700)
        self.screen.cv._rootwindow.resizable(False, False)  # Access Tkinter function from Canvas screen
        self.screen.bgpic('gfx/border.gif')
        self.screen.title("Snake Game")
        self.screen.tracer(0)  # Turn off automatic screen update

        self.snake = Snake()
        self.food = SnakeFood(self.snake.body)
        self.scoreboard = ScoreBoard()
        self.speed = .1

        self.__bind_key()
        self.scoreboard.display_score()

        self.is_paused = False
        self.__text = Turtle()
        self.__text.color('white')
        self.__text.hideturtle()
        self.__text.speed('fastest')
        self.__text.penup()
        self.__text.goto(0, -335)
        self.__text.write("Press 'Space' to pause the game.", **FORMAT)

    def __bind_key(self):
        self.screen.listen()
        self.screen.onkey(self.pause, 'space')

        def up(): self.snake.up(self.is_paused)
        def down(): self.snake.down(self.is_paused)
        def left(): self.snake.left(self.is_paused)
        def right(): self.snake.right(self.is_paused)
        movement = [up, down, left, right]

        for move, key in zip(movement, ['Up', 'Down', 'Left', 'Right']):
            # self.screen.onkey(move, key)
            self.screen.onkeypress(move, key)

        # Alternative keys
        for move, key in zip(movement, 'wsad'):
            # self.screen.onkey(move, key)
            self.screen.onkeypress(move, key)

        # Capslock case
        for move, key in zip(movement, 'WSAD'):
            # self.screen.onkey(move, key)
            self.screen.onkeypress(move, key)

    def __change_text(self):
        if self.is_paused is None:
            self.__text.clear()
            self.__text.color('red')
            self.__text.goto(0, 0)
            self.__text.write('GAME OVER!', align='center', font=("Courier", 25, "bold"))

            # Restart game suggestion
            self.__text.color('white')
            self.__text.goto(0, -18)
            self.__text.write("Press 'Enter' to restart the game.", align='center', font=("Courier", 15, "normal"))

        elif self.is_paused:
            self.__text.clear()
            self.__text.write("Press 'Space' to continue the game.", **FORMAT)
            self.__text.goto(0, 0)
            self.__text.write("GAME PAUSED.", **FORMAT)

        else:
            for _ in range(3):
                self.__text.undo()
            self.__text.write("Press 'Space' to pause the game.", **FORMAT)

    def save_score(self):
        # Save highest score
        if self.scoreboard.high_score < self.scoreboard.score:
            with open('pp.dat', 'w') as f:
                f.write(str(self.scoreboard.score))

    def pause(self):
        if self.is_paused is not None:
            self.is_paused = not self.is_paused
        self.__change_text()

    def end(self):
        self.is_paused = None  # Block 'pause' text appearance after game is over
        self.save_score()
        self.__change_text()

    def play(self):
        while True:
            self.screen.update()
            time.sleep(self.speed)

            if not self.is_paused:
                self.snake.move()

                # Detect collision with food
                if self.snake.head.distance(self.food) < 10:
                    self.food.refresh(self.snake.body)
                    self.scoreboard.increase_score()
                    self.snake.grow()

                    # Increase the speed
                    if self.scoreboard.score % 10 == 0:
                        self.speed = (100 - self.scoreboard.score) / 1000

                # Detect collision with border or with itself
                if self.snake.is_out_of_bound() or self.snake.is_hit():
                    self.end()
                    break
