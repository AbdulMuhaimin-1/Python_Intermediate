from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
coffee_machine = CoffeeMaker()
profit = MoneyMachine()


is_on = True
while is_on:
    choice = input(f"What would you like? {coffee_menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        profit.report()
    else:
        drink = coffee_menu.find_drink(choice)
        coffee = MenuItem(drink.name, drink.ingredients["water"], drink.ingredients["milk"],
                          drink.ingredients["coffee"], drink.cost)
        if coffee_machine.is_resource_sufficient(drink):
            if profit.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
