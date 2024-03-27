# Mi código
# from question_model import Question
# from data import question_data
#
# score = 0
# num = 1
#
# for item in question_data:
#     question = Question(item["text"], item["answer"])
#     answer = input(f"Q.{num}: {question.text} True/False?: ").title()
#     if question.check_answer(answer):
#         score += 1
#         print("You got it right!")
#     else:
#         print("That's wrong.")
#     print(f"The correct answer was: {question.answer}")
#     print(f"Your current score is: {score}/{num}\n")
#     num += 1
# print("You've completed the quiz")
# print(f"Your final score was: {score}/{num - 1}\n")

# Respuesta
# from question_model import Question
# from quiz_brain import QuizBrain
# from data import question_data
#
# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)
#
# quiz = QuizBrain(question_bank)
# while quiz.still_has_questions():
#     quiz.next_question()
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# Respuesta con API de preguntas
# import the requests module to be able to make api requests (must install module first)
import requests
# import the html module to be able to clean raw json data from api call
import html
from question_model import Question
from quiz_brain import QuizBrain

# call to open trivia database API. We get ahold of info stored in "results" keyword
r = requests.get("https://opentdb.com/api.php?amount=50&category=9&type=boolean").json()
raw_data = r["results"]

question_bank = []
for item in raw_data:
    # for each item on raw_data we get ahold of info stored in "question" keyword and clean it by using the
    # html.unescape() function
    question_text = html.unescape(item["question"])
    question_answer = item["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
