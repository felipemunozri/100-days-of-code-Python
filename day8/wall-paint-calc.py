#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    # number_of_cans = round((height * width) / cover)
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# la función math.ceil() no es igual que la función round(). math.ceil() siempre redondea hacia arriba al entero más cercano, mientras que round() puede redondear hacia arriba o hacia abajo. Además round() si el número esta en un punto medio (ej: 4.5), redondea al número entero par más cercano, es decir, redondeará 4.5 a 4.
print()
print("Diferencia entre funciones round() y math.ceil():")
print(" round(4.4) =       ", round(4.4))
print(" math.ceil(4.4) =   ", math.ceil(4.4))
print(" round(4.5) =       ", round(4.5))
print(" math.ceil(4.5) =   ", math.ceil(4.5))
print()