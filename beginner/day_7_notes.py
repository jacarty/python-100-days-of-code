"""
Day Seven Content - Hangman Game

This will reenforce the concepts covered so far:
-- For/while loops
-- If/Else
-- Lists
-- Strings
-- Range
-- Modules
"""

"""

The hangman logic:

                    ┌─────────────┐
                    │    START    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Generate a │
                    │ random word │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │Generate as  │
                    │many blanks  │
                    │as letters   │
                    │in word      │
                    └──────┬──────┘
                           │
                           ▼
         ┌─────────►┌─────────────┐◄─────────┐
         │          │Ask the user │          │
         │          │to guess a   │          │
         │          │letter       │          │
         │          └──────┬──────┘          │
         │                 │                 │
         │                 ▼                 │
         │          ┌─────────────┐          │
         │          │Is the       │          │
         │          │guessed      │          │
         │          │letter in    │          │
         │          │the word?    │          │
         │          └──┬──────┬───┘          │
         │             │      │              │
         │         Yes │      │ No           │
         │             ▼      ▼              │
         │      ┌──────────┐ ┌──────────┐    │
         │      │Replace   │ │Lose a    │    │
         │      │the blank │ │life      │    │
         │      │with the  │ │          │    │
         │      │letter    │ │          │    │
         │      └────┬─────┘ └────┬─────┘    │
         │           │            │          │
         │           ▼            ▼          │
         │    ┌──────────┐ ┌──────────┐      │
         │    │Are all   │ │Have they │      │
         │    │the blanks│ │run out   │      │
         │    │filled?   │ │of lives? │      │
         │    └──┬───┬───┘ └──┬───┬───┘      │
         │       │   │        │   │          │
         │    No │   │ Yes    │   │ No       │
         └───────┘   │    Yes │   └──────────┘
                     │        │
                     └────┬───┘
                          │
                          ▼
                   ┌─────────────┐
                   │ GAME OVER   │
                   └─────────────┘
"""

"""
STEP 1

word_list = ["aardvark", "baboon", "camel", "dog", "elephant"]

TODO #1 - Randomly choose a word from the list and assign it to a variable called chosen_word. Then print it.

TODO #2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

TODO #3 - Check if the letter that used guessed (guess) is one of the letters in chosen_word. 
       Print "Right" if it is and "Wrong" if it isn'.

"""

import random

word_list = ["aardvark", "baboon", "camel", "dog", "elephant"]

# TODO #1 - Randomly choose a word from the list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO #2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Please choose a letter?\n").lower()

# TODO #3 - Check if the letter that used guessed (guess) is one of the letters in chosen_word. Print "Right" if it is and "Wrong" if it isn'.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

"""
STEP 2

import random

word_list = ["aardvark", "baboon", "camel", "dog", "elephant"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO #1 - Create a placeholder with the same number of blanks as the word. Use the string placeholder

guess = input("Please choose a letter?\n").lower()

# TODO #2 - Create a "display" that puts the guessed letter into the right position

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

"""


import random

word_list = ["aardvark", "baboon", "camel", "dog", "elephant"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO #1 - Create a placeholder with the same number of blanks as the word. Use the string placeholder

## placeholder = "_" * len(chosen_word) This is the most pythonic way to do the loop below

placeholder = ""
for each_character in chosen_word:
    placeholder += "_"
print(placeholder)

guess = input("Please choose a letter?\n").lower()

# TODO #2 - Create a string "display" that puts the guessed letter into the right position or an _ if wrong.

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)

"""
STEP 3

import random

word_list = ["aardvark", "baboon", "camel", "dog", "elephant"]

chosen_word = random.choice(word_list)
print(chosen_word)

## placeholder = "_" * len(chosen_word) This is the most pythonic way to do the loop below

placeholder = ""
for each_character in chosen_word:
    placeholder += "_"
print(placeholder)

# TODO #1 - Use a while loop let the user guess again

guess = input("Please choose a letter?\n").lower()

# TODO #2 - Change the for loop so that you keep the previous correct answer

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)
"""

import random

# word list to select answer from
word_list = ["aardvark", "baboon", "camel", "dog", "elephant"]

# use random to pick a random word from the list
chosen_word = random.choice(word_list)
print(chosen_word)

## placeholder = "_" * len(chosen_word) <---- This is the most pythonic way to do the loop below

# migrate the string to a dictionary and put in _ for each character
word_status = []
for each_character in chosen_word:
    word_status.append("_")

# need a variable to use in while loop
game_over = False

# loop while game over is False
while not game_over:
    # get input and set to lower case
    guess = input("Please choose a letter?\n").lower()
    
    # use enumerate to returns index, and character
    # get the two variables for the loop
    for index, character in enumerate(chosen_word):
        if character == guess:
            word_status[index] = guess
    
    # return current game_status to the user
    print(word_status)

    # loop until there are no _ in word_status 
    if "_" not in word_status:
        print("Congratulations - you win!")
        game_over = True


##
## Instructor loop
## 
correct_letters = []
# loop while game over is False
while not game_over:
    # get input and set to lower case
    guess = input("Please choose a letter?\n").lower()
    
    # display and add to the list
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        # also, checking if there is a letter that doesn't match guess
        # but is in the list of correct letters
        # if yes, display that too
        elif letter in correct_letters:
            display += letter
        #otherwise show _
        else:
            display += "_"
    # return current game_status to the user
    print(word_status)

    # loop until there are no _ in word_status 
    if "_" not in word_status:
        print("Congratulations - you win!")
        game_over = True


"""
STEP 4

# TODO #1 - Create a variable called lives to track the number of lives left. Start at 6.

# TODO #2 - If guess is not a character in chosen_word reduce lives by 1. At 0, return "Game Over".

# TODO #3 - Print the ascii art that corresponds to the lives remaining.
"""

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random

word_list = ["aardvark", "baboon", "camel", "dog", "elephant"]

# use random to pick a random word from the list
chosen_word = random.choice(word_list)
print(chosen_word)

## placeholder = "_" * len(chosen_word) <---- This is the most pythonic way to do the loop below

# migrate the string to a dictionary and put in _ for each character
word_status = []
for each_character in chosen_word:
    word_status.append("_")

# need a variable to use in while loop
game_over = False
# add maximum number of lives to track
lives = 6

# loop while game over is False
while not game_over:
    # get input and set to lower case
    guess = input("Please choose a letter?\n").lower()
    
    if guess in chosen_word:
        # use enumerate to returns index, and character
        # get the two variables for the loop
        for index, character in enumerate(chosen_word):
            if character == guess:
                word_status[index] = guess
        # return current game_status to the user
        # lookup the ascii stage in the list based on current lives
        print(stages[lives])
        print(''.join(word_status))
    else:
        lives -= 1
        print("Wrong guess!")
        # return current game_status to the user
        print(stages[lives])
        print(''.join(word_status))
    
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


"""
STEP 4

# TODO #1 - Update the word list to use the word_list from hangman_words.py
done

# TODO #2 - Update the code to use stages from hangman_art.py
done

# TODO #3 - Import the logo from hangman_art.py and print at start of game
done

# TODO #4 - If the user reguesses a letter print to let them know. They don't lose a life.
done

# TODO #5 - If the letter is not in the word print and let them know.
done 
"""

import random
import beginner.day_7_hangman_art as day_7_hangman_art
import beginner.day_7_hangman_words as day_7_hangman_words

print(day_7_hangman_art.logo)

# old word list for building
# word_list = ["aardvark", "baboon", "camel", "dog", "elephant"]

# select work from word list
# chosen_word = random.choice(word_list)
# use random to pick a random word from the list that is imported from hangman_words
chosen_word = random.choice(day_7_hangman_words.word_list)
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
        print(day_7_hangman_art.stages[lives])
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
        print(day_7_hangman_art.stages[lives])
        print(f"Correct, {guess} is in the word.")
        print(''.join(word_status))
    # reduce lives if not in word
    else:
        lives -= 1
        # return current game_status to the user
        print(day_7_hangman_art.stages[lives])
        print(f"You guessed incorrectly, {guess} is not in the word.")
        print(''.join(word_status))
    
    # end game if lives run out
    if lives == 0:
        print(day_7_hangman_art.stages[lives])
        print(''.join(word_status))
        print("GAME OVER")
        print(f"The word was: {chosen_word}")
        game_over = True
    # loop until there are no _ in word_status 
    elif "_" not in word_status:
        print(day_7_hangman_art.stages[lives])
        print(''.join(word_status))
        print("Congratulations - you win!")
        game_over = True
