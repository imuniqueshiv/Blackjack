import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has blackjack!"
    elif u_score == 0:
        return "You win! You have blackjack!"
    elif u_score > 21:
        return "You Lose!"
    elif c_score > 21:
        return "Opponent went over, you win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print(logo)

    user_cards = []
    computers_cards = []
    user_score = -1
    computer_score = -1

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computers_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computers_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computers_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal_card())
        computer_score = calculate_score(computers_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computers_cards}, Computer score: {computer_score}")

    print(compare(user_score, computer_score))

# Main loop to start the game
stop = True
while stop:
    game = input("Do you want to play a game of blackjack? Type 'y' for yes or 'n' for no: ").lower()
    if game == "y":
        print("\n" * 20)  # Clears the console screen
        play_game()
    else:
        stop = False
