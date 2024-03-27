## Mi codigo
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# name1 = name1.lower()
# name2 = name2.lower()

# num_t = name1.count("t") + name2.count("t")
# num_r = name1.count("r") + name2.count("r")
# num_u = name1.count("u") + name2.count("u")
# num_e = name1.count("e") + name2.count("e")

# num_l = name1.count("l") + name2.count("l")
# num_o = name1.count("o") + name2.count("o")
# num_v = name1.count("v") + name2.count("v")

# fst_dig = num_t + num_r + num_u + num_e
# sec_dig = num_l + num_o + num_v + num_e

# love_per = str(fst_dig) + str(sec_dig)

# int_love_per = int(love_per)

# if int_love_per < 10 or int_love_per > 90:
#     print(f"Your score is {int_love_per}, you go together like coke and mentos.")
# elif int_love_per >= 40 and int_love_per <= 50:
#     print(f"Your score is {int_love_per}, you are alright together.")
# else:
#     print(f"Your score is {int_love_per}.")

## Respuesta
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")