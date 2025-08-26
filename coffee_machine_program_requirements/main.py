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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_available(ingredients):
    """Returns True if the ingredients are available, False otherwise."""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough available {item}")
            return False
    return True

def process_coins():
    """Returns the total amount of coins."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns True if the transaction is successful, False otherwise."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in dollars refunded.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, ingredients):
    """Deduct the ingredients and cost of the drink."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}'s coffee now.")

is_on = True

while True:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_available(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



