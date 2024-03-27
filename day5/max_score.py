# Mi codigo
# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# #Inicializamos la variable max_score en el primer elemento
# max_score = student_scores[0]

# #Inicializamos i en 1 para partir recorriendo y comparando a partir del segundo elemento, ya que el primero lo tenemos almacenado en la variable max_score
# for i in range (1, len(student_scores)):
#   if (student_scores[i] > max_score):
#     max_score = student_scores[i]
#   else:
#       max_score = max_score

# print(f"The highest score in the class is: {max_score}")

# Respuesta
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    # print(highest_score)
    
print(f"The highest score in the class is: {highest_score}")