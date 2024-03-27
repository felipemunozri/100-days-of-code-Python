################### Scope ####################
#global variable defined at the top level
enemies = 1

def increase_enemies():
    #local variable defined inside a function
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
#gives error because from outside the function we can't reference the variable potion_strength which was defined inside the function drink_potion()
print(potion_strength)

#global scope
player_health = 2

def drink_potion():
    potion_strength = 2
    #we can use the variable player_health with no problem from inside the function drink_potion() as player_health was defined as a global variable at the top level
    print(player_health)

#There is no block scope in python!!!
#Variables defined within if statements, for loops, or while loops can be used outside of them as they do not count as a local scope. If they are enclosed within a function then they become local scoped an hence can't be used outside of this functions
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

#modifying a global scope variable
enemies = 1

def increase_enemies():
    #we must explicitly declare inside a function the global variable that we wish to modify calling it by it's name, and we must use the keyword global. However, but it's not a good practice to modify them. We can read them and use them but it's not adviced to modify them
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#global constants
#it is a convention in python to declare constants with all uppercase
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

def calc_perim():
    r = 2
    perim = 2 * PI * r
    return perim