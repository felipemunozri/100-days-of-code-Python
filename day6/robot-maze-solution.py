# Mi código1
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()    

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         if front_is_clear():
#             move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()


# Mi código 2 (mi solución a loop infinito)
def turn_right():
    turn_left()
    turn_left()
    turn_left()    

count = 0

while not at_goal():
    if count < 4:
        if right_is_clear():
            turn_right()
            if front_is_clear():
                move()
                count += 1
        elif front_is_clear():
            move()
            count = 0
        else:
            turn_left()
            count = 0
    else:
        move()
        count = 0

# Respuesta (solución a loop infinito)
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()