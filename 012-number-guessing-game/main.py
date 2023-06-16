import random


EASY_LIFE_NUM = 10
HARD_LIFE_NUM = 5

print("Welcome to the Number Guessing Game!")

chosen_number = random.randint(1, 100)
print(f"(The number: {chosen_number})")


def evaluater(num1, num2=chosen_number):  # kiértékelő function
    if num1 > num2:
        print("Too high")
    elif num1 < num2:
        print("Too low")


def play(life):
    while life != 0:
        print(f"You have {life} life")
        guess = int(input("Guess a number: "))

        if guess == chosen_number:
            print("You got it")
            break
        elif life == 1:
            print("You run out of guesses, you lose.")
            print(f"(The number was: {chosen_number})")
            break
        else:
            evaluater(guess, chosen_number)
            life -= 1


difficulty = input("Choose a difficulty: 'easy' or 'hard': ")

if difficulty == "easy":
    play(EASY_LIFE_NUM)
elif difficulty == "hard":
    play(HARD_LIFE_NUM)
else:
    print("I dont found that kind of difficulty")
