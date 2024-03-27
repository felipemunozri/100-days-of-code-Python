# ----------------------- TYPES OF ERRORS ----------------------- #

# FileNotFound
# with open("a_file.txt", "r") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# ----------------------- MANAGING ERRORS ----------------------- #

try:  # try this actions

    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    # value = a_dictionary["non_existent_key"]  # would give KeyError
    value = a_dictionary["key"]

except FileNotFoundError:  # if first action failed do this

    # print("There was an error")  # not so good error handling
    open("a_file.txt", "w")  # if file doesn't exist we create it, this is better

except KeyError as error_message:  # if second action failed do this

    print(f"The key {error_message} doesn't exist.")  # we capture the error_message and use it to provide better info

else:  # if both action succeeded do this, if any one failed this code will not be executed

    content = file.read()
    print(content)

finally:  # no matter what execute this

    file.close()
    print("File was closed.")

    raise ValueError("This is an error that I made up.")  # We use raise to raise our own custom errors


