#import modules, game_data, art
import random
import os
from game_data import data
from art import logo, vs

#implement clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#implement random subject picker function from data
def pick_subject():
    subject = random.choice(data)
    return subject

#implement check guess function
def check(a_sub, b_sub, guess):
    if guess == "a":
        if a_sub["follower_count"] > b_sub["follower_count"]:
            return True
    elif guess == "b":
        if b_sub["follower_count"] > a_sub["follower_count"]:
            return True

#implement game function
def game():
    print(logo)

    run_game = True
    score  = 0

    a = pick_subject()
    b = pick_subject()

    while run_game:
        #after a sucsessful guess we keep the last subject b and pass it as subject a, then we pick a new subject b  
        a = b
        b = pick_subject()

        #prevents that subject a and b are the same
        while a == b:
            b = pick_subject()

        print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
        print(vs)
        print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.')

        #for debug only
        # print(a["follower_count"])
        # print(b["follower_count"])

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        if check(a, b, guess):
            score += 1
            clear_screen()
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return

game()
