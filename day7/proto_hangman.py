import os
import random

# function clears terminal using command 'cls' or 'clear' depending on OS system ('nt' = Windows)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# function to ask if player wants to keep playing
def try_again():
    global keep_playing
    message = '❓ Wanna try again? Type "Y" or "N".\n'
    while True:
        answer = input(message).lower()
        if (answer == 'y'):
            keep_playing = True
            clear_screen()
            return keep_playing
        elif (answer == 'n'):
            keep_playing = False
            print()
            print("👋 Thanks for Playing!!!")
            print()
            return keep_playing
        else:
            print("Please enter a valid option.")

# hang_6 = ('''
#      _______
#     |       |
#             |
#             |
#             |
#     🕯️     __|__
# ''')

# hang_5 = ('''
#      _______
#     |       |
#    🙁       |
#             |
#             |
#     🕯️     __|__
# ''')

# hang_4 = ('''
#      _______
#     |       |
#    😧       |
#     |       |
#             |
#    🔥     __|__
# ''')

# hang_3 = ('''
#      _______
#     |       |
#    😨       |
#    /|       |
#             |
#   🔥🔥    __|__
# ''')

# hang_2 = ('''
#      _______
#     |       |
#    😭       |
#    /|\      |
#             |
#   🔥🔥    __|__
# ''')

# hang_1 = ('''
#      _______
#     |       |
#    🥵       |
#    /|\      |
#    /        |
#   🔥🔥🔥  __|__
# ''')

# hang_0 = ('''
#      _______
#     |       |
#    😡       |
#    /|\      |
#    / \      |
#   🔥🔥🔥  __|__
# ''')

hang_6 = ('''
     _______
    |       |
            |
            |
            |
          __|__
''')

hang_5 = ('''
     _______
    |       |
    0       |
            |
            |
          __|__
''')

hang_4 = ('''
     _______
    |       |
    0       |
    |       |
            |
          __|__
''')

hang_3 = ('''
     _______
    |       |
    0       |
   /|       |
            |
          __|__
''')

hang_2 = ('''
     _______
    |       |
    0       |
   /|\      |
            |
          __|__
''')

hang_1 = ('''
     _______
    |       |
    0       |
   /|\      |
   /        |
          __|__
''')

hang_0 = ('''
     _______
    |       |
    0       |
   /|\      |
   / \      |
          __|__
''')

# list to store hangman drawings
hangman = [hang_0, hang_1, hang_2, hang_3, hang_4, hang_5, hang_6]

# pool of words to guess
group = ["hello", "python", "angela", "hangman", "word", "code"]

# when changed to "False" game ends
keep_playing = True

# loop to keep game running
while keep_playing:

    # random word to guess
    guess_word = list(random.choice(group))

    # list to store all user guesses (right and wrong)
    all_guesses = []

    # list to show user correct guesses
    correct_guesses = ["_"] * len(guess_word)

    # number of attempts needed to complete hangman drawing
    attempts = 6

    print("Welcome to the Hangman Game!!!😵")
    print(hangman[attempts])
    result = ''.join(correct_guesses)
    print(f"Your word is: '{result}'")

    # while there are attempts left and guess_word has not been guessed yet
    while (attempts != 0) and (guess_word != correct_guesses):
        print()

        # validate if user input is a letter
        while True:
            letter = input("Guess a letter:\n").lower()
            if len(letter) != 1 or not letter.isalpha():
                clear_screen()
                print("Please enter a valid character.")
                continue
            else:
                break
        
        # evaluates if letter was already inputted, if it wasn't then store it in all_guesses list to check again next time
        if (letter in all_guesses):
            clear_screen()
            print(f"⚡ Letter '{letter}' was already guessed! ⛔")
            print(hangman[attempts])
            print(f"Current guess: '{result}'")
        else:
            all_guesses.append(letter)

            # evaluates if letter exists in word, if it does exists then appends it to correct_guesses, if not then reduce number of attempts left
            if (letter in guess_word):
                for i in range(0, len(guess_word)):
                    if letter == guess_word[i]:
                        correct_guesses[guess_word.index(letter, i)] = letter
                result = ''.join(correct_guesses)
                clear_screen()
                print(f"👑 Correct!!! Attempts left: {attempts}")
                print(hangman[attempts])
                print(f"Current guess: '{result}'")
            else:
                attempts -= 1
                clear_screen()
                print(f"❌ Wrong!!! Attempts left: {attempts}")
                print(hangman[attempts])
                print(f"Current guess: '{result}'")

    # evaluates if user guessed correctly and won or not
    if (guess_word == correct_guesses):
        print()
        print("You win!!😅\n")
    else:
        print()
        print("You lose!!🤪\n")
        result = ''.join(guess_word)
        print(f"Your word was: '{result}'\n")

    # calls function to ask player if wants to keep playing
    try_again()
