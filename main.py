MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 600,
    "milk": 400,
    "coffee": 200,
}
from art import logo
money = 0

print(logo)
def sufficient():
    """Check if there are enough resources to make the drink."""
    if resources["water"] < MENU[user_input]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["milk"] < MENU[user_input]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif resources["coffee"] < MENU[user_input]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True


def coins():
    """Handle the coin input and payment process."""
    global money
    print("Please insert coins")
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    total_coins = quarters + dimes + nickles + pennies
    if total_coins >= MENU[user_input]["cost"]:
        remainings = round((total_coins - MENU[user_input]["cost"]), 2)
        print(f"Here is ${remainings} in change.")
        money += MENU[user_input]["cost"]
        update_resources()
        print(f"Here is your {user_input} ☕. Enjoy!")
        print(("\n"*1))
    else:
        print("Sorry that's not enough money. Money refunded.")


def update_resources():
    """Update the resources after making the drink."""
    resources["water"] -= MENU[user_input]["ingredients"]["water"]
    resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
    resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]


should_continue = True
while should_continue:
    user_input = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        should_continue = False
        print("Turning off. Goodbye!")

    elif user_input == "report":
        # Print both key and value in resources
        for key, value in resources.items():
            print(f"{key.capitalize()}: {value}ml")
        print(f"Money: ${money}")

    elif user_input in MENU:
        if sufficient():  # Only proceed to coins() if resources are sufficient
            coins()

    else:
        print("Invalid selection. Please choose again.")
