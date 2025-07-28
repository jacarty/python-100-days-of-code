import random
from day_7_hangman_art import logo, stages
# import day_7_hangman_art
from day_7_hangman_words import word_list
# import day_7_hangman_words

print(logo)

# old word list for building
# word_list = ["aardvark", "baboon", "camel", "dog", "elephant"]

# select work from word list
# chosen_word = random.choice(word_list)
# use random to pick a random word from the list that is imported from hangman_words
chosen_word = random.choice(word_list)
# print(chosen_word)

## placeholder = "_" * len(chosen_word) <---- This is the most pythonic way to do the loop below

# migrate the string to a dictionary and put in _ for each character
word_status = []
for each_character in chosen_word:
    word_status.append("_")

# need a variable to use in while loop
game_over = False
# track guessed letters
guessed_letters = []
# add maximum number of lives to track
lives = 6

# loop while game over is False
while not game_over:
    # get input and set to lower case
    guess = input("Please choose a letter?\n").lower()

    # checks if they already guessed that letter
    if guess in guessed_letters:
        # return current game_status to the user
        print(stages[lives])
        print(f"You already guessed {guess} - try again :)")
        print(''.join(word_status))
        continue

    # add guess to guessed letters for tracking
    guessed_letters.append(guess)
    # print(guessed_letters)

    # add higher if statement to check it letter in chosed word
    if guess in chosen_word:
        # use enumerate to returns index, and character
        # get the two variables for the loop
        for index, character in enumerate(chosen_word):
            if character == guess:
                word_status[index] = guess
        # return current game_status to the user
        # lookup the ascii stage in the list based on current lives
        print(stages[lives])
        print(f"Correct, {guess} is in the word.")
        print(''.join(word_status))
    # reduce lives if not in word
    else:
        lives -= 1
        # return current game_status to the user
        print(stages[lives])
        print(f"You guessed incorrectly, {guess} is not in the word.")
        print(''.join(word_status))
    
    # end game if lives run out
    if lives == 0:
        print(stages[lives])
        print(''.join(word_status))
        print("GAME OVER")
        print(f"The word was: {chosen_word}")
        game_over = True
    # loop until there are no _ in word_status 
    elif "_" not in word_status:
        print(stages[lives])
        print(''.join(word_status))
        print("Congratulations - you win!")
        game_over = True
