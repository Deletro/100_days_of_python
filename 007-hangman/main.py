import random

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
print(chosen_word)


display = []
for i in chosen_word:
    display.append("_")
underscore = "_"
life = 5

while underscore in display:
    print(display)
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        life -= 1
        print(f"You lose a life, current life is {life}")
        if life == 0:
            print("Game Over")
            break

if life > 0:
    print(display)
    print("Victory")
