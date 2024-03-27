# Mi codigo
for n in range(1, 101):
  if(n % 3 == 0) and (n % 5 == 0):
      print("FizzBuzz")
  elif(n % 3 == 0):
      print("Fizz")
  elif(n % 5 == 0):
      print("Buzz")
  else:
      print(n)

# Respuesta
# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)

# Otra forma
# for num in range (1,101):
#   output = ""
#   if num % 3 == 0:
#     output += "Fizz"
#   if num % 5 == 0:
#     output += "Buzz"
#   print(output if output != "" else num)

# Otra forma
# for number in range(1, 101):
#   if number % 3 == 0:
#     if number % 5 == 0:
#       print("FizzBuzz")
#     else:
#       print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#       print(number)