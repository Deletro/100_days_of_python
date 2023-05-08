# 1. Create a greeting for your program.
name = input("Hey rockstar! How can I call you?\n")
print(
    f"Hi {name}, let's see some questions, and I'll help you to choose the right name to your band"
)

# 2. Ask the user for the city that they grew up in.
city = input(f"{name}, tell me please where do you live?\n")

# 3. Ask the user for the name of a pet.
pet_name = input(
    f"And the last question to you {name} what is your favourite pet name?\n"
)

# 4. Combine the name of their city and pet and show them their band name.
print(f"So {name}, I strongly recommend the '{city} {pet_name}' to your band name!")
