# Mi codigo
#Password Generator Project
import random
import os

#Function clears terminal using command 'cls' or 'clear' depending on OS system ('nt' = Windows)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator 🔐 !\n")
# Validamos entrada de usuario para cantidad de letras
while True:
    nr_letters = input("How many letters would you like in your password?\n")
    if(not(nr_letters.isdigit())):
        print("Input is not a number. Please enter a valid number.")
        continue
    else:
        nr_letters = int(nr_letters)
        if(nr_letters < 0):
            print(f"The number of letters can't be less than 0. Please enter a valid option.")
            continue
        else:
            clear_screen()
            break

# Validamos entrada de usuario para cantidad de símbolos
while True:
    nr_symbols = input("How many symbols would you like in your password?\n")
    if(not(nr_symbols.isdigit())):
        print("Input is not a number. Please enter a valid number.")
        continue
    else:
        nr_symbols = int(nr_symbols)
        if(nr_symbols < 0):
            print(f"The number of symbols can't be less than 0. Please enter a valid option.")
            continue
        else:
            clear_screen()
            break

# Validamos entrada de usuario para cantindad de números
while True:
    nr_numbers = input("How many numbers would you like in your password?\n")
    if(not(nr_numbers.isdigit())):
        print("Input is not a number. Please enter a valid number.")
        continue
    else:
        nr_numbers = int(nr_numbers)
        if(nr_numbers < 0):
            print(f"The number of numbers can't be less than 0. Please enter a valid option.")
            continue
        else:
            clear_screen()
            break

picked_letters = []
picked_symbols = []
picked_numbers = []

password = []
rand_password = ""

# Generamos letras al azar según el número de letras nr_letters
# if (nr_letters != 0):
for l in range(1, nr_letters + 1):
    picked_letters.append(letters[random.randint(0, len(letters) - 1)])

# Generamos símbolos al azar según el número de letras nr_symbols
# if (nr_symbols != 0):
for s in range(1, nr_symbols + 1):
    picked_symbols.append(symbols[random.randint(0, len(symbols) - 1)])

# Generamos números al azar según el número de números nr_numbers
# if (nr_numbers != 0):
for n in range(1, nr_numbers + 1):
    picked_numbers.append(numbers[random.randint(0, len(numbers) - 1)])

# Unimos todos las listas de caracteres en una sola lista
password = picked_letters + picked_numbers + picked_symbols

# Desordenamos la lista con la función .shuffle()
random.shuffle(password)

# Juntamos los caracteres en una string que guardamos en la variable rand_password 
for c in password:
    rand_password += c

# Imprimimos la contraseña randomizada
print(f"Here is your password: {rand_password}\n")
print("Thanks for using our app 🔐.\n")

# Respuesta
# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level
# # password = ""

# # for char in range(1, nr_letters + 1):
# #   password += random.choice(letters)

# # for char in range(1, nr_symbols + 1):
# #   password += random.choice(symbols)

# # for char in range(1, nr_numbers + 1):
# #   password += random.choice(numbers)

# # print(password)

# #Hard Level
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")