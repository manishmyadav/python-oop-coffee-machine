from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_coffee_maker_on = True

while is_coffee_maker_on:
    # Task 1
    choice = input(f"What would you like? {menu.get_items()} ").lower()
    # Task 2
    if choice == 'off':
        is_coffee_maker_on = False
        print("Coffee Maker Turned Off.")
    # Task 3
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            # Task 4
            sufficient_resources = coffee_maker.is_resource_sufficient(drink)
            if sufficient_resources:
                # Task 5 & 6
                payment_successful = money_machine.make_payment(drink.cost)
                # Task 7
                if payment_successful:
                    coffee_maker.make_coffee(drink)



