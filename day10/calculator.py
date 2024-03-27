# Mi código
# import os
# from art import logo

# # function clears terminal using command 'cls' or 'clear' depending on OS system ('nt' = Windows)
# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def add(n1, n2):
#     return n1 + n2
    
# def substract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# operations = {
#     "+": add,
#     "-": substract,
#     "*": multiply,
#     "/": divide
# }

# new_calculator = False

# while not new_calculator:
#     print(logo)
#     print("Welcome to Python Calculator!!!\n")

#     num1 = float(input("What's the first number?: "))

#     for symbol in operations:
#         print(symbol)
#     keep_result = True

#     operation_symbol = input("Pick an operation: ")
#     num2 = float(input("What's the next number?: "))
    
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")

#     while keep_result:
#         response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. Type 'e' to end Python Calculator: ").lower()
        
#         if response == "y":
#             num1 = answer
#             operation_symbol = input("Pick an operation: ")
#             num2 = float(input("What's the next number?: "))
        
#             calculation_function = operations[operation_symbol]
#             answer = calculation_function(num1, num2)
#             print(f"{num1} {operation_symbol} {num2} = {answer}")
#         elif response == "n":
#             keep_result = False
#             clear_screen()
#         else:
#             print("\nThanks for using Python Calculator!!!\n")
#             keep_result = False
#             new_calculator = True

# Respuesta
from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": substract, "*": multiply, "/": divide}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: "
        ).lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
