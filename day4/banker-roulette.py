# Mi codigo
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_lenght = len(names)
rand_num =  random.randint(0, names_lenght -1 )
0
print(f"{names[rand_num]} is going to buy the meal today!")

# Respuesta
# import random

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# #Write your code below this line 👇
# #Get the total number of items in list.
# num_items = len(names)
# #Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# #Pick out random person from list of names using the random number.
# person_who_will_pay = names[random_choice]

# print(person_who_will_pay + " is going to buy the meal today!")