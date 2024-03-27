# Mi codigo
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#Separamos el número ingresado por el usuario donde (para él) el primer dígito es el número de columna y el segúndo dígito es el número de fila.
col_num = int(position[0]) - 1
row_num = int(position[1]) - 1

#Para nosotros el número de fila del usuario determinará el número del elemento dentro de la lista "map", y el número de columna determinará la posición del elemnto a modificar dentro del elemento.
element_num = row_num
element_to_modify_inside_element = col_num

#Modificamos la lista "map", pasando primero el número de elemento y luego el elemento a modificar, en este caso, reemplazándolo con una "X".
map[element_num][element_to_modify_inside_element] = "X"

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# Respuesta
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# horizontal = int(position[0])
# vertical = int(position[1])

# map[vertical - 1][horizontal - 1] = "X"

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")