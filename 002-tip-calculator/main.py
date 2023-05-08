# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator, please answer the questions below.")
bill = input("Total food cost in Hungaryan Forint(Ft):\n")

person_num = input("How many parts do we divide it into?:\n")

tip = input("What percentage u want to tip?:\n")
if tip == "20%":
    tip = "20"
    tip_count = int(tip) / 100 + 1.00
else:
    tip_count = int(tip) / 100 + 1.00

price_per_person = (int(bill) / int(person_num)) * tip_count

rounded = round(price_per_person, 2)

print(f"The bill is {rounded} Ft per person")
