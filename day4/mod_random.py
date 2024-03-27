import random

# ejemplo importación de un modulo propio
# import my_module

# accedemos a la variable "pi" creada en el modulo que importamos
# print(my_module.pi)

# genera un numero entero aleatorio entre a y b (inclusive). Falla para a > b
random_integer = random.randint(1, 10)
print(random_integer)

# genera un numero float aleatorio entre 0 y 1 sin incluir 1.
random_float = random.random()
print(random_float)

# genera un numero float aleatorio entre a y b (inclusive). Funciona tanto para a <= b como para b < a
random_float2 = random.uniform(5, -1)
print(random_float2)