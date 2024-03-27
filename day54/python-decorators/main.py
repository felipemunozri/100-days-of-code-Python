# # Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# # Functions are first-class objects, that means they can be passed around as arguments like e.g. int/string/float etc.
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(add, 2, 3)
# print(result)
#
#
# # Functions can be nested in other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
#
# outer_function()


# # Functions can also be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
#
# inner_function = outer_function()
# inner_function()  # note we can call the stored function by adding () to the name of the variable where we stored it


# # Note that we can return multiple functions and that the assignment of the returned functions is position specific
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     def one():
#         print("one")
#
#     def two():
#         print("two")
#
#     return nested_function, one, two
#
#
# inner_function, a, b = outer_function()
# inner_function(), b()


# Now, a decorator function is a function that wraps another function and gives it some additional functionality or
# modifies its functionality. In other words, they let you execute code before and after the function they decorate
# without modifying the function itself.


# Simple Python Decorator Functions
import time


# We define a delay_decorator() function which receives an external function and inside has an internal function defined
# called wrapper_function(), which delays the execution of the main program by 2 seconds and then executes the received
# function twice. Finally, this function returns the internal function
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # We do something before the received function
        function()
        function()
        # We could also do something after the received function

    return wrapper_function


# To apply a decorator function we can use the @ syntactic sugar by calling the decorator function just before another
# function
@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


# Or we could also apply a decorator function without the @ syntactic sugar. For this we call the delay_decorator()
# function passing the say_greeting() function as its argument. Once we stored the returned value in the
# decorated_function variable, we can call the inner function (aka. the wrapper_function() declared inside the
# delay_decorator() function)
def say_greeting():
    print("How are you?")


decorated_function = delay_decorator(say_greeting)
decorated_function()
