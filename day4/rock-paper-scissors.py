# imports os module necesary for clear_screen function definded below
import os
import random

#Function clears terminal using command 'cls' or 'clear' depending on OS system ('nt' = Windows)
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear') 

#Function to validate if player wants to keep playing
def try_again():
  global keep_playing
  message = 'Wanna try again? Type "Y" or "N".\n'
  while True:
      answer = input(message).lower()
      if (answer == 'y'):
          keep_playing = True
          clear_screen()
          return keep_playing
      elif (answer == 'n'):
          keep_playing = False
          print()
          print("Thanks for Playing!!! 🌑 📄 ✂️")
          print()
          return keep_playing
      else:
          print("Please enter a valid option.")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#Variable global estado del juego
keep_playing = True

#Creamos lista con las opciones
list = [rock, paper, scissors]

#Loop para seguir corriendo el juego mientras keep_playin sea "True"
while keep_playing:

  print("Welcome to 🌑 Rock, 📄 Paper, ✂️  Scissors Game!!!\n")
  #Validamos entrada del usuario.
  while True:
    user = input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n")
    if (user == "0") or (user == "1") or (user == "2"):
      user = int(user)
      break
    else:
      print("Please enter a valid option.")
      continue

  #Creamos opción de la A.I.
  ai = random.randint(0, 2)

  #Caso empate.
  if user == ai:
    print("You choose:")
    print(list[user])
    print("Computer choose:")
    print(list[ai])
    print("It's a draw!!")

  #Casos gana usuario.
  elif (user == 0 and ai == 2) or (user == 1 and ai == 0) or (user == 2 and ai == 1):
    print("You choose:")
    print(list[user])
    print("Computer choose:")
    print(list[ai])
    print("You win!!")

  #Sino pierde usuario.
  else:
    print("You choose:")
    print(list[user])
    print("Computer choose:")
    print(list[ai])
    print("You lose!!")
  
  print()
  try_again()
