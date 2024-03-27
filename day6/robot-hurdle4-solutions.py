# Mi código
def turn_right():
    turn_left()
    turn_left()
    turn_left()    

def jump():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    if wall_in_front():
        turn_left()
    if right_is_clear() and is_facing_north():
        jump()

# Respuesta
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()    

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# Otra respuesta
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#         if right_is_clear():
#             turn_right()
#     elif wall_in_front():
#         turn_left()