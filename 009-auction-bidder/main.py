import os


def clear():  # Cross-platform clear screen
    os.system("cls" if os.name == "nt" else "clear")


print("Welcome to the secret auction program.")

bidders = {}
other_bidders = "yes"
while other_bidders == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == "yes":
        clear()

highest_bidder = ""
highest_bid = 0
for key in bidders:
    if bidders[key] > highest_bid:
        highest_bid = bidders[key]
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
