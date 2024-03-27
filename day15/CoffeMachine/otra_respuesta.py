from clint.textui import colored, puts, indent

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report(res):
    """returns report on statuses of vending machine"""
    with indent(4, quote=' >'):
        puts(colored.yellow(f"Water: {res['water']}ml\nMilk: {res['milk']}ml"))
        puts(colored.yellow(f"Coffee: {res['coffee']}g\nMoney: ${res['money']}"))


def update_machine(item, resources):  # item is a dictionary
    """update vending machine after transaction"""
    ingredients = item["ingredients"]
    for i in ingredients:
        resources[i] -= ingredients[i]
    resources['money'] += item["cost"]
    return resources


def check_input(prompt, _type):
    """makes sure that input is proper type and > 0"""
    # since this is checking the input for the vending machine, we can't allow negative input
    types = {
        int: lambda x: int(x),
        float: lambda x: float(x)
    }
    while True:
        try:
            val = types[_type](input(prompt))
            if val < 0:
                puts(colored.red("Invalid input. Can't pay with less than 0"))
            else:
                return val
        except ValueError:
            puts(colored.red("Invalid input. Try again: "))


def make_transaction(price):
    """Returns difference between price and money paid. If returned value is negative,
    it means user still needs to pay more."""
    puts(colored.cyan("Please insert coins."))
    money_paid = check_input("how many quarters?: ", int) * 0.25
    money_paid += check_input("how many dimes?: ", int) * 0.1
    money_paid += check_input("how many nickels?: ", int) * 0.05
    money_paid += check_input("how many pennies?: ", int) * 0.01
    return round(money_paid - price, 2)


def check_missing(ingredients, resources):
    """check if any ingredients are missing to make user's request"""
    for i in ingredients:
        if ingredients[i] > resources[i]:
            return i  # stop processing drink, return which ingredient caused error
    return None


def check_command(commands, command):
    """checks user's command to see if it's valid"""
    for i in commands:
        if i == command:
            return True
    return False


# create global vending machine vars, menu and res are names for convenience
resources["money"] = 0  # initialize no money
valid_commands = ['report', 'off', 'espresso', 'latte', 'cappuccino']
off = "off"  # would just rather keep track of the quit variable here

# vending machine loop
default_question = "What would you like? (espresso/latte/cappuccino): "
user_choice = input(default_question)

while user_choice != off:  # exit loop if user chooses 'off'

    user_choice = user_choice.lower()  # make user_choice not case sensitive

    if not check_command(valid_commands, user_choice):  # make sure user is using a valid choice
        puts(colored.red("Invalid option. Please choose: 'espresso', 'latte', or 'cappuccino'"))

    elif user_choice == "report":
        report(resources)  # return report of amount of ingredients and money in machine

    else:  # transaction section

        missing = check_missing(MENU[user_choice]["ingredients"], resources)  # check if there are missing ingredients for user_choice

        if missing:  # if missing isn't None, it will be a missing item, so we show the missing item
            puts(colored.yellow(f"Sorry, there is not enough {missing}."))

        else:
            change = make_transaction(MENU[user_choice]["cost"])  # calculate change if transaction goes through

            if change < 0:  # if change < 0, user needs to pay more money; cancel and try again
                puts(colored.yellow("Sorry, that's not enough money. Money refunded."))

            else:  # no errors, so we complete transaction
                # update machine with new amounts of ingredients and money
                update_machine(MENU[user_choice], resources)
                # print results
                puts(colored.green(f"Here is ${change} in change."))
                puts(colored.green(f"Here is your {user_choice} ☕  Enjoy!"))

    # ask user input again
    user_choice = input(default_question)
