import os
import pandas as pd
import random
from tkinter import *
import pandas.errors
from gtts import gTTS
from playaudio import playaudio

# Colors
BACKGROUND_COLOR = "#B1DDC6"

# Fonts
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# initial words dictionary
words_dictionary = {}

# initial card
current_card = {}

# initial source and target language names
source_lang_name = ""
target_lang_name = ""


# ------------------------------- READ DATA FROM CSV ------------------------------- #
try:
    # try to create a DataFrame from the words_to_learn.csv file
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    # if file is not found, then create a DataFrame from the original french_words.csv file instead
    original_data = pd.read_csv("./data/french_words.csv")
    words_dictionary = original_data.to_dict(orient="records")
    source_lang_name = original_data.columns[0]
    target_lang_name = original_data.columns[1]
except pandas.errors.EmptyDataError:
    # if words_to_learn.csv file exits but is empty, then use the original french_words.csv instead
    original_data = pd.read_csv("./data/french_words.csv")
    words_dictionary = original_data.to_dict(orient="records")
    source_lang_name = original_data.columns[0]
    target_lang_name = original_data.columns[1]
else:
    words_dictionary = data.to_dict(orient="records")  # create the dictionary from created DataFrame
    source_lang_name = data.columns[0]
    target_lang_name = data.columns[1]


# ------------------------------- CREATE CARD ------------------------------- #
def create_card():
    """Cancels any current window timer, retrieves a random element from words_dictionary and updates a card's title,
    word, background image and text color with the information retrieved. Finally, calls the flip_card function after 3
    seconds."""
    language = 'fr'
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dictionary)
    canvas.itemconfig(card_title, text=source_lang_name, fill="black")
    canvas.itemconfig(card_word, text=current_card[source_lang_name], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(100)
    audio_output = gTTS(text=current_card["French"], lang=language)
    audio_output.save("english_word.mp3")
    playaudio("english_word.mp3", True)
    os.remove("english_word.mp3")
    flip_timer = window.after(3000, flip_card)


# ------------------------------- FLIP CARD ------------------------------- #
def flip_card():
    """Changes a card's title, word, background image and text color to show the translation of the current word
    displayed inside a card."""
    language = 'en'
    canvas.itemconfig(card_title, text=target_lang_name, fill="white")
    canvas.itemconfig(card_word, text=current_card[target_lang_name], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    audio_output = gTTS(text=current_card["English"], lang=language)
    audio_output.save("french_word.mp3")
    playaudio("french_word.mp3", True)
    os.remove("french_word.mp3")


# ------------------------------- CREATE WORDS_TO_LEARN.CSV ------------------------------- #
def create_words_to_learn():
    """When the user click the known_button because he knows a word then this function gets executed. This function
    removes the data associated with the current word learned by the user from the words_dictionary. Then, it creates a
    new .csv file from the modified dictionary called words_to_learn.csv. This .csv file will be used to keep track of
    the words the user still has to learn, and so this is the file that should be loaded the next time the user opens up
    the program."""
    words_dictionary.remove(current_card)
    words_to_learn_data = pandas.DataFrame(words_dictionary)
    words_to_learn_data.to_csv("./data/words_to_learn.csv", index=False)
    create_card()


# ------------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Flash Card App")
window.resizable(False, False)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# in 3 seconds call the flip_card function for the first time
flip_timer = window.after(3000, flip_card)

# Images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
known_button_img = PhotoImage(file=r"./images/right.png")
unknown_button_img = PhotoImage(file=r"./images/wrong.png")

# Canvas
canvas = Canvas()
canvas.config(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# Canvas text items
card_title = canvas.create_text(400, 150, text="", font=LANG_FONT)
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT)

# function to create a card for the first time
create_card()

# Buttons
unknown_button = Button(command=create_card, image=unknown_button_img, highlightthickness=0, borderwidth=0,
                        relief=FLAT)
unknown_button.grid(column=0, row=1)
known_button = Button(command=create_words_to_learn, image=known_button_img, highlightthickness=0, borderwidth=0,
                      relief=FLAT)
known_button.grid(column=1, row=1)

window.mainloop()
