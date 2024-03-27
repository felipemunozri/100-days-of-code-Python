# Mi código
import os
import random
from art import logo2

HARD_LEVEL_ATTEMPTS = 10
EASY_LEVEL_ATTEMPTS = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_difficulty():
    difficulty = input("Choose a dificulty. Type '(e)asy' or '(h)ard': ").lower()
    if (difficulty == "e"):
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def compare(num_attempts, rand_number):
    print(f"You have {num_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == rand_number:
        print(f"You've got it! The answer was {rand_number}.")
        num_attempts = -1
        return num_attempts
    elif guess > rand_number:
        print("Too high.")
        return num_attempts - 1
    else:
        print("Too low.")
        return num_attempts - 1

def play_game():
    print(logo2)
    print("Welcome to the Number Guessing Game!!!🔮\n")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)

    attempts = set_difficulty()
    while attempts > 0:
        attempts = compare(attempts, number)

    if attempts == 0:
        print("You've run out of guesses, you lose.")

    while input("\nWanna play again? Type 'y' or 'n': ").lower() == "y":
        clear_screen()
        play_game()

play_game()
print("\nThanks for playing Number Guessing Game!!!🔮\n")
