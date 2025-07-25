# This is the game logic that needs to be coded
#
#
#                     ┌─────────────────────────────────────┐
#                     │   Welcome to Treasure Island.       │
#                     │Your mission is to find the treasure.│
#                     └─────────────────┬───────────────────┘
#                                       │
#                                       ▼
#                               ┌───────────────┐
#                               │ left or right?│
#                               └───────┬───────┘
#                                       │
#                     ┌─────────────────┴─────────────────┐
#                     │                                   │
#                     ▼                                   ▼
#                   Left                         Right or anything else
#                     │                                   │
#                     ▼                                   ▼
#             ┌───────────────┐                   ┌──────────────────┐
#             │ swim or wait? │                   │ Fall into a hole.│
#             └───────┬───────┘                   │   Game Over.     │
#                     │                           └──────────────────┘
#     ┌───────────────┴───────────────┐
#     │                               │
#     ▼                               ▼
#   Wait                    Swim or anything else
#     │                               │
#     ▼                               ▼
# ┌─────────────┐              ┌──────────────────┐
# │Which door?  │              │Attacked by trout.│
# └──────┬──────┘              │   Game Over.     │
#        │                     └──────────────────┘
#        │
# ┌──────┼──────┬─────────────────┐
# │      │      │                 │
# ▼      ▼      ▼                 ▼
# Red  Yellow Blue         Anything else
# │      │      │                 │
# ▼      ▼      ▼                 ▼
# ┌──────────────┐ ┌─────────┐ ┌─────────────────┐ ┌────────────┐
# │Burned by fire│ │You Win! │ │Eaten by beasts. │ │ Game Over. │
# │ Game Over.   │ └─────────┘ │  Game Over.     │ └────────────┘
# └──────────────┘             └─────────────────┘

# https://ascii.co.uk/art/treasure
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************

Welcome to the treasure hunt!
Your mission is to find the treasure...
''')

# Left or Right
# Using '' to surround text and escaping the ' with a backslack \
print('You\'re at a crossroads.')
turn = input('Do you want to turn "Left" or "Right"?\n').lower # All lowercase. Using '' as want to use "" around words
if not turn == "left":
    print("You fell into a hole. GAME OVER.")
    quit()

# Swim or Wait
print("You've come to a moat that surrounds an Island.")
swim_or_wait = input('Do you want to "Swim" or "Wait" for a boat?\n').lower
if not swim_or_wait == "swim":
    print("You were attacked by a trout. GAME OVER")
    quit()

# Which Door to Enter?
door = input('Which door do you want to open? "Red", "Yellow" or "Blue"?\n').lower
if door == "red":
    print("You've been burned by Fire. GAME OVER.")
    quit()
elif door == "yellow":
    print("Congratulations - you win!")
    quit()
elif door == "blue":
    print("You've been eaten by Beasts. GAME OVER")
    quit()
else:
    print("Unlucky. GAME OVER.")


#
#
# INSTRUCTOR Version
#
#
print('You\'re at a crossroads.')
turn = input('Do you want to turn "Left" or "Right"?\n').lower 
if turn == "left":
    print("You've come to a moat that surrounds an Island.")
    swim_or_wait = input('Do you want to "Swim" or "Wait" for a boat?\n').lower
    if swim_or_wait == "swim":
        print("You've arrived on the island and approach the castle.")
        door = input('Which door do you want to open? "Red", "Yellow" or "Blue"?\n').lower
        if door == "red":
            print("You've been burned by Fire. GAME OVER.")
        elif door == "yellow":
            print("Congratulations - you've found the treasure and win!")
        elif door == "blue":
            print("You've been eaten by Beasts. GAME OVER")
    else:
        print("You were attacked by a trout. GAME OVER")
else:
    print("You fell into a hole. GAME OVER.")
