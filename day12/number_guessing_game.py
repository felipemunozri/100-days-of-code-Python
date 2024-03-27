# Mi código
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    run_game = True

    while run_game:
        clear_screen()
        number = random.randint(1, 100)

        print("Welcome to the Number Guessing Game!!!🔮\n")
        print("I'm thinking of a number between 1 and 100.")

        difficulty = input("Choose a dificulty. Type '(e)asy' or '(h)ard': ").lower()
        if (difficulty == "e"):
            attempts = 10
        else:
            attempts = 5

        not_guessed_yet = True

        while not_guessed_yet:
            if attempts == 0:
                print("You've run out of guesses, you lose.")
                not_guessed_yet = False
            else:
                print(f"You have {attempts} attempts remaining to guess the number.")
                guess = int(input("Make a guess: "))
                if guess == number:
                    print(f"You've got it! The answer was {number}.")
                    not_guessed_yet = False
                elif guess > number:
                    print("Too high.")
                    attempts -= 1
                else:
                    print("Too low.")
                    attempts -= 1

        answer = input("\nWanna play again? Type 'y' or 'n': ").lower()
        if answer == "n":
            run_game = False
            print("\nThanks for playing Number Guessing Game!!!🔮\n")

play_game()
