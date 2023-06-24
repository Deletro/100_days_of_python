class Coffee:
    def __init__(self, coffee_type, water, milk, coffee, cost):
        self.coffee_type = coffee_type
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost


class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 100
        self.coffee = 100
        self.money = 0
        self.coffees = [
            Coffee("espresso", 50, 0, 18, 1.5),
            Coffee("latte", 200, 150, 24, 2.5),
            Coffee("cappuccino", 250, 100, 24, 3.0),
        ]

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money}")

    def check_resources(self, coffee_nr):
        coffee = self.coffees[coffee_nr]
        if self.water < coffee.water:
            print("Not Enough Water")
            return False
        elif self.milk < coffee.milk:
            print("Not Enough Milk")
            return False
        elif self.coffee < coffee.coffee:
            print("Not Enough Coffee")
            return False
        return True

    @staticmethod
    def process_coins():
        quarters = int(input("How many quarters: ")) * 0.25
        dimes = int(input("How many dimes: ")) * 0.10
        nickles = int(input("How many nickles: ")) * 0.05
        pennies = int(input("How many pennies: ")) * 0.01
        return quarters + dimes + nickles + pennies

    def make_transaction(self, coffee_nr, inserted_money):
        ordered_coffee = self.coffees[coffee_nr]

        if ordered_coffee.cost > inserted_money:
            print("Sorry that's not enough money. Money refunded.")
            return

        self.water -= ordered_coffee.water
        self.milk -= ordered_coffee.milk
        self.coffee -= ordered_coffee.coffee

        self.money += ordered_coffee.cost

        change = round(inserted_money - ordered_coffee.cost, 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        print(f"Here is your {ordered_coffee.coffee_type}. Enjoy!")
