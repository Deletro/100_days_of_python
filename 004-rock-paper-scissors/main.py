import random

a = "Rock"
b = "Paper"
c = "Scissors"

ai_choice_1 = [a, b, c]

print(
    "Welcome to the Rock/Paper/Scissors tournament against the smartest AI in the world"
)
print("Choose your weapon:\n'Rock'\n'Paper'\n'Scissors'")

player_choice = input("")
print("Your coice:" + player_choice)
ai_choice = random.choice(ai_choice_1)
print("The world smartest AI:" + ai_choice)

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

if ai_choice == player_choice:
    if ai_choice == a:
        print(rock, rock)
    elif ai_choice == b:
        print(paper, paper)
    elif ai_choice == c:
        print(scissors, scissors)
    print("Draw")
elif ai_choice == "Rock" and player_choice == "Paper":
    print(paper, rock)
    print("Player Win")
elif ai_choice == "Rock" and player_choice == "Scissors":
    print(scissors, rock)
    print("AI Win")
elif ai_choice == "Paper" and player_choice == "Rock":
    print(rock, paper)
    print("AI Win")
elif ai_choice == "Paper" and player_choice == "Scissors":
    print(scissors, paper)
    print("Player Win")
elif ai_choice == "Scissors" and player_choice == "Rock":
    print(rock, scissors)
    print("Player Win")
else:
    print(paper, scissors)
    print("AI Win")
