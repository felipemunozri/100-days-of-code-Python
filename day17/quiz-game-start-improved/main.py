import os
import html
from art import logo
from data import Data
from question_model import Question
from quiz_brain import QuizBrain


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


play_game = True

while play_game:
    clear_screen()
    print(logo)
    print("Welcome to The Quiz Game!!!😄")
    data = Data()
    raw_question_list = data.initialize_data()
    print("\nQUESTIONS:\n")

    question_bank = []
    
    for item in raw_question_list:
        q_category = item["category"]
        q_difficulty = item["difficulty"]
        # remove weird characters in question text by using the html.unescape() function
        q_text = html.unescape(item["question"])
        q_answer = item["correct_answer"]
        new_question = Question(q_category, q_difficulty, q_text, q_answer)
        question_bank.append(new_question)
    
    quiz = QuizBrain(question_bank)
    
    while quiz.still_has_questions():
        quiz.next_question()
    
    print("\nQUIZ FINISHED:")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}.\n")
    while True:
        answr = input("Do you want to take another quiz? Type 'Y' or 'N': ")
        if answr.lower() == "n":
            play_game = False
            break
        elif answr.lower() == "y":
            break
        else:
            print("Please chose a correct option.")
            continue

print("\nThanks for playing The Quiz Game!!👋\n")
