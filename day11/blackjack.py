# Mi código
import os
import random
from art import logo

# list of cards 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# limit of number of cards to generate. We pass this value to generate_user_hand() and generate_dealer_hand() functions defined below
limit = 2
# variable to keep game running while True
run_game = True

# function clears terminal using command 'cls' or 'clear' depending on OS system ('nt' = Windows)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# function to pick a random card from cards list
def generate_card():
    card = random.choice(cards)
    return card

# function to generate both user and dealer first hand
def generate_hand(limit):
    hand = []
    for i in range(0, limit):
        card = generate_card()
        hand.append(card)
    return hand

# function to calculate score in users hands
def calculate_score(hand):
    score = 0
    for card in hand:
        score += card
    return score

# function to print both user and dealer hands
def print_hands():
    print(f"    Your cards: {user_hand}, current score: {user_score}")
    print(f"    Computer's first card: {dealer_hand[0]}")

# function to replace an '11' card for a '1' card
def elevent_to_one(hand):
    position = hand.index(11)
    hand[position] = 1
    return hand

# function evaluates conditions to win/lose the game and prints the result
def result():
    print(f"    Your final hand: {user_hand}, final score: {user_score}")
    print(f"    Computer's final hand: {dealer_hand}, final score: {dealer_score}")

    if user_score > 21:
        print("You went over. You lose 😤")
    elif dealer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score == dealer_score:
        print("Draw 🙃")
    elif (dealer_hand == [11, 10]) or (dealer_hand == [10, 11]):
        print("Lose, opponent has Blackjack 😱")
    elif (user_hand == [11, 10]) or (user_hand == [10, 11]):
        print("Win with a Blackjack 😎")
    elif user_score > dealer_score:
        print("You win 😃")
    else:
        print("You lose 😤")

# while True game keeps running
while run_game:
    # list to strore user's hand
    user_hand = []
    # list to strore ai's hand
    dealer_hand = []
    # variable to strore user's score
    user_score = 0
    # variable to strore ai's score
    dealer_score = 0
    # variable to asses if user would want another card. We assume it to 'True' unless stated 
    user_wants_card = True

    answer1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if answer1 == 'y':
        clear_screen()
        print(logo)
        # generate user's first hand and calculate score
        user_hand = generate_hand(2)
        user_score = calculate_score(user_hand)
        # generate dealer's first hand and calculate score
        dealer_hand = generate_hand(2)
        dealer_score = calculate_score(dealer_hand)
        # evaluate if user or dealer score a blackjack on their first hand, if one oh them did we step out of the loop
        if (user_score == 21) or (dealer_score == 21):
            print_hands()
            user_wants_card = False
        else:
            # while user_wants_card is 'True' we generate another card for user
            while user_wants_card:
                print_hands()
                answer2 = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if answer2 == "y":
                    user_hand.append(generate_card())
                    user_score = calculate_score(user_hand)
                    # if user_score goes over 21 after adding an extra card but there was an '11' card we replace it with a '1' card and recalculate the user_score 
                    if user_score > 21 and 11 in user_hand:
                        user_hand = elevent_to_one(user_hand)
                        user_score = calculate_score(user_hand)
                    # if user_score goes over 21 after adding an extra card and there weren't any '11' cards we step out of the loop, the user already lose
                    elif user_score > 21 and 11 not in user_hand:
                        print_hands()
                        user_wants_card = False
                # if user doesn't want more cards we step out of the loop
                else:
                    user_wants_card = False
        
        # while dealer_score is less than 17 we must add extra cards
        while dealer_score < 17:
            dealer_hand.append(generate_card())
            dealer_score = calculate_score(dealer_hand)
            # if dealer_score goes over 21 after adding an extra card but there was an '11' card we replace it with a '1' card and recalculate the dealer_score 
            if dealer_score > 21 and 11 in dealer_hand:
                dealer_hand = elevent_to_one(dealer_hand)
                dealer_score = calculate_score(dealer_hand)
        
        # evaluate game logic and print results 
        result()
    else:
        run_game = False
