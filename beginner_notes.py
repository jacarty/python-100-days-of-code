"""
Consolidated Beginner Notes from 100 Days of Code Python Bootcamp
Days 1-13 (excluding Days 11 and 14-15 which don't have notes files)
"""

# ==========================================
# DAY 1 - String Manipulation and Variables
# ==========================================

"""
Day One Content - String Manipulation and Variables

Looks like we'll be making a Band Generator for the Task
"""

# Example print statements
print("Hello World")

# Example multi-line print statemeent
print(""" 
      this is a long line
      split across two using triple quotation marks """)

"""
Task 1:
Write a program that uses print statements to print the following recipe into the Output console. 
The text to print is already there, you just need to make it into code. 
Your code should print all five lines exactly the same as the example output below. 
Make sure that you don't change any of these existing text as everything, punctuation and casing all need to match!

"1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl."
"2. Knead the dough for 10 minutes."
"3. Add 3g of Salt."
"4. Leave to rise for 2 hours."
"5. Bake at 200 degrees C for 30 minutes."
"""

# Solution
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# Split to new Line in a single print statement with \n
print("Hello world!\nHello world!")

# Contatenate Strings
print("Hello" + "James")

# Contatenate Strings that are readable
print("Hello" + " " + "James")

"""
Debugging Practice
Look at the code in the code editor. There are errors on all 5 lines of code. Fix the code so that it runs without errors.
Try to run the code and debug each line using the error messages and feedback.

# Fix the code below 👇

print(Notes from Day 1")
 print("The print statement is used to output strings")
print("Strings are strings of characters"
priint("String Concatenation is done with the + sign")
print(("New lines can be created with a \ and the letter n")
"""

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")

# Print can't take input
print("What is your name?")

# Input example
input("What is your name?")

# Output with input
print("Hello " + input("What is your name?"))

# Output with input and concatenation
print("Hello " + input("What is your name?") + "!")

# Variable example - so the input can be referenced later on
name = input("What is your name?")
print(name)

"""
Variables can be mutable or immutable. This example is mutable 
Python has both mutable and immutable collection data types. 
Strings and tuples are immutable, while lists, dictionaries, and sets are mutable. 
This distinction is crucial for you as a Python developer
"""
# The variable is mutable and can be overwritten
name = "Jack"
print(name)
name = "James"
print(name)

# Example to find the length of a string
name = "Jack"
print(name) # prints the name variable
print(len(name)) # prints the lenght of the variable

# Take user input and return the length of the variable
name = input("What is your name?")
print(name)
print(len(name))

# Same as above in one line
print(len(input("What is your name?")))

# Same but using multiple variables to split it out and make it more readable
username = input("What is your name?")
length = len(username)
print(length)

"""
Variables

We have 2 variables glass1 and glass2. 
glass1 contains milk and glass2 contains juice. 
Write 3 lines of code to switch the contents of the variables. 
You are not allowed to type the words "milk" or "juice". 
You are only allowed to use variables to solve this exercise. 

glass1 = "milk"
glass2 = "juice"
"""

glass1 = "milk"
glass2 = "juice"

print("Original glass 1 = " + glass1)
print("Original glass 2 = " + glass2)

temp = glass2
glass2 = glass1
glass1 = temp

print("New glass 1 = " + glass1)
print("New glass 2 = " + glass2)

# Swap back using Tuple
glass1, glass2 = glass2, glass1
print("Swap back with Tuple. Glass 1 = " + glass1)
print("Swap back with Tuple. Glass 2 = " + glass2)


"""
Variable required Rules:

Must start with a letter (a-z, A-Z) or underscore (_)
Can contain letters, numbers (0-9), and underscores after the first character
Cannot start with a number
Cannot contain spaces or special characters like @, #, $, %, etc.
Cannot be Python keywords (like if, for, class, def, etc.)

Case Sensitivity:

Variable names are case-sensitive (myVar and myvar are different variables)

Convention Guidelines (PEP 8):

Use lowercase with underscores for regular variables (my_variable)
Use UPPERCASE with underscores for constants (MAX_SIZE)
Use leading underscore for internal use (_private_var)
Avoid single character names except for short loop counters
Choose descriptive names that indicate the variable's purpose
"""

# ==========================================
# DAY 2 - Data Types, Numbers, Operations, Type Conversations, f-Strings
# ==========================================

"""
Day Two Content - Data Types, Numbers, Operations, Type Conversations, f-Strings

Looks like we'll be making a tip calculator for the Task
"""

# Reminder - getting length of a string
print((len("hello")))

"""
This would error as it's not a string
print((len(12345)))

Data Types - String, Interger, Float, Boolean
"""

# Subscripting
# We always start counting at zero 
# This returns the character in specified position, e.g. (H) or (o)
print("Hello"[0])
print("Hello"[4])

# Negative numbers start at the end and returns (o) or (e)
print("Hello"[-1])
print("Hello"[-4])

""" 
Integer is a whole number
"""

# This will do addition (579)
print(123 + 456)

# Large Integerr - underscores are like commas in large numbers and just for readability
print(123_456_789)

# Floats = Floating Point Number
print(3.14159)

# Boolean - true or false
print(True)
print(False)

# Type checking - Type will return the data type 
print(type("Hello"))
print(type(1234))
print(type(3.222))
print(type(False))

# You can convert between types
int()
str()
float()
bool()

"""
Fix this
print("Number of letters in your name: " + len(input("Enter your name")))
"""
# error 
# TypeError: can only concatenate str (not "int") to str

# Convert the length into a string so that it can be concatenated
print("Number of letters in your name: " + str(len(input("Enter your name"))))

# or 

name_of_user = input("Enter your name: \n")
length_of_name = len(name_of_user)

print(type("Number of letters in your name: ")) # str
print(type(length_of_name)) # int

print("Number of letters in your name: " + str(length_of_name))

# Examples of concatendated conversions
print("My age is: " + str(21))

# Integers
print(123 + 123)
print(10 - 3)
print(3 * 2)
print(6 / 3) # always returns a float (implicit typecasting)
print(6 // 3) # will return an integer but simply removes the decimal point and trailing numbers; effectively rounds
print(2 ** 3) # raises to the power

"""
PEMDAS
Parentheses, Exponents, Multiplication/Division, Addition, Subtraction
Also factors left to right
"""

# Returns 7.0
print(3 * 3 + 3 / 3 - 3)

# Returns 3.0
print(3 * (3 + 3) / 3 - 3)


"""
BMI Calculator

The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. 
This is the formula used to calculate it:

bmi is equal to the person's weight divided by the person's height squared.

Convert this sentence into code on line 6. 

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi =

print(bmi)

"""

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print(bmi) # returns (30.85399449035813)
print(int(bmi)) # returns a floor (30)
print(round(bmi))
print(round(bmi,2)) # rounds up to (30.85); rounds to specified digits

"""
# Assignment Operator
+=
-+
*=
/+
"""

score = 0
score = score + 1 # one way
score += 1 # assignment way

"""
f_Strings
"""

print("Your score is " + score) # errors due to mix of str and int
print("Your score is " + str(score)) # converted but can be painful to have to mix all these at scale


score = 0
height= 1.84
is_winning = True

print(f"Your score is {score}, your height is {height}. You are winning is {is_winning}.") # f-String
# ==========================================
# DAY 3 - Conditional Statements, Logical Operators, Code Blocks and Scope
# ==========================================

"""
Day Three Content - Conditional Statements, Logical Operators, Code Blocks and Scope

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

# ==========================================
# DAY 4 - Randomisation and Python Lists
# ==========================================

"""
Day Four Content - Randomisation and Python Lists

Looks like we'll be making the Rock, Papers & Scissors game



Python uses Mersenne Twister for randomisation

--> Watch: Khan Academy - Pseudorandom Number Generator
"""

# Random module
import random

# Random Integer
random_number = random.randint(1, 1000)
print(random_number)

# Random low number
random_0_to_1 = random.random()
print(random_0_to_1)

# Random Float
random_float = random.uniform(1, 100)
print(random_float)

"""
Heads or Tails Program
"""

import random

random_int = random.randint(1,10)
print(f"This is the random number - {random_int}")

if random_int % 2 == 0:
    print("Even Number")
    print("Heads")
else:
    print("Odd Number")
    print("Tails")

"""
Instructor Heads or Tails Program
"""

import random

random_int = random.randint(0,1)
print(f"This is the random number - {random_int}")

if random_int == 0:
    print("Heads")
else:
    print("Tails")

"""
Lists

Can have mixed data types

list = [item1, item2]
"""

fruits = ["apple", "pear", "strawberry"]
print(fruits) # returns all
print(fruits[0]) # returns position (0 apple)
print(fruits[-1]) # returns position (-1 strawberry)
fruits[2] = "raspberry" # would update it 2 to raspberry
fruits.append("blackberry") # adds one item to the list
fruits.extend(["mango", "watermelon", "strawberry"]) # adds a list of items to the list
print(fruits)
print(len(fruits)) # tells you how many items in the list

"""
Who will pay the bill?

Pick a random name from the list.
"""

import random

friends = ["Tom", "Stuart", "Giles", "James", "Adam"]

# Using list range
position = random.randint(0,4)
print(friends[position])

# Instructor Option 2
print(random.choice(friends))

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Grapes", "Peaches", "Cherries", 
#               "Nectarines", "Pears", "Apples", "Blackberries", "Blueberries", "Potatoes"]

fruits = ["Strawberries", "Grapes", "Peaches", "Cherries", "Nectarines", "Pears", "Apples", "Blackberries", "Blueberries"]
vegetables = ["Spinach", "Kale", "Potatoes"]

dirty_dozen = [fruits,vegetables]
     
print(dirty_dozen[1][1]) # would return Kale. List 1, place 1

# ==========================================
# DAY 5 - For Loops, Range and Code Blocks
# ==========================================

"""
Day Five Content - For Loops, Range and Code Blocks

Looks like we'll be making a password generator
"""

"""
for item in list_or_items:
    do something for each item
"""

fruits = ["Strawberries", "Grapes", "Peaches"]

for fruit in fruits:
    print(fruit)

### example how to recreate a sum function with for loop
student_scores= [123, 111, 143, 153, 113, 114, 122, 124]

total_exam_scores = sum(student_scores)
print(total_exam_scores)

sum = 0
for score in student_scores:
    sum += score
print(sum)

### example how to recreate a max function with for loop
student_scores= [123, 111, 143, 153, 113, 114, 122, 124]

print(max(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

"""
Range Function

for number in range(a, b):
    print(number)
"""

for number in range(0, 10):
    print(number)

for number in range(0, 10, 2):
    print(number)

# Add up 1 to 100
sum = 0
for number in range(1,101):
    sum += number
print(sum)

# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. 
# These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# e.g. it might start off like this:

#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz

# ...etc

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
# ==========================================
# DAY 6 - Functions, Code Blocks and While Loops
# ==========================================

"""
Day Six Content - Functions, Code Blocks and While Loops

Looks like we'll be making a Escape the Maze game
"""

"""
Already used a lot of built-in functions - e.g. print, len, range
"""

print("Hello")
num_char = len("Hello")
print(num_char)

"""
Defining our own function is easy def function_name():
"""
# Defining function
def my_function():
    print("Hello")
    print("Bye")

# Calling function
my_function()


"""
Reeborg's Python
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fselect_collection_en.json&name=Other%20worlds&url=%2Fworlds%2Fmenus%2Fselect_collection_en.json

# Hurdles Game
"""

# define right turn
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# define jump
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# hurdle six times
for step in range(6): # 6 times
    jump()

"""
Reminder -- For Loops

for item in list_of_items:
    do something to each item

for number in range(a, b):
    do something 

While Loops

whilst something_is_true:
    do something
"""

# hurdle while loop example
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1 # decrease by one each time
    print(number_of_hurdles) #

# for the one with the random goal line
while at_goal() != True:
    jump()

# using it't negation (whilst False)
while not at_goal():
    jump()

"""
For loops are great when you want to iterate over something and you need to do something with each thing.
For loops are great when you want to do something in a range.

While loops are best when you just want to do something until the condition changes.
Whilst loops are more dangerous as they can create infinite loops.
"""

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# Hurdles 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Hurdles 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
# ==========================================
# DAY 7 - Hangman Game
# ==========================================

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

# ==========================================
# DAY 8 - Functions with Inputs
# ==========================================

"""
Day Eight Content - Functions with Inputs

The challenge will be Caeser cypher
"""

"""
Standard function

def my_function():
    do this
    then this
    finally this

my_function()
"""

# create function called greet and give it three things to print
# define
def greet():
    print("Hello!")
    print("I'm the greet function.")
    print("Hope you're having a good day?")

# call
greet()

"""
Function that allows for Inputs

def my_function(something):
    do this
    then this
    finally this

my_function()
"""

# create function called greet with input and give it three things to print
# define function and parameter
def greet_with_name(name):
    print(f"Hello {name}!")
    print("I'm the greet function.")
    print("Hope you're having a good day?")

# call with argument
greet_with_name("James")

"""
Life in Weeks

I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, 
if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.

Where x is replaced with the actual calculated number of weeks the input age has left until age 90.


**Warning** The function must be called life_in_weeks for the tests to pass. 
Also the output must have the same punctuation and spelling as the example. Including the full stop!

Example Input
56


Example Output
You have 1768 weeks left.
"""

def life_in_weeks(current_age):
    years_remaining = 90 - current_age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")

life_in_weeks(X)

"""
Multiple Inputs Example

Default way is to use Positional Argument, i.e. just take the input order and use. 

Keyword arg
"""

def greet_with(name, location):
    print(F"Hi {name}, I understand you're from {location}?")

greet_with("James", "Hove")

greet_with("Hove", "James")

"""
Multiple Inputs Example

Keyword arg always ties the parameter to the argument
"""

def greet_with(name, location):
    print(F"Hi {name}, I understand you're from {location}?")

greet_with(location="Hove", name="James")

"""
Love Calculator
💪 This is a difficult challenge! 💪 
You are going to write a function called calculate_love_score() that tests the compatibility between two names.  
To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 

Total = 5 

L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 
Total = 3 

Love Score = 53

Example Input 
calculate_love_score("Kanye West", "Kim Kardashian")
Example Output
42
"""


### I've seemingly overcomplicated this and reflected on why strings would be better
###

def calculate_love_score(name1, name2):
    
    combined_names = []
    true_list = ["t", "r", "u", "e" ]
    love_list = ["l", "o", "v", "e"]
    score_one = 0
    score_two = 0

    # add each letter of the names to a list; remove spaces; lower as added
    for index, each_char in enumerate(name1+name2):
        if each_char == " ":
            continue
        else: 
            combined_names.append(each_char.lower())
        print(combined_names)

    # lookup each letter vs the two lists
    for each_char in combined_names:

        if each_char in true_list:
            score_one += 1
            print(score_one)

        if each_char in love_list:
            score_two += 1
            print(score_two)

    print(f"Your love score is {score_one}{score_two}")

calculate_love_score("Kanye West", "Kim Kardashian")

"""
Instructor 

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
        
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
        
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
            
    score = int(str(first_digit) + str(second_digit))
    print(score)
        
calculate_love_score("Kanye West", "Kim Kardashian")

"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text, shift_amount):
    # print(original_text)
    # print(shift_amount)

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

    cipher_word = ""
    
    # rather than double the alphabet
    # instructor did below modulo to get the remainder
    # remainder is the correct offset 0-25
    # 35 % 26 = 9 (example of Z offset 9)
    # example letter 1 offset 20
    # 11 (12th letter) % 26 = 5 which is F
    # this would work for any list - modulo the list length
    # new_position %= len(alphabet)

    # double the alphabet list to allow for offset of up to 25 chars (TODO 4)
    cipher_alphabet = alphabet * 2

    for each_letter in original_text:
        # find position of original letter
        original_position = alphabet.index(each_letter)
        # calculate new position
        new_position = original_position + shift_amount
        # add new letter to new word
        cipher_word +=  cipher_alphabet[new_position]
    
    print(f"This is your encoded word: {cipher_word}")

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    "Please retry"

"""
    Note on ABOVE
    rather than double the alphabet
    instructor did below modulo to get the remainder
    remainder is the correct offset 0-25
    35 % 26 = 9 (example of Z offset 9)
    this would work for any list - modulo the list length
    new_position %= len(alphabet)
"""
# ==========================================
# DAY 9 - Dictionaries and Nesting
# ==========================================

"""
Day Nine Content - Dictionaries and Nesting

The challenge will be an Auction Program

Dictionaries are {Key: Value pairs}

Examples:
Key: Vaulue
Bug: An error in a program that prevents the program from functioning as expected.
Function: A piece of code that you can easily call again and again.
Loop: The action of doing something over and over again.

"""

# Best practice is to leave a comma at the end ready for next entry.
# Best practice format
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from functioning as expected.",
    "Function": "A piece of code that you can easily call again and again.",
}

print(programming_dictionary["Bug"])

"""
Common errors:
Typos in Key
Not storing as "strings"
Not calling "strings"
"""

# To add a key
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

empty_dictionary = {}

# Wipe an existing dictionary by setting it to empty again
programming_dictionary = {}
print(programming_dictionary)

# Add back after removing
programming_dictionary["Bug"] = "An error in a program that prevents the program from functioning as expected."
programming_dictionary["Function"] = "A piece of code that you can easily call again and again."
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Redefine a value
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# This Loop through a dictionary only returns the Key
for key in programming_dictionary:
    print(key)

# This Loop through a dictionary returns both
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


"""
Grading Program

You have access to a database of student_scores in the format of a dictionary. 
The keys in student_scores are the names of the students and the values are their exam scores. 

Write a program that converts their scores to grades.

By the end of your program, you should have a new dictionary called student_grades that should contain 
student names as keys and their assessed grades for values.  

This is the scoring criteria: 

- Scores 91 - 100: Grade = "Outstanding" 
- Scores 81 - 90: Grade = "Exceeds Expectations" 
- Scores 71 - 80: Grade = "Acceptable" 
- Scores 70 or lower: Grade = "Fail" 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades =
"""

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    # print(str(student) + ": " + str(student_scores[student]))

    # would have been better to add
    # score = student_scores[student]
    # then just used score to make it more readable

    if student_scores[student] <= 70:
        student_grades[student] = "Fail"

    elif  71 <= student_scores[student] <= 80:
        student_grades[student] = "Acceptable"

    elif  81 <= student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
        
    else:
        student_grades[student] = "Outstanding"

print(student_grades)

"""
Nesting

Standard dictionary
{
Key1: Value,
Key2 : Value,
}

Nested dictionary
{
Key1: [List],
Key2 : {Dictionary},
}
"""

#List
capitals = {
    "France": "Paris",
    "UK": "London",
}

# Nested List in Dictionary
travel_log = {
    "France": ["Paris", "Dijon", "Lille "],
    "UK": ["London", "Manchester", "St Ives"],
}

# Nested List in Dictionary
travel_log = {
    "France": ["Paris", "Dijon", "Lille "],
    "UK": ["London", "Manchester", "St Ives"],
}

# Print Lille
print(travel_log["France"][2])

# Print France
print(travel_log["France"])

# Nested List
nested_list = ["A", "B", ["C", "D"]]

# Print D
print(nested_list[2][1])

# Nested Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Dijon", "Lille "],
        "num_times_visited": 4
    },
    "UK": {
        "cities_visited": ["London", "Manchester", "St Ives"],
        "num_times_visited": 6
    }
}

# Print St Ives
print(travel_log["UK"]["cities_visited"][2])

# Print UK Cities
print(travel_log["UK"]["cities_visited"])


"""
Without key parameter:

pythonwinner = max(open_bids)

This finds the maximum key (name) in the dictionary, using alphabetical order.

With key parameter:

pythonwinner = max(open_bids, key=open_bids.get)

This finds the key (name) that has the maximum value (bid amount).
"""
# ==========================================
# DAY 10 - Functions with Outputs
# ==========================================

"""
Day Ten Content - Functions with Outputs

The challenge will be a Calculator App

Reminder:

Standard function \/

def my_function():
    do this
    then this
    finally this

my_function()

Function that allows for Inputs \/

def my_function(something):
    do this
    then this
    finally this

my_function()
"""

"""
Function with Outputs

def my_function():
    result = 3 * 2
    return result

output = my_fuction()
"""

def my_function():
    # result = 3 * 2
    # return result
    return 3 * 2

output = my_function()
print(output)

#####
# example
#####
def format_name(first_name, last_name):
    # .title() converts a string to Capitalised
    return(first_name.title() + " " + last_name.title())

f_name = input("What is your first name?\n")
l_name = input("What is your last name?\n")
output = format_name(first_name=f_name, last_name=l_name)
print(output)

#####
# instructor example
#####
def format_name(first_name, last_name):
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"{formatted_first_name} {formatted_last_name}"

print(format_name(first_name="jim", last_name="cAr"))

#####
# Example of output fron one function as input to a second
#####

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_1("hello")
print(output)
# hellohello

output = function_2(function_1("hello"))
print(output)
# Hellohello

#####
# Example of multiple return
#####

def format_name(first_name, last_name):
    if first_name == "" or last_name =="":
        return "You did not provide valid inputs"
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"{formatted_first_name} {formatted_last_name}"

f_name = input("What is your first name?\n")
l_name = input("What is your last name?\n")
print(format_name(first_name=f_name, last_name=l_name))


"""
Leap Year

💪 This is a difficult challenge! 💪 

Write a program that returns True or False whether if a given year is a leap year.

A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice - https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year. 
- on every year that is divisible by 4 with no remainder
- except every year that is evenly divisible by 100 with no remainder 
- unless the year is also divisible by 400 with no remainder   

If English is not your first language, or if the above logic is confusing, try using this flow chart.

e.g. The year 2000: 

    2000 ÷ 4 = 500 (Leap)  
    2000 ÷ 100 = 20 (Not Leap)  
    2000 ÷ 400 = 5 (Leap!)  

So the year 2000 is a leap year. 

But the year 2100 is not a leap year because: 

    2100 ÷ 4 = 525 (Leap)  
    2100 ÷ 100 = 21 (Not Leap)  
    2100 ÷ 400 = 5.25 (Not Leap)  

Warning
Your return should be a boolean and match the Example Output format exactly, including spelling and punctuation. 

Example Input 1
2400
Example Return 1
True


Example Input 2
1989
Example Return 2
False
"""

def is_leap_year(year):

    divisible_by_4 = year % 4
    divisible_by_100 = year % 100
    divisible_by_400 = year % 400

    if divisible_by_4 == 0 and divisible_by_100 == 0 and divisible_by_400 == 0:
        return True
    elif divisible_by_4 == 0 and not divisible_by_100 == 0 and not divisible_by_400 == 0:
        return True
    else:
        return False

input_year = int(input("What year would you like to validate?\n"))
output = is_leap_year(input_year)
print(output)

#####
# Instructor version
#####
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

"""
Docstrings

Describe the function
Must go on first line after
"""

def format_name(first_name, last_name):
    """Take a first and last name and format it to 
    return the title case version of the name."""
    # .title() converts a string to Capitalised
    return(first_name.title() + " " + last_name.title())

f_name = input("What is your first name?\n")
l_name = input("What is your last name?\n")
output = format_name(first_name=f_name, last_name=l_name)
print(output)


###########################
# Calculator challenge
###########################
from day_10_art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2
    
def multiply(n1, n2):
    return n1 * n2
    
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)
first_number = float(input("What's the first number?: "))
keep_calculating = True

while keep_calculating:

    ## instuctor used this to print the symbols
    #for symbol in operations:
    #    print(symbol)

    calc_type = input("Operator options are: + - * /\nWhich would you like?: ")
    second_number = float(input("What's the second number?: "))

    # looks up the calc_type in the operations dictionary to return the function name
    my_operator = operations[calc_type]

    # uses the output of above (function name) and then inputs the two numbers
    output = my_operator(first_number, second_number)

    # prints the function output
    print(f"{first_number} + {calc_type} + {second_number} = {output}")

    continue_calc = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation, or anything else to quit:\n").lower()

    if continue_calc == "y":
        first_number = output
    elif continue_calc == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        first_number = float(input("What's the first number?: "))
    else:
        quit()


"""
INSTRUCTOR
import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
"""
# ==========================================
# DAY 12 - Scope, Namespaces, Global Variables
# ==========================================

"""
Day 12 Content - Scopoe, Namespaces, Global Variables

The challenge will be a Number Guessing game.

"""

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# enemies inside function: 2
# enemies outside function: 1

"""
Variables declared inside a function have local scope.
They are only seen by other code within the same block of code.
"""
#local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) ## will error as potion_strength is not defined

# global scope variables are available at any level of code
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()  

# There is no Block Scope within Python; the variable has the same scope as it's enclosing function
if 3 > 2:
    a_variable = 10

## Global & Local example two

game_level = 3
enemies = ["skeleton", "zombie", "alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

#####

game_level = 3
enemies = ["skeleton", "zombie", "alien"]

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

#### same as above but the variable has been initialised; above would never print if level 5 or above
#### this one would return ""
game_level = 3
enemies = ["skeleton", "zombie", "alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

    """
Prime Number Checker

Prime numbers are numbers that can only be cleanly divided by themselves and 1. Wikipedia  

You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  It should return True or False.

e.g. 7 is a primer number because it is only divisible by 1 and itself.
But 4 is not a prime number because you can divide it by 1, 2 or 4.
NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.

Example Input 1
73
Example Output 1
True

Example Input 2
75
Example Output 2
False
"""

def is_prime(num):
    
    for x in range(2, num):
        if num % x == 0:
            return("Not prime")
    else:
        return("Prime")

result = is_prime(75)
print(result)

"""
Modifying global scope

They are actually two entirely different variables.

enemies = "skeleton"

def increase_enemies():
    enemies = "zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

enemies inside function: zombie
enemies outside function: skeleton

"""

## Errors as it's looking for the local variable
enemies = 0

def increase_enemies():
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()


## This tells it we're using the global variable enemies
enemies = 0

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()

"""
Modifying global variables is error prone / open to bugs as the global could have been created anywhere in the code
Reading is fine
Below is a better way of doing it
"""

enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1
    

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

"""
Global Constants

use all upper case

URL = a.com
PI = 3.14159
"""

"""
# ASCII art generator https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
"""
# ==========================================
# DAY 13 - Debugging
# ==========================================

"""
Day 13 Content - Debugging

The challenge will be a Number Guessing game.

Tips:
  - Describe the Problem
  - Reproduce the Bug
  - Play Computer
  - Fix the Errors
  - Use Print
  - Use a Debugger

"""

"""
It never gets to 20 as stop range is number -1. It loops 1-19.
"""

def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?


"""
using the wrong list range on Randit; should be 0, 5
"""
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_num)
print(dice_images[dice_num])


"""
Searches below 1994 and over 1994. No = 1994
"""

year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

"""
Errors if non numerical entry is received
"""
age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")


"""
Fixed. It catches the value error if someone writes ten rather than 10.
"""
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")

"""
The double = causes the issue.
"""
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


#### fixed; use print to identify the errors
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)

word_per_page == int(input("Number of words per page: "))
print(word_per_page)

total_words = pages * word_per_page
print(total_words)

"""
Original 
"""

import random
import day_13_maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = day_13_maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


"""
Updated after walking through the debugger example; indent error with b_list
"""

import random
import day_13_maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = day_13_maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


"""
Debugging Odd or Even

- Read the code in exercise.py - Spot the problems 🐞. - Modify the code to fix the program. Fix the code so that it works and passes the tests when you submit. 
"""

def odd_or_even(number):
    if number % 2 = 0:
        return "This is an even number."
    else:
        return "This is an odd number."

"""
After
"""

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
    
print(odd_or_even(2))

"""
Debugging Leap Year
- Read the code in exercise.py
- Spot the problems 🐞.
- Modify the code to fix the program.   

Fix the code so that it works and when you hit submit it should pass all the tests. 

This is how you work out whether if a particular year is a leap year.
- on every year that is divisible by 4 with no remainder
- except every year that is evenly divisible by 100 with no remainder
- unless the year is also divisible by 400 with no remainder
"""

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
"""
After
"""

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
is_leap(2000)

"""
Debugging FizzBuzz
- Read the code in exercise.py
- Spot the problems 🐞. 
- Modify the code to fix the program. 
- No shortcuts 
- don't copy-paste to replace the code entirely with a previous working solution.   

The code needs to print the solution to the FizzBuzz game.   
- Your program should print each number from 1 to x where x is the input number. 
- However when the number is divisible by 3 then instead of printing the number it should print "Fizz".   
- When the number is divisible by 5, then instead of printing the number it should print "Buzz". 
- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz". 
"""

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])

"""
Fixed; AND not or. ELIF not if. Remove brackets from print number.
"""

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

print(fizz_buzz(15))
