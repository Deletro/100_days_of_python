import random

print("Welcome to the Number Guessing Game!")

chosen_number = random.randint(1, 100)
print(f"(The number: {chosen_number})")


def evaluater(num1, num2=chosen_number):  # kiértékelő function
    if num1 > num2:
        print("Too high")
    elif num1 < num2:
        print("Too low")


def life_check(life):
    if life == 0:
        print("Game Over")
    else:
        print(f"You have {life} life")


def play_easy():
    life = 10

    while life != 0:
        life_check(life)
        guess = int(input("Guess a number: "))

        if guess == chosen_number:
            print("You got it")
            break
        elif guess != chosen_number and life == 1:
            print("You run out of guesses, you lose.")
            break
        elif guess != chosen_number:
            evaluater(guess, chosen_number)
            life -= 1


def play_hard():
    life = 5

    while life != 0:
        life_check(life)
        guess = int(input("Guess a number: "))

        if guess == chosen_number:
            print("You got it")
            break
        elif guess != chosen_number and life == 1:
            print("You run out of guesses, you lose.")
            break
        elif guess != chosen_number:
            evaluater(guess, chosen_number)
            life -= 1


difficulty = input("Choose a difficulty: 'easy' or 'hard': ")

if difficulty == "easy":
    play_easy()
elif difficulty == "hard":
    play_hard()
else:
    print("I dont found that kind of difficulty")
