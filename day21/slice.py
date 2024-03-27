# Uso del operador : slice. Se puede utilizar sobre cualquier iterable y su sintaxis es [start:stop:step]. Devuelve una copia superficial

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])  # ["c", "d", "e"] 

print(piano_keys[2:])  # ["c", "d", "e", "f", "g"] 

print(piano_keys[:5])  # ["a", "b", "c", "d", "e"] 

print(piano_keys[2:5:2])  # ["c", "e"] 

print(piano_keys[::2])  # ["a", "c", "e", "g"] 