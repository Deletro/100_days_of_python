import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

print(
    "Welcome to the Rock/Paper/Scissors tournament against the smartest AI in the world"
)
print("Choose your weapon:\n'Rock: 0'\n'Paper: 1'\n'Scissors: 2'")

player_choice_num = int(input(""))
player_choice = choices[player_choice_num]
ai_choice = random.choice(choices)

print(player_choice)
print(ai_choice)

if ai_choice == player_choice:
    print("Draw")
elif ai_choice == rock and player_choice == paper:
    print("Player Win")
elif ai_choice == rock and player_choice == scissors:
    print("AI Win")
elif ai_choice == paper and player_choice == rock:
    print("AI Win")
elif ai_choice == paper and player_choice == scissors:
    print("Player Win")
elif ai_choice == scissors and player_choice == rock:
    print("Player Win")
else:
    print("AI Win")
