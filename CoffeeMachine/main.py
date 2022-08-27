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


MONEY = 0


# TODO: 6. Calculate the monetary value of all the coins inserted.
def calculate_coins(request, quarter, dime, nickle, penny):
    amount = (0.25 * quarter) + (0.10 * dime) + (0.05 * nickle) + (0.01 * penny)
    # TODO: 7. Check if money is enough to purchase the flavor chosen.
    if amount == flavor["cost"]:
        print(f"Here is your {request}  ☕. Enjoy!")
        return True
    # TODO: 10. If too much money is inserted, deduct cost of coffee and offer change. Print "Here is {change} dollars
    #  in change."
    elif amount > flavor["cost"]:
        change = round((amount - flavor["cost"]), 2)
        print(f"Here is {change} dollars change.")
        print(f"Here is your {request} ☕. Enjoy!")
        return True
    # TODO: 8. Print "Sorry, that's not enough money. Money refunded." if money is not enough.
    else:
        print("Sorry that's not enough money. Money refunded.")


# TODO: 4. Check resources sufficient to make order.
def choice(request):
    """Take user input and check if there is enough resource."""
    if ingredient["water"] > water_quant:
        print("Sorry there is not enough water.")
    elif ingredient["coffee"] > coffee_quant:
        print("Sorry there is not enough coffee.")
    elif request != "espresso" and ingredient["milk"] > milk_quant:
        print("Sorry there is not enough milk.")
    else:
        return True


# TODO: 11. If transaction successful, deduct the resources of the selected flavor from the coffee machine resources.
def update_resources():
    if ingredient["water"] <= water_quant and ingredient["coffee"] <= coffee_quant:
        updated_water = water_quant - ingredient["water"]
        updated_coffee = coffee_quant - ingredient["coffee"]
        if user_request != "espresso" and ingredient["milk"] <= milk_quant:
            updated_milk = milk_quant - ingredient["milk"]
            return {"new_water": updated_water, "new_coffee": updated_coffee, "new_milk": updated_milk}
        else:
            return {"new_water": updated_water, "new_coffee": updated_coffee}


# def new_resources(updated_water, updated_coffee, updated_milk):


# TODO: 2. Print a report of all coffee machine resources.
def resource():
    return f"Water: {water_quant}ml\nMilk: {milk_quant}ml\nCoffee: {coffee_quant}g\nMoney: ${MONEY}"


coffee_machine_on = True
# TODO: 13. Everytime codes/actions complete prompt for flavor or report should show.
while coffee_machine_on:
    water_quant = resources["water"]
    milk_quant = resources["milk"]
    coffee_quant = resources["coffee"]
    # TODO: 1. Print a prompt to take user input flavor or report.
    user_request = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    # flavor = MENU[user_request]
    # TODO: 3. If user enters 'Off' the program should end.
    if user_request == "off":
        coffee_machine_on = False
    elif user_request == "report":
        print(resource())
    else:
        flavor = MENU[user_request]
        ingredient = flavor["ingredients"]
        # TODO: 5. If resources are sufficient, prompt user to insert coins.
        if choice(user_request):
            print("Please insert coins 👇.")
            quarter_coin = int(input("How many quarters?: "))
            dime_coin = int(input("How many dimes?: "))
            nickle_coin = int(input("How many nickles?: "))
            penny_coin = int(input("How many pennies?: "))
            # TODO: 9. If enough money is inserted, add the cost of the flavor chosen to coffee machine.
            if calculate_coins(user_request, quarter_coin, dime_coin, nickle_coin, penny_coin):
                coffee_cup = MENU[user_request]
                MONEY += coffee_cup["cost"]
            # TODO: 12. The remaining resources should be what will be printed if user should enter "report".
            resources.update({
                "water": update_resources()["new_water"],
                "coffee": update_resources()["new_coffee"]
            })
            if user_request != "espresso":
                resources.update({
                    "milk": update_resources()["new_milk"]
                })
