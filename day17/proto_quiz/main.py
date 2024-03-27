from data import question_data

num = 1
score = 0

for item in question_data:
    answer = input(f"Q{num}: {item['question']} (True/False)?: ").title()
    if answer == item["correct_answer"]:
        score += 1
        print("You got it right!")
    else:
        print("That's wrong.")
    print(f"The correct answer was: {item['correct_answer']}")
    print(f"Your current score is: {score}/{num}\n")
    num += 1

print("You've completed the quiz")
print(f"Your final score was: {score}/{num - 1}\n")