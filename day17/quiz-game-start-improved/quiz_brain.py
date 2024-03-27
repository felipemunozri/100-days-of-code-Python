from colorama import Fore


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        """Prints a question from self.question_list, increments self.question_number, and takes an user
        input to pass to self.check_answer() class method."""
        current_question = self.question_list[self.question_number]
        # after getting a hold of question we increase self.question_number
        self.question_number += 1
        # validates if user input is 'true' or 'false'
        while True:
            print(f"Q.{self.question_number} {current_question.text} True/False?: ")
            print(f"   -category: {current_question.category}")
            print(f"   -difficulty: {current_question.difficulty}")
            user_answer = input().lower()
            if user_answer != 'true' and user_answer != 'false':
                print(Fore.YELLOW + "    Please type 'true' or 'false' as an answer.\n"  + Fore.WHITE)
            else:
                break
        self.check_answer(user_answer, current_question.answer)  # call to self.check_answer() class method

    def still_has_questions(self):
        """Validates if self.question_list is greater than self.question_number. If not returns false."""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """Takes an user input answer and the current_question answer and compares them. If true increments self.score
        attribute. Prints message to user."""
        if user_answer == correct_answer.lower():
            print(Fore.GREEN + "    You got it right!")
            self.score += 1
        else:
            print(Fore.RED + "    That's wrong!")
        print(f"    The correct answer was: {correct_answer}")
        print(f"    Your current score is: {self.score}/{self.question_number}")
        print(Fore.WHITE + "")
