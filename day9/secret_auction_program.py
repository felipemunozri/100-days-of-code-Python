# Mi código
# import os

# # function clears terminal using command 'cls' or 'clear' depending on OS system ('nt' = Windows)
# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# from art import logo

# print(logo)
# print("Welcome to the secret auction program.")

# bidders = {}

# keep_going = True

# while keep_going:
#     name = input("What is your name?: ")
#     bid = int(input("What's your bid?: $"))
#     result = input("Are there any other bidders? Type 'yes' or 'no'.\n")

#     bidders[name] = bid
    
#     if result == "no":
#         keep_going = False
#         clear_screen()
#     else:
#         clear_screen()

# max_bidder = ""
# max_bid = 0

# for bidder, bid in bidders.items():
#     if bid > max_bid:
#         max_bid = bid
#         max_bidder = bidder

# print(f"The winner is {max_bidder} with a bid of ${max_bid}")

# Respuesta
import os

# function clears terminal using command 'cls' or 'clear' depending on OS system ('nt' = Windows)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # recorre el objeto bidding_record y al recorrerlo bidder no corresponde a un item sino que directamente a cada una de las keys guardadas en el objeto. Por lo anterior, se puede acceder al valor de cada key directamente de esta forma bidding_record[bidder]. Luego guarda ese valor en una variabla y compara para determinar el máximo
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount    
        winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear_screen()