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


def coffee_machine():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    choice(user_choice)


def choice(user_choice):
    if user_choice == "off":
        print("Coffee machine is going to turn off.")
        exit()
    elif user_choice == "report":
        print_resources()
        coffee_machine()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        result = check_resources_sufficient(user_choice)
        if result:
            coin_result = coin_processing(user_choice)
            if coin_result:
                make_coffee(user_choice)
            else:
                coffee_machine()
        else:
            coffee_machine()
    else:
        print("You picked wrong!")
        coffee_machine()


def print_resources():
    for key, value in resources.items():
        print(key, ' : ', value)


def check_resources_sufficient(user_choice):
    if user_choice == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    else:
        if resources["water"] < MENU[user_choice]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"] < MENU[user_choice]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif resources["coffee"] < MENU[user_choice]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True


def coin_processing(user_choice):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    sum_of_coins = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    if sum_of_coins >= MENU[user_choice]["cost"]:
        change = sum_of_coins - MENU[user_choice]["cost"]
        change = round(change, 2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(user_choice):
    if user_choice == "espresso":
        resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
    else:
        resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
    print(f"Here is Your {user_choice}. Enjoy!")
    coffee_machine()


coffee_machine()
