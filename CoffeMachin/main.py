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


money = 0.0

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money ${money}")

def get_customer_coins():
    print("Please insert coins.")

    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))

    return round(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies, 2)

def calculate_change(total_money, coffe_value):
    if total_money >= coffe_value:
        return total_money - coffe_value
    else:
        print("Sorry that's not enough money. Money refunded.")
        return -1


def check_resource(customer_coffe_type):
    milk = 0
    if not "milk" in customer_coffe_type["ingredients"]:
        milk = 0
    else:
        int(customer_coffe_type["ingredients"]["milk"])

    if resources["milk"] < milk:
        print("Sorry that's not enough milk.")
        return False
    if resources["water"] < int(customer_coffe_type["ingredients"]["water"]):
        print("Sorry that's not enough water.")
        return False
    if resources["coffee"] < int(customer_coffe_type["ingredients"]["coffee"]):
        print("Sorry that's not enough coffe.")
        return False

    return True

def update_resource(customer_coffe_type):
    if not "milk" in customer_coffe_type["ingredients"]:
        milk = 0
    else:
        milk = customer_coffe_type["ingredients"]["milk"]

    water = customer_coffe_type["ingredients"]["water"]
    coffe = customer_coffe_type["ingredients"]["coffee"]

    resources["milk"] -= milk
    resources["water"] -= water
    resources["coffee"] -= coffe

    return resources



start_machine = True

while start_machine:
    #TODO 1: Ask you for coffe type
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'off':
        start_machine = False
    if choice == 'report':
        print_report()
    elif choice in MENU.keys():
        coffe_type = MENU[choice]
        if check_resource(coffe_type):
            total = get_customer_coins()
            change = calculate_change(total, coffe_type["cost"])
            if change >= 0:
                print(f"Here is {change} in change")
                print(f"Here is your {choice} . Enjoy!")
                money += coffe_type["cost"]
                resources = update_resource(coffe_type)
            else:
                print("Sorry that's not enough money. Money refunded.")

