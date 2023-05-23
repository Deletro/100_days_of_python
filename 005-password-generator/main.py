# Password Generator Project
import random

# fmt: off
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# fmt: on

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_slice_1 = ""
for _ in range(nr_letters):
    random_letter = random.choice(letters)
    password_slice_1 += random_letter


password_slice_2 = ""
for _ in range(nr_symbols):
    random_symbol = random.choice(symbols)
    password_slice_2 += random_symbol


password_slice_3 = ""
for _ in range(nr_numbers):
    random_number = random.choice(numbers)
    password_slice_3 += random_number

password = password_slice_1 + password_slice_2 + password_slice_3
print(password)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&s

password = list(password)
random.shuffle(password)

print("".join(password))
