# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row["letter"]: row["code"] for (index, row) in df.iterrows()}
# print(dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    word = input("Enter a word: ").upper()
    try:
        phonetic_list = [dictionary[char] for char in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.\n")
        continue
    else:
        print(phonetic_list)
        break
