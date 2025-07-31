from day_14_art import logo, vs
from day_14_game_data import data
import random

# print(logo)

# Compare A: data "name", data "description"

# print(vs)

# Compare B: data "name", data "description"

COMPARISON = {}

def random_celeb(letter):
    celeb = random.choice(data)
    celeb_name = celeb["name"]
    celeb_description = celeb["description"]
    celeb_followers = celeb["follower_count"]
    COMPARISON[letter] = celeb_followers
    return(f"Compare {letter}: {celeb_name}, {celeb_description}")

def get_user_guess():
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ")
        if guess == "A" or guess == "B":
            print(guess)
            return guess
        else:
            print("Invalid input. Please try again.")

def compare_followers(u_guess):
    print(u_guess)
    print(COMPARISON)
    winning_celeb = max(COMPARISON, key=COMPARISON.get)
    print(winning_celeb)
    return(winning_celeb)
    if u_guess == winning_celeb:
        print("correct")
    

def game():

    celeb_A = random_celeb("A")
    celeb_B = random_celeb("B")

    #print(logo)
    #print(celeb_A)
    #print(vs)
    #print(celeb_B)

    get_user_guess()
    print(get_user_guess)
    # compare_followers(get_user_guess)

game()