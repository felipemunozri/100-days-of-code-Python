# Mi código
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(message, shift_amount):
#     alphabet_length = len(alphabet)
#     encoded_message = ""

#     for letter in message:
#         letter_index = alphabet.index(letter)
#         shifted_letter_index = letter_index + shift_amount
        
#         if shifted_letter_index == 26:
#             encoded_message += "z"
#         elif shifted_letter_index > alphabet_length:
#             shifted_letter_index -= alphabet_length
#             encoded_message += alphabet[shifted_letter_index]
#         else:
#             encoded_message += alphabet[shifted_letter_index]

#     print(f"The encoded text is {encoded_message}")

# def decrypt(message, shift_amount):
#     alphabet_length = len(alphabet)
#     decoded_message = ""

#     for letter in message:
#         letter_index = alphabet.index(letter)
#         shifted_letter_index = letter_index - shift_amount
        
#         if letter == "z":
#             shifted_letter_index += 1
#             decoded_message += alphabet[shifted_letter_index]
#         else:
#             decoded_message += alphabet[shifted_letter_index]

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)

# Mi código (optimizado)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # si vamos a decodificar simplemente multiplicamos shift_amount por -1 para hacerlo negativo y asi se lo restamos al index de la letra
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char.isalpha():
            position = alphabet.index(char)
            # aqui se produce el shifteo
            new_position = position + shift_amount
            # obtenemos el resto (mediante operador %) de la division entre new_position y el largo del alfabeto para obtener la posición de la nueva letra. Guardamos en la misma variable new_position
            new_position = new_position % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"Here's the {cipher_direction}d result: {end_text}")

import art

print(art.logo)

end_program = False

while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")

    if answer == "no":
        end_program = True
        print("Thanks for using Caesar Cipher!!!")
    elif answer == "yes":
        end_program = False

# Respuesta
# # Su solución (no buena) fue duplicar el alfabeto y asi pasar el error de index out of lenght
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text = new_letter
    
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text = new_letter
    
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)

# Respuesta (optimizada)
# Su solución (no buena) fue duplicar el alfabeto y asi pasar el error de index out of lenght
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1 
#     for letter in start_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"The {cipher_direction}d text is {end_text}")
    
# caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

# Respuesta (mas optimizada)
# Su solución (mejor pero no correcta) fue mantener el duplicado del alfabeto y ocupar el operador % que entrega el resto de la división entre el shift ingresado por el usuario y el largo del alfabeto. El resto de la división es entonces la posición del nuevo caracter a usar. El programa se cae igual pues no se deberia usar el modulo en shift directamente sino en position + shift_amount, y quitar el duplicado del alfabeto
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     if char in alphabet:
#         position = alphabet.index(char)
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     else:
#         end_text += char
    
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# # import logo
# import art

# print(art.logo)

# should_continue = True

# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#     result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")

#     if result == "no":
#         should_continue = False
#         print("Goodbye")

