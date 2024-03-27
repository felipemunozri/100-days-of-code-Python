# Ejercicios con copia de listas 
print()
print('" # Copiamos usando my_list.copy()."')
my_list = [[1, 2, 3], 4, 5, 6]
print("my_list:", my_list)
copy_list = my_list.copy()
print("copy_list:", copy_list)
print()

print('" # Modificamos my_list y copy_list no cambia."')
my_list[0] = [10, 11, 12]
print("my_list:", my_list)
print("copy_list:", copy_list)
print()

print('" # Modificamos copy_list y my_list no cambia."')
copy_list[0] = [7, 8, 9]
print("copy_list:", copy_list)
print("my_list:", my_list)
print()

print('" # Copiamos usando equal_list = my_list."')
equal_list = my_list
print("equal_list:", equal_list)
print("my_list:", my_list)
print()

print('" # Modificamos equal_list y my_list si cambia."')
equal_list[0] = [20, 21, 22]
print("equal_list:", equal_list)
print("my_list:", my_list)
print()

