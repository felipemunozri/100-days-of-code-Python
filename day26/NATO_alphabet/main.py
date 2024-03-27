# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row["letter"]: row["code"] for (index, row) in df.iterrows()}
# print(dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
# chars_in_word = [*word]  # alt_1: create list of characters on a word using unpack * method
# chars_in_word = list(word)  # alt_2: create list of characters on a word using list() casting
# print(chars_in_word)

phonetic_list = [dictionary[char] for char in word]
print(phonetic_list)
