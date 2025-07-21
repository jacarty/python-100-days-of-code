"""
Day Two Content - Conditional Statements, Logical Operators, Code Blocks and Scope

Looks like we'll be making Choose Your Own Adventure Game
"""

""" 
If / Else conditional 

if:
    do this
else:
    do this
    """

# Roller coaster - ride if over 1.2M
print("Welcome to the rollercoaster.")
height = int(input("How tall are you in cm?\n"))

# If 120cm or taller you can ride

if height >= 120:
    print("You can ride!")
else:
    print("Sorry, you have to come back when you're taller")

"""
Greater than >
Less than <
Greater than or equal to >=
Less than or equal to <=
Equal to ==
Not equal to !=

Assignment is one =
Check equality is two ==
"""

"""
Modulo Operator --- %

It calculates the remainder

10 % 5 = 0 as it's a clean division
10 % 3 = 1      # 10 ÷ 3 = 3 with 1 remaining
"""

"""
Using Modulo
Check if the input number is Odd or Even
Reminder: Even are always no remainder
Output the words Odd or Even
"""

number = int(input("Please input a number: \n"))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

"""
Nested Else/If Condidition

if:
    if another condition:
        do this
    else:
        do this
else:
    do this
"""

# Roller coaster - ride if over 1.2M
# If over 18 or older it's £12
# If under 18 it's £7
print("Welcome to the rollercoaster.")
height = int(input("How tall are you in cm?\n"))

if height >= 120:
    age = int(input("How old are you?\n"))
    if age <= 18:
        print("You can ride and it will cost £7")
    else:
        print("You can ride and it will cost £12")
else:
    print("Sorry, you have to come back when you're taller")

"""
ELIF
You can add as many elif as needed

if condition1:
    do A
elif condition2:
    do B
else:
    do this
"""

# Roller coaster - ride if over 1.2M
# If over 18 or older it's £12
# If under 12-18 it's £7
# If under 12 it's £5
print("Welcome to the rollercoaster.")
height = int(input("How tall are you in cm?\n"))

if height >= 120:
    age = int(input("How old are you?\n"))
    if age <= 12:
        print("You can ride and it will cost £5")
    if age > 18:
        print("You can ride and it will cost £12")
    else:
        print("You can ride and it will cost £7")
else:
    print("Sorry, you have to come back when you're taller")

"""
BMI Calculator with Interpretations
Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

If the bmi is under 18.5 (not including), print out "underweight"
If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
If the bmi is 25 (including) or over, print out "overweight"

Refer to this graphic for help:
"""

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi >= 25:
    print("overweight")
else:
    print("normal weight")

"""
Multiple IF

if condition1:
    do A
if condition2:
    do B
if condition3:
    do C
"""

# Roller coaster - ride if over 1.2M
# If over 18 or older it's £12
# If under 12-18 it's £7
# If under 12 it's £5
# After working out ticket price we need to check if they want a photo for £3
# And then return final bill

# Start
# |
# v
# [Decision: Height > 120cm?]
# |
# ├─ No → "Can't ride"
# |
# └─ Yes → "Can ride"
# |
# v
# [Decision: Age?]
# |
# ├─ Less than 12 → +$5 ─┐
# |                      |
# ├─ 12-18 → +$7 ────────┤
# |                      |
# └─ 18 or over → +$12 ──┘
# |
# v
# [Decision: Want photos?]
# |
# ├─ No ─────┐
# |          |
# └─ Yes →  +$3
# |
# v
# "The total bill is $x"

# Add 44-55 as a free ride

print("Welcome to the rollercoaster.")
height = int(input("How tall are you in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.\n")
    age = int(input("How old are you?\n"))
    if age <= 12:
        bill = 5
        print("Child tickets are £5.")
    if age <= 18:
        bill = 7
        print("Youth tickets are £7.")
    else:
        bill = 12
        print("Adult tickets are £12.")

    wants_photo = input("Do you want a photo taken? Type y for Yes or n for No.\n")
    if wants_photo == "y":
        # Add £3
        bill += 3
    
    print(f"Your final ticket cost is £{bill}")

else:
    print("Sorry, you have to come back when you're taller")

"""
Pizza Delivery

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza would you like? S, M or L:\n")
pepperoni = input("Would you like pepperone on your pizza? Y or N?\n")
extra_cheese = input("Do you want extra cheese? Y or N?")

# todo: work out how much they need to pay based on their size choice
# todo: work out how much to add to their bill if they want pepperoni
# todo: work out how much to add to their bill if they want cheese
# show final bill

# Small = £15
# Medium = £20
# Large = £25
# S Pepperoni = £2
# M or L Pepperone = £3
# Extra Cheese = £1

"""

# todo: work out how much they need to pay based on their size choice
# todo: work out how much to add to their bill if they want pepperoni
# todo: work out how much to add to their bill if they want cheese
# show final bill

# MINE

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza would you like? S, M or L:\n")
pepperoni = input("Would you like pepperone on your pizza? Y or N?\n")
extra_cheese = input("Do you want extra cheese? Y or N?")
bill = 0

if extra_cheese == "Y":
    bill += 1

if size == "S":
    bill += 15

    if pepperoni == "Y":
        bill += 2
    print(f"Your bill is £{bill}")

elif size == "M":
    bill += 20

    if pepperoni == "Y":
        bill += 2      
    print(f"Your bill is £{bill}")

else:
    bill += 25

    if pepperoni == "Y":
        bill += 2
    
    print(f"Your bill is £{bill}")

# INSTRUCTOR

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza would you like? S, M or L:\n")
pepperoni = input("Would you like pepperoni on your pizza? Y or N?\n")
extra_cheese = input("Do you want extra cheese? Y or N?\n")
bill = 0

# todo: work out how much they need to pay based on their size choice
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs")

# todo: work out how much to add to their bill if they want pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out how much to add to their bill if they want cheese
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is £{bill}")

"""
Multiple conditions in the same line of code

if condition1 & condition2 & condition3:
    do this
else:
    do this

You need to use Logical Operators:
and # All need to be true
or # Both need to be false
not # Reverses the situation; i.e. not True becomes False

A and B
C or D
not E
"""

# Add age 44-55 as a free ride. They still need to pay for the photo.

print("Welcome to the rollercoaster.")
height = int(input("How tall are you in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.\n")
    age = int(input("How old are you?\n"))
    if age <= 12:
        bill = 5
        print("Child tickets are £5.")
    if age <= 18:
        bill = 7
        print("Youth tickets are £7.")
    elif age >= 44 and age <= 55:
    # elif 44 <= age <= 55: This is a simpler way of doing it; but less readable
        print("You ride for free!")
    else:
        bill = 12
        print("Adult tickets are £12.")

    wants_photo = input("Do you want a photo taken? Type y for Yes or n for No.\n")
    if wants_photo == "y":
        # Add £3
        bill += 3
    
    print(f"Your final ticket cost is £{bill}")

else:
    print("Sorry, you have to come back when you're taller")

#
# Treasure Island Game
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
