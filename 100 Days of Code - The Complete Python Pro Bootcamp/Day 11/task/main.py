import random

from art import logo

def sum_cards(player_cards):
    player_cards_copy = player_cards.copy()
    player_cards_sum = sum(player_cards_copy)
    if player_cards_sum > 21 and 11 in player_cards_copy:
        player_cards_copy[player_cards_copy.index(11)] = 1
        player_cards_sum = sum_cards(player_cards_copy)
    return player_cards_sum

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_game():
    wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if wanna_play == 'y':
        print(logo)

        player = []
        computer = []

        player_score = 0
        computer_score = 0

        # Computer hand. Keep play while sum < 18
        while computer_score < 17:
            computer.append(random.choice(cards))
            computer_score = sum_cards(computer)

        # First handom card.
        player.append(random.choice(cards))
        player.append(random.choice(cards))
        keep_playing = True

        while keep_playing:
            player_score = sum_cards(player)
            print(f"Your cards: {player}, current score: {player_score}")
            print(f"Computer's first card: {computer[0]}")

            if player_score <= 21:
                call_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if call_card == 'y':
                    player.append(random.choice(cards))
                    keep_playing = True
                else:
                    keep_playing = False
            else:
                keep_playing = False

        print(f"Your final hand: {player}, final score: {player_score}")
        print(f"Computer final hand: {computer}, final score: {computer_score}")
        if player_score > 21:
            print("You lose!")
        elif computer_score > 21:
            print("You win!")
        elif player_score == computer_score:
            print("You draw!")
        elif computer_score < player_score <= 21:
            print("You win!")
        else:
            print("You lose!")
        play_game()

play_game()