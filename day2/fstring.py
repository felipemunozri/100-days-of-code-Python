score = 0
height = 1.8
isWinning = True

print (type(score))
print (type(height))
print (type(isWinning))

# Usando la forma tradicional antes de concatenar un string con otros tipos de variables debemos convertir a string dichas variables
print("Your score is " + str(score) + ", your height is " + str(height) + ", you are winning is " + str(isWinning))

# Usando f-String esto es mucho más facil. Solo debemos anteponer una "f" antes de las " " y poner las variables entre {}
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

