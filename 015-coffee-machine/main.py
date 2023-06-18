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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def make_transaction(ordered_coffee, inserted_money):
    if ordered_coffee["cost"] > inserted_money:
        print("Sorry that's not enough money. Money refunded.")
        return False

    for material, ammounts in ordered_coffee["ingredients"].items():
        resources[material] -= ammounts

    resources["money"] += ordered_coffee["cost"]

    change = round(inserted_money - ordered_coffee["cost"], 2)
    if change > 0:
        print(f"Here is ${change} dollars in change.")
    return True


def process_coins():
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    return quarters + dimes + nickles + pennies


def check_resources(ordered_coffee):
    for material, ammounts in ordered_coffee["ingredients"].items():
        if resources[material] < ammounts:
            print(f"Sorry there is not enough {material}")
            return False
    return True


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


while True:
    selected_coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if selected_coffee == "off":
        break
    elif selected_coffee == "report":
        report()
        continue

    ordered_coffee = MENU[selected_coffee]
    if check_resources(ordered_coffee) == False:
        continue

    inserted_money = process_coins()
    if make_transaction(ordered_coffee, inserted_money):
        print(f"Here is your {selected_coffee}. Enjoy!")
