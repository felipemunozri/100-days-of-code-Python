"""
NOTA SOBRE ARRAYS vs LISTAS EN PYTHON!!!
Los arrays y listas son tipos de estructuras de datos diferentes en Python. Los arrays solo pueden almacenar elementos de un mismo tipo mientras  que las listas pueden almacenar varios tipos de datos. Los arrays necesitan ser declarados y para usarlos se debe importar el modulo array o la libreria NumPy, mientras que las listas no necesitan ser declaradas pues vienen por defecto con Python. Ambos son ordenados. Las listas son redimensionables mientras que los arrays tiene un tamaño fijo que no se puede alterar despues de declararlos. Los arrays son mas eficientes y son mejores para almacenar grandes cantidades de datos de un mismo tipo. Las listas consumen mas memoria y espacio y son mejores para almacenar pequeñas cantidades de datos de varios tipos. Los elementos de una lista se pueden imprimir directamente mientras que para un array se debe utilizar un loop con un print o similar. Los arrays estan escritos en C mientras que las listas en Python mismo.
"""

# creación de una lista.
states_of_america = ["delaware", "Pencilvania"]
print(states_of_america)

# accedemos a los elementos de una lista refereciándolos por su índice o posición (contada a partir de 0).
print(states_of_america[0])

# podemos usar índices negativos para acceder a elementos al final de una lista (donde -1 es el último, -2 el penultimo, etc).
print(states_of_america[-1])

# podemos alterar directamente el valor de un elemento en una lista referenciándolo por su posición y asignándole el nuevo valor.
states_of_america[1] = "Pennsylvania"
print(states_of_america)

# la función .append() sirve para agregar un elemento al final de una lista.
states_of_america.append("state3")
print(states_of_america)

# la función .extend() sirve para agregar una lista de elementos al final de una lista.
states_of_america.extend(["4", 5, "State6"])
print(states_of_america)

# la función .insert(i, x) sirve para insertar un elemento en una posición. El argumento "i" es el índice o posición en la lista en la cual queremos insertar el elemento "x" (recordar que las posiciones son contadas a partir de 0).
states_of_america.insert(0, "State0")
print(states_of_america)

# la función .remove(x) sirve para quitar el primer elemento cuyo valor coincida con "x". Si el elemento no existe en la lista arroja error.
states_of_america.remove("State0")
print(states_of_america)

# la función .pop(i) sirve para quitar el elemento en la posición "i" y lo devuelve. Si no se especifica una posición quitará y devolverá el último elemento en la lista. 
print(states_of_america.pop(4))
print(states_of_america)

# la función .count(x) devuelve el número de veces que aparece el elemento "x" en una lista.
print(states_of_america.count("delaware"))

# la función .index(x) devuelve la posición de la primera ocurrencia del elemento "x" en una lista. Tiene parámetros opcionales como .index(x, start, end) donde "start" y "end" son posiciones para poder especificar un rango de busqueda, es decir, "start" como la posición a partir desde la cual empezar la búsqueda y "end" la posición donde dejar de buscar. El indice que se retorna siempre va a ser relativo al tamaño de toda la lista y no al parámetro "start". Si el elemento "x" no se encuentra arroja error.
print(states_of_america.index("delaware"))

# la función .reverse() invierte el orden de los elementos en la lista.
states_of_america.reverse()
print(states_of_america)

# la función .sort() ordena los elementos de una lista y tiene parámetros opcionales (ver en documentación). Importante notar que .sort() no puede ordenar ni comparar todos los datos en una lista, por ejemplo, no puede comparar ints con strings. En este ejemplo ordena números (como string) primero, luego palabras en mayúsculas por orden alfabético, y luego palabras en minúsculas por orden alfabético
states_of_america.sort()
print(states_of_america)

# la función .copy() devuelve una copia "superfcial" de una lista. El hecho de que la copia sea "superficial" significa que no está viculada a la lista original, por lo que si posterior a la copia modificamos la lista original el cambio no se reflejará en la copia. Si modificamos la copia tampoco se afecta a la lista original
copy_of_states_of_america = states_of_america.copy()
print(states_of_america)
print(copy_of_states_of_america)

# la función .clear() sirve para quitar todos los elementos de una lista
states_of_america.clear()
print(states_of_america)
print(copy_of_states_of_america)