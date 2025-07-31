from day_12_art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
     while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")

def guess_game():
    random_number = random.randint(1, 100)
    # print(random_number)

    # call the set difficulty function to get number of guesses
    number_of_guesses = set_difficulty()

    while number_of_guesses > 0:
        print(f"You have {number_of_guesses} attempts to guess the number.")
        guess = int(input("Make a guess': "))
        if guess > random_number:
            print("Too high.\nGuess Again.")
            number_of_guesses -= 1
        elif guess < random_number:
            print("Too Low.\nGuess Again.")
            number_of_guesses -= 1
        elif guess == random_number:
            print("Congratulations. You were correct!")
            return

    print(f"You've run out of guesses, you Lose. The number was: {random_number}")

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
guess_game()
