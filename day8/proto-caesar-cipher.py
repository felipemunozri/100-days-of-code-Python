
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#            0    1    2    3    4    5    6                                                                    -6   -5   -4   -3   -2   -1

end_program = False

print("Welcome to Caesar Cipher!!!\n")

while not end_program:

    option = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()

    message = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    alphabet_length = len(alphabet)

    encrypted_message = []

    decrypted_message = []

    if option == "encode":
        for letter in message:
            shifted_letter_index = alphabet.index(letter) + shift
            # if shifted_letter_index is '26' then it should be the character on alphabet at position '26', but since we count from 0 there is no character at position '26' but at '25', which is 'z'
            if shifted_letter_index == 26:
                encrypted_message.append("z")
            # if shifted letter number is bigger than alphabet length then substract shifted_letter_index - alphabet_length and use the result as the new letter index to append to encrypted_message
            elif shifted_letter_index > alphabet_length:
                result = shifted_letter_index - alphabet_length
                encrypted_message.append(alphabet[result])
            # if shifted_letter_index y less or equal than alphabet_lenght just append the shifted_letter_index letter to encrypted_message
            else:
                encrypted_message.append(alphabet[shifted_letter_index])
                
        encrypted_message_text = ''.join(encrypted_message)
        print(f"Here is the encoded result: {encrypted_message_text}")

    elif option == "decode":
        for letter in message:
            # if letter is 'z' then alphabet_index is 25 and by substracting shift we end up with a misalignment of 1 letter, so we must add 1
            if letter == "z":
                shifted_letter_index = alphabet.index(letter) - shift + 1
                decrypted_message.append(alphabet[shifted_letter_index])
            else:
                shifted_letter_index = alphabet.index(letter) - shift
                decrypted_message.append(alphabet[shifted_letter_index])
                
        decrypted_message_text = ''.join(decrypted_message)
        print(f"Here is the decoded result: {decrypted_message_text}")
    
    answer = input("Type 'yes' if you wnat to go again, otherwise type 'no'.\n")

    if answer == 'no':
        print("Thanks for using Caesar Cipher!!!\n")
        end_program = True
