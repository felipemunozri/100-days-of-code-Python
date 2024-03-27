# Create a list containing the squared numbers in numbers list

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:
squared_numbers = [num ** 2 for num in numbers]

# Write your code 👆 above:
print(squared_numbers)

##############################################################################################################

# Create a list containing only the even numbers in numbers list

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:
result = [num for num in numbers if num % 2 == 0]

# Write your code 👆 above:
print(result)

##############################################################################################################

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.

with open("file1.txt", "r") as file1:
    file1_numbers = file1.readlines()  # readlines() return all lines in the file as a list

with open("file2.txt", "r") as file2:
    file2_numbers = file2.readlines()

result = [int(num.strip()) for num in file1_numbers if num in file2_numbers]

# Write your code above 👆
print(result)

##############################################################################################################

# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given
# sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Don't change code above 👆


# Write your code below:
words_list = sentence.split()  # split() returns a list of the words separated by something, in this case a blank space
result = {word: len(word) for word in words_list}

print(result)

##############################################################################################################

# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in
# degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:

# the items() method returns an object containing a list of tuples with (key: value) pairs from the original object
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

##############################################################################################################

# Use Dictionary Comprehension to create a dictionary called student_scores that takes a list of students and generate a
# random score for each one. Then create another dictionary called passed_students with students with scores greater or
# equal to 60

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor"]

student_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
