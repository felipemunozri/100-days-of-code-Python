from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

flip_timer = 0


def button_next_card():
    # Upon button click, reset timer and calls get_random_word
    global flip_timer
    window.after_cancel(flip_timer)
    get_random_word()


def get_random_word():
    # Retrieves random french word, waits 3s and calls flip card with random_word_num as argument
    global flip_timer
    random_word_num = random.randint(0, 100)
    french_word = words_dict[random_word_num]["French"]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")
    canvas.itemconfig(canvas_image, image=back_img)
    flip_timer = window.after(3000, flip_card, random_word_num)


def flip_card(random_word_num):
    # flips card and shows English word
    english_word = words_dict[random_word_num]["English"]
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")
    canvas.itemconfig(canvas_image, image=front_img)


# -------------Initialise PANDAS--------------------
words_data = pd.read_csv("./data/french_words.csv")
words_dict = words_data.to_dict(orient="records")

# --------Initialise window, images and canvas---------
window = Tk(className="Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

front_img = PhotoImage(file="./images/card_back.png")
back_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=500, height=300, highlightthickness=0)
canvas.grid(column=1, row=1, columnspan=3, rowspan=2)
canvas_image = canvas.create_image(200, 100, image=back_img)
title = canvas.create_text(250, 100, text="title", font=("Ariel", 20, "italic"))
word = canvas.create_text(250, 180, text="word", font=("Ariel", 30, "bold"))

get_random_word()

# Buttons 
right_button = (Button(image=right_img, highlightthickness=0, command=button_next_card, relief=FLAT, borderwidth=0)
                .grid(column=3, row=3, pady=10))
wrong_button = (Button(image=wrong_img, highlightthickness=0, command=button_next_card, relief=FLAT, borderwidth=0)
                .grid(column=1, row=3, pady=10))

window.mainloop()
