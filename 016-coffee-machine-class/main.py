from coffee import CoffeeMachine


machine = CoffeeMachine()


while True:
    selected_coffee = input(
        "What would you like? (espresso(0)/latte(1)/cappuccino(2)): "
    )

    if selected_coffee == "off":
        break
    elif selected_coffee == "report":
        machine.report()
        continue

    coffee_nr = int(selected_coffee)

    if machine.check_resources(coffee_nr) == False:
        continue

    inserted_money = machine.process_coins()
    machine.make_transaction(coffee_nr, inserted_money)
