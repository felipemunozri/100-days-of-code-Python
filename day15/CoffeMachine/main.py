MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            # "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 400,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNIE = 0.01


# TODO: 1. print report of all coffee machine resources.
# For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine.

def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


# TODO: 2. check if resources are sufficient to make drink order.
# When the user chooses a drink, the program should check if there are enough
# resources to make that drink.


def check_resources(drink):
    # # my code assumes that espresso has the "milk" keyword with value 0
    # drink_water = drink['ingredients']['water']
    # drink_milk = drink["ingredients"]["milk"]
    # drink_coffee = drink["ingredients"]["coffee"]
    # if drink_water > resources["water"]:
    #     print("Sorry there is not enough water")
    #     return False
    # elif drink_milk > resources["milk"]:
    #     print("Sorry there is not enough milk")
    #     return False
    # elif drink_coffee > resources["coffee"]:
    #     print("Sorry there is not enough coffe")
    #     return False
    # else:
    #     return True

    drink_ingredients = drink["ingredients"]
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 3. process coins, calculate the monetary value of the coins inserted.
# Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01


def process_coins(drink):
    drink_cost = drink["cost"]
    print(f"The cost is ${drink_cost}. Please insert coins.")
    quarters = int(input("how many quarters?: ")) * QUARTER
    dimes = int(input("how many dimes?: ")) * DIME
    nickles = int(input("how many nickles?: ")) * NICKLE
    pennies = int(input("how many pennies?: ")) * PENNIE
    total_coins = quarters + dimes + nickles + pennies
    return total_coins


# TODO: 4. check transaction successful?
# Check that the user has inserted enough money to purchase the drink they selected.
# after counting the coins the program should say“ Sorry that's not enough money. Money refunded. ”
# if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit
# If the user has inserted too much money, the machine should offer change.
# “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.


def check_transaction(drink, money_received):
    drink_cost = drink["cost"]
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True

# TODO : 5. make coffe
# If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.


def make_coffee(drink_name, drink):
    # # my code assumes that espresso has the "milk" keyword with value 0
    # resources["water"] -= drink["ingredients"]["water"]
    # resources["milk"] -= drink["ingredients"]["milk"]
    # resources["coffee"] -= drink["ingredients"]["coffee"]

    drink_ingredients = drink["ingredients"]
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


def coffee_machine():
    drink = {}
    run_machine = True

    while run_machine:
        choice = input(" What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            print("Turning off machine...")
            run_machine = False
        elif choice == "report":
            print_report()
        elif choice == "espresso":
            drink = MENU[choice]
        elif choice == "latte":
            drink = MENU[choice]
        elif choice == "cappuccino":
            drink = MENU[choice]

        # # instead of comparing choice to each drink in MENU, it's a better solution to just pass choice and grab
        # # directly from MENU. We put that instruction in the else statement and the next
        # # if choice != "report" and choice != "off": block is redundant
        # else: drink = MENU[choice]

        if choice != "report" and choice != "off":
            # for debug only
            # print(drink)
            if check_resources(drink):
                coins = process_coins(drink)
                if check_transaction(drink, coins):
                    resources["money"] += drink["cost"]
                    make_coffee(choice, drink)


coffee_machine()
