## Mi codigo
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height < 120:
#     print("Sorry, you are to short. You are not allowed to buy a ticket")
# else:
#     print("You can buy a ticket")

## Respuesta
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
      print("Please pay $5.")
    elif age <= 18:
      print("Please pay 7.")
    else:
      print("Please pay $12.")
else:
    print("Sorry, you can grow taller before you can ride.")