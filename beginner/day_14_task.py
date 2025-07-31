from day_14_art import logo, vs
from day_14_game_data import data
import random

COMPARISON = {}

def random_celeb_generator(letter):
    """Get a random celebrity from the dictionary and add to the list."""
    celeb = random.choice(data)
    celeb_name = celeb["name"]
    celeb_description = celeb["description"]
    celeb_followers = celeb["follower_count"]
    COMPARISON[letter] = celeb_followers
    return(f"Compare {letter}: {celeb_name}, {celeb_description}")

def get_user_guess():
    """Get user input for which celebrity they think has the most followers."""
    while True:
        guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()
        if guess == "A" or guess == "B":
            return guess
        else:
            print("Invalid input. Please try again.")

def check_guess(u_guess):
    """Find the winning celebrity and return the results."""
    # print(COMPARISON)
    winning_celeb = max(COMPARISON, key=COMPARISON.get)
    losing_celeb = min(COMPARISON, key=COMPARISON.get)
    comparison_result = COMPARISON
    # print(comparison_result)
    # print(losing_celeb)
    # print(winning_celeb)
    if u_guess == winning_celeb:
        return True, losing_celeb, comparison_result
    else:
        return False, losing_celeb, comparison_result

def game():
    
    score = 0
    verify_guess = True

    A = random_celeb_generator("A")
    B = random_celeb_generator("B")

    while verify_guess is True:

        print(logo)
        if score != 0 and previous_comparison:
            print(f"✓ Correct! A = {previous_comparison["A"]} B = {previous_comparison["B"]}")
            print(f"You're right! Current score is: {score}\n")
        print(A)
        print(vs)
        print(B)

        guess = get_user_guess()
        result, loser, comparison = check_guess(guess)
        # print(result)
        # print(loser)
        if result == True:
            score += 1
            
            # copy the old score so we can show result
            # delete losing score
            previous_comparison = comparison.copy()
            del COMPARISON[loser]

            # add a new celebrity to replace loser
            if loser == "A":
                A = random_celeb_generator("A")
            elif loser == "B":
                B = random_celeb_generator("B")

        # end game when losing
        if result == False:
            print(f"\n✗ Sorry, that's wrong! A = {comparison["A"]} B = {comparison["B"]}")
            print(f"Final score: {score}\n")
            break

game()
