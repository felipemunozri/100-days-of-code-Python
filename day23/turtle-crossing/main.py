import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initial delay time between screen updates
INIT_DLY_TIME = 0.1

# Flag
play_again = True

while play_again:
    # Init screen canvas
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgpic("road.png")
    screen.title("Road-Crossing")
    screen.tracer(0)

    # Game objects
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    # Screen listeners
    screen.listen()
    screen.onkeypress(fun=player.go_up, key="Up")
    screen.onkeypress(fun=player.go_down, key="Down")
    screen.onkeypress(fun=player.go_left, key="Left")
    screen.onkeypress(fun=player.go_right, key="Right")

    # Flag
    game_is_on = True
    dly_time = INIT_DLY_TIME

    while game_is_on:
        time.sleep(dly_time)
        screen.update()

        # Create cars
        car_manager.create_car()

        # Move cars
        car_manager.move_car()
        car_manager.dispose_car()

        print(len(car_manager.car_list))  # debug only

        # Detect player at upper border of screen
        if player.at_upper_border():
            player.reset_position()
            # car_manager.increase_movement()
            dly_time *= 0.8  # reduce delay time to accelerate objects on screen instead of increase cars move distance
            scoreboard.increase_level()

        # Detect collision with cars
        for car in car_manager.car_list:
            if car.distance(player) < 20:
                answer = screen.textinput(title="Game over 🐢", prompt="Wanna play again? Type 'Y' or 'N': ")
                # End game
                if answer is None or answer.lower() == "n":
                    game_is_on = False
                    play_again = False
                # Keep playing
                elif answer.lower() == "y" or answer == "":
                    screen.clear()
                    game_is_on = False
                # Also keep playing
                else:
                    screen.clear()
                    game_is_on = False

# screen.exitonclick()
