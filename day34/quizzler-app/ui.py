from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
RED = "#EE665D"
GREEN = "#29B677"
FONT = ("Arial", 20, "italic")
FONT2 = ("Arial", 10, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # quiz_brain
        self.quiz = quiz_brain
        # window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        # canvas
        self.canvas = Canvas(width=300, height=250, )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)
        # canvas text
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=FONT)
        # label
        self.score_label = Label(text="", bg=THEME_COLOR, fg="white", font=FONT2)
        self.score_label.grid(column=1, row=0)
        # images
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        # buttons
        self.true_button = Button(command=self.true_pressed, image=true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(command=self.false_pressed, image=false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)
        # get first question
        self.get_next_question()
        # get initial score value
        self.update_score()
        # main loop
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_button.config(state=ACTIVE)
            self.false_button.config(state=ACTIVE)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            # self.true_button.config(state=DISABLED)
            # self.false_button.config(state=DISABLED)
            # if messagebox.askyesno("Game Over", "The game is over, do you want to play again?"):

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def update_score(self):
        self.score_label.configure(text=f"Score: {self.quiz.score}")

    def give_feedback(self, value):
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)
        if value:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.canvas.update()
        self.window.after(1000, self.get_next_question)
        self.update_score()
