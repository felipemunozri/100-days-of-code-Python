import time
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row["letter"]: row["code"] for (index, row) in df.iterrows()}


def generate_phonetic():
    word = "123"  # Fixed value to mock input
    try:
        output_list = [dictionary[char] for char in word]
    except KeyError:
        generate_phonetic()
    else:
        print(output_list)


before = time.time()
try:
    generate_phonetic()
except RecursionError:
    after = time.time()
    print(f"This took just {round(after - before, 3)} seconds to crash!")
