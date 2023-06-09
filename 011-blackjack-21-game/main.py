import random
import os


def clear():  # Cross-platform clear screen
    os.system("cls" if os.name == "nt" else "clear")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(card_list):
    score = sum(card_list)
    if score == 21 and len(card_list) == 2:
        # Blackjack
        return 0

    if score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        score = sum(card_list)

    return score


def compare(score1, score2):
    if score1 == score2:
        return "Draw"
    elif score2 == 0 or score1 > 21:
        return "Computer Win"
    elif score1 == 0 or score2 > 21:
        return "Player Win"
    elif score1 > score2:
        return "Player Win"
    else:
        return "Computer Win"


def play_blackjack(user_cards, computer_cards):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    while True:
        if computer_score == 0 or user_score > 21:
            return user_score, computer_score
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        draw_more = input("Do you want to draw another card?:\n'y' or 'n'\n")
        if draw_more == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
        else:
            # computer turn
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
            return user_score, computer_score


while True:
    play_again = input("Do you want to play BlackJackGame? 'y' or 'n': ")
    clear()
    if play_again != "y":
        break

    user_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())

    computer_cards = []
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    user_score, computer_score = play_blackjack(user_cards, computer_cards)

    winner = compare(user_score, computer_score)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's cards: {computer_cards}, current score: {computer_score}")
    print(winner)
