from tkinter import *
from playsound import playsound
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0  # number of pomodoro cycles
timer = None  # variable to store a window.after() element used below


# ---------------------------- WINDOW TO FRONT ------------------------------- #
def bring_to_front():
    window.state("normal")  # Restore if window is minimized
    window.attributes("-topmost", True)  # Bring to top level above all windows
    window.attributes("-topmost", False)  # Allows other windows to top level again


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    reset_button.config(state="disabled")
    start_button.config(state="normal")
    global reps
    global timer
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    global reps
    reps += 1
    # print(reps)  # debug only
    work_sec = WORK_MIN * 60  # times 60 to get value of minutes in seconds
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # format count_min so if it's less than 10 we append a "0" at the beginning to make it look like a digital clock
    if count_min < 10:
        count_min = f"0{count_min}"
    # same for count_sec
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # itemconfig() allows to modify a canvas element
    if count > 0:
        global timer
        # after() calls a function after n ms. after () receives ms, a function, and *args. In this example after() it's
        # calling the count_down() function itself and is passing count - 1 as the argument
        timer = window.after(1000, count_down, count - 1)  # use 2 instead of 1000 to test quickly
    else:
        start_timer()
        bring_to_front()
        playsound("Bell.mp3")
        # window.bell()  # makes default system notification sound

        text = ""
        work_cycle = math.floor(reps / 2)  # every 2 reps we add a check
        for _ in range(work_cycle):
            # text += "🍅" # if using this icon use foreground=PINK for checkmark_label instead of GREEN
            text += "✔"
            checkmark_label.config(text=text)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.resizable(False, False)
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # highlightthickness= removes canvas border
tomato_img = PhotoImage(file="tomato.png")  # allows to read image from file
canvas.create_image(100, 112, image=tomato_img)  # creates an image at x,y cords
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)  # we must place the canvas using grid()

# Labels
timer_label = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label = Label(background=YELLOW, foreground=GREEN, font=(FONT_NAME, 13, "bold"))
checkmark_label.grid(column=1, row=2)
checkmark_label.config(pady=17)

# Buttons
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer, state="normal",
                      activebackground=RED, bg=PINK, fg=YELLOW, font=(FONT_NAME, 14, "bold"), relief="flat")
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer, state="disabled",
                      activebackground=RED, bg=GREEN, fg=YELLOW, font=(FONT_NAME, 14, "bold"), relief="flat")
reset_button.grid(column=2, row=3)

window.mainloop()
