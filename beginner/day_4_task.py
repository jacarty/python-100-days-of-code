"""
Rock, Paper and Scissors

Rock wins against scissors
Scissors wins against paper
Paper wins against rock
"""

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)    
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random

options = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_input < 0 or user_input > 2:
    print("Please try again.")
    quit()

human_selection = options[user_input]
computer_choice = options[random.randint(0, 2)]

print("You chose" + human_selection)
print("The computer chose" + computer_choice)

if human_selection == rock:
    if computer_choice == rock:
        print("It's a Draw")
    elif computer_choice == paper:
        print("You Lose")
    else:
        print("You Win")
elif human_selection == paper:
    if computer_choice == paper:
        print("It's a Draw")
    elif computer_choice == scissors:
        print("You Lose")
    else:
        print("You Win")
elif human_selection == scissors:
    if computer_choice == scissors:
        print("It's a Draw")
    elif computer_choice == rock:
        print("You Lose")
    else:
        print("You Win")
else:
    print("Please try again.")
