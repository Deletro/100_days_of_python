# valami nagyon nem klappol az if statementekkel
import random

a = "Rock"
b = "Paper"
c = "Scissors"

ai_choice_1 = [a, b, c]

print(
    "Welcome to the Rock/Paper/Scissors tournament against the smartest AI in the world"
)
print("Choose your weapon:\n'Rock'\n'Paper'\n'Scissors'")

player_choice = print("Your coice:" + input(""))

ai_choice = random.choice(ai_choice_1)
print("The world smartest AI:" + ai_choice)
if ai_choice == player_choice:
    print("Equal")
elif ai_choice == "Rock" and player_choice == "Paper":
    print("Player Win")
elif ai_choice == "Rock" and player_choice == "Scissors":
    print("AI Win")
elif ai_choice == "Paper" and player_choice == "Rock":
    print("AI Win")
elif ai_choice == "Paper" and player_choice == "Scissors":
    print("Player Win")
elif ai_choice == "Scissors" and player_choice == "Rock":
    print("Player Win")
else:
    print("AI Win")
