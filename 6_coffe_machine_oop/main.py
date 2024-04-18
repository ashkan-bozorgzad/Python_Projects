from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


should_continue = True
while should_continue:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "report":
        coffee.report()
        money.report()

    elif choice == "off":
        should_continue = False

    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)