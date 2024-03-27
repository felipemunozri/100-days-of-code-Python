############DEBUGGING#####################
#Uncomment the blocks of code one by one and describe what's the problem on each of them

# #Describe Problem
# the for loop goes from 1 to 20 (not included) so 'i' never equals to 20, and so the function never prints the message
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
# my_function()

# # Reproduce the Bug
# randint() goes from 1 to 6 but posittions in dice_imgs list are counnted from 0 to 5, so it never prints the first element and it goes out of index range when it picks '6'. randint() should go from 0 to 5
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# the year 1994 it's not covered in any case. Maybe it should be included in the elif statement as elif year >= 1994:
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# # Fix the Errors
# the first error is the indentation. the second error is that input is always a string and if we want to use a comparison operator we should convert it to a number (either int or float). the third error is that to combine text and variables in a print statement we should use the fstring syntaxis and hence, we should put and f in front of the ""
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# the error is the double == sign in word_per_page == int(input("Number of words per page: ")), it should be a single = sign. When using the double == we are comparing word_per_page to the user input instead of asignin it it's value, so they are not equal and word_per_page is equal to False or 0 in this case. Then when we multiply it for pages we are effectively multiplying by 0, hence total_words is equal to 0
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# b_list.append(new_item) instruction should be inside the for loop. since it is outside what happens is that only the last item on a_list is mutated and stored in new_item. when we append new_item to b_list that's the only item on b_list and it's the only item that gets printed
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])