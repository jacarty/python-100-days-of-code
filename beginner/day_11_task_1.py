# ### Our Blackjack Game House Rules

# - The deck is unlimited in size. 
# - There are no jokers. 
# - The Jack/Queen/King all count as 10.
# - The Ace can count as 11 or 1.
# - Use the following list as the deck of cards:

# - The cards in the list have equal probability of being drawn.
# - Cards are not removed from the deck as they are drawn.
# - The computer is the dealer.

import day_11_art
import random
import os

def draw_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

your_cards = []
computer_cards = []

def blackjack():
    """Play Blackjack"""
    print(day_11_art.logo)

    # draw first card
    for cards in [your_cards, computer_cards]:
        cards.append(draw_card())
    
    # draw second card
    for cards in [your_cards, computer_cards]:
        new_card = draw_card()
        if sum(cards) + new_card > 21 and new_card == 11:
            new_card = 1
        cards.append(new_card)

    print(f"Your cards: {your_cards}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    # human cards
    keep_human_drawing_cards = True
    while keep_human_drawing_cards:
        another_card = input("Type 'y' for another card, type 'n' to pass.\n").lower()

        if another_card == "y":
            new_card = draw_card()

            if sum(your_cards) + new_card > 21 and new_card == 11:
                new_card = 1
            your_cards.append(new_card)

            your_total = sum(your_cards)
            print(f"Your cards: {your_cards} = {your_total}")
            
            if sum(your_cards) > 21:
                print("YOU BUST - GAME OVER")
                quit()

        if another_card == "n":
            your_total = sum(your_cards)
            print(f"\nYour final hand: {your_cards} = Total {your_total}\n")
            keep_human_drawing_cards = False

    # computer cards
    keep_computer_drawing_cards = True
    while keep_computer_drawing_cards:

        if sum(computer_cards) < 17:
            new_card = draw_card()
            if sum(computer_cards)  + new_card > 21 and new_card == 11:
                new_card = 1
            computer_cards.append(new_card)
            
            computer_total = sum(computer_cards)
            print(f"Computer cards: {computer_cards} = {computer_total}")

            if sum(computer_cards) > 21:
                print("Computer BUST - You Win!")
                quit()

        if sum(computer_cards) == 17:
            computer_total = sum(computer_cards)
            print(f"Computer's final hand: {computer_cards} = Total {computer_total}\n")
            keep_computer_drawing_cards = False

        if 18 <= sum(computer_cards) <= 21:
            computer_total = sum(computer_cards)
            print(f"Computer's final hand: {computer_cards} = Total {computer_total}\n")
            keep_computer_drawing_cards = False

    # calculate winner
    if your_total == computer_total:
        print("It's a draw!\n")
    elif your_total > computer_total:
        print("You Win!\n")
    else:
        print("Computer Wins!\n")

    keep_playing_blackjack = input("Do you want to play again. Type 'y' or 'n'.").lower()
    if keep_playing_blackjack == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        your_cards.clear()
        computer_cards.clear()
        blackjack()
    else:
        quit()

blackjack()

