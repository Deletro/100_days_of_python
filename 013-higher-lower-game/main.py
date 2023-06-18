from art import logo, vs
from game_data import data
import random


def checker(compare_a_followers, compare_b_followers):
    if compare_a_followers > compare_b_followers:
        return "A"
    else:
        return "B"


def play():
    compare_b = random.choice(data)
    points = 0

    while True:
        print(logo)
        compare_a = compare_b
        compare_b = random.choice(data)
        while compare_a == compare_b:
            compare_b = random.choice(data)

        compare_a_followers = compare_a["follower_count"]
        compare_b_followers = compare_b["follower_count"]

        print(
            f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}"
        )
        print(f"hidden score: {compare_a_followers}")
        print(vs)
        print(
            f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}"
        )
        print(f"hidden score: {compare_b_followers}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        winner = checker(compare_a_followers, compare_b_followers)

        if guess == winner:
            points += 1
            print(f"You are right! Current score {points}.")
        else:
            print(f"Sorry, that's wrong, Final score: {points}.")
            break


play()
