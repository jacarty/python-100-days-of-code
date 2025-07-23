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

"""STEP 1

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

