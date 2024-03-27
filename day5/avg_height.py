# Mi codigo (alturas como float en vez de int)
user_input = input("Input a list of students heights ")

heights = user_input.split()

quantity = 0
heights_sum = 0
avg_height = 0

for height in heights:
  quantity += 1
  heights_sum += float(height)

avg_height =  round(heights_sum / quantity, 2)

print(avg_height)

# Respuesta
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # print(student_heights)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# total_height = 0
# for height in student_heights:
#   total_height += height
# print(f"total height = {total_height}")

# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1
# print(f"number of students = {number_of_students}")
  
# average_height = round(total_height / number_of_students)
# print(average_height)
