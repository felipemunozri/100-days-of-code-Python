from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# instance of Menu() class
menu = Menu()

# instance of MoneyMachine() class
money_machine = MoneyMachine()

# instance of CoffeeMaker() class
coffe_machine = CoffeeMaker()

is_on = True

while is_on:
    choice = input(f"What would you like? {menu.get_items()}?: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_machine.make_coffee(drink)


