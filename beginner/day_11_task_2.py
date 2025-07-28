# ### Our Blackjack Game House Rules

# - The deck is unlimited in size. 
# - There are no jokers. 
# - The Jack/Queen/King all count as 10.
# - The Ace can count as 11 or 1.
# - Use the following list as the deck of cards:

# - The cards in the list have equal probability of being drawn.
# - Cards are not removed from the deck as they are drawn.
# - The computer is the dealer.

"""Rewrote my original after watching some lesson tips."""

import day_11_art
import random
import os

def draw_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate(cards):
    """Calculates scores."""
    if sum(cards) == 21 and len(cards) == 2:
        return -1
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

def compare(y_score, c_score):
    """This calcuates the winner by comparing scores."""
    if y_score == c_score:
        return "It's a draw."
    elif c_score == -1:
        return "Blackjack - you lose!"
    elif y_score == -1:
        return "Blackjack - you win!"
    elif c_score > 21 and y_score > 21:
        return "You both bust!"
    elif c_score > 21:
        return "Computer busts - you win!" 
    elif y_score > 21:
        return "You bust!" 
    elif c_score > y_score:
        return "You Lose!"
    else:
        return "You win!"

def blackjack():
    """Play Blackjack"""

    your_cards = []
    computer_cards = []

    print(day_11_art.logo)

    # draw cards
    for X in range(2):
        your_cards.append(draw_card())
        computer_cards.append(draw_card())

    your_score = calculate(your_cards)
    computer_score = calculate(computer_cards)

    print(f"Your cards: {your_cards}. Total is {your_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    # human cards
    human_keep_drawing_cards = True
    while human_keep_drawing_cards:

        another_card = input("Type 'y' for another card, type 'n' to pass.\n").lower()

        if another_card == "y":
            your_cards.append(draw_card())
            your_score = calculate(your_cards)
            print(f"Your cards: {your_cards} = {your_score}")
            
            if calculate(your_cards) > 21:
                human_keep_drawing_cards = False

        if another_card == "n":
            your_score = calculate(your_cards)
            human_keep_drawing_cards = False

    # computer cards
    computer_keep_drawing_cards = True
    while computer_keep_drawing_cards:

        # Twist below 17
        if calculate(computer_cards) < 17:
            computer_cards.append(draw_card())
            computer_score = calculate(computer_cards)
        
        else:
            computer_keep_drawing_cards = False
        
    # calculate winner
    print(f"\nYour final hand: {your_cards} = Total {your_score}")
    print(f"Computer's final hand: {computer_cards} = Total {computer_score}\n")
    winner = compare(your_score, computer_score)
    print(f"{winner}\n")

    # check if the player wants to keep going
    keep_playing_blackjack = input("Do you want to play again. Type 'y' or 'n'.").lower()
    if keep_playing_blackjack == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        your_cards.clear()
        computer_cards.clear()
        blackjack()
    else:
        quit()

blackjack()
