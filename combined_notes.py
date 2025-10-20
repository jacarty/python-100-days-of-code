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

"""
Consolidated Notes from Intermediate Section (Days 16-26)
This file contains a copy of all notes.py files from the intermediate folder.
"""

# =============================================================================
# DAY 16 - Object Oriented Programming
# =============================================================================

"""
Day 16 Content - Object Oriented Programming

The challenge will be a building the Coffee Machine with OOP.
"""

"""
Objects - consider two things:

What it has (attributes)
What it does (methods)

Can call / run multiple versions of the same object; we treat them as blueprints

Class (bluprint) & Ojects (created from the blueprint)

Example
Class = Car
Object = Car instance

# Pascal case used to capitalise the first letter of class to differentiate from variables, functions etc. which use underscores
car = CarBlueprint (class) 

"""

# example import of module
# import module
# fetch the variable from the module
import another_module
print(another_module.another_variable)


"""
Similar to above. In simple terms:
Import the Module turtle
Fetch the class Turtle and construct object from that blueprint with ()
Assigned to an object named Dan """

import turtle
dan = turtle.Turtle()

"""
Alternate is to just import the Class 
"""

from turtle import Turtle, Screen
dan = Turtle()
print(dan)

"""
To access the objects attributes

car.speed
car.fuel
"""

from turtle import Turtle, Screen

dan = Turtle()
print(dan)

my_screen = Screen()
print(my_screen.canvheight)

"""
To access the objects methods (things it does)

car.move()
car.stop()

Turtle documentation
https://docs.python.org/3/library/turtle.html 
"""

from turtle import Turtle, Screen

# create object dan from Class Turtle
dan = Turtle()
print(dan)
# call the method and set shape to Turtle
dan.shape("turtle")
# set colour of Dan using method color
dan.color("blue")
# move forward 100 paces
dan.forward(100)

# create object my_screen from Class Screen 
my_screen = Screen()
# set attribute
print(my_screen.canvheight)
# set attribute
my_screen.exitonclick()

"""
Python Packages

Collections of premade files that are packed together for a goal or purpose

e.g. To create an ascii table manually would be painful

print("| Pokemon Name | Type |")
print("-----------------------")

Python Package Index - pypi.org

use venv to isolate to this repo
pip install PrettyTable 

"""

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

"""
I added this to demonstrate a way to use a dictionary for the data
"""

from prettytable import PrettyTable

table = PrettyTable()
# change attribute to centre align (it already did but don't like right or left)
table.align = "c"

# create dictionary that fits the input requirements
data = {
    "Pokemon Name": ["Pikachu", "Squirtle", "Charmander"],
    "Type": ["Electric", "Water", "Fire"]
}

# loop dictionary to add colums and data
for column_name, column_data in data.items():
    table.add_column(column_name, column_data)

print(table)


# =============================================================================
# DAY 17 - Building Classes
# =============================================================================

"""
Day 17 Content - Building Classes

The challenge will be a building a Quiz Game with OOP.
"""

"""
Simply defined by class Name:
Then code follows.

Classes should have each letter of the first word Capitilised
Reminder it's called: PascalCase 

vs camelCase which has the first word lower, and the rest first char upper

vs snake_case which is lower case and separated by _ (variables, py files etc.)

camelCase - commonly used for variable and function names in languages like JavaScript and Java

PascalCase - often used for class names and type names in languages like Python, C# and .NET

class Car:
"""
# Pass simply used to avoid the formatting error of expecting code after the :
class User: # define class
    pass

user1 = User() # create object from Class

"""
How to create an attribute for your class

An attribute is a variable associated with an object

Examples:

But notice, unless defined in the Class you can create any attributes, 
and it's also errorprone/potentially inconsitent

The notion of a Class is to specify these pieces of information 
when creating the object from the Class in the form of Constructors
"""

class User: # define class
    pass

user1 = User() # create object from Class
user1.id = "001"
user1.username = "alan"

print(user1.username)

user2 = User()
user1.id = "002"
user1.name = "steve"

"""
Constructor
A part of the blueprint that specifies what should happen when the object is being constructed

When the object is being initialised from the Class
you set the variables, counters, switches to their starting values 

You create the Constructor by using the init function - it's a special method

class Car:
    def __init__(self):
    #intialise attributes

Self is the Object being created
"""

class User: # define class
    
    # this is where we create or intialise the starting values for our attributes
    # the __init__ function is called ever time you create a new object from this Class
    def __init__(self):
        print("new user being created")

user1 = User() # create object from Class
user1.id = "001"
user1.username = "alan"
print(user1.username)

user2 = User()
user2.id = "002"
user2.name = "steve"
print(user2.name)

"""
Will result in:

new user being created
alan
new user being created
steve

Reminder:
Attributes - things a Class has
Methods - things a Class does

Example on setting attributes
E.g. a car has 5 seats
You pass in the parameter alongside the Object being created (initialised)
The parameter gets passed in when the Object is constructed from the Class
You can pass in as many parameters as you want
When you recieve that data you can use it to set that Objects attributes
"""

# sets the numher of seats to 5
class Car:
    def __init__(self, seats):
        self.seats = seats
        print(seats)

my_car = Car(5)

# which is effectively the same result as

my_car.seats = 5

"""
/\ /\ /\ The key Point on above
The __init__ method is convenient, automated way to set attributes when an object is created. 
But the actual mechanism of setting self.seats = seats inside __init__ 
is the same as setting my_car.seats = 5 outside of it.
"""

class User: 

    def __init__(self):
        pass

user1 = User() # create object from Class
user1.id = "001"
user1.username = "alan"
print(user1.username)

#returns alan

""" we're creating attributes at the time of constuction 
typical convention is for the name of parameter to match name of attribute (doesnt have to)
"""

class User: # define class

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user1 = User("001", "alan") 
print(user1.username)

"""Because we've now set the parameters in the constructor, 
you have to use them when creating the object from the Class

If not you will receive an error:
TypeError: __init__() missing 2 required positional arguments: 'user_id' and 'username'
See below
"""
user2 = User()
user2.id = "002"
user2.name = "steve"
print(user2.name)

"""
You can also set default values that done have to be passed as parameters
"""

class User: # define class

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 

user1 = User("001", "alan") 
print(user1.followers)

# returns 0

"""
methods = things the Class does

e.g attribute = has 5 seats
method = change to 2 seats

example
"""

class User: # define class

    def enter_race_mode(): # method
        self.seats = 2 # gets seats attribute and changes to 2

my_car.enter_race_mode()


"""
in practice - instagram followers
"""
class User: # define class

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 
        self.following = 0

    # you always use 'self' as first parameter in a method so the function knows the Ojnect that called it
    # assume we follow a user (instagram)
    def follow(self, user):
        user.followers += 1     # the user we're following goes up by 1
        self.following += 1     # the user count we're following goes up by 1

user1 = User("001", "alan") 
user2 = User("002", "dan") 

user1.follow(user2)

print(f" user 1 followers: {user1.followers}")
print(f" user 1 following: {user1.following}")

print(f" user 2 followers: {user2.followers}")
print(f" user 2 following: {user2.following}")

 """
 returns
 user 1 followers: 0
 user 1 following: 1
 user 2 followers: 1
 user 2 following: 0
 """


# =============================================================================
# DAY 18 - Turtle Graphics, Tuples and Importing Modules
# =============================================================================

"""
Day 18 Content - Turtle Graphics, Tuples and Importing Modules

The challenge will be a building a Drawing.
"""

from turtle import Turtle, Screen

dave = Turtle()
dave.shape("turtle")
dave.color("orange")
dave.pencolor("orange")

for move in range(4):
    dave.forward(50)
    dave.left(90)

screen = Screen()
screen.exitonclick()

"""
Importing Modules

Basic = import ModuleName
e.g. 
import turle
dave = turtle.Turtle()

Specific
e.g usefule when calling a lot
from turtle import Turtle
dave = Turtle()
steve = Turtle()
alan = Turtle()

Import everything (it's not good practice to do this)
from turtle import *
BUT it;s less obvious where things come from
i.e. where does the method come from? which Class?

forward(100)
vs dave.forward(100) when you import a specific Module
"""

"""
Import method as.... ALIAS

import turtle as t
dave = t.Turtle()
"""

"""
Dashed drawing
"""

from turtle import Turtle, Screen

dave = Turtle()
dave.shape("turtle")
dave.color("orange")
dave.pencolor("orange")

for move in range(4):
    dave.forward(50)
    dave.penup()
    dave.forward(50)
    dave.pendown()
    dave.left(90)

screen = Screen()
screen.exitonclick()

"""
Drawing shapes continuosly (in sequence)
Triangle, Square, Pentagon, Hexagon, Heptagon, Octogon, Nonogon and Decacon
Lenght of all = 100
Random colours

Maths:
360 / num_of_sides = angle
"""

from turtle import Turtle, Screen

dave = Turtle()
dave.shape("turtle")
dave.color("orange")
dave.pencolor("orange")

number_of_sides = 4

while number_of_sides < 11:
    angle = 360/number_of_sides
    for sides in range(number_of_sides):
        dave.forward(100)
        dave.right(angle)

    number_of_sides +=1
    
screen = Screen()
screen.exitonclick()


"""
Instructor
They created a function over loop (didnt suggest function in course)
"""

import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

"""
Random Walk
Move Faster
Thicker lines

"""

from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

dave = Turtle()
dave.shape("turtle")

def draw_shape(move,rotate):
    dave.forward(move)
    dave.setheading(rotate)
    dave.color(random.choice(colours))

turn = [0, 90, 180, 270]
dave.width(5)
dave.speed(8)

for moves in range(50):
    rotation = random.choice(turn)
    move = random.randint(10, 50)
    draw_shape(move, rotation)

screen = Screen()
screen.exitonclick()

"""
Tuples
Ordered Data type (1, 3, 4)
my_tuple = (1, 3, 9)
my_tuple[0] = 1

You can't change or remove items in a Tuple
Once created it is immutable
You can convert to list by list(my_tuple)
"""

from turtle import Turtle, Screen
import random

dave = Turtle()
screen = Screen()
screen.colormode(255)

dave.shape("turtle")
dave.width(5)
dave.speed(8)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_colour = (r, g, b)
    return turtle_colour

def draw_shape(move, rotate, colour):
    dave.forward(move)
    dave.right(rotate)
    dave.color(colour)

turn = [90, 180, 270]

for moves in range(50):
    rotation = random.choice(turn)
    move = random.randint(10, 50)
    colour = random_colour()
    draw_shape(move, rotation, colour)

screen.exitonclick()

"""
Create Spirograph
"""

from turtle import Turtle, Screen
import random

dave = Turtle()
screen = Screen()
screen.colormode(255)

dave.shape("turtle")
dave.width(3)
dave.speed("fastest")

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_colour = (r, g, b)
    return turtle_colour

def draw_shape(move, rotate, colour):
    dave.circle(move)
    dave.left(rotate)
    dave.color(colour)

def draw_spirograph(num_circles, size):
    rotate = 360 / num_circles
    for moves in range(num_circles):
        circle_size = size
        colour = random_colour()
        draw_shape(circle_size, rotate, colour)

draw_spirograph(num_circles=70, size=125)

screen.exitonclick()


"""
Instructor version
"""

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()


# =============================================================================
# DAY 19 - More Turtle Graphics, Event Listeners, State and Multiple Instances
# =============================================================================

"""
More Turtle Graphics, Event Listeners, State and Multiple Instances

The Challenge is Turtle Coordinate System Quiz
"""

"""
Event listeners allow you to tap into key strokes etc.
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen() # set focus on TurtleScreen (in order to collect key-events)
# reminder, when you pass a function as an input, you only pass the name
screen.onkey(key="space", fun=move_forwards) # this function is used to bind fun to the key-release event of the key
screen.exitonclick() 

"""
Example higher order function.
Frequently used when needing to listen for events then trigger a function

def apply_operation(func, x, y):
    '''Higher-order function that applies any function to two numbers'''
    return func(x, y)

# Define basic operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

# Usage
print(apply_operation(add, 8, 3))       # Output: 11
print(apply_operation(multiply, 4, 7))  # Output: 28
print(apply_operation(divide, 15, 3))   # Output: 5.0

"""

"""
Etch a Sketch

Mine
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(5)

def move_backwards():
    tim.backward(5)

def counter_clockwise():
    tim.left(5)

def clockwise():
    tim.right(5)

def clear_and_centre():
    screen.reset()


screen.listen() # set focus on TurtleScreen (in order to collect key-events)
# reminder, when you pass a function as an input, you only pass the name
screen.onkey(fun=move_forwards, key="Up") 
screen.onkey(fun=move_backwards, key="Down") 
screen.onkey(fun=counter_clockwise, key="Left")
screen.onkey(fun=clockwise, key="Right")
screen.onkey(fun=clear_and_centre, key="c")
screen.exitonclick() 


"""
Instructor
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()

"""
Turtle Race Game
"""

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turle will win the race? Enter a colour: ")
print(user_bet)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
height = -125

for turtle in range(0, 6):
    colour = colours[turtle]
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour)
    new_turtle.penup() 
    new_turtle.goto(x=-200, y=height)
    turtle_list.append(new_turtle)
    height += 50


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("You win")
            else:
                print(f"You've lost. The winning turtle was {winning_colour}.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick() 


# =============================================================================
# DAY 21 - Inheritance & Slicing
# =============================================================================

"""
Inheritance & Slicing

class Fish():
    def __init__(self):

    
class Fish(Animal):
    def __init__(self):
        super().__init__()

"""

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe() # this does everything the breathe method above does
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()
nemo.swim()
print(nemo.num_eyes)

"""

slicing works on lists and tuples
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

piano_keys[2:5]
returns c, d, e
2, 3 and 4

piano_keys[2:5:2]
returns c, e
every other one

piano_keys[::-1]
returns, g, f, e, d, c, b, a

"""

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[1:])

# returns 're', 'mi', 'fa', 'so', 'la', 'ti'

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[:5])

# returns 'do', 're', 'mi', 'fa', 'so'


# =============================================================================
# DAY 22 - Making Pong
# =============================================================================

"""
Making Pong

1. Set up the Main Screen

2. Create a Paddle that responds to Key Presses

3. Write the Paddle Class and Create the Second Paddle

4. Write the Ball Class and Make the Ball Move

5. Add the Ball Bouncing Logic

6. How to Detect Collisions with the Paddle

7. How to Detect when the Ball goes Out of Bounds

8. Score Keeping and Changing the Ball Speed

"""


# =============================================================================
# DAY 24 - Working with local files and directories
# =============================================================================

"""
Working with local files and directories
"""

# Open, read and close a file
# You need to rememeber to close to free up memory
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Using with method closes files when you've finished with it
with open("my_file.txt") as f:
    contents = f.read()
    print(contents)

# Writing to a file; w overwrites the content
with open("my_file.txt", mode="w") as f:
    contents = f.write("My text.")

# Writing to a file; a appends
with open("my_file.txt", mode="a") as f:
    contents = f.write("\nAdditional text.")
    print(contents)

# Writing to a file that doesn't exist, creates it.
with open("new_file.txt", mode="a") as f:
    contents = f.write("Hello, this is a new file with text.")
    print(contents)

# Related to files
# import OS
import os
# Show current working directory
print("Current working directory:", os.getcwd())
# List files in current directory
print("Files in current directory:", os.listdir())


"""
Instructor Mail Merge
"""

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


# =============================================================================
# DAY 25 - Working with CSV files and analysing data with Pandas
# =============================================================================

"""
Working with CSV files and analysing data with Pandas
"""

# open CSV and add to list
# results in a a messy list though

with open("./weather_data.csv") as file:
    data = file.readlines()
    print(data)
    # ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

######
# use the python csv module
######

import csv

with open("./weather_data.csv") as file:
    data = csv.reader(file)
    print(data)
    # create object
    # <_csv.reader object at 0x10510d2a0> 
    for row in data:
        print(row)
        """
        ['day', 'temp', 'condition']
        ['Monday', '12', 'Sunny']
        ['Tuesday', '14', 'Rain']
        ['Wednesday', '15', 'Rain']
        ['Thursday', '14', 'Cloudy']
        ['Friday', '21', 'Sunny']
        ['Saturday', '22', 'Sunny']
        ['Sunday', '24', 'Sunny']
        """

# add just the temperatures to the list temp
# no heading
# add as integer
import csv

with open("./weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
print(data)
"""
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
"""

data = pandas.read_csv("./weather_data.csv")
print(data["temp"])

"""
0    12
1    14
2    15
3    14
4    21
5    22
6    24
"""

######
# Check data type
######
data = pandas.read_csv("./weather_data.csv")
print(type(data))
# <class 'pandas.core.frame.DataFrame'>

######
# Check data type
######
data = pandas.read_csv("./weather_data.csv")
print(type(data["temp"]))
# <class 'pandas.core.series.Series'>

"""
The two primary data structures of pandas, Series (1-dimensional) and DataFrame (2-dimensional), handle the vast majority of typical use cases in finance, statistics, social science, and many areas of engineering. For R users, DataFrame provides everything that R's data.frame provides and much more. pandas is built on top of NumPy and is intended to integrate well within a scientific computing environment with many other 3rd party libraries.
"""

######
# Open Data
######
data = pandas.read_csv("./weather_data.csv")

######
# Pandas DataFrame (workbook) To_Dictionary
######
data_dict = data.to_dict()
print(data_dict)

######
# # Pandas Series (column) To_List
######
temp_list = data["temp"].to_list()
print(temp_list)


######
# calculate the average temperature
# manual way
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

total = 0 

# Pandas Series (column) To_List
for temperature in data["temp"].to_list():
    total += temperature

average = total / len(data["temp"].to_list())
print(average)

######
# calculate the average temperature
# with statistics
######

import pandas
import statistics

# Open Data
data = pandas.read_csv("./weather_data.csv")

temperatures = data["temp"].to_list()
statistics.mean(temperatures)

######
# calculate the average temperature
# with pandas
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

print(data["temp"].mean())

######
# find the maximum temperature
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

print(data["temp"].max())

"""
Get temp column
data["temp"]

Another way to call a column is simply
data.temp
"""

print(data.temp)

######
# return a row of data, e.g. Monday
######

print(data[data.day == "Monday"])

######
# return the row with highest temp of week
######

max_temp = data.temp.max()
print(data[data.temp == max_temp])

######
# alternative
######

print(data[data.temp == data.temp.max()])

######
# tapping in to a row
######

monday = data[data.day == "Monday"]
print(monday.condition)

monday = data[data.day == "Monday"]
print(monday.temp)


######
# get temp and convert to Fahrenheit
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

monday = data[data.day == "Monday"]
fahrenheit = (monday.temp[0] * (9/5)) + 32
print(fahrenheit)

"""
Create a Dataframe
"""

import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

#####
# output to CSV
#####

data.to_csv("new_data.csv")


"""
https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data

Count Squirrels By Fur Colour

Gray
Cinnamon
Black
"""

import pandas
data = pandas.read_csv("./squirrel_data.csv")
# print(data["Primary Fur Color"])

values = data["Primary Fur Color"].value_counts()
print(values)
values.to_csv("squirrel_count.csv")


########
# Instructor making dataframe and exporting
# Central Park Squirrel Data Analysis
########
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


# =============================================================================
# DAY 26 - Lists and Dictionary Comprehensions
# =============================================================================

"""
Lists and Dictionary Comprehensions
"""


# =============================================================================
# DAY 27 - GUI with Tkinter and Functional Arguments
# =============================================================================

"""
GUI with Tkinter and Functional Arguments
"""
# import
import tkinter

#### Windows

# create a window
window = tkinter.Tk()

# title window
window.title("My GUI Program")
# minimum size (autoscales by default)
window.minsize(width=500, height=300)

#### Labels
my_label = tkinter.Label(text="I am a label", font=("courier", 11, "bold"))
my_label.pack(side="left")

# keep window on screen; has to be at the bottom of program
window.mainloop()

"""
##### Keyword arguments
"""

def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    pass

my_function(a=1, b=2, c=2)    

#### Arguments with default values
def my_function(a=1, b=2, c=3):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    pass

my_function()    

#### Overwrite one value
def my_function(a=1, b=2, c=3):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    pass

my_function(b=4)    

"""
##### Unlimited positional arguments

They get passed in as a Tuple

"""

#print them
def add(*args):
    for n in args:
        print(n)

add(1, 2, 6, 10)

### add them
def add(*args):
    return(sum(args))

print(add(1, 2, 6, 10))

# get one value
def add(*args):
    print(args[1])

add(1, 2, 6, 10)

"""
##### Unlimited positional keyword arguments

They get passed in as a Dictionary

"""
### kwargs
def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    
    print(kwargs["add"])

calculate(add=3, multiply=8)

### with a value and kwargs
def calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply=8)

### create Class with kwargs (kw)
class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Bugait", model="Veyron")
print(my_car.model)

### using get is the way for Classes with optional inputs
### if the value is empty it just returns none
### the key lookup would cause an error if not passed
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")

my_car = Car(make="Bugait", model="Veyron")
print(my_car.colour)


### you can mix all three
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
    # 4 (7, 3, 0) {'x': 10, 'y': 64}
    
all_aboard(4, 7, 3, 0, x=10, y=64)


"""
Examples of widgets

"""

from tkinter import *

def center_window(window, min_width=500, min_height=500):
    """Center window with minimum size but allow growth for content"""
    
    # Get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    
    # Use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    
    # Get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

my_window = Tk()
# show all available methods
# print(dir(my_window))
# give window a title
my_window.title("Distance Converter")
# function to set size and centre on screen
center_window(my_window)



# on screen label
my_label = Label(text="I am a label")
# lots of element can be configured with .config or individually
my_label.config(font=("courier", 12))
# pack always needed to position on screen
my_label.pack()


def button_clicked():
    print("I got clicked")
    # update the label text
    # my_label.config(text="Button was clicked")
    # use the input window text
    my_label.config(text=my_entry.get())

# on screen button
# command defines what happens when clicked; it calls the name of a function
my_button = Button(text="Click me", command=button_clicked)
# pack always needed to position on screen
my_button.pack()


# on screen Entry box
my_entry = Entry()
my_entry.pack()
my_entry.config(width=20)
# default text
my_entry.insert(END, string="enter email")


# multi line Text entry
my_text_entry = Text()
# box size
my_text_entry.config(width=30, height=10)
# start cursor in this box
my_text_entry.focus()
my_text_entry.insert(END, "Some starting text in the box")
print(my_text_entry.get(1.0, END))
my_text_entry.pack()


# spinbox 
def spinbox_used():
    print(my_spinbox.get())

my_spinbox = Spinbox()
my_spinbox.config(from_=0, to=10, width=5, command=spinbox_used)
my_spinbox.pack()


# scale / scroll to set number
def scale_used(value):
    print(value)

# scale / scroll to set number
my_scale = Scale()
my_scale.config(from_=0, to=100, command=scale_used)
my_scale.pack()

# checkbutton
def checkbutton_used():
    # prints 1 in clicked otherwise 0
    print(checked_state.get())

checked_state = IntVar()
my_checkbutton = Checkbutton()
my_checkbutton.config(text="Is On?", variable=checked_state, command=checkbutton_used)
my_checkbutton.pack()

# radio button 
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
my_radiobutton1 = Radiobutton()
my_radiobutton2 = Radiobutton()
my_radiobutton1.config(text="Option1", value=1, variable=radio_state, command=radio_used)
my_radiobutton2.config(text="Option2", value=2, variable=radio_state, command=radio_used)
my_radiobutton1.pack()
my_radiobutton2.pack()

# listbox
def listbox_used(event):
    # gets current selection from listbox
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
my_listbox.config(height=4)
fruits = ["Apple", "Orange", "Pineapple", "Strawberry"]
for item in fruits:
    my_listbox.insert(fruits.index(item), item)
my_listbox.bind("<<ListboxSelect>>", listbox_used)
my_listbox.pack()

# keep window open; last line
my_window.mainloop()


"""
can't mix pack and grid in same program

let Tk order and place on window
my_label.pack()

specific places on window
my_label.place(x=50, y=50)

using grid to divide the window and place
my_label.grid(column=0, row=0)
"""

from tkinter import *

def center_window(window, min_width=0, min_height=0):
    """Center window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

def button_clicked():
    """Create a button"""
    print("I got clicked")
    label.config(text=entry.get())

# create Window and centre in screen
window = Tk()
window.title("Distance Converter")
center_window(window)

# label
label = Label(text="I am a label")
#label.config(font=("courier", 12), padx=20, pady=20)
label.grid(column=0, row=0)

# button one
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# button two
button_2 = Button(text="Button 2")
button_2.grid(column=2, row=0)

# entry box
entry = Entry()
entry.config(width=20)
entry.insert(END, string="enter email")
entry.grid(column=3, row=3)

# centre window
center_window(window, min_width=0, min_height=0)
# keep alive
window.mainloop()

#######################
# miles to KM converter
#######################

from tkinter import *

def center_window(window, min_width=0, min_height=0):
    """Center window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

def button_clicked():
    """Create a button"""
    print("I got clicked")
    calc = round((float(miles_entry.get()) * 1.609), 2)
    calc_label.config(text=calc)

# create Window and centre in screen
window = Tk()
window.title("Distance Converter")
center_window(window)
window.config(padx=10, pady=10)

# entry box
miles_entry = Entry()
miles_entry.config(width=10)
miles_entry.insert(END,string="0")
miles_entry.grid(column=1, row=0)

# miles label
miles_label = Label(text="Miles")
miles_label.config(font=("courier", 12))
miles_label.grid(column=2, row=0)

# equals to label
equals_label = Label(text="Is equal to")
equals_label.config(font=("courier", 12))
equals_label.grid(column=0, row=1)

# km label
calc_label = Label(text="0")
calc_label.config(font=("courier", 12))
calc_label.grid(column=1, row=1)

# label4
km_label = Label(text="KM")
km_label.config(font=("courier", 12))
km_label.grid(column=2, row=1)

# button
calc_button = Button(text="Calculate", command=button_clicked)
calc_button.config(font=("courier", 12))
calc_button.grid(column=1, row=2)

# centre window
center_window(window)
# keep alive
window.mainloop()


# =============================================================================
# DAY 28 - Building a Pomodoro App with Tkinter
# =============================================================================

"""
Building a Pomodoro App with Tkinter

The Pomodoro Technique
A time management method that breaks work into focused intervals, traditionally 25 minutes long, separated by short breaks.

Basic Flow:
Work (25 min) → Break (5 min) → Work (25 min) → Break (5 min) → 
Work (25 min) → Break (5 min) → Work (25 min) → Long Break (15-30 min)

Key Steps:
-- Choose a task to work on
-- Set timer for 25 minutes
-- Work with full focus until timer rings
-- Take a short break (5 minutes)

Repeat - After 4 pomodoros, take a longer break

The technique helps maintain focus, prevents burnout, and makes large tasks feel more manageable by breaking them into smaller, timed chunks.

"""

# https://colorhunt.co/


#######################################################################
#
# Dynamic Datatyping
# We're changing the Variable from Int to Str
# This isn't possible in all languages 
#
# https://stackoverflow.com/questions/11328920/is-python-strongly-typed
#
#######################################################################

def count_down(count):
    # timer function; 1s (1000ms)

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec == f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)



"""

Pomodoro Application

"""

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps

    reps += 1

    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    work_min = WORK_MIN * 60

    # 8th round
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    # 2nd, 4th and 6th round
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)
    # 1st, 3rd, 5th, 7th round
    else:
        count_down(work_min)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    # timer function; 1s (1000ms)

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

def center_window(window, min_width=200, min_height=200):
    """Center window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, fg=GREEN, font=("FONT_NAME", 30, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.config(
    bg=YELLOW, 
    activebackground=YELLOW,
    highlightbackground=YELLOW,
    highlightcolor=YELLOW
)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(
    bg=YELLOW, 
    activebackground=YELLOW,
    highlightbackground=YELLOW,
    highlightcolor=YELLOW
)
reset_button.grid(column=2, row=2)

checkmarks = Label()
checkmarks.config(bg=YELLOW, fg=GREEN, font=("FONT_NAME", 16, "bold"))
checkmarks.grid(column=1, row=3)

canvas = Canvas(width=220, height=250, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="tomato.png")
canvas.create_image(110, 125, image=bg_image)
timer_text = canvas.create_text(110, 140, text="00:00", fill="white", font=("FONT_NAME", 16, "bold"))
canvas.grid(column=1, row=1)

center_window(window)
window.mainloop()


# =============================================================================
# DAY 29 - Building a Password Generator with Tkinter
# =============================================================================

"""

Building a Password Generator with Tkinter

File output format
website | email | password

"""

from tkinter import *
from tkinter import messagebox # need to import message box
import string # used to get letters, digits and punctuation
import pyperclip
import random

FONT = "courier"
FONT_SIZE = 11

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(16))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy()

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"""These are the details entered: \n
                                Website: {website}\n
                                Email: {email}\n
                                Password: {password}\n
                                Is it okay to save?""")

        if is_ok:
            with open("./passwords.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

def centre_window(window, min_width=0, min_height=0):
    """Centre window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(127, 100, image=bg_image)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website:", font=(FONT, FONT_SIZE))
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.config(width=42)
website_entry.focus() # default cursor to this box
website_entry.grid(column=1, columnspan=2, row=1)

email_label = Label()
email_label.config(text="Email/Username:", font=(FONT, FONT_SIZE))
email_label.grid(column=0, row=2)

email_entry = Entry()
email_entry.config(width=42)
email_entry.insert(0, "test@email.com") # default text
email_entry.grid(column=1, columnspan=2, row=2)

password_label = Label()
password_label.config(text="Password:", font=(FONT, FONT_SIZE))
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(command=generate_password)
password_button.config(text="Generate Password", font=(FONT, FONT_SIZE))
password_button.grid(column=2, row=3)

add_button = Button(command=save_password)
add_button.config(text="Add", width=40, font=(FONT, FONT_SIZE))
add_button.grid(column=1, columnspan=2, row=4)

#centre_window(window)
window.mainloop()


# =============================================================================
# DAY 30 - Errors, Exceptions and Saving JSON Data
# =============================================================================

"""
Errors, Exceptions and Saving JSON Data

try:

except:

else:

finallly:

"""

######
# File Example
######

# would fail if file doesn't exist
# with open("a_file.txt") as f:
#     f.read()

# try this
try:
    f = open("a_file.txt")
    a_dict = {"key" : "value"}
    print(a_dict["ads"])
# error specific
except FileNotFoundError:
    print("There was an error opening, creating file")
    f = open("a_file.txt", "w")
    f.write("Hello")
# error specific that's captured
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist.")
# run if the try succeeds
else:
    content = f.read()
    print(content)
# happens regardless if the code succeeds or fails
finally:
    f.close()
    print("The file was closed.")

    # allows you to raise an error and message
    raise TypeError("This is an error I made up.")

######
# Realk Example
# Valid code but nonsense result
######

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)

"""
IndexError Handling

Issue 

We've got some buggy code. Try running the code. The code will crash and give you an IndexError.
This is because we're looking through the list of fruits for an index that is out of range. 


Objective 

Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie". 


IMPORTANT: The exception handling should NOT allow each fruit to be printed when there is an exception. e.g. it should not print out Apple pie, Pear pie and Orange pie, when there is an exception it should only print "Fruit pie".  
"""

fruits = ["Apple", "Pear", "Orange"]
     
# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")
     
make_pie(4)



"""
KeyError Handling

We've got some buggy code, try running the code. The code will crash and give you a KeyError.
This is because some of the posts in the facebook_posts don't have any "Likes". 

Objective 
Use what you've learnt about exception handling to prevent the program from crashing.
"""

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
 
    total_likes = 0
    for post in posts:
      try:
        total_likes = total_likes + post['Likes']
      except KeyError:
        pass 
    
    return total_likes
 
 
count_likes(facebook_posts)



############
# Mine
############

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

while True:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, please only enter letters of the alphabet.")
        continue
    else:
        print(output_list)
        break

""""
JSON
"""

########
# JSON file to read
########
# dict = dictionary to pass in (serialise)
# file_name is output
# indent=4 is number spaces to add (for readability)
json.dump(dict, file_names, indent=4)

########
# JSON file name to load
########
# outputs back to dictionary (deserialise)
json.load(file_name)

########
# update a JSON file
########
# read old data from file
data = json.load(data_file)
# update old data with new data
json.update(dict)
# write file back
json.dump(data, file_name, indent=4)

"""

Update Password Generator

File output format JSON

"""

from tkinter import *
from tkinter import messagebox # need to import message box
import string # used to get letters, digits and punctuation
import pyperclip
import random
import json

FONT = "courier"
FONT_SIZE = 11

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(16))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"""These are the details entered: \n
                                       Website: {website}\n
                                       Email: {email}\n
                                       Password: {password}\n
                                       Is it okay to save?""")

####################
# we could avoid except / else repitition with a function
# being left like this for future readability
####################

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # read data file
                    data = json.load(file)

            except FileNotFoundError:
                print("File not found. Needs to be created.")
                with open("data.json", "w") as file:
                    # saving updated data
                    json.dump(new_data, file, indent=4)

            else:
                # update old data with new data
                data.update(new_data)

                with open("data.json", "w") as file:
                    # saving updated data
                    json.dump(data, file, indent=4)
                
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    # print("search")
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        email_lookup = data[website]["email"]
        pw_lookup = data[website]["password"]

    except FileNotFoundError:
        messagebox.showinfo(title=f"{website}", message="No data file found.")

    except KeyError:
        messagebox.showinfo(title=f"{website}", message="No details exist for the website.")

    else:
        messagebox.showinfo(title=f"{website}", message=f"""Email: {email_lookup}\n
                                                        Password: {pw_lookup}""")

# ---------------------------- UI SETUP ------------------------------- #

def centre_window(window, min_width=0, min_height=0):
    """Centre window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(127, 100, image=bg_image)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website:", font=(FONT, FONT_SIZE))
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.config(width=21)
website_entry.focus() # default cursor to this box
website_entry.grid(column=1, row=1)

search_button = Button(command=search_password)
search_button.config(text="Search Password", width=17, font=(FONT, FONT_SIZE))
search_button.grid(column=2, row=1)

email_label = Label()
email_label.config(text="Email/Username:", font=(FONT, FONT_SIZE))
email_label.grid(column=0, row=2)

email_entry = Entry()
email_entry.config(width=42)
email_entry.insert(0, "test@email.com") # default text
email_entry.grid(column=1, columnspan=2, row=2)

password_label = Label()
password_label.config(text="Password:", font=(FONT, FONT_SIZE))
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(command=generate_password)
password_button.config(text="Generate Password", font=(FONT, FONT_SIZE))
password_button.grid(column=2, row=3)

add_button = Button(command=save_password)
add_button.config(text="Add", width=40, font=(FONT, FONT_SIZE))
add_button.grid(column=1, columnspan=2, row=4)

#centre_window(window)
window.mainloop()


# =============================================================================
# DAY 31 - Flashcard Capstone Project
# =============================================================================

"""
Flashcard Project

https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists

https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish

https://github.com/hermitdave/FrequencyWords/tree/master/content/2018

"""


from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("./data/spanish_words_to_learn.csv")
    spanish_list = df.to_dict('records')
except:
    df = pd.read_csv("./data/spanish_words_1k.csv")
    spanish_list = df.to_dict('records')

random_word = {}
flip_timer = None

def known_word():
    global random_word
    spanish_list.remove(random_word)
    
    df = pd.DataFrame(spanish_list)
    df.to_csv("./data/spanish_words_to_learn.csv", index=False)
    generate_card()


def generate_card():
    global random_word, flip_timer
    random_word = random.choice(spanish_list)

    canvas.itemconfig(canvas_image, image=spanish_image)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=random_word["word"], fill="black")

    # cancel any running timer when a new card is generated
    if flip_timer:
        window.after_cancel(flip_timer)

    # set timer
    flip_timer = window.after(3000, flip_card)


def flip_card():
    english_word = random_word['translation']

    canvas.itemconfig(canvas_image, image=english_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")


def centre_window(window, min_width=0, min_height=0):
    """Centre window with minimum size but allow growth for content"""
    # Update to calculate widget sizes
    window.update_idletasks()
    # get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    # use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    # get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # set screen location
    window.geometry(f"{width}x{height}+{x}+{y}")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
spanish_image = PhotoImage(file="./images/card_front.png")
english_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(410, 263, image=spanish_image)
card_title = canvas.create_text(400, 120, font=("ariel", 35, "italic"))
card_word = canvas.create_text(400, 263, font=("ariel", 60, "italic"))
canvas.grid(column=0, columnspan=2, row=0)

cross_button = Button(command=generate_card)
cross_image = PhotoImage(file="./images/wrong.png")
cross_button.config(image=cross_image, highlightthickness=0, bd=0)
cross_button.grid(column=0, row=1)

check_button = Button(command=known_word)
check_image = PhotoImage(file="./images/right.png")
check_button.config(image=check_image, highlightthickness=0, bd=0)
check_button.grid(column=1, row=1)

centre_window(window)
generate_card()
window.mainloop()

"""
INTERMEDIATE+ NOTES CONSOLIDATION
Contains all notes from intermediate+ section (Days 32-58)
"""

##############################################################################
# DAY 32 - SMTP and Datetime module
##############################################################################

"""
STMP and Datetime module
"""

###############
# Sending email
###############

import smtplib

email_add = "test@test.com"
password = "pass"

with smtplib.SMTP("smtp.live.com") as connection:
    connection.starttls()
    connection.login(user=email_add, password=password)
    connection.sendmail(
        from_addr=email_add, 
        to_addrs="test2@test.com",
        msg="Subject:Hello\n\nThis is the email body."
    )

###############
# Date and Time
###############

import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)

month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year= 2000, month= 1, day= 1)

"""
Monday motivational email
"""

import datetime as dt
import random
import smtplib

EMAIL_ADDR = "test@test.com"
EMAIL_PASS = "pass"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("./quotes.txt") as file:
        list_of_quotes = file.readlines()
        random_quote = random.choice(list_of_quotes)

    print(random_quote)

    with smtplib.SMTP("smtp.live.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDR, password=EMAIL_PASS)
        connection.sendmail(
            from_addr=EMAIL_ADDR, 
            to_addrs=EMAIL_ADDR,
            msg=f"Subject:Happy Monday!\n\n{random_quote}"
        )

"""
Birthday Email
"""

#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


##############################################################################
# DAY 33 - API Endpoints
##############################################################################

"""
API Endpoints

The projects is to build an ISS Tracker

An Application Programming Interface is a set of commands, functions, protocols, and objects
that programmers can use to create software or interact with external systems.

                API Request
Your Program ---------------> External System                      
            <----------------
                API Response
                
"""


##########################################################
#
# ISS Location API
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
#
##########################################################

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
# returns <Response [200]>

########################################################################################
# There are five classes defined by the standard:
#    1xx informational response – the request was received, continuing process
#    2xx successful – the request was successfully received, understood, and accepted
#    3xx redirection – further action needs to be taken in order to complete the request
#    4xx client error – the request contains bad syntax or cannot be fulfilled
#    5xx server error – the server failed to fulfil an apparently valid request
########################################################################################

print(response.status_code)
# returns 200

print(response.json())
# returns the JSON reponse

print(response.raise_for_status())
# will tell you the status code returned (for error handling)

######################################################
# Return ISS location
# 
# https://www.latlong.net/Show-Latitude-Longitude.html
#
######################################################

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_location = (longitude, latitude)
print(iss_location)

################################
# Sunrise & Sunset for Location
# https://sunrise-sunset.org/api
################################

import requests
from datetime import datetime

# London
#LAT = 51.507351
#LNG = -0.127758

# Hove 
LAT = 50.827930
LNG = -0.168749

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hour = sunrise.split("T")[1].split(":")[0]
print(sunrise_hour)
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunset_hour)

time_now = datetime.now()
hour_now = time_now.hour
print(hour_now)


######################################
# Check if ISS overhead and dark
######################################

import requests
from datetime import datetime

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    print(sunrise)
    print(sunset)
    print(hour_now)

    if not sunrise < hour_now < sunset:
        return True

if is_iss_overhead and is_night:
    print("ISS is overhead and you can see it")


##############################################
# Instructor
#
# Check every 60 sec if ISS overhead and dark
#
# Email you
##############################################

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )


##############################################################################
# DAY 34 - Trivia API and GUI Quiz App
##############################################################################

"""
Trivia API and The Quizzler App

"""

##################################################
# HTML Entities
# https://www.w3schools.com/html/html_entities.asp
##################################################

import html

text = html.unescape("Q.1: Valve&#039;s &quot;Portal&quot; and &quot;Half-Life&quot; " \
                    "franchises exist within the same in-game universe.")
print(text)

# Q.1: Valve&#039;s &quot;Portal&quot; and &quot;Half-Life&quot; franchises exist within the same in-game universe. (True/False): 
# Q.1: Valve's "Portal" and "Half-Life" franchises exist within the same in-game universe.

###################
# Type Hints
###################

# sets what the input type should be, and also what the returned data type will be

def greeting(name: str) -> str:
    return 'Hello ' + name


###########################
# Quiz Game Updates
#
# Uses API to get questions
#
# Has GUI to display quiz
#
# Read UI.py 
# Read Data.py
# Read Quiz_Brain.py
###########################


##############################################################################
# DAY 35 - API Keys, Authentication, Environment Variables and SMS
##############################################################################

"""
API Keys, Authentication, Environment Variables and Sending SMS

Build a rain alert App

Used mailgun and email rather than Twillio

"""
import os
from dotenv import load_dotenv
import requests

load_dotenv("../../.env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
RECIPIENT = os.getenv("RECIPIENT")

latitude = "50.827778" 
longitude = "-0.152778"

# Google Weather APIs
current = "https://weather.googleapis.com/v1/currentConditions:lookup"
hourly = "https://weather.googleapis.com/v1/forecast/hours:lookup" # up to 240 hours
daily = "https://weather.googleapis.com/v1/forecast/days:lookup" # up to 10 days

current_parameters = {
    "key": GOOGLE_API_KEY,
    "location.latitude": latitude,
    "location.longitude": longitude
}

hourly_parameters = {
    "key": GOOGLE_API_KEY,
    "location.latitude": latitude,
    "location.longitude": longitude,
    "hours": "12"   
}

daily_parameters = {
    "key": GOOGLE_API_KEY,
    "location.latitude": latitude,
    "location.longitude": longitude,
    "days": "3"
}

response = requests.get(url=hourly, params=hourly_parameters)
response.raise_for_status()
forecast_hours = response.json()["forecastHours"]
# print(forecast_hours)

rain_probability = [hours["precipitation"]["probability"]["percent"] for hours in forecast_hours]
print(rain_probability)

if any(n > 25 for n in rain_probability):
    print("Umbrella needed")

    response = requests.post(
        f"https://api.eu.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": f"James <mailgun@{MAILGUN_DOMAIN}>",
            "to": [RECIPIENT],
            "subject": "Weather Alert",
            "text": "Don't forget your umbrella today! Rain probability is high."
        }
    )

    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())


##############################################################################
# DAY 36 - Stock Trading News Alert
##############################################################################

"""
Stock News Monitoring Project

Skipped Twilio; will use AWS later

"""

from dotenv import load_dotenv
import os
import requests
import boto3

###########################
# Read API Keys
###########################

load_dotenv("../../.env")
ALPHA_API_KEY = os.getenv("ALPHA_API_KEY")
NEWS_API = os.getenv("NEWS_API")

###########################
# Global Vars
###########################

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

###########################
# Get Stock Data & Trim
###########################

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHA_API_KEY
}

# Get API data
data = requests.get(url=ALPHA_URL, params=alpha_parameters)
# Check for error response
data.raise_for_status()
# Trim data for Daily information
tsla_stock_data = data.json()["Time Series (Daily)"]
print(tsla_stock_data)

# List comporehension to just get values by day
values = [value for (key, value) in tsla_stock_data.items()]
print(values)

# Trim to get the Closing prices as float
close = float(values[0]["4. close"])   # 333.87
previous_close = float(values[1]["4. close"])  # 345.98
percentage_change = ((close - previous_close) / previous_close) * 100

###########################
# Get News If Needed
# Return First 3 Articles
###########################

if abs(percentage_change) > 1: # If + or - 1%
    up_down = "🔺" if percentage_change > 0 else "🔻"
    print(f"Get News - Stock moved {percentage_change:+.1f}%")

    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API
    }

    news = requests.get(url=NEWS_URL, params=news_parameters)
    news.raise_for_status()
    news_articles = news.json()["articles"][:3]
    print(news_articles)

formatted_articles = [f"""Headline: {article['title'][:50]}{'...' if len(article['title']) > 50 else ''}
                      \nLink: {article['url']}""" 
                      for article in news_articles]
print(formatted_articles)

###########################
# Send SMS Message with AWS
###########################

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')
AWS_SENDER_ID= os.getenv('AWS_SENDER_ID')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')

# Create SNS client
sns = boto3.client(
    'sns',
    region_name=AWS_DEFAULT_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Create concise SMS message
sms_message = f"{STOCK}: {up_down}{percentage_change}%\n\n" + "\n---\n".join(formatted_articles[:3])

# Send SMS
response = sns.publish(
    PhoneNumber=PHONE_NUMBER,
    MessageAttributes={
        'AWS.SNS.SMS.SenderID': {
            'DataType': 'String',
            'StringValue': AWS_SENDER_ID
        },
        'AWS.SNS.SMS.SMSType': {
            'DataType': 'String',
            'StringValue': 'Transactional'
        }
    },
    Message=sms_message
)

print(f"Message sent! MessageId: {response['MessageId']}")

##############################################################################
# DAY 37 - Advanced Authentication with POST/PUT/DELETE
##############################################################################

"""
Advanced Authentication and POST / PUT / DELETE Requests

Build a Habit Tracker with Pixela
"""

import requests

# requests.get() - Fetching/Reading data
"""
     CLIENT                    SERVER
        │                         │
        │  GET /api/users ────────>
        │                         │
        │<──────── 200 OK         │
        │   [{"id":1,"name":..}]  │
        │                         │
    📥 GETTING                 📚 DATA
"""

# requests.post() - Creating new data
"""
     CLIENT                    SERVER
        │                         │
        │  POST /api/users ──────>
        │  {"name":"John"}        │
        │                         │
        │<──────── 201 Created    │
        │   {"id":2,"name":"John"}│
        │                         │
    📤 SENDING                 ➕ CREATING
"""

# requests.put() - Updating/Replacing data
"""
     CLIENT                    SERVER
        │                         │
        │  PUT /api/users/2 ─────>
        │  {"name":"Jane"}        │
        │                         │
        │<──────── 200 OK         │
        │   {"id":2,"name":"Jane"}│
        │                         │
    ✏️ UPDATING               🔄 REPLACING
"""

# requests.delete() - Removing data
"""
     CLIENT                    SERVER
        │                         │
        │  DELETE /api/users/2 ──>
        │                         │
        │<──────── 204 No Content │
        │                         │
        │                         │
    🗑️ DELETING               ❌ REMOVED
"""

import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv("../../.env")
PIXELA_API = os.getenv("PIXELA_API")
USERNAME = "j1m"
GRAPH_ID = "g1"

#####################
# Create User
#####################

# user endpoint
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_API, 
    "username": USERNAME, 
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#####################
# Create Graph
#####################

# graph endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# send token in header
headers = {
    "X-USER-TOKEN": PIXELA_API
}

# new graph config
graph_config = {
    "id": GRAPH_ID,
    "name": "Pages Read",
    "unit": "Pages",
    "type": "int",
    "color": "sora"
}

# response = requests.post(headers=headers, url=graph_endpoint, json=graph_config)
# print(response.text)

# result
# https://pixe.la/v1/users/j1m/graphs/g1.html

#####################
# Post Pixel
#####################

# Get todays date
today = datetime.now()
# Format date with strftime
today_formatted = today.strftime("%Y%m%d")

pixel_create_url = f"{graph_endpoint}/{GRAPH_ID}"

# new graph config
post_pixel = {
    "id": GRAPH_ID,
    "date": today_formatted,
    "quantity": "5"
}

# response = requests.post(headers=headers, url=pixel_create_url, json=post_pixel)
# print(response.text)

#####################
# Update Pixel
#####################

DATE = "20250904"
pixel_update_url = f"{graph_endpoint}/{GRAPH_ID}/{DATE}"

# new graph config
update_pixel = {
    "quantity": "25"
}

# response = requests.put(headers=headers, url=pixel_update_url, json=update_pixel)
# print(response.text)

#####################
# Delete Pixel
#####################

DATE = "20250904"
pixel_update_url = f"{graph_endpoint}/{GRAPH_ID}/{DATE}"

# response = requests.delete(headers=headers, url=pixel_update_url, json=update_pixel)
# print(response.text)


#####################
# Delete User
#####################

# user endpoint
pixela_endpoint = f"https://pixe.la/v1/users/{USERNAME}"

user_params = {
    "token": PIXELA_API,
}

response = requests.delete(url=pixela_endpoint, json=user_params)
print(response.text)


##############################################################################
# DAY 38 - Exercise Tracking with Python
##############################################################################

"""
Exercise energy tracking with Python

I didnt want to sign up to Sheetly and provide access to Google
"""

######################
# Imports
######################

from dotenv import load_dotenv
import os
import requests

######################
# Load local ENVs
######################

load_dotenv("../../.env")
NUTRITIONIX_APP_ID= os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY= os.getenv("NUTRITIONIX_API_KEY")

######################
# URLs
######################

exercise_api = "https://trackapi.nutritionix.com/v2/natural/exercise"

######################
# Exercise Auth Header
######################

exercise_headers = {
    "x-app-id": NUTRITIONIX_APP_ID, 
    "x-app-key": NUTRITIONIX_API_KEY
}

######################
# Exercise Query
######################

exercise_query = str(input("What exercise did you do?: "))
weight = int(input("What is your weight in kg?: "))
height = float(input("What is your height in cm?: "))
age= str(input("How old are you?: "))

exercise_params = {
    "query": exercise_query,
    "gender": "male",
	"weight_kg": weight,
	"height_cm": height,
    "age": age	
}

response = requests.post(headers=exercise_headers, url=exercise_api, json=exercise_params)
result = response.json()
print(result)

##############################################################################
# DAY 39 - Flight Deal Finder Part 1
##############################################################################

"""
Flight tracker part one

Handy JSON tool https://jsonformatter.curiousconcept.com/#

Lots more code in Classes
"""

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

############################
# Create Instances
############################
data_manager = DataManager()
flight_search = FlightSearch()
notifications = NotificationManager()

############################
# Update CSV with Iata Codes
############################
city_code = data_manager.read_cities()
print(f"Searching the following: {city_code}")
# for city in cities:
#     iata_code = flight_search.iata_search(city)
#     print(iata_code)
#     data_manager.update_iata_code(city, iata_code)

############################
# Search Flights
############################

cheap_flights_found = []

for city in city_code:
    origin = "LON"
    destination = city
    today = datetime.now()
    tomorrow = today + timedelta(weeks=1)
    six_months = today + timedelta(weeks=4)

    flights = flight_search.flight_search(origin, destination, tomorrow, six_months)
    # print(flights)
    cheap_flight = data_manager.cheaper_flight(city, flights)

    if cheap_flight and cheap_flight not in ["No flights found", "No cheaper flights found", False]:
        cheap_flights_found.append(f"{city}: {cheap_flight}")
        print(f"Found cheap flight to {city}")
        # print(cheap_flight)
    else:
        print(f"No cheap flights to {city}")

############################
# Send SMS
############################
if cheap_flights_found:
    message = "Low price alerts!\n" + "\n".join(cheap_flights_found)
    sms = notifications.send_sms(message)
    print(f"SMS sent with {len(cheap_flights_found)} flight deals")
else:
    print("No cheap flights found for any destination")


##############################################################################
# DAY 40 - Flight Deal Finder Part 2
##############################################################################

"""
Flight tracker part two

Handy JSON tool https://jsonformatter.curiousconcept.com/#
"""

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from users import UserManagement

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

############################
# Create Instances
############################
data_manager = DataManager()
flight_search = FlightSearch()
notifications = NotificationManager()
user = UserManagement()

############################
# Check / Create User
############################
while True:
    new_user = input("Do you want to create a New User? Y or N: ").lower()
    
    if new_user == "y":
        user.signup_user()
        break
    elif new_user == "n":
        print("Skipping user creation")
        break
    else:
        print("Please try again. Enter Y or N")

############################
# Update CSV with Iata Codes
############################
city_code = data_manager.read_cities()
print(f"Searching the following: {city_code}")
for city in city_code:
    iata_code = flight_search.iata_search(city)
    print(iata_code)
    data_manager.update_iata_code(city, iata_code)

############################
# Search Flights
############################

cheap_flights_found = []

for city in city_code:
    origin = "LON"
    destination = city
    today = datetime.now()
    tomorrow = today + timedelta(weeks=1)
    six_months = today + timedelta(weeks=4)

    flights = flight_search.flight_search(origin, destination, tomorrow, six_months)
    # print(flights)
    cheap_flight = data_manager.cheaper_flight(city, flights)

    if cheap_flight == "No flights found":
        # Try indirect flights
        print(f"No direct flights to {city}, trying indirect...")
        flights = flight_search.flight_search(origin, destination, tomorrow, six_months, non_stop=False)
        cheap_flight = data_manager.cheaper_flight(city, flights)
        
        if cheap_flight and cheap_flight not in ["No flights found", "No cheaper flights found", False]:
            cheap_flights_found.append(f"{city} (indirect): {cheap_flight}")
            print(f"Found indirect cheap flight to {city}")
        else:
            print(f"No indirect flights to {city} either")
            
    elif cheap_flight == "No cheaper flights found":
        print(f"No cheap flights to {city}")
        
    elif cheap_flight and cheap_flight not in [False, "City code not found"]:
        cheap_flights_found.append(f"{city} (direct): {cheap_flight}")
        print(f"Found direct cheap flight to {city}")
        

############################
# Send SMS
############################
if cheap_flights_found:
    message = "Low price alerts!\n" + "\n".join(cheap_flights_found)
    sms = notifications.send_sms(message)
    print(f"SMS sent with {len(cheap_flights_found)} flight deals")
else:
    print("No cheap flights found for any destination")

############################
# Send Email To Mailing List
############################

emails = user.return_emails()

if cheap_flights_found:
    message = "Low price alerts!\n" + "\n".join(cheap_flights_found)
    for subscriber in emails:
        notifications.send_email(subscriber, message)
        print(f"Email sent with {len(cheap_flights_found)} flight deals")
else:
    print("No cheap flights found for any destination")


##############################################################################
# DAY 41 - Introduction to HTML
##############################################################################

"""
Websites - HTML, CSS and JavaScript

HTML = Structure
CSS = Sytle
JavaScript = Functionaility/Behaviour


🔧 1. Basic HTML Structure Tags
Tag 	Description 	Example
<html> 	Root of the HTML document 	<html> ... </html>
<head> 	Metadata container 	<head> ... </head>
<body> 	Main document content 	<body> ... </body>
<title> 	Page title (in browser tab) 	<title>My Page</title>
<!DOCTYPE> 	Declares document type 	<!DOCTYPE html>

📝 2. Text Formatting Tags
Tag 	Description 	Example
<p> 	Paragraph 	<p>This is a paragraph.</p>
<br> 	Line break 	Hello<br>World
<hr> 	Horizontal line 	<hr>
<h1> to <h6> 	Headings 	<h1>Heading 1</h1>
<strong> 	Bold (semantic) 	<strong>Important</strong>
<b> 	Bold (visual only) 	<b>Bold Text</b>
<i> 	Italic (visual only) 	<i>Italic Text</i>
<em> 	Emphasis (semantic italic) 	<em>Emphasized</em>
<mark> 	Highlighted text 	<mark>Highlight</mark>
<small> 	Smaller text 	<small>Note</small>
<sub> 	Subscript 	H<sub>2</sub>O
<sup> 	Superscript 	E = mc<sup>2</sup>
<u> 	Underline 	<u>Underlined</u>
<del> 	Deleted text 	<del>Old</del>
<ins> 	Inserted text 	<ins>New</ins>

🔗 3. Links & Anchors
Tag 	Description 	Example
<a> 	Hyperlink 	<a href="https://example.com">Visit</a>
<link> 	External resources (e.g., CSS) 	<link rel="stylesheet" href="style.css">
<nav> 	Navigation block 	<nav><a href="#home">Home</a></nav>

🖼️ 4. Media Tags
Tag 	Description 	Example
<img> 	Image 	<img src="img.jpg" alt="Image">
<video> 	Video 	<video controls><source src="video.mp4"></video>
<audio> 	Audio 	<audio controls><source src="audio.mp3"></audio>
<source> 	Media source 	<source src="movie.mp4" type="video/mp4">
<track> 	Captions/subtitles 	<track src="subs.vtt" kind="subtitles">
<embed> 	External resource (e.g., PDF) 	<embed src="file.pdf">

📋 5. Lists
Tag 	Description 	Example
<ul> 	Unordered list 	<ul><li>Item</li></ul>
<ol> 	Ordered list 	<ol><li>First</li></ol>
<li> 	List item 	<li>Element</li>
<dl> 	Description list 	<dl><dt>HTML</dt><dd>Markup</dd></dl>
<dt> 	Term in <dl> 	<dt>Term</dt>
<dd> 	Description in <dl> 	<dd>Definition</dd>

📦 6. Table Tags
Tag 	Description 	Example
<table> 	Table container 	<table> ... </table>
<tr> 	Table row 	<tr> ... </tr>
<td> 	Table data cell 	<td>Data</td>
<th> 	Table header cell 	<th>Header</th>
<thead> 	Table header section 	<thead><tr><th>Col</th></tr></thead>
<tbody> 	Table body section 	<tbody><tr><td>Row</td></tr></tbody>
<tfoot> 	Table footer section 	<tfoot><tr><td>Foot</td></tr></tfoot>
<caption> 	Table caption/title 	<caption>Sales Data</caption>
<col> 	Column formatting 	<col span="2">
<colgroup> 	Group of columns 	<colgroup><col></colgroup>

🧩 7. Form & Input Tags
Tag 	Description 	Example
<form> 	Form container 	<form> ... </form>
<input> 	User input 	<input type="text">
<textarea> 	Multi-line input 	<textarea></textarea>
<label> 	Form label 	<label for="name">Name</label>
<select> 	Dropdown 	<select><option>One</option></select>
<option> 	Dropdown item 	<option value="1">One</option>
<button> 	Button 	<button>Click</button>
<fieldset> 	Group form fields 	<fieldset><legend>Info</legend></fieldset>
<legend> 	Caption for <fieldset> 	<legend>User Info</legend>
<datalist> 	Predefined input list 	<datalist id="browsers"><option>Chrome</option></datalist>
<output> 	Output result 	<output>Result</output>

📁 8. Semantic Layout Tags
Tag 	Description 	Example
<header> 	Page or section header 	<header> ... </header>
<footer> 	Page or section footer 	<footer> ... </footer>
<section> 	Generic section 	<section> ... </section>
<article> 	Independent content 	<article> ... </article>
<aside> 	Sidebar content 	<aside> ... </aside>
<main> 	Main content 	<main> ... </main>
<div> 	Generic container 	<div> ... </div>
<span> 	Inline container 	<span> ... </span>

🧠 9. Scripting & Meta Tags
Tag 	Description 	Example
<script> 	JavaScript code 	<script>alert('Hi')</script>
<noscript> 	Shown if JS disabled 	<noscript>No JS</noscript>
<meta> 	Metadata 	<meta charset="UTF-8">
<style> 	Internal CSS 	<style>p{color:red}</style>

🔎 10. Interactive Tags
Tag 	Description 	Example
<details> 	Toggle details 	<details><summary>Click</summary>Info</details>
<summary> 	Visible heading in <details> 	<summary>More</summary>
<dialog> 	Dialog box 	<dialog open>Hi</dialog>

🔄 11. Deprecated/Obsolete Tags (for reference only)
Tag 	Description 	Example
<center> 	Center align 	<center>Centered</center>
<font> 	Font formatting 	<font color="red">Text</font>
<marquee> 	Scrolling text 	<marquee>Scroll</marquee>

✅ 12. Miscellaneous Tags
Tag 	Description 	Example
<iframe> 	Inline frame (embed) 	<iframe src="page.html"></iframe>
<base> 	Base URL for links 	<base href="https://example.com/">
<time> 	Time value 	<time datetime="2025-07-30">Today</time>
<code> 	Code snippet 	<code>print()</code>
<kbd> 	Keyboard input 	<kbd>Ctrl</kbd>
<samp> 	Sample output 	<samp>Hello</samp>
<var> 	Variable name 	<var>x</var>
<bdi> 	Isolate bidirectional text 	<bdi>abc</bdi>
<bdo> 	Override text direction 	<bdo dir="rtl">Text</bdo>

"""

#############################
# Tags vs Element
#############################

# The Element is the entire thing
# Tags and Content

# <h1>content</>
# opening tag -- content -- closing tag

# Example
# <h1>Book</h1>
#   <h2>Chapter 1</h2>
#     <h3>Section 1</h3>
#     <h3>Section 2</h3>
#   <h2>Chapter 2</h2>
#     <h3>Section 1</h3>
#       <h4>Diagram 1</h4>
#   <h2>Chapter 3</h2>
#     <h3>Section 1</h3>
#     <h3>Section 2</h3>

#############################
# Paragraph
#############################

# <p>paragraph of text</p>

#############################
# Void Elements
#############################

# Horizontal Rule
# <hr />

# Break Rule (new line in Poem or address)
# <br /> 

#############################
# Challenge
#############################

# <!DOCTYPE html>
# <h1>James' Top TV Shows</h1>
# <h2>In no particular order - 5 of my favourite TV series!</h2>
# <hr />
# <h3>Bron ||| Broen</h3>
# <p>
#     When a body is found on the bridge between Denmark and Sweden, right on the border, Danish inspector Martin Rohde and
#     Swedish Saga Norén have to share jurisdiction and work together to find the killer.
# </p>
# <h3>Ted Lasso</h2>
# <p>
#     American college football coach Ted Lasso heads to London to manage AFC Richmond, a struggling English Premier League
#     soccer team.
# </p>
# <h3>The Sorpanos</h3>
# <p>
#     New Jersey mob boss Tony Soprano deals with personal and professional issues in his home and business life that affect
#     his mental state, leading him to seek professional psychiatric counseling.
# </p>
# <h3>Breaking Bad</h3>
# <p>
#     A chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine with a
#     former student to secure his family's future.
# </p>
# <h3>Taskmaster</h3>
# <p>
#     Five comedians are set tasks challenging their creativity and wit. The tasks are supervised by Alex Horne but the
#     Taskmaster, Greg Davies, always has the final word.
# </p>


##############################################################################
# DAY 42 - HTML Intermediate
##############################################################################

"""
The HTML Boilderplate

Understanding HTML Structure
"""

###########################
# Boilderplate
###########################

# <!-- Set to HTML5 -->
# <!DOCTYPE html>
# <!-- Specify language; useful for screen readers -->
# <html lang="en">
    
#     <!-- Page data for browser -->
#      <head>
#         <!-- Specify page is using UTF-8 characters-->
#         <meta charset="UTF-8">
#         <!-- Specify Page Title -->
#         <title>Page Title</title>
#     </head>

#     <!-- Page content -->
#     <body>
#         <h1>Hello World!</h1>
#     </body>
# </html>

###########################
# Lists
###########################

# <h2>Unordered List...</h2>
# <ul>
#     <li>milk</li>
#     <li>bread</li>
#     <li>cheese</li>
#     <li>bacon</li>
# </ul>
# <h2>Ordered List...</h2>
# <ol>
#     <li>milk</li>
#     <li>bread</li>
#     <li>cheese</li>
#     <li>bacon</li>
# </ol>

###########################
# Nested Lists
###########################

# <ul>
#     <li>milk</li>
#     <li>bread</li>
#     <li>brown sauce</li>
#     <li>bacon</li>
#     <li>cheeses:
#         <ul>
#             <li>cheddar</li>
#             <li>jarlsberg</li>
#             <li>port salut</li>
#         </ul>
#     </li>
# </ul>

###########################
# Anchor Tags
###########################

# URL
# <a href="https://www.google.com/">Google Link</a>

# Draggable
# <a draggable="true" href="https://www.google.com/">Google Link</a>

# Image
# <!-- Random Image Website-->
# <img src="https://picsum.photos/400" alt="Random photo via picsum.photos"/><br>


###########################
# Birthday Site Example
###########################

# <!-- This is one possible solution -->
# <h1>It's My Birthday!</h1>
# <h2>On the 12th May</h2>

# <img src="https://raw.githubusercontent.com/appbrewery/webdev/main/birthday-cake3.4.jpeg"
#   alt="purple birthday cake with candles" />

# <h3>What to bring:</h3>
# <ul>
#   <li>Baloons (I love baloons)</li>
#   <li>Cake (I'm really good at eating)</li>
#   <li>An appetite (There will be lots of food)</li>
# </ul>

# <h3>This is where you need to go:</h3>
# <a
#   href="https://www.google.com/maps/@35.7040744,139.5577317,3a,75y,289.6h,87.01t,0.72r/data=!3m6!1e1!3m4!1sgT28ssf0BB2LxZ63JNcL1w!2e0!7i13312!8i6656">Google
#   map link</a>


##############################################################################
# DAY 43 - CSS Introduction
##############################################################################

"""
Cascading Style Sheets
CSS - Why Do We Need It?

https://appbrewery.github.io/just-add-css/

You can add in three ways:

-- Inline 
-- Was used for a particular Element
<tag style="css"/>

-- Internal
-- Was used for an individual Page
<style>css</style>

-- External
-- Used for an entire site
<link 
    rel="stylesheet" 
    href="./style.css"
/>

"""
# Should be Unique within HTML
# #ID-Selector
# #main{
# color: red;
# }

# Many elements
# .Class-Selector
# .red-text{
# color: red;
# }

# Attiribute selector
# p[draggable]{
# color: red;
# }

# Universal selector
# *{
# color: red;
# }


##############################################################################
# DAY 44 - CSS Properties
##############################################################################

"""
CSS Properties

colorhunt.co
fonts.google.com
"""

############################
# Colour
############################

# html {
# background-color: blue
# }
#
# h1 {
# color: blue
# }
#
# h2 {
# color: 0D1164
# }

############################
# Font Property Examples
############################

# 1 px = 1/96th Inch
# 1 px = 0.26 mm

# 1 pt = 1/72nd Inch
# 1 pt = 0.35 mm

# 1 em = 100% of parent
# 1 rem = 100% of root

# #color {
#     color: coral;
#     font-size: 2rem; # 2x parent size
#     font-weight: 900;
#     font-family: 'Caveat', cursive;
#     text-align: right;
# }

############################
# Margin, Padding & Border
############################

# borders expand out; they dont reduce the box
# border: thickness style colour
# border-top: value
# border-width: top right bottom left
# border-width: top-bottom right-left
#
# padding pushes out border by value; box stays same size
# padding: value
#
# margin is the bit outside the border
# margin: value

# ┌─────────────────────────────────────────────────────────────────┐
# │                           MARGIN                                │
# │  ┌───────────────────────────────────────────────────────────┐  │
# │  │                        BORDER                             │  │
# │  │  ┌─────────────────────────────────────────────────────┐  │  │
# │  │  │                    PADDING                          │  │  │
# │  │  │  ┌───────────────────────────────────────────────┐  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  │                 CONTENT                       │  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  │            (Your actual element               │  │  │  │
# │  │  │  │             text, images, etc.)               │  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  └───────────────────────────────────────────────┘  │  │  │
# │  │  │                                                     │  │  │
# │  │  └─────────────────────────────────────────────────────┘  │  │
# │  │                                                           │  │
# │  └───────────────────────────────────────────────────────────┘  │
# │                                                                 │
# └─────────────────────────────────────────────────────────────────┘

#                         Box Model Layers:
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 1. CONTENT   - The actual content (text, images, etc.)
# 2. PADDING   - Space between content and border (inside border)
# 3. BORDER    - The border surrounding padding and content
# 4. MARGIN    - Space outside the border (between elements)

# Example CSS:
# ───────────
# .box {
#     margin: 20px;      /* Outermost spacing */
#     border: 5px solid; /* Border thickness & style */
#     padding: 15px;     /* Inner spacing */
#     width: 200px;      /* Content width */
#     height: 100px;     /* Content height */
# }

# Total Width  = margin + border + padding + content + padding + border + margin
# Total Height = margin + border + padding + content + padding + border + margin

############################
# HTML Div
############################

# A <div> (division) is a generic HTML container element that groups content together. 
# By itself, it's invisible and has no visual styling—it's like an empty box waiting to be decorated.

# Class Selector example

# <div class="my-box">Content here</div>

# .my-box {
#     background-color: lightgray;
#     padding: 20px;
#     border: 2px solid black;
# }

##############################################################################
# DAY 45 - Webscraping with Beatiful Soup
##############################################################################

"""
 Web Scraping With Beautiful Soup

 https://www.crummy.com/software/BeautifulSoup/bs4/doc/

"""

# Beautiful Soup
from bs4 import BeautifulSoup
# import lxml

with open("./index.html") as file:
    html_content = file.read()
    print(html_content)

# if html doesnt work try lxml
soup = BeautifulSoup(html_content, 'html.parser')

# print title tag
print(soup.title)
# print title name
print(soup.title.name)
# print title text
print(soup.title.string)
# formats the output
print(soup.prettify())

# print first anchor tag it finds
print(soup.a)
# print first list it finds
print(soup.li)
# print first paragraph it finds
print(soup.p)

# find all instances of X
all_paragraphs = soup.find_all("p")
print(all_paragraphs)

# find all instances of X
all_anchor_tags = soup.find_all("a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

# search by tag or heading
heading = soup.find(name="h1", id="heading")

# search by class, note _ at end of class
section_heading = soup.find(name="h3", class_="TV")
print(section_heading)

# search by CSS selector
selector = soup.select_one(selector="#name")

# search by CSS class
headings = soup.select(".heading")


######################################################
# Hackernew 
# Aim is to get the most upvoted article in the top 30
######################################################

from bs4 import BeautifulSoup
import requests

site = "https://news.ycombinator.com/news"
response = requests.get(site)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# return articles from first page
articles = soup.find_all("span", class_="titleline")

# generate two lists
articles_text = [] 
articles_url = []

# add Article Header and URL to lists
for article in articles:

    text = article.get_text()
    articles_text.append(text)

    url = article.find("a").get("href")
    articles_url.append(url)

# list comprehension to get the scores per article
article_upvotes = [int(votes.get_text().split()[0]) for votes in soup.find_all("span", class_="score")]

# print(articles_text)
# print(articles_url)
# print(article_upvotes)

# return index of highest score
max_score_index = article_upvotes.index(max(article_upvotes))

# print the list items corresponding to score
print(f"This article with the most votes is: {articles_text[max_score_index]} -> {articles_url[max_score_index]}")

######################################################
# Webscraping
# 
# Legal Rules for Web Scraping (via Claude)
#
# 1. Check the robots.txt File
# Before scraping any website, always check website.com/robots.txt. This file tells you:
# Which parts of the site you can scrape
# Which parts are off-limits
# Crawl delay requirements
# Example:
# Always check: https://example.com/robots.txt
# # It might contain:
#   User-agent: *
#   Disallow: /private/
#   Crawl-delay: 1
#
# 2. Review the Terms of Service (ToS)
# Many websites explicitly prohibit scraping in their Terms of Service. Violating ToS can lead to:
#   IP bans
#   Legal action
#   Account termination (if logged in)
#
# 3. Respect Rate Limits
#   Add delays between requests (typically 1-3 seconds)
#   Don't overwhelm servers with rapid requests
#   This is both ethical and helps avoid getting blocked
#       pythonimport time
#       time.sleep(2)  # Wait 2 seconds between requests
#
# 4. Copyright and Data Ownership
#   Factual data generally can't be copyrighted
#   Creative content (articles, images) is usually protected
#   Database compilations may have protection
#   Always consider fair use, but it's complex
# 
# Best Practices for Legal Scraping
# 
#   1. Use APIs When Available
#       Many sites offer APIs specifically for data access - always prefer these over scraping.
#   2. Identify Yourself
#       Set a proper User-Agent header:
#       pythonheaders = {
#           'User-Agent': 'Your Bot Name (your-email@example.com)'
#       }
#
#   3. Handle Personal Data Carefully
#
#       GDPR (Europe) and CCPA (California) have strict rules about personal data
#       Avoid scraping personal information when possible
#       If you must, ensure compliance with privacy laws
#
#   4. Respect "No Scraping" Signs
#
#   If you see:
#       Meta tags like <meta name="robots" content="noindex,nofollow">
#       Explicit "no scraping" notices
#       CAPTCHA challenges
#       These are clear signals to stop.
#
# Common Legal Pitfalls to Avoid
#
#   Don't bypass security measures (login walls, CAPTCHAs)
#   Don't scrape copyrighted content for commercial use
#   Don't violate Computer Fraud and Abuse Act (CFAA) - unauthorized access
#   Don't ignore cease and desist letters
#   Don't resell or redistribute scraped data without permission
#
# Gray Areas and Recent Cases
#
#   LinkedIn vs. HiQ Labs (2019): Publicly available data may be fair game
#   Facebook vs. Power Ventures: Logged-in scraping is riskier
# 
#   The legal landscape is evolving - what's okay today might not be tomorrow
######################################################

"""
Challenge

Empire 
Return the Top 100 Movies and output to txt file
"""

from bs4 import BeautifulSoup
import requests

site = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(site)
website_html = response.text
# print(response.text)

soup = BeautifulSoup(website_html, 'html.parser')
# print(soup.prettify())

# list comprehensin for movie names; 100 to 1
movies = [movie.text for movie in soup.find_all("h3", class_="title")]

# reverse list and appeend each to file
with open("./movies.txt", "a") as f:
    for movie in reversed(movies):
        f.write(f"{movie}\n")

##############################################################################
# DAY 46 - Billboard 100 Scraping and Spotify Playlist creatiom
##############################################################################

from billboard import BillboardSoup
from spotify_api import Spotify
from my_spotipy import MySpotipy
from datetime import datetime, timedelta
import sys

def main(date):
    ##############################################
    # Find previous Saturday to get Billboard Date
    ##############################################

    # Parse the input date
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Get day of week (0=Monday, 5=Saturday, 6=Sunday)
    days_since_saturday = (date.weekday() + 1) % 7
    
    # If it's already Saturday, use it; otherwise go to previous Saturday
    if days_since_saturday == 0:
        billboard_date = date
    else:
        billboard_date = date - timedelta(days=days_since_saturday)
    
    billboard_date_str = billboard_date.strftime("%Y-%m-%d")

    ##############################################
    # Billboard Soup - Get Top100 for Week
    ##############################################

    # date = "2000-08-19"
    soup = BillboardSoup()
    top_100 = soup.get_chart(date=billboard_date_str)
    # print(top_100)

    ##############################################
    # Spotify - Lookup Top 100
    ##############################################

    spotify = Spotify()
    track_uris = []

    for title, artist in top_100.items():
        uri = spotify.search_track(artist_name=artist, track_name=title)
        if uri:
            track_uris.append(uri.split(":")[2])
            print(f"✓ Found: {title} - {artist}")
        else:
            print(f"✗ Not found: {title} - {artist}")
    # print(track_uris)

    ##############################################
    # Spotipy - Create Playlist for Top 100
    ##############################################

    playlist_name = f"Billboard 100 - {billboard_date_str}"
    spotipy = MySpotipy()
    spotipy.create_playlist(playlist_name, f"Playlist for the week {billboard_date_str}")
    spotipy.add_to_playlist(playlist_name, track_uris)

    ##############################################
    # Results
    ##############################################

    print(f"\n📊 Playlist Statistics:")
    print(f"   Date: {billboard_date_str}")
    print(f"   Found: {len(track_uris)}/{len(top_100)} tracks")
    print(f"   Success rate: {len(track_uris)/len(top_100)*100:.1f}%")
    print(f"   Playlist: {playlist_name}")


if __name__ == "__main__":
    default_date = "2000-08-19"
    
    if len(sys.argv) > 1:
        date = sys.argv[1]
    else:
        user_input = input(f"Enter date (YYYY-MM-DD) [default: {default_date}]: ")
        date_str = user_input if user_input else default_date
    
    main(date_str)

##############################################################################
# DAY 47 - Amazon Price Checker
##############################################################################

"""
Amazon Price Tracker

Check Price. Compare to Target. Email if cheaper.

Camel Camel Camel
https://uk.camelcamelcamel.com/product/B000CSCRHY 
average price over 12 months = £28.67 
live price today on Amazon = £51.60
"""

import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from dotenv import load_dotenv
import os
from notification_manager import NotificationManager

load_dotenv("../../.env")

GU_BARS_URL = "https://www.amazon.co.uk/GU-Chocolate-Outrage-Flavour-Energy/dp/B000CSCRHY"
HEADERS = {"User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
TARGET_PRICE = Decimal('28.67')

def fetch_amazon_page(gu_bars_url, headers):
    """Fetch the Amazon Product Page"""

    response = requests.get(gu_bars_url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_price(website_html):
    """Soup Price Extraction"""

    soup = BeautifulSoup(website_html, 'html.parser')

    try:
        gu_price_whole = soup.find("span", class_="a-price-whole").get_text()
        gu_price_fraction = soup.find("span", class_="a-price-fraction").get_text()
    except AttributeError:
        return "Could not find price on page. Amazon may have changed their HTML structure."

    gu_price = Decimal(f"{gu_price_whole}{gu_price_fraction}")
    return gu_price

def check_and_notify(current_price, target_price, gu_bars_url):
    """Price Check and Email"""

    notifications = NotificationManager()

    if current_price < target_price:
        recipient = os.getenv("RECIPIENT")
        subject = "Amazon Price Alert - Gu Buy Time!"
        message = f"Guud news. The price has dropped to {current_price}. Time to stock up.\n{gu_bars_url}"
        send_email = notifications.send_email(recipient, subject, message)
        return send_email
    else:
        return "No Gu Buy"

def main():
    try:
        website_html = fetch_amazon_page(GU_BARS_URL, HEADERS)
        current_price = extract_price(website_html)
        outcome = check_and_notify(current_price, TARGET_PRICE, GU_BARS_URL)
        print(outcome)
    except (requests.RequestException, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

##############################################################################
# DAY 48 - Selenium Webdriver and Game Playing Bot
##############################################################################

"""
Selenium Webdriver and Game Playing Bot

https://selenium-python.readthedocs.io/

"""

##############################
# Example 1 - Amazon
##############################

GU_BARS_URL = "https://www.amazon.co.uk/GU-Chocolate-Outrage-Flavour-Energy/dp/B000CSCRHY"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(GU_BARS_URL)
pound_price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
pence_price = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

print(f"£{pound_price}.{pence_price}")

# closes the active tab
# driver.close()
# closes the entire browser
driver.quit()

##############################
# Example 2 - Python.org
##############################

URL = "https://www.python.org"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# forms typically use name
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

# find by ID
button = driver.find_element(By.ID, value="submit")
print(search_bar.size)

# find by CSS Selector
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# find by XPATH
jobs_link = driver.find_element(By.XPATH, value='/html/body/div/div[3]/div/section/div[1]/div[4]/p[2]/a')
print(jobs_link.text)

# closes the active tab
# driver.close()
# closes the entire browser
driver.quit()

##############################
# Example 3 - Python.org
##############################

URL = "https://www.python.org"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# find by CSS Selector
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# dictionary comprehension with index as key, from the two lists
events = {n: {time.text: name.text} for n, (time, name) in enumerate(zip(event_times, event_names))}
print(events)

# closes the entire browser
driver.quit()

##############################
# Example 4 - Wikipedia
##############################

URL = "https://en.wikipedia.org/wiki/Main_Page"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# find total articles by CSS Selector
article_count = driver.find_elements(By.CSS_SELECTOR, "a[href='/wiki/Special:Statistics']")
print(article_count[1].text)

article_count.click()

# closes the entire browser
driver.quit()

################################
# Example 5 - Click By Link Text
################################

URL = "https://en.wikipedia.org/wiki/Main_Page"

from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

teahouse = driver.find_element(By.LINK_TEXT, value="Teahouse")
teahouse.click()

# closes the entire browser
driver.quit()

################################
# Example 6 - Input Box Example
################################

URL = "https://en.wikipedia.org/wiki/Main_Page"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# find search box
search = driver.find_element(By.NAME, value="search")
# enter text and retrun
search.send_keys("Python", Keys.ENTER)

# closes the entire browser
driver.quit()

################################
# Example 7 - Webpage Sign Up
################################

URL = "https://secure-retreat-92358.herokuapp.com/"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome Browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

fname.send_keys("Rydon")
lname.send_keys("Man")
email.send_keys("rydonman@mailinator.com")

# instructor
# button = driver.find_element(By.CSS_SELECTOR, value="form button")
button = driver.find_element(By.CSS_SELECTOR, value="button.btn.btn-lg.btn-primary.btn-block")
button.click()

# closes the entire browser
driver.quit()

################################
# Challenge - Cookie Clicker
################################

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://ozh.github.io/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, value="bigCookie")

def click_button(duration):
    round_time = time.time()
    while time.time() - round_time < duration:
        cookie.click()
        time.sleep(0.01)

    upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

    if upgrades:
        upgrades[-1].click()
        print("Purchased an upgrade!")

rounds = 0
while rounds <= 20:
    button = click_button(20)
    rounds -= 1
    print(f"Round {rounds}/20 completed!")


##############################################################################
# DAY 49 - Selenium Gym Class Booking Bot
##############################################################################

"""
Selenium to book fake gym classes

"""

import os
import tempfile
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LOGIN_URL = "https://appbrewery.github.io/gym/"
SCHEDULE_URL = "https://appbrewery.github.io/gym/schedule/"
ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""

days = ["tue", "thu"]
timeslot = "1800"
already_on = 0
waitlist = 0
booked = 0
classes = []

# Chrome profile data
user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_py_profile")

# Chrome setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=chrome_options)

def login(driver, url, email, password):
    driver.get(url)
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    wait = WebDriverWait(driver, timeout=5)

    try:
        email_field = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
        email_field.clear()
        email_field.send_keys(email)

        password_field = wait.until(EC.presence_of_element_located((By.ID, "password-input")))
        password_field.clear()
        password_field.send_keys(password)

        submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit-button")))
        submit_button.click()

        wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

        return True

    except Exception as e:
        print(f"Login unsuccessful: {e}")
        return False

def find_day_container(driver, day):

    selectors = [
        f"div[id*='day-group-today-({day},']",      # Today pattern
        f"div[id*='day-group-tomorrow-({day},']",   # Tomorrow pattern
        f"div[id*='day-group-{day}']"               # Regular day pattern
    ]

    for selector in selectors:
        try:
            return driver.find_element(By.CSS_SELECTOR, selector)
        except:
            continue

    raise Exception(f"Could not find container for day: {day}")

def book_class(container, day, time):

    global already_on
    global waitlist
    global booked
    global classes

    try:
        # find card for time (e.g. 1800)
        gym_class = container.find_element(By.CSS_SELECTOR, f"div[id^='class-card-'][id*='{time}']")
        # find the date (of class)
        gym_class_date = container.find_element(By.CLASS_NAME, "Schedule_dayTitle__YBybs")
        # find the class type
        gym_class_type = container.find_element(By.CSS_SELECTOR, "h3[id^='class-name']")
        # find the button
        gym_class_button = gym_class.find_element(By.CSS_SELECTOR, "button")

        # Check if a class is already booked (button reads "Booked")
        if gym_class_button.text == "Booked":
            classes.append(f"Booked: {gym_class_type.text} on {gym_class_date.text} at {time}")
            already_on += 1
            return True

        # Check if you're on the waitlist (button reads "Waitlisted")
        elif gym_class_button.text == "Waitlisted":
            classes.append(f"Waitlisted: {gym_class_type.text} on {gym_class_date.text} at {time}")
            already_on += 1
            return True

        # Join the waitlist if the class is full (button says "Join Waitlist")
        elif gym_class_button.text == "Join Waitlist":
            gym_class_button.click()
            # print(f"✓ Waitlisted: {gym_class_type.text} on {gym_class_date.text} at {time}")
            waitlist +=1
            classes.append(f"Waitlisted: {gym_class_type.text} on {gym_class_date.text} at {time}")
            return True

        else:
            gym_class_button.click()
            # print(f"✓ Booked: {gym_class_type.text} on {gym_class_date.text} at {time}")
            booked += 1
            classes.append(f"New booking: {gym_class_type.text} on {gym_class_date.text} at {time}")
            return True

    except Exception as e:
        print(f"Booking unsuccessful: {e}")
        return False

def verify_bookings(driver):
    my_bookings = driver.find_element(By.ID, "my-bookings-link")
    my_bookings.click()

    wait = WebDriverWait(driver, timeout=5)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".MyBookings_bookingCard__VRdrR")))

    try:
        booked_classes = driver.find_elements(By.CLASS_NAME, "MyBookings_bookingCard__VRdrR")
        print(booked_classes)
        booked_total = len(booked_classes)

        return booked_total

    except NoSuchElementException:
        return 0

def counters(total_booked):

    total_classes = booked + waitlist + already_on

    if total_classes == total_booked:
        result = "✅ SUCCESS: All bookings verified!"
    else:
        result = "❌ MISSING: Booking mismatch!"

    return f"""
    --- BOOKING SUMMARY ---
    Classes booked: {booked}
    Waitlists joined: {waitlist}
    Already booked/waitlisted: {already_on}
    Total 6pm classes processed: {total_classes}

    --- DETAILED CLASS LIST ---
    {'\n    '.join(classes)}

    --- VERIFICATION RESULT ---
    Found: {total_booked} bookings
    {result}
    """

def retry(func, retries=7):

    for _ in range(retries):
        if func():
            return True

    return False

def main(driver, url, email, password, days, timeslot):

    # login
    retry(lambda: login(driver, url, email, password))

    # book classes
    for day in days:
        container = find_day_container(driver, day)
        booking = retry(lambda: book_class(container, day, timeslot))
        print(booking)

    # verify what is booked
    total_booked = verify_bookings(driver)

    # return counters
    summary = counters(total_booked)
    print(summary)

    #driver.quit()

if __name__ == "__main__":
    main(driver,
         LOGIN_URL,
         ACCOUNT_EMAIL,
         ACCOUNT_PASSWORD,
         days,
         timeslot)


##############################################################################
# DAY 50 - Auto Swipe Bot
##############################################################################

"""
Day 50 - Auto Swipe Bot
Instructor code

Fake photos https://www.thispersondoesnotexist.com/

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = YOUR FACEBOOK LOGIN EMAIL
FB_PASSWORD = YOUR FACEBOOK PASSWORD

driver = webdriver.Chrome()

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()


##############################################################################
# DAY 51 - Twitter Complaints Bot
##############################################################################

"""
Twitter Complaints Bot
"""

from dotenv import load_dotenv
import os
import tempfile
import time
from random import uniform
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Constants
load_dotenv("../../.env")
SPEEDTEST_URL = "https://www.speedtest.net/"
SLA_DOWN = 2500
SLA_UP = 250
TWITTER_URL = "https://twitter.com"
TWITTER_U = os.getenv("TWITTER_U")
TWITTER_PW = os.getenv("TWITTER_PW")

class InternetSpeedTwitterBot:

    def __init__(self):
        # Chrome
        user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_py_profile")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--disable-extensions")

        # Selenium
        self.driver = webdriver.Chrome(options=chrome_options)
        self.test_wait = WebDriverWait(self.driver, timeout=60)
        self.standard_wait = WebDriverWait(self.driver, timeout=5)

        # Properties
        self.up = 0
        self.down = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #self.driver.quit()
        pass

    def get_internet_speed(self):
        try:
            self.driver.get(SPEEDTEST_URL)
            test_button = self.standard_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "start-button")))
            test_button.click()

            try:
                close_popup = self.test_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close-btn")))
                close_popup.click()
                print("Closed popup")
            except:
                print("No popup appeared")

            download = self.standard_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-download-status-value].result-data-large")))
            upload = self.standard_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-upload-status-value].result-data-large")))

            self.down = float(download.text)
            self.up = float(upload.text)

            print(f"Download: {self.down} Mbps")
            print(f"Upload: {self.up} Mbps")
            print(f"SLA - Down: {SLA_DOWN} Mbps, Up: {SLA_UP} Mbps")

            if self.down < SLA_DOWN or self.up < SLA_UP:
                print("⚠️  Speed below SLA! Time to tweet at provider!")
                return True
            else:
                print("✅ Speed meets SLA requirements")
                return False

        except Exception as e:
            return f"Start unsuccessful: {e}"


    def human_delay(self, action_type="default"):
        delays = {
            "typing": (4.5, 8.5),      # Shorter for typing
            "clicking": (0.8, 2.2),    # Medium for clicks
            "loading": (3.0, 6.0),     # Longer for page loads
        }
        min_time, max_time = delays.get(action_type, delays["default"])
        time.sleep(uniform(min_time, max_time))

    def tweet_at_provider(self):
        try:
            self.driver.get(TWITTER_URL)
            print("Navigated to Twitter")

            self.human_delay("clicking")

            login_button = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="loginButton"]')))
            login_button.click()
            print("Login button clicked")

            # Wait for the login modal to appear (no iframe needed)
            login_modal = self.standard_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[role="dialog"]')))
            print("Login modal appeared")

            self.human_delay("loading")

            input_area = self.standard_wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Phone, email address, or username']")))
            self.driver.execute_script("arguments[0].click();", input_area)
            print("Clicked on input area using JavaScript")

            # Wait a moment for the input field to be created
            self.human_delay("typing")

            username = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
            username.send_keys(TWITTER_U)
            print("Username entered")

            self.human_delay("clicking")

            next_button = self.standard_wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]')))
            next_button.click()
            print("Next button clicked")

            self.human_delay("loading")

            password = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="current-password"]')))
            password.send_keys(TWITTER_PW)  # Fixed: use password, not username
            print("Password entered")

            self.human_delay("typing")

            final_login_button = self.standard_wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Log in"]')))
            final_login_button.click()
            print("Final login button clicked")

            # Wait a bit for login to complete
            print("Waiting for login to complete...")

            self.human_delay("loading")

            tweet_box = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))
            tweet_box.send_keys(f"Hey Internet Provider. Why is my internet {self.down}down/{self.up}up when I pay for {SLA_DOWN}down and {SLA_UP}up?")
            print("Tweet text entered")

            self.human_delay("typing")

            tweet_button = self.standard_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')))
            tweet_button.click()
            print("Tweet posted!")

            return "Tweet sent successfully"

        except Exception as e:
            print(f"Twitter automation failed at step: {e}")
            return f"Failed to tweet: {e}"

if __name__ == "__main__":
    with InternetSpeedTwitterBot() as app:
        should_tweet = app.get_internet_speed()

        if should_tweet is True:
            tweet_result = app.tweet_at_provider()
            print(f"Tweet result: {tweet_result}")

        elif should_tweet is False:
            print("No need to complain - speeds are good!")

        else:
            print(f"Error: {should_tweet}")


##############################################################################
# DAY 52 - Instagram Bot To Follow Accounts
##############################################################################

"""
Instagram Bot To Follow Accounts
"""

from dotenv import load_dotenv
import os
import tempfile
import time
from random import randint, uniform
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import WebDriverException

# Constants
load_dotenv("../../.env")
URL = "https://instagram.com"
INSTAGRAM_U = os.getenv("INSTAGRAM_U")
INSTAGRAM_PW = os.getenv("INSTAGRAM_PW")
INSTAGRAM_ACC = ""

class InstaFollower:

    def __init__(self):
        # Chrome
        user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_py_profile")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--disable-extensions")

        # Selenium
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=10)

        # Insta
        self.followers_list = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #self.driver.quit()
        pass

    def human_delay(self, action_type="default"):
        delays = {
            "clicking": (0.8, 2.2),
            "default": (0.9, 3.2),
            "typing": (2.5, 8.5)
        }
        min_time, max_time = delays.get(action_type, delays["default"])
        time.sleep(uniform(min_time, max_time))

    def login(self):
        try:
            # Navigate to Page
            self.driver.get(URL)
            print("Navigated to Instagram")

            # Username field
            try:
                self.human_delay("clicking")
                uname_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Phone number, username or email address']")))
                uname_field.clear()
                self.human_delay("typing")
                uname_field.send_keys(INSTAGRAM_U)
                print("Entered Username")
            except Exception as e:
                print(f"Failed to find Username field: {e}")
                return False

            # Password field
            try:
                pword_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Password']")))
                pword_field.clear()
                self.human_delay("typing")
                pword_field.send_keys(INSTAGRAM_PW)
                print("Entered Password")
            except Exception as e:
                print(f"Failed to find Password field: {e}")
                return False

            # Login button
            try:
                self.human_delay("clicking")
                login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and not(@disabled)]")))
                login_button.click()
                print("Clicked Login")
            except Exception as e:
                print(f"Failed to click Login button: {e}")
                return False

            # Click "Not now" to Save Password
            try:
                save_login_prompt = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now')]")))
                save_login_prompt.click()
                print("Dismissed save login prompt")
            except Exception as e:
                print(f"Failed to click Login button: {e}")
                return False

        except WebDriverException as e:
            print(f"WEBDRIVER ERROR: Browser/connection issue - {e}")
            return False
        except Exception as e:
            print(f"UNEXPECTED ERROR: {type(e).__name__} - {e}")
            return False

    def find_followers(self):
        try:
            # Navigate to Page
            self.human_delay("default")
            self.driver.get(f"{URL}/{INSTAGRAM_ACC}")
            print(f"Navigated to {INSTAGRAM_ACC}'s Page")

            # Open Followers
            try:
                followers_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]")))
                self.human_delay("clicking")
                followers_link.click()
                print("Clicked followers link")
            except Exception as e:
                print(f"Failed to find followers link: {e}")
                return False

            # List Followers
            try:
                print("Waiting for followers modal to load...")
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='heading' and contains(text(), 'Followers')]")))
                print("Followers modal loaded")

                time.sleep(2)  # Give content time to load

                self.followers_list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[.//div[text()='Follow']]")))
                print(f"Found {len(self.followers_list)} users to follow")
            except Exception as e:
                print(f"Failed to create followers list: {e}")
                return False

        except WebDriverException as e:
            print(f"WEBDRIVER ERROR: Browser/connection issue - {e}")
            return False
        except Exception as e:
            print(f"UNEXPECTED ERROR: {type(e).__name__} - {e}")
            return False

    def follow(self):
        max_follows = randint(4, 12)

        # Click each button with delays
        for i, button in enumerate(self.followers_list[:max_follows]):
            try:
                # Scroll to button if needed
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                self.human_delay("clicking")
                button.click()
                print(f"Followed user {i+1}")

            except Exception as e:
                print(f"Failed to follow user {i+1}: {e}")

if __name__ == "__main__":
    with InstaFollower() as app:
        login = app.login()

        if login:
            find_followers = app.find_followers()

            if find_followers:
                follow = app.follow()


##############################################################################
# DAY 53 - Zillow Web Scraping and Data Entry
##############################################################################

"""
Zillow = San Fran, Rent, 3K Max, 1 Bedroom
Use this - https://appbrewery.github.io/Zillow-Clone/

Beautful Soup to Scrape
Selenium to Enter Form
"""

from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import tempfile
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import WebDriverException

# Constants
load_dotenv("../../.env")
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GFORM_URL = os.getenv("D53_GFROM_URL")

def scrape_data(url):
    """Get Zillow Reponse"""
    headers = {
        "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
        }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_info(website_html):
    """Soup List Extraction"""

    soup = BeautifulSoup(website_html, 'html.parser')

    try:
        data = soup.find_all("div", class_="StyledPropertyCardDataWrapper")

        addresses = [item.select_one("address[data-test='property-card-addr']").get_text(strip=True).replace(" |", ",")
                for item in data
                if item.select_one("address[data-test='property-card-addr']")]

        prices = [item.select_one("span[data-test='property-card-price']").get_text(strip=True)[:6]
                for item in data
                if item.select_one("span[data-test='property-card-price']")]

        urls = [item.select_one("a[data-test='property-card-link']")['href']
                for item in data
                if item.select_one("a[data-test='property-card-link']")]

        properties = list(zip(addresses, prices, urls))

        return properties

    except Exception as e:
        print(f"Could not create dictionary. Error: {e}")
        return False

def fill_google_form_by_question_text(driver, question_text, answer):
    """Fill form field by locating the question text first"""
    try:
        # Find the question span
        question_xpath = f"//span[contains(text(), '{question_text}')]"
        question_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, question_xpath)))

        # Find the input container for this question
        container = question_element.find_element(By.XPATH, "./ancestor::div[@jscontroller]")

        # Look for textarea or input field
        try:
            input_field = container.find_element(By.TAG_NAME, "textarea")
        except:
            input_field = container.find_element(By.TAG_NAME, "input")

        input_field.clear()
        input_field.send_keys(answer)
        return True

    except Exception as e:
        print(f"Error filling '{question_text}': {e}")
        return False

def submit_form(url, property_list):
    """Submit form fields and loop"""
    # Chrome
    user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_py_profile")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-extensions")

    # Selenium
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    print("Navigated to Form")

    for address, price, url in property_list:
        # Fill each question by its text
        fill_google_form_by_question_text(driver, "address", address)
        fill_google_form_by_question_text(driver, "price", price)
        fill_google_form_by_question_text(driver, "URL", url)

        # Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, "div[role='button'][aria-label*='Submit']")
        submit_button.click()

        time.sleep(1)

        # Wait for success page to load
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Your response has been recorded')]")))

        # Click "Submit another response"
        submit_another_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Submit another response")))
        submit_another_button.click()

        # Wait for form to reload
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))

        print(f"Successfully submitted: {address}")

    # Quit browser
    driver.quit()

if __name__ == "__main__":
    zillow_data = scrape_data(ZILLOW_URL)
    soup_list = extract_info(zillow_data)
    submit_form(GFORM_URL, soup_list)


##############################################################################
# DAY 54 - WebDev with Flask
##############################################################################

"""
WebDev with Flask

FE Frameworks = Angular, React
BE Frameworks = Node, Django/Flask
FE Languages = HTML, CSS, JS
BE Languages = JS, Java, Python, Ruby etc

Python BEs = Flask, Django, Bottle, CherryPie, Pyramid


https://pythontutor.com/visualize.html#mode=edit
"""

# run hello.py
# export FLASK_APP=hello.py
# flask run

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()


## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()

"""
Objective Create your own decorator function to measure the amount of seconds that a function takes to execute.

Expected Output:
    1695050908.1985211
    fast_function run speed: 0.33974480628967285s
    slow_function run speed: 2.9590742588043213s

Calculating Time

time.time() will return the current time in seconds since January 1, 1970, 00:00:00.

Try running the starting code to see the current time printed.
If you run the code after a while, you'll see a new time printed.

e.g. first run:  1598524371.736911
second run:  1598524436.357875

The time difference = second run - first run  64.62096405029297  (approx 1 minute)

Given the above information, complete the code exercise by printing out the time it takes to run the fast_function() vs the slow_function().

You will need to complete the speed_calc_decorator() function.
 """

import time

def speed_calc_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()

# fast_function run speed: 0.030230998992919922s
# slow_function run speed: 0.3031938076019287s


##############################################################################
# DAY 55 - HTML & URL Parsing in Flask
##############################################################################

"""
HTML & URL Parsing in Flask
Higher / Lower Game
"""

# Decorator functions can be used for Routing

# https://www.mysite.com/
# https://www.mysite.com/bye

from flask import Flask

app = Flask(__name__)

# Decorator functions can be used for Routing
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Thanks for coming, goodbye!</p>"

# Decorator functions with Variables can be used for advanced Routing
@app.route("/<name>")
def greet(name):
    return f"Hello, {name}!"

# Decorator functions using Path
@app.route("/username/<path:name>/")
def greeting(name):
    return f"Hello, {name}!"
# http://127.0.0.1:5000/username/james/112/
# Hello, james/112!

# Decorator functions with multiple variables
@app.route("/username/<name>/<int:number>")
def age(name, number):
    return f"Hello, {name}, you are {number} years old!"

# Debug mode autoreloads when file saved
if __name__ == "__main__":
    app.run(debug=True)


"""
Example Decorators
"""

from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        bold = function()
        return f"<b>{bold}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        emphasis = function()
        return f"<i>{emphasis}</i>"
    return wrapper

def make_underline(function):
    def wrapper():
        italic = function()
        return f"<u>{italic}</u>"
    return wrapper

@app.route("/")
@make_bold
@make_emphasis
@make_underline
def hello_world():
    return "Hello, World!"

# Debug mode autoreloads when file saved
if __name__ == "__main__":
    app.run(debug=True)


"""
## Advanced Python Decorator Functions
"""

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("James")
new_user.is_logged_in = True
create_blog_post(new_user)

"""
Advanced Decorators

Create a logging_decorator() which is going to print the name of the function that was called,
the arguments it was given and finally the returned output:
    You called a_function(1,2,3)
    It returned: 6

The value 6 is the return value of the function.

Don't change the body of a_function.
"""

def logging_decorator(func):
    def wrapper(*args):
        result = func(*args)
        print(f"You called {func.__name__}{args}")
        print(f"It returned: {result}")
        return result
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1,2,3)

"""
Final Project - Higher or Lower URLs

Now it's time to complete the final project of the day, the higher lower game that we created in Day 14, but now with a real website.

1. Create a new project in PyCharm called higher-lower, add a server.py file.
2. Create a new Flask application where the home route displays an

<h1> that says "Guess a number between 0 and 9" and display a gif of your choice from giphy.com.

Alternatively use the one I found on Giphy: https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif

3. Generate a random number between 0 and 9 or any range of numbers of your choice.
4. Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9"
and checks that number against the generated random number.
If the number is too low, tell the user it's too low, same with too high or if they found the correct number.
Try to make the <h1> text a different colour for each page.  e.g. If the random number was 5:

    3 is too low:
    7 is too high:
    and 5 is just right:

Here are the GIF URLs I used, but it's way more fun finding your own on giphy.com
High: https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif
Low: https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif
Correct: https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif
"""

from flask import Flask
import random

answer = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <h1>Guess a number between 0 and 9</h1>
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Number guessing game'>
        """

@app.route("/<int:number>")
def guess(number):
    if number > answer:
        return """
            <h1 style='color: red'>You guessed too high</h1>
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='Too high'>
            """
    elif number < answer:
        return """
            <h1 style='color: blue'>You guessed too low</h1>
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='Too low'>
            """
    else:
        return """
            <h1 style='color: green'>You are correct!</h1>
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='Correct'>
            """

if __name__ == "__main__":
    app.run(debug=True)


##############################################################################
# DAY 56 - Static Files, HTML/CSS File Rendering
##############################################################################

"""
Static Files, HTML/CSS File Rendering
Project is Personal Namecard Site

HTML files go in the templates folder
Static files such as media, css etc. go in static folder

In Chrome Dev for real time field editing
Then save the page

document.body.contentEditable=true
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def website():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


##############################################################################
# DAY 57 - URL building and templating with Jinja in Flask
##############################################################################

"""
URL building and templating with Jinja in Flask

Jinja is a templating language

Project is to build a simple blog with posts based on the template
"""

from flask import Flask
from flask import render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def website():
    random_number = random.randint(1, 50)
    current_year = datetime.date.today().strftime("%Y")
    return render_template("index.html", num=random_number, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Jinja Ninja</title>
#     <link rel="stylesheet" href="static/style.css" />
# </head>
# <body>
#     <h1>I am Jinja</h1>
#     <p>This is using Jinja and Python to calculate 5 * 6 = {{ 5 * 6 }}</p>
#     <p>Random number between 1 and 50 generated by randint: {{ num }}</p>
# </body>
# <footer>
#     <p>© {{ year }} - built by James. The year is dynamically generated with the timedate module.</p>
# </footer>
# </html>

from flask import Flask
from flask import render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def website():
    random_number = random.randint(1, 50)
    current_year = datetime.date.today().strftime("%Y")
    return render_template("index.html", num=random_number, year=current_year)

@app.guess("/guess")
def guess()

print(f"Hi James")
gender = "https://api.agify.io?<name>"
print(f"I think you are {gender}")
age = "https://api.genderize.io?<name>"
print(f"And maybe {age} years old")


if __name__ == "__main__":
    app.run(debug=True)


"""
Guess Example
"""

from flask import Flask
from flask import render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def website():
    # number
    random_number = random.randint(1, 50)

    # year
    current_year = datetime.date.today().strftime("%Y")
    return render_template("index.html",
                           num=random_number,
                           year=current_year
                           )

@app.route("/guess/<name>")
def guess(name):
    # name
    upper_name = name.title()

    # gender
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    guessed_gender = gender_response.json()["gender"]

    # age
    age_response = requests.get(f"https://api.agify.io?name={name}")
    guessed_age = age_response.json()["age"]

    # year
    random_number = random.randint(1, 50)
    current_year = datetime.date.today().strftime("%Y")

    return render_template("guess.html",
                           name = upper_name,
                           gender = guessed_gender,
                           age = guessed_age,
                           year = current_year
                           )

@app.route("/blog/<num>")
def get_blog(num):
    #blogs
    blogs_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = blogs_response.json()
    return render_template("blog.html",
                           posts = all_posts
                            )

if __name__ == "__main__":
    app.run(debug=True)

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Jinja Ninja Blog</title>
#     <link rel="stylesheet" href="static/style.css" />
# </head>
# <body>
#     <h1>I am Jinja Blog</h1>
#     {% for blog_post in posts: %}
#         <h2>{{ blog_post["title"] }}</h1>
#         <h3>{{ blog_post["subtitle"] }}</h2>
#     {% endfor %}
# <a href="{{ url_for('get_blog', num=3) }}">Go To Blog</a>
# </body>
# <footer>
# </footer>
# </html>


##############################################################################
# DAY 58 - Bootstrap
##############################################################################

"""
Bootstrap

############################
# Bootstrap Columns Overview
############################

Bootstrap uses a 12-column grid system that's responsive and flexible for creating layouts.
Basic Structure
html<div class="container">
  <div class="row">
    <div class="col-md-6">Half width</div>
    <div class="col-md-6">Half width</div>
  </div>
</div>
Key Classes

Container: .container (fixed width) or .container-fluid (full width)
Row: .row - wraps columns, creates horizontal groups
Columns: .col-{breakpoint}-{size} where size is 1-12

Breakpoints

xs - Extra small (<576px)
sm - Small (≥576px)
md - Medium (≥768px)
lg - Large (≥992px)
xl - Extra large (≥1200px)

Common Patterns
html<!-- Equal width columns -->
<div class="col">Auto width</div>
<div class="col">Auto width</div>

<!-- Specific sizes -->
<div class="col-md-8">8 columns wide</div>
<div class="col-md-4">4 columns wide</div>

<!-- Responsive -->
<div class="col-12 col-md-6 col-lg-4">
  Full on mobile, half on tablet, third on desktop
</div>
Utilities

Offset: .offset-md-2 (push column right)
Order: .order-md-2 (change visual order)
Gutters: .g-0 (no gaps), .gx-3 (horizontal gaps), .gy-2 (vertical gaps)

Remember: Columns must always be inside a .row, and rows should be in a .container.

############################
# Bootstrap Buttons Overview
############################

Basic Button Classes
html<!-- Primary button -->
<button type="button" class="btn btn-primary">Primary</button>

<!-- Other color variants -->
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>
Button Sizes
html<button class="btn btn-primary btn-lg">Large</button>
<button class="btn btn-primary">Default</button>
<button class="btn btn-primary btn-sm">Small</button>
Button States
html<!-- Outline buttons -->
<button class="btn btn-outline-primary">Outline</button>

<!-- Disabled -->
<button class="btn btn-primary" disabled>Disabled</button>

<!-- Active state -->
<button class="btn btn-primary active">Active</button>
Block & Group
html<!-- Full width -->
<button class="btn btn-primary d-grid">Block Button</button>

<!-- Button group -->
<div class="btn-group">
  <button class="btn btn-primary">Left</button>
  <button class="btn btn-primary">Middle</button>
  <button class="btn btn-primary">Right</button>
</div>
Works on <button>, <a>, and <input> elements with .btn class.


############################
# Bootstrap Cards Overview
############################

Basic Card Structure
html<div class="card">
  <div class="card-header">
    Card Header
  </div>
  <div class="card-body">
    <h5 class="card-title">Card Title</h5>
    <p class="card-text">Some quick example text to build on the card title.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
  <div class="card-footer text-muted">
    Card Footer
  </div>
</div>
Card with Image
html<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
Card Grid
html<div class="row">
  <div class="col-md-4">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Card 1</h5>
        <p class="card-text">Content here.</p>
      </div>
    </div>
  </div>
  <div class="col-md-4">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Card 2</h5>
        <p class="card-text">Content here.</p>
      </div>
    </div>
  </div>
</div>
Key Classes

.card - Main container
.card-body - Main content area
.card-title - Card title styling
.card-text - Card text styling
.card-header / .card-footer - Top/bottom sections
.card-img-top / .card-img-bottom - Images

Cards are flexible and can contain headers, footers, images, lists, and any content.


############################
# Bootstrap Navs Overview
############################

Basic Nav (Tabs Style)
html<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled" href="#">Disabled</a>
  </li>
</ul>
Pills Style
html<ul class="nav nav-pills">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
</ul>
Vertical Nav
html<ul class="nav nav-pills flex-column">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
</ul>
Nav with Dropdown
html<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#">Dropdown</a>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Action</a></li>
      <li><a class="dropdown-item" href="#">Another action</a></li>
    </ul>
  </li>
</ul>
Nav Alignment
html<!-- Centered -->
<ul class="nav nav-tabs justify-content-center">
  <!-- nav items -->
</ul>

<!-- Right aligned -->
<ul class="nav nav-tabs justify-content-end">
  <!-- nav items -->
</ul>
Key Classes

.nav - Base nav class
.nav-tabs - Tab style
.nav-pills - Pill style
.nav-item - Nav item wrapper
.nav-link - Nav link styling
.active - Active state
.disabled - Disabled state

############################
# Bootstrap Spacing Overview
############################

Spacing Classes Format
.{property}{sides}-{size} or .{property}{sides}-{breakpoint}-{size}
Properties

m - margin
p - padding

Sides

t - top
b - bottom
s - start (left in LTR)
e - end (right in LTR)
x - horizontal (left & right)
y - vertical (top & bottom)
(no letter) - all sides

Sizes

0 - 0
1 - 0.25rem
2 - 0.5rem
3 - 1rem
4 - 1.5rem
5 - 3rem
auto - auto

Examples
html<!-- Margins -->
<div class="m-3">Margin all sides</div>
<div class="mt-2">Margin top</div>
<div class="mx-auto">Margin horizontal auto (center)</div>
<div class="ms-4">Margin start (left)</div>

<!-- Padding -->
<div class="p-3">Padding all sides</div>
<div class="px-2">Padding horizontal</div>
<div class="py-4">Padding vertical</div>

<!-- Responsive -->
<div class="m-2 m-md-4">Small margin on mobile, larger on medium+</div>

<!-- Remove spacing -->
<div class="m-0">No margin</div>
<div class="p-0">No padding</div>
Common Patterns

mx-auto - Center horizontally
mb-3 - Bottom margin
px-4 py-2 - Horizontal and vertical padding
me-2 - Right margin (between elements)

"""

##############################################################################
# DAY 59 - Flask and Bootstrap
##############################################################################

"""
Flask Templates with a Bootstrap Template

Blog
Dynamic Posts
Bootstrap
"""

############################################################
# Website Template
# https://startbootstrap.com/previews/clean-blog
############################################################

from flask import Flask, render_template
import requests

app = Flask(__name__)

blogs_api = "https://api.npoint.io/e9d9c46c7277cb7135c7"
blog_data = requests.get(blogs_api).json()

@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html", all_posts = blog_data)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = next((post for post in blog_data if post['id'] == index), None)
    return render_template("post.html", post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)


##############################################################################
# DAY 60 - Capturing Input
##############################################################################

"""
Flask - Capturing Input; e.g. Contact Forms
"""

############################################################
# Website Template
# https://startbootstrap.com/previews/clean-blog
############################################################

from flask import Flask, render_template, request
import requests
from notification_manager import NotificationManager

blogs_api = "https://api.npoint.io/e9d9c46c7277cb7135c7"
blog_data = requests.get(blogs_api).json()

app = Flask(__name__)
notifications = NotificationManager()

@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html", all_posts = blog_data)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        notifications.send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)    
    return render_template("contact.html", msg_sent=False)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = next((post for post in blog_data if post['id'] == index), None)
    return render_template("post.html", post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)


##############################################################################
# DAY 61 - Bootstrap & Flask
##############################################################################

"""
Using WTForms for Username & Password.

We're using template inheritance from Base.html to Success.html and Denied.html.

You can override inherited elements by using Super Blocks (super.init()).

Using flask_bootstrap too.
"""

from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import random
import string
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
app.secret_key = random_string

demo_user = ""
demo_pass = ""

class ContactForm(FlaskForm):
    email = EmailField(
        label='Email', 
        validators=[
            DataRequired(),
            Email(message='Please enter a valid email address')
        ]
    )
    password = PasswordField(
        label='Password', 
        validators=[
            DataRequired(),
            Length(min=8, message='Password must be at least 8 characters long')
        ]
    )
    login = SubmitField('Login')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    form = ContactForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == demo_user and password == demo_pass:
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template('login.html', form=form)

@app.route('/success', methods=["GET", "POST"])
def login_success():
    return render_template('success.html')
    
@app.route('/denied', methods=["GET", "POST"])
def login_denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)

##############################################################################
# DAY 62 - Flask, WTForms, Bootstrap and CSV
##############################################################################

"""
Flask, WTForms, Bootstrap and CSV
"""

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

##############################################################################
# DAY 63 - Flask and SQLite - Book Ranking
##############################################################################

"""
Flask and SQLite for a Book Ranking Website
Add and Delete record
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float

app = Flask(__name__)

# SQLAlchemy Base class definition
class Base(DeclarativeBase):
  pass

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# ORM Model definition
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250),nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Database table creation
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(
                title = request.form['title'],
                author = request.form['author'],
                rating = request.form['rating']
            )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
      
    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_rating(id):
    book = db.session.get(Book, id)
    if request.method == "POST":
        book.rating = request.form['new_rating']
        db.session.commit()  
        return redirect(url_for('home'))
    return render_template("edit.html", book=book)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    book = db.session.get(Book, id)
    if book:
        db.session.delete(book)
        db.session.commit()  
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)


##############################################################################
# DAY 64 - Flask and SQLite - Movie Site
##############################################################################

"""
Create a moving raking website with Flask, Jinja, Bootstrap & SQLite

Movie lookup on TMDB with API integration

Dynamic ordering based on rating

Add, edit, delete

"""

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os


#################################################
# Setup App
#################################################

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")
Bootstrap5(app)


#################################################
# Config Database
#################################################

class Base(DeclarativeBase):
  pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()


#################################################
# Create Forms
#################################################

class EditForm(FlaskForm):
    rating = IntegerField("Your Rating - 0 to 10", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField('Add Movie')


#################################################
# TMDB Movie Search
#################################################

TMDB_TOKEN = os.getenv("TMDB_TOKEN")

def search_movie(film):
    url = "https://api.themoviedb.org/3/search/movie"

    headers = {
        "Authorization": f"Bearer {TMDB_TOKEN}"
    } 

    params = {
        "query": film,
        "include_adult": "true"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    movies = data['results']
    return movies


#################################################
# Flask
#################################################

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.asc()))
    all_movies = result.scalars().all()
    return render_template("index.html", all_movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    id = request.args.get("id")
    movie = db.get_or_404(Movie, id)
    if form.validate_on_submit():
        movie.rating = int(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))  
    return render_template("edit.html", form=form)


@app.route("/delete", methods=["GET"])
def delete():
    id = request.args.get("id")
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit() 
    return redirect(url_for('home'))  


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        film = add_form.title.data
        search_results = search_movie(film)
        return render_template("select.html", results=search_results)
    return render_template("add.html", form=add_form)


@app.route("/select", methods=["GET", "POST"])
def select():
    id = request.args.get("id")
    url = f"https://api.themoviedb.org/3/movie/{id}"
    response = requests.get(url, headers={"Authorization": f"Bearer {TMDB_TOKEN}"})
    data = response.json()

    new_movie = Movie(
        title=data['title'],
        year=data['release_date'][:4],
        description=data['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        rating=0,
        review="placeholder"
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", id=new_movie.id))


#################################################
# Application Entry Point
#################################################

if __name__ == '__main__':
    app.run(debug=True)



##############################################################################
# DAY 65 - Web Design & Canva
##############################################################################

"""
Core Web Design Features

Four Pillars of web design: Colour Theory, Typography, UI Design, UX Design

https://www.canva.com/design/DAG02HGC1t0/MUlpL9pSCQhUdtHhfaMLVA/edit?ui=e30

"""

##############################################
# Colour Palette
##############################################


"""
Color Palette Moods for Web Design
Warm Palettes

Reds/Oranges/Yellows: Energetic, passionate, exciting, urgent
Creates feelings of warmth, enthusiasm, and action
Often used for calls-to-action, food brands, entertainment
Can increase heart rate and create sense of urgency

Cool Palettes

Blues/Greens/Purples: Calming, trustworthy, professional, serene
Evokes stability, reliability, and tranquility
Popular for corporate sites, healthcare, finance, tech
Blues especially associated with trust and competence

Neutral Palettes

Grays/Beiges/Whites/Blacks: Sophisticated, minimal, timeless, balanced
Provides clean backdrop and emphasizes content
Common in luxury brands, portfolios, modern design
Creates sense of elegance and simplicity

Vibrant/Saturated

Bold, High-Saturation Colors: Playful, youthful, dynamic, creative
Grabs attention and conveys energy
Effective for brands targeting younger audiences, creative industries
Can feel fun but may overwhelm if overused

Muted/Desaturated

Soft, Low-Saturation Colors: Gentle, sophisticated, vintage, approachable
Creates calm, refined atmosphere
Works well for wellness, lifestyle, artisanal brands
Feels more subtle and easier on the eyes

Monochromatic

Single Hue with Variations: Cohesive, harmonious, focused, elegant
Creates unified look with different shades/tints of one color
Emphasizes hierarchy through lightness/darkness
Professional and visually organized

Key Considerations

Context matters: Same color can feel different depending on saturation, surrounding colors, and cultural context
Accessibility: Ensure sufficient contrast for readability
Brand alignment: Colors should reflect brand personality and values

"""

##############################################
# By Colour
##############################################

"""
Color Moods for Web Design

###############
### Red
###############

Emotions: Passion, energy, urgency, excitement, danger, love, power
Psychological Effects:

Increases heart rate and creates sense of urgency
Grabs attention immediately
Stimulates appetite

Best Used For:

Call-to-action buttons ("Buy Now", "Sale")
Food and restaurant websites
Entertainment and gaming
Emergency or warning messages
Brands wanting bold, energetic presence

Cautions: Can feel aggressive or overwhelming if overused; may signal error or danger

###############
### Yellow
###############
Emotions: Happiness, optimism, warmth, creativity, caution, energy
Psychological Effects:

Most visible color to human eye
Stimulates mental activity and energy
Creates cheerful, welcoming feeling
Can cause eye strain in large amounts

Best Used For:

Highlighting important information
Children's products/websites
Creative or playful brands
Drawing attention to specific elements
Warnings or caution areas

Cautions: Pure bright yellow can be harsh; often works better in softer tones or as accent color

###############
### Green
###############
Emotions: Growth, nature, health, tranquility, freshness, prosperity, harmony
Psychological Effects:

Most restful color for eyes
Associated with balance and stability
Conveys environmental consciousness
Suggests wealth and success

Best Used For:

Environmental/eco-friendly brands
Health and wellness sites
Financial services (money association)
Organic/natural products
Call-to-action buttons (secondary to red)

Variations:

Dark green: wealth, prestige, tradition
Light green: calm, freshness, youth
Olive green: peace, earthiness

###############
### Blue
###############
Emotions: Trust, stability, calm, professionalism, security, intelligence, sadness
Psychological Effects:

Most universally liked color
Lowers heart rate and reduces stress
Creates sense of reliability
Suppresses appetite

Best Used For:

Corporate and professional websites
Technology companies
Healthcare and medical sites
Financial institutions
Social media platforms
Productivity tools

Variations:

Navy blue: authority, confidence, power
Light blue: calm, peace, freedom
Bright blue: energy, clarity, innovation

Cautions: Can feel cold or impersonal; avoid for food brands

###############
### Purple
###############
Emotions: Luxury, creativity, spirituality, mystery, royalty, imagination, wisdom
Psychological Effects:

Historically associated with wealth and royalty
Stimulates creativity and problem-solving
Balances calm (blue) and energy (red)
Rare in nature, feels special

Best Used For:

Luxury and premium brands
Beauty and cosmetics
Creative industries
Spiritual or meditation sites
Youth brands (especially lavender/lighter purples)
Innovation and imagination-focused companies

Variations:

Deep purple: sophistication, luxury, mystery
Light purple/Lavender: feminine, nostalgic, romantic
Violet: creativity, uniqueness

Cautions: Can feel overly feminine or frivolous in some contexts; use carefully in corporate settings

##############################
# Quick Reference for Combinations
##############################
Red + Yellow: Fast food, energy, excitement
Blue + Green: Healthcare, natural tech, trustworthy eco-brands
Purple + Gold: Ultimate luxury
Blue + White: Clean, professional, tech
Green + Brown: Organic, natural, earthy
"""


##############################
# Analogous Colors
##############################

"""
What Are Analogous Colors?

Colors that sit next to each other on the color wheel (typically 2-4 adjacent colors)
Examples:

Blue, blue-green, green
Red, red-orange, orange
Yellow, yellow-green, green


Visual Characteristics
Harmonious & Cohesive

Naturally pleasing to the eye
Low contrast between colors
Creates smooth visual flow

One Dominant Color

Usually choose one color as primary
Others act as supporting/accent colors
Creates clear hierarchy


Mood & Effect
Calming & Unified

Less visual tension than complementary schemes
Feels serene and comfortable
Easy to look at for extended periods

Natural Feel

Often mirrors color combinations found in nature
Sunset: red-orange-yellow
Forest: yellow-green-blue-green
Ocean: blue-green-blue-purple


Best Used For

Backgrounds and sections that need to feel cohesive
Nature/organic brands wanting natural harmony
Calming interfaces (wellness, meditation, healthcare)
Creating depth without harsh contrast
Gradient designs with smooth transitions


Web Design Tips
Pros:

Easy to create visually pleasing designs
Low risk of color clashing
Professional and polished look

Cons:

Can lack visual excitement or punch
May need neutral color (white/gray/black) for contrast
Important elements might not stand out enough

Pro Tip: Use the 60-30-10 rule

60% dominant color
30% supporting color
10% accent color


Common Analogous Combinations

Warm: Red → Orange → Yellow
Cool: Blue → Blue-Purple → Purple
Fresh: Yellow → Yellow-Green → Green
Sunset: Orange → Red-Orange → Red
Ocean: Blue → Blue-Green → Green
"""


##############################
# Complementary Colors
##############################

"""

What Are Complementary Colors?

Colors that sit directly opposite each other on the color wheel
Examples:

Red ↔ Green
Blue ↔ Orange
Yellow ↔ Purple
Red-Orange ↔ Blue-Green


##############
# Visual Characteristics
##############

##############
High Contrast & Vibrant

Maximum color contrast possible
Creates visual tension and energy
Colors make each other appear more intense

##############
Eye-Catching

Instantly grabs attention
Creates strong focal points
Very dynamic when placed side-by-side

##############
# Mood & Effect
###############

##############
Energetic & Bold

Creates excitement and vibrancy
Feels dynamic and active
Can be jarring if not balanced properly

##############
Balanced Opposition

Warm vs Cool contrast
Creates visual equilibrium
Naturally draws the eye


Best Used For

Call-to-action buttons (stand out dramatically)
Sports brands wanting energy and competition
Drawing attention to specific elements
Creating visual pop in designs
Highlighting important information
Brand differentiation (memorable combinations)


##############
# Web Design Tips
##############

Pros:

Maximum visual impact
Excellent for emphasis and hierarchy
Memorable and distinctive
Creates clear focal points

Cons:

Can be overwhelming or chaotic
May feel too intense for long viewing
Requires careful balance
Accessibility concerns if not managed

Pro Tip: Use the 80-20 or 90-10 rule

80-90% one color (dominant)
10-20% complementary color (accent)
Avoid 50-50 splits (too jarring)


##############
# Making It Work
##############

Tone It Down:

Use desaturated/muted versions for softer look
Add neutrals (white, gray, black) to buffer
Use complementary color sparingly as accent only

Increase Readability:

Never place complementary colors directly adjacent for text
Use neutral backgrounds for text
Ensure sufficient contrast ratios for accessibility


##############
# Common Complementary Combinations
###############

Red ↔ Green: Christmas, bold, natural
Blue ↔ Orange: Sports, tech, energetic
Yellow ↔ Purple: Luxury contrast, creative
Teal ↔ Coral: Modern, fresh, vibrant
Navy ↔ Gold: Sophisticated, premium


##############
# Quick Comparison
##############

Analogous       Complementary
Harmonious      High contrast
Calming         Energetic
Subtle          Bold
Easy on eyes    Attention-grabbing
Low risk        High impact
"""

##############################################
# Typography
##############################################

"""
Typography - High Level Overview

Major Typeface Categories

##############
# Serif
##############

Characteristics: Small decorative strokes (serifs) at the ends of letters
Mood: Traditional, trustworthy, authoritative, elegant, established
Best Used For:

Long-form body text (print and digital)
Traditional/established brands
Publishing, news, editorial
Legal, financial, academic sites
Print materials (highly readable)

Examples: Times New Roman, Georgia, Garamond, Merriweather
Digital Note: Works well at larger sizes; ensure good rendering at small sizes on screens

##############
# Sans Serif
##############

Characteristics: Clean lines without decorative strokes; "sans" = without
Mood: Modern, clean, minimal, approachable, friendly, straightforward
Best Used For:

Digital interfaces and UI elements
Body text on screens
Tech and startup brands
Modern, minimalist designs
Mobile applications
Headlines and navigation

Examples: Helvetica, Arial, Open Sans, Roboto, Inter
Digital Note: Generally most readable on screens; dominates web design

##############
# Script
##############

Characteristics: Mimics handwriting or calligraphy; flowing, connected letters
Mood: Elegant, feminine, creative, personal, luxurious, romantic
Best Used For:

Logos and branding (sparingly)
Wedding/event websites
Luxury or boutique brands
Decorative headlines only
Invitations and certificates
Beauty and fashion sites

Examples: Brush Script, Pacifico, Dancing Script, Great Vibes
Cautions:

Never use for body text (illegible)
Use sparingly and at larger sizes
Poor accessibility at small sizes


##############
# Display/Decorative
##############

Characteristics: Highly stylized, unique, attention-grabbing; designed for impact
Mood: Creative, bold, unique, playful, distinctive (varies widely by style)
Best Used For:

Headlines and titles only
Branding and logos
Posters and hero sections
Creative/artistic projects
Making bold statements
Short text that needs impact

Examples: Impact, Bebas Neue, Lobster, Playfair Display
Cautions:

Never for body text
Use very sparingly
Can quickly feel dated or gimmicky


##############
# Monospace
##############

Characteristics: Each character occupies the same horizontal space (fixed-width)
Mood: Technical, precise, retro, code-like, systematic
Best Used For:

Code snippets and technical documentation
Developer/tech brands
Typewriter/retro aesthetics
Data tables and alignment-critical text
Terminal/command-line interfaces

Examples: Courier, Consolas, Monaco, Source Code Pro
Digital Note: Essential for displaying code; rarely used for regular body text

##############
# Quick Selection Guide
##############

For Readability: Sans Serif (digital), Serif (print/long-form)
For Trust/Authority: Serif
For Modern/Clean: Sans Serif
For Luxury/Elegance: Serif or Script (minimal use)
For Tech/Innovation: Sans Serif or Monospace
For Creativity: Display or Script (headlines only)

##############
# Web Design Best Practices
##############

Hierarchy Rule:

Maximum 2-3 typefaces per site
Pair complementary styles (e.g., Serif headline + Sans Serif body)

Readability:

Body text: 16px minimum
Line height: 1.5-1.7 for body text
Line length: 50-75 characters optimal

Pairing Formula:

Contrast: Pair different categories (Serif + Sans Serif)
Harmony: Share similar proportions or mood
Hierarchy: Clear distinction between headline and body

##############
# Common Successful Pairings
##############

Playfair Display (Serif) + Open Sans (Sans Serif): Elegant + Modern
Montserrat (Sans Serif) + Merriweather (Serif): Clean + Readable
Bebas Neue (Display) + Roboto (Sans Serif): Bold + Functional
Lora (Serif) + Lato (Sans Serif): Classic + Contemporary
"""

##############################################
# A Web UI Design Principles & Best Practices
## Reading blocks; typically 40-60 char for easy readability
##############################################

"""
######################
# Core Principles
######################

Clarity & Simplicity
######################

Remove unnecessary elements - every component should serve a purpose
Use clear, concise language and intuitive labels
Avoid overwhelming users with too many choices at once


Consistency
######################

Maintain uniform patterns across the interface (colors, typography, spacing, interactions)
Follow platform conventions and established design systems
Keep navigation predictable throughout the site

Visual Hierarchy
######################

Guide attention with size, color, contrast, and positioning
Most important elements should be most prominent
Use whitespace strategically to create breathing room

Responsive Design
######################

Design mobile-first, then scale up
Ensure functionality across all device sizes
Consider touch targets (minimum 44x44px for mobile)

######################
Best Practices
######################

Navigation
######################

Keep main navigation visible and accessible
Limit top-level menu items (5-7 max)
Show users where they are (breadcrumbs, active states)

Performance
######################

Optimize images and assets for fast loading
Lazy load content when appropriate
Provide loading indicators for slow operations

Accessibility
######################

Use sufficient color contrast (WCAG AA minimum: 4.5:1 for text)
Support keyboard navigation
Include descriptive alt text for images
Don't rely on color alone to convey information

Interaction Design
######################

Provide immediate feedback for user actions
Use familiar UI patterns (buttons look clickable)
Make interactive elements obvious with hover/focus states
Keep forms short and validate in real-time

Typography
######################

Use 2-3 fonts maximum
Maintain readable font sizes (16px+ for body text)
Ensure adequate line height (1.5 for body text)

Call-to-Actions
######################

Make primary actions prominent and obvious
Use action-oriented language ("Get Started" vs "Submit")
Create visual contrast for important buttons

"""

##############################################
# Web UX Design Principles & Best Practices
##############################################

"""
######################
# Core Principles
######################

User-Centered Design
######################

Design for your actual users, not yourself
Base decisions on user research and data, not assumptions
Consider user goals, context, and pain points throughout

Usability
######################

Make interfaces intuitive and easy to learn
Minimize cognitive load - don't make users think unnecessarily
Reduce steps required to complete tasks

Accessibility for All
######################

Design for diverse abilities, ages, and technical skill levels
Consider assistive technologies from the start
Follow WCAG guidelines and inclusive design principles

Feedback & Communication
######################

Always inform users what's happening (loading, errors, success)
Use clear error messages that explain how to fix issues
Provide confirmation for important actions

######################
# Best Practices
######################

Information Architecture
######################

Organize content logically based on user mental models
Use clear categorization and labeling
Implement effective search when content is extensive
Keep important content within 3 clicks

User Research & Testing
######################

Conduct usability testing with real users regularly
Create user personas based on actual data
Map user journeys to identify friction points
A/B test significant design decisions

Content Strategy
######################

Write for scannability (headings, short paragraphs, bullet points)
Front-load important information
Use plain language, avoid jargon
Provide content in the format users expect

Forms & Input
######################

Only ask for essential information
Use appropriate input types (date pickers, dropdowns)
Provide inline validation with helpful error messages
Show progress indicators for multi-step forms
Allow easy error correction

Progressive Disclosure
######################

Show only necessary information initially
Reveal complexity gradually as needed
Use tooltips, expandable sections, and modals strategically

Error Prevention & Recovery
######################

Design to prevent errors before they happen
Provide undo options for destructive actions
Use confirmations for irreversible actions
Make error recovery straightforward

Performance & Speed
######################

Optimize perceived performance (skeleton screens, optimistic UI)
Set user expectations for wait times
Prioritize above-the-fold content loading

Mobile UX Considerations
######################

Design for thumb-friendly zones
Minimize text input requirements
Consider offline functionality
Respect mobile data and battery constraints

Trust & Security
######################

Be transparent about data collection
Provide clear privacy controls
Use secure connections (HTTPS)
Display trust signals (security badges, reviews)

Emotional Design
######################

Create delightful micro-interactions
Use appropriate tone and personality
Design empty states thoughtfully
Celebrate user achievements

######################
# Key Methodologies
######################

Design Thinking Process
######################

Empathize → Define → Ideate → Prototype → Test

Lean UX
######################

Build-Measure-Learn cycles
Focus on outcomes over deliverables
Collaborate cross-functionally

Jobs-to-be-Done Framework
######################

Understand what users are trying to accomplish
Design solutions around user goals, not features


######################
# F-Layout & Z-Layout Patterns
######################

F-Layout Pattern
######################

What It Is
######################

Users scan content in an F-shaped pattern
Based on eye-tracking studies showing how people read web pages
Common on text-heavy pages (blogs, articles, search results)

The Pattern
######################

Horizontal movement across the top (header/navigation)
Second horizontal movement slightly down the page (subheading/intro)
Vertical movement down the left side, scanning for keywords

When to Use
######################

Content-heavy websites (news sites, blogs)
Search engine results pages
List-based content
Text-focused designs

Best Practices
######################

Place most important information in the top-left area
Use compelling headlines at the top
Left-align text and key elements
Front-load paragraphs with important keywords
Use bullet points and subheadings on the left
Place secondary content/ads on the right (less attention)

Structure
[====================] ← Top horizontal bar (logo, nav)
[==========]           ← Second horizontal scan
[===]
[===]                  ← Vertical scan down left
[===]
[==]

######################
# Z-Layout Pattern
######################

What It Is
######################

Users scan in a Z-shaped pattern
Eyes move horizontally across top, diagonally down, then horizontally across bottom
Common on simpler, less text-heavy pages

The Pattern
######################

Top-left to top-right (header, logo to navigation/CTA)
Diagonal down-left (scanning middle content)
Bottom-left to bottom-right (footer, final CTA)

When to Use
######################

Landing pages with minimal text
Simple homepages
Registration/signup pages
Promotional pages
Pages with clear conversion goals

Best Practices
######################

Place logo top-left
Put primary CTA or key navigation top-right
Guide eye with visual hierarchy along the Z-path
Place secondary CTA bottom-right
Use visual elements (images, arrows) to reinforce the Z-flow
Keep content minimal and scannable

Structure
[Logo ============= CTA] ← Horizontal top
       \
         \                ← Diagonal
           \
[Content    \    Image  ]
              \
[Info ========== CTA   ] ← Horizontal bottom

Key Differences
######################
F-Layou                     Z-Layout
Text-heavy content          Minimal content
Multiple sections           Few distinct sections
Blog posts, articles        Landing pages, promos
Slower, detailed reading    Quick scanning
Multiple focal points       2-3 main focal points

Combined Approach
Many modern websites use both patterns strategically:

Z-pattern for hero section/above fold
F-pattern for content sections below

Responsive designs may switch patterns based on screen size

Pro Tip: Don't force these patterns - use them as guidelines. Eye-tracking shows natural reading behavior, but good visual hierarchy and clear CTAs matter more than strict adherence to these layouts.
"""


##############################################################################
# DAY 66 - Flask and APIs with RESTful Routing
##############################################################################

"""
Build APIs with RESTful Routing & Flask
"""

# Representative State Transfer
# Different types
# GraphQL
# SOAP & REST
# Falcor

"""
REST (Representational State Transfer) is an architectural pattern for designing web APIs using standard HTTP methods and URL conventions.
Core Principles
RESTful routing maps HTTP verbs to CRUD operations on resources:

- GET - Retrieve/read resources
- POST - Create new resources
- PUT/PATCH - Update existing resources
- DELETE - Remove resources

Standard Route Patterns
For a resource like "articles":

HTTP Verb   Path            Action      Purpose
GET         /articles       index       List all articles
GET         /articles/:id   show        Display one article
GET         /articles/new   new         Show form to create article
POST        /articles       create      Create new article
GET         /articles/:id/  editedit    Show form to edit article
PUT/PATCH   /articles/:id   update      Update specific article
DELETE      /articles/:id   destroy     Delete specific article

Key Conventions

- URLs represent resources (nouns), not actions
- Use plural resource names (/articles, not /article)
- HTTP methods indicate the action being performed
- Keep routes predictable and consistent across your API
- Use nested routes for related resources (e.g., /articles/:id/comments)

This pattern creates clean, intuitive APIs that are easy to understand and maintain.
"""


################################################
# Challenge - RESTful Routing
################################################



"""
Example
https://laptopfriendly.co/london
"""

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):   
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_cafe():
    random_cafe = db.session.execute(
        db.select(Cafe).order_by(func.random()).limit(1)
        ).scalar_one_or_none()

    if random_cafe is None:
        return jsonify(error={"Not Found": "No cafes in the database."}), 404
    
    return jsonify(cafe=random_cafe.to_dict())

    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #.    "coffee_price": random_cafe.coffee_price,
    # })


@app.route("/all", methods=["GET"])
def all_cafes():
    all_cafes = db.session.execute(
        db.select(Cafe).order_by(Cafe.name)
        ).scalars().all()

    if all_cafes is None:
        return jsonify(error={"Not Found": "No cafes in the database."}), 404
    
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search", methods=["GET"])
def search_cafes():
    query_location = request.args.get("loc")

    matched_cafes = db.session.execute(
        db.select(Cafe).where(Cafe.location == query_location)
        ).scalars().all()

    if matched_cafes is None:
        return jsonify(error={"Not Found": "No cafes in the database."}), 404
    
    return jsonify(cafes=[cafe.to_dict() for cafe in matched_cafes])


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
# http://127.0.0.1:5000/update-price/CAFE_ID?new_price=£5.67
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.get(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    

# HTTP DELETE - Delete Record
# http://127.0.0.1:5000/report-closed/1?api-key=TopSecretAPIKey
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.get(Cafe, cafe_id) 
        if cafe is None:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404     
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)

##############################################################################
# DAY 67 - Flask, SQLite, CKEditor5, Add, Edit & Delete Posts
##############################################################################

"""
Blog Site with Add, Edit, Delete Posts

Flask
SQLite
CKEditor5

"""

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Create Database
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Configure Table
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# Create New Post Form
class NewPost(FlaskForm):
    title = StringField("Article Title", validators=[DataRequired()])
    subtitle = StringField("Article Subtitle", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    img_url = StringField("Background Image URL", validators=[DataRequired()])
    body = TextAreaField("Body", validators=[DataRequired()])
    submit = SubmitField('Submit')


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = []

    get_all_posts = db.session.execute(
        db.select(BlogPost).order_by(BlogPost.id.desc())
    ).scalars().all()

    if get_all_posts is None:
        return f"No posts found in the database."

    return render_template("index.html", all_posts=get_all_posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    new_post_form = NewPost()

    if new_post_form.validate_on_submit():  
        new_post = BlogPost(
            title = new_post_form.title.data,
            subtitle = new_post_form.subtitle.data,
            author = new_post_form.author.data,
            img_url = new_post_form.img_url.data,
            body = new_post_form.body.data,
            date = date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))
    
    return render_template("make-post.html", form=new_post_form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = NewPost(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data    
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)

@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

##############################################################################
# DAY 68 - Blog
##############################################################################

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Create user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# Create DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create Table with UserMixin
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # Passing True or False if the user is authenticated. 
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        
        hashed_salted_pw =  generate_password_hash(
            request.form['password'], 
            method='pbkdf2:sha256', 
            salt_length=8
        )

        new_user = User(
            name = request.form['name'],
            email = request.form['email'],
            password = hashed_salted_pw
        )
    
        db.session.add(new_user)
        db.session.commit()
    
        # Log in and authenticate user after adding details to DB
        login_user(new_user)

        # Can redirect() and get name from the current_user
        return redirect(url_for("secrets"))
    
    # Passing True or False if the user is authenticated. 
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":

        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email 
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
    
        # Email doesn't exist or password incorrect.
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        
        # Check stored password hash against entered password hashed
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    # Passing True or False if the user is authenticated. 
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    # Passing the name from the current_user
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)

##############################################################################
# DAY 69 - More Forms
##############################################################################

"""
Main
"""

from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm


#############################################################
# Configure App
#############################################################

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


#############################################################
# Configure Web Elements 
#############################################################

ckeditor = CKEditor(app)
Bootstrap5(app)


#############################################################
# Configure Login Elements
#############################################################

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


#############################################################
# Create and Configure Database
#############################################################

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(1000), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")

with app.app_context():
    db.create_all()


#############################################################
# Admin Decorator
#############################################################

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


#############################################################
# Configure Flask Routes
#############################################################

@app.route('/register', methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        email_add = form.email.data
        result = db.session.execute(db.select(User).where(User.email == email_add))
        user = result.scalar()

        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))
           
        else:
            hash_and_salted_password = generate_password_hash(
                form.password.data,
                method = 'pbkdf2:sha256',
                salt_length = 8
            )
            new_user = User(
                email = email_add,
                name = form.name.data,
                password = hash_and_salted_password,
            )
            
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)

            return redirect(url_for("get_all_posts"))
    
    return render_template("register.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        
        # Find user by email 
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        
        # Check stored password hash against entered password hashed
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))

    # Passing True or False if the user is authenticated. 
    return render_template("login.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated)


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):

    requested_post = db.get_or_404(BlogPost, post_id)

    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )

        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('show_post', post_id=post_id))
    
    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


#############################################################
# Init
#############################################################

if __name__ == "__main__":
    app.run(debug=True, port=5000)

"""
Forms
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

#############################################################
# Create Blog Post
#############################################################

class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

#############################################################
# User Registration
#############################################################

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

#############################################################
# Login Form
#############################################################

class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")

#############################################################
# Comment Form
#############################################################

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

##############################################################################
# DAY 70 - Git
##############################################################################

# Good ignore files - https://github.com/github/gitignore

##############################################################################
# DAY 71 - Full Working Blog
# Fully working blog - Python, Flask, Bootstrap, CKEditor, SQLAlchemy, PostgreSQL, Gunicorn, Mailgun
# Note: Final had CKE 4 rather than 5 which I did earlier
##############################################################################

"""
Main.py
"""

from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
# from flask_gravatar import GravatarXx
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import os
from dotenv import load_dotenv
from notifications import NotificationManager


#############################################################
# Configure App
#############################################################

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

ckeditor = CKEditor(app)
Bootstrap5(app)
notifications = NotificationManager()


#############################################################
# Configure Flask Login
#############################################################

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


#############################################################
# Gravatar
#############################################################

# For adding profile images to the comment section
# gravatar = Gravatar(app,
#                     size=100,
#                     rating='g',
#                     default='retro',
#                     force_default=False,
#                     force_lower=False,
#                     use_ssl=False,
#                     base_url=None)


#############################################################
# Configure Database
#############################################################

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    # Create reference to the User object. The "posts" refers to the posts property in the User class.
    author = relationship("User", back_populates="posts")
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    # Parent relationship to the comments
    comments = relationship("Comment", back_populates="parent_post")


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    # This will act like a list of BlogPost objects attached to each User.
    # The "author" refers to the author property in the BlogPost class.
    posts = relationship("BlogPost", back_populates="author")
    # Parent relationship: "comment_author" refers to the comment_author property in the Comment class.
    comments = relationship("Comment", back_populates="comment_author")


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    # Child relationship:"users.id" The users refers to the tablename of the User class.
    # "comments" refers to the comments property in the User class.
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    # Child Relationship to the BlogPosts
    post_id: Mapped[str] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")


with app.app_context():
    db.create_all()


#############################################################
# Admin Decorator
#############################################################

# Create an admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


#############################################################
# Flask Routes
#############################################################

######################
# Register
######################

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # Check if user email is already present in the database.
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        # This line will authenticate the user with Flask-Login
        login_user(new_user)
        return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=form, current_user=current_user)


######################
# Login
######################

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))

    return render_template("login.html", form=form, current_user=current_user)


######################
# Logout
######################

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


######################
# Home Page
######################

@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


######################
# Comments 
######################

# Add a POST method to be able to post comments
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    # Add the CommentForm to the route
    comment_form = CommentForm()
    # Only allow logged-in users to comment on posts
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form)


######################
# New Post
######################

@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


######################
# Edit Post
######################

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


######################
# Delete Post
######################

@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


######################
# About
######################

@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


######################
# Contact Page
######################

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        notifications.send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)    
    return render_template("contact.html", current_user=current_user, msg_sent=False)


#############################################################
# Init
#############################################################

if __name__ == "__main__":
    app.run(debug=True, port=5000)


"""
Forms.py
"""


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Create a form to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


# Create a form to add comments
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

##############################################################################
# DAY 72 - Pandas Data Manipulation
##############################################################################

# Use .head(), .tail(), .shape and .columns to explore your DataFrame and find out the number of rows and columns as well as the column names.

# Look for NaN (not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.

# You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]

# You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or using df['column name'].loc[index]

# The largest and smallest values, as well as their positions, can be found with methods like .max(), .min(), .idxmax() and .idxmin()

# You can sort the DataFrame with .sort_values() and add new columns with .insert()

# To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the .groupby() method

##############################################################################
# DAY 73 - Data Visualisation with Metaplotlib
#
# How to visualise your data and create charts with Matplotlib
# How to pivot, group and manipulate your data with Pandas to get it into the format you want
# How to work with timestamps and time-series data
# How to style and customise a line chart to your liking
##############################################################################

"""
Day 73 Goals: what you will make by the end of the day

Analyse the Popularity of Different Programming Languages over Time

The oldest programming language still in use today is FORTRAN, which was developed in 1957. Since then many other programming languages have been developed. But which programming language is the most popular? Which programming language is the Kim Kardashian of programming languages; the one people just can't stop talking about? 

StackOverflow will help us answer this burning question. Each post on Stack OverFlow comes with a Tag. And this Tag can be the name of a programming language.

To figure out which language is the most popular, all we need to do is count the number of posts on Stack Overflow that are tagged with each language. The language with the most posts wins!

Today you will learn:

    How to visualise your data and create charts with Matplotlib

    How to pivot, group and manipulate your data with Pandas to get it into the format you want

    How to work with timestamps and time-series data

    How to style and customise a line chart to your liking
"""

##############################################################################
# DAY 74 - Aggregate and Merge Data in Pandas
#
##############################################################################

"""
Day 74 Goals: what you will make by the end of the day

Learn to Aggregate and Merge Data in Pandas while Analysing a Dataset of LEGO Pieces

Today we're going to be diving deep into a dataset all about LEGO, which will help us answer a whole bunch of interesting questions about the history of the company, their product offering, and which LEGO set rules them all:

    What is the most enormous LEGO set ever created and how many parts did it have?

    In which year were the first LEGO sets released and how many sets did the company sell when it first launched?

    Which LEGO theme has the most sets? Is it Harry Potter, Ninjago, Friends or something else?

    When did the LEGO company really take-off based on its product offering? How many themes and sets did it release every year?

    Did LEGO sets grow in size and complexity over time? Do older LEGO sets tend to have more or fewer parts than newer sets?


What you'll learn today

    How to combine a Notebook with HTML Markup.

    Apply Python List slicing techniques to Pandas DataFrames.

    How to aggregate data using the .agg() function.

    How to create scatter plots, bar charts, and line charts with two axes in Matplotlib.

    Understand database schemas that are organised by primary and foreign keys.

    How to merge DataFrames that share a common key

    
## Learning Points & Summary

In this lesson we looked at how to:

    use HTML Markdown in Notebooks, such as section headings # and how to embed images with the <img> tag.

    combine the groupby() and count() functions to aggregate data

    use the .value_counts() function

    slice DataFrames using the square bracket notation e.g., df[:-2] or df[:10]

    use the .agg() function to run an operation on a particular column

    rename() columns of DataFrames

    create a line chart with two separate axes to visualise data that have different scales.

    create a scatter plot in Matplotlib

    work with tables in a relational database by using primary and foreign keys

    .merge() DataFrames along a particular column

    create a bar chart with Matplotlib
    """

##############################################################################
# DAY 75 - Time-series Data
#
# Matplotlib
##############################################################################

"""
What you'll learn today

    How to make time-series data comparable by resampling and converting to the same periodicity (e.g., from daily data to monthly data).

    Fine-tuning the styling of Matplotlib charts by using limits, labels, linestyles, markers, colours, and the chart's resolution.

    Using grids to help visually identify seasonality in a time series.

    Finding the number of missing and NaN values and how to locate NaN values in a DataFrame.

    How to work with Locators to better style the time axis on a chart

    Review the concepts learned in the previous three days and apply them to new datasets
"""

"""

What do the Search Numbers mean?

We can see from our DataFrames that Google's search interest ranges between 0 and 100. 
But what does that mean? Google defines the values of search interest as: 

    Numbers represent search interest relative to the highest point on the chart for the given region and time. 
    A value of 100 is the peak popularity for the term. 
    A value of 50 means that the term is half as popular. 
    A score of 0 means there was not enough data for this term. 

Basically, the actual search volume of a term is not publicly available. 
Google only offers a scaled number. 
Each data point is divided by the total searches of the geography and time range it represents to compare relative popularity.

For each word in your search, Google finds how much search volume in each region 
and time period your term had relative to all the searches in that region and time period. 
It then combines all of these measures into a single measure of popularity, 
and then it scales the values across your topics, so the largest measure is set to 100. 
In short: Google Trends doesn’t exactly tell you how many searches occurred for your topic, 
but it does give you a nice proxy.

Here are the Google Trends Search Parameters that I used to generate the .csv data:

    "Tesla", Worldwide, Web Search

    "Bitcoin", Worldwide, News Search

    "Unemployment Benefits", United States, Web Search
"""

"""
In this lesson we looked at how to:

    How to use .describe() to quickly see some descriptive statistics at a glance.

    How to use .resample() to make a time-series data comparable to another by changing the periodicity.

    How to work with matplotlib.dates Locators to better style a timeline (e.g., an axis on a chart).

    How to find the number of NaN values with .isna().values.sum()

    How to change the resolution of a chart using the figure's dpi

    How to create dashed '--' and dotted '-.' lines using linestyles

    How to use different kinds of markers (e.g., 'o' or '^') on charts.

    Fine-tuning the styling of Matplotlib charts by using limits, labels, linewidth and colours (both in the form of named colours and HEX codes).

    Using .grid() to help visually identify seasonality in a time series.
   
"""

##############################################################################
# DAY 76 - Pandas, Handle Duplicate etc.
#
# Pie Chart, Donut Chart, Scatter Plots
##############################################################################

"""
In this module, we will compare thousands of apps in the Google Play Store so that we can gain insight into:

    How competitive different app categories (e.g., Games, Lifestyle, Weather) are

    Which app category offers compelling opportunities based on its popularity

    How many downloads you would give up by making your app paid vs. free

    How much you can reasonably charge for a paid app

    Which paid apps have had the highest revenue

    How many paid apps will recoup their development costs based on their sales revenue


Today you'll learn:

    How to quickly remove duplicates

    How to remove unwanted symbols and convert data into a numeric format

    How to wrangle columns containing nested data with Pandas

    How to create compelling data visualisations with the plotly library

    Create vertical, horizontal and grouped bar charts

    Create pie and donut charts for categorical data

    Use colour scales to make beautiful scatter plots
"""

"""
In this lesson we looked at how to:

    Pull a random sample from a DataFrame using .sample()

    How to find duplicate entries with .duplicated() and .drop_duplicates()

    How to convert string and object data types into numbers with .to_numeric()

    How to use plotly to generate beautiful pie, donut, and bar charts as well as box and scatter plots 
"""

##############################################################################
# DAY 77 - Numpy
#
##############################################################################

"""
NumPy is a Python library that’s used in almost every field of science and engineering. It’s practically THE standard for working with numerical data in Python. The case studies for how NumPy is being used speak for themselves 😮 

So far, we’ve been using Pandas, which is built on top of NumPy. Think of Pandas as a high-level data manipulation tool that includes functionality for working with time-series or for grouping, joining, merging and finding missing data (i.e., everything we’ve been doing so far). NumPy on the other hand shines with low-level tasks, like doing serious math and calculations.


Today you'll learn:

    How to leverage the power 💪 of NumPy's ndarrays.

    How to access individual values and subsets inside an n-dimensional array.

    How broadcasting 📣 works with ndarrays.

    How to do linear algebra with NumPy.

    How to generate points that you can plot on a chart.

    How to manipulate images as ndarrays. 
"""

"""
In this lesson we looked at how to:

    Create arrays manually with np.array()

    Generate arrays using  .arange(), .random(), and .linspace()

    Analyse the shape and dimensions of a ndarray

    Slice and subset a ndarray based on its indices

    Do linear algebra like operations with scalars and matrix multiplication

    Use NumPys broadcasting to make ndarray shapes compatible

    Manipulate images in the form of ndarrays
    """

##############################################################################
# DAY 78 - scikit-learn, linear regression and seabor
#
##############################################################################

"""
In this lesson, we're going to be looking at movie budget and revenue data. This dataset is perfect for trying out some new tools like scikit-learn to run a linear regression and seaborn, a popular data visualisation library built on top of Matplotlib. 

The question we want to answer today is: Do higher film budgets lead to more revenue in the box office? In other words, should a movie studio spend more on a film to make more? 


Today you'll learn:

    How to use a popular data visualisation library called Seaborn

    How to run and interpret a linear regression with scikit-learn

    How to plot a regression a scatter plot to visualise relationships in the data

    How to add a third dimension to a scatter plot to create a bubble chart

    How to cleverly use floor division // to convert your data
    
    """

"""
Learning Points & Summary

Today was a pretty packed lesson where we introduced a lot of new concepts. In this lesson we looked at how to:

    Use nested loops to remove unwanted characters from multiple columns

    Filter Pandas DataFrames based on multiple conditions using both .loc[] and .query()

    Create bubble charts using the Seaborn Library

    Style Seaborn charts using the pre-built styles and by modifying Matplotlib parameters

    Use floor division (i.e., integer division) to convert years to decades

    Use Seaborn to superimpose a linear regressions over our data

    Make a judgement if our regression is good or bad based on how well the model fits our data and the r-squared metric

    Run regressions with scikit-learn and calculate the coefficients. 
"""

##############################################################################
# DAY 79 - Choropleth (Maps), Sunburst Charts, Seaborn
#
# Donut, Bar Charts
##############################################################################

"""
Today we're going to analyse a dataset on the past winners of the Nobel Prize. Let's see what patterns we can uncover in the past Nobel laureates and what can we learn about the Nobel prize and our world more generally.

On November 27, 1895, Alfred Nobel signed his last will in Paris. When it was opened after his death, the will caused a lot of controversy, as Nobel had left much of his wealth for the establishment of a prize. Alfred Nobel dictates that his entire remaining estate should be used to endow “prizes to those who, during the preceding year, have conferred the greatest benefit to humankind”. Every year the Nobel Prize is given to scientists and scholars in the categories chemistry, literature, physics, physiology or medicine, economics, and peace.


This project will bring a lot of the tools and techniques that we've covered previously together. While we will review many concepts that we've covered in the previous days, you'll also learn a lot of new things.


Today you'll learn:

    Create a Choropleth to display data on a map.

    Create bar charts showing different segments of the data with plotly.

    Create Sunburst charts with plotly.

    Use Seaborn's .lmplot() and show best-fit lines across multiple categories using the row, hue, and lowess parameters.

    Understand how a different picture emerges when looking at the same data in different ways (e.g., box plots vs a time series analysis).

    See the distribution of our data and visualise descriptive statistics with the help of a histogram in Seaborn. 
    """

"""
Today was a big and difficult project. Congratulations on making it all the way through! You too deserve a prize 🏅!


In this lesson, we reviewed many concepts that we've covered previously, including:

    How to uncover and investigate NaN values.

    How to convert objects and string data types to numbers.

    Creating donut and bar charts with plotly.

    Create a rolling average to smooth out time-series data and show a trend.

    How to use .value_counts(), .groupby(), .merge(), .sort_values() and .agg().


In addition, we learned many new things too. We looked at how to:

    Create a Choropleth to display data on a map.

    Create bar charts showing different segments of the data with plotly.

    Create Sunburst charts with plotly.

    Use Seaborn's .lmplot() and show best-fit lines across multiple categories using the row, hue, and lowess parameters.

    Understand how a different picture emerges when looking at the same data in different ways (e.g., box plots vs a time series analysis).

    See the distribution of our data and visualise descriptive statistics with the help of a histogram in Seaborn. 
"""

##############################################################################
# DAY 80 - Histograms, Numpy, KDE
#
##############################################################################

"""
Day 80 Goals: what you will make by the end of the day

Your Story

Today you will become a doctor, but not just any doctor. You will become Dr Ignaz Semmelweis, a Hungarian physician born in 1818 who worked in the Vienna General Hospital.

In the past, people didn't know about bacteria, germs, or viruses. People illness was caused by "bad air" or evil spirits. But in the 1800s Doctors started looking more at anatomy, doing autopsies and making arguments based on data. Dr Semmelweis suspected that something was going wrong with the procedures at Vienna General Hospital. Dr Semmelweis wanted to figure out why so many women in maternity wards were dying from childbed fever (i.e., puerperal fever).


Today you'll learn:

    How to make a compelling argument using data

    How to superimpose histograms to show differences in distributions

    How to use a Kernel Density Estimate (KDE) to show a graphic estimate of a distribution.

    How to use scipy and test for statistical significance by looking at p-values.

    How to highlight different parts of a time series chart in Matplotib.

    How to add and configure a Legend in Matplotlib.

    Use NumPy's .where() function to process elements depending on a condition.
    """


"""

Today you've learned

    How to use histograms to visualise distributions

    How to superimpose histograms on top of each other even when the data series have different lengths

    How to use a to smooth out kinks in a histogram and visualise a distribution with a Kernel Density Estimate (KDE)

    How to improve a KDE by specifying boundaries on the estimates

    How to use scipy and test for statistical significance by looking at p-values.

    How to highlight different parts of a time series chart in Matplotib.

    How to add and configure a Legend in Matplotlib.

    Use NumPy's .where() function to process elements depending on a condition.

The Tragic Story of Dr Semmelweis

Gather round, gather round. Now I'll tell you how our story ends. Despite the incredible evidence in favour of Dr Semmelweis' theory - that childbed fever was caused by some "substance" (which today we know as bacteria) from autopsy room corpses - was rejected by the medical community at the time. But why?! 

Part of the reason is that Semmelweis was not very tactful. He made it look like doctors were giving childbed fever to women (which they in fact were). This is not something people wanted to hear.

However, he also published his data in the form of long tables without any data visualisations:

The long tables made it very hard to see what's actually going on! Also, at the time statistics and statistical arguments were quite uncommon in the field of medicine.

Eventually, Dr Semmelweis belligerent campaigning made him some powerful and influential enemies. He lost his job at the Vienna hospital, and doctors gave up washing their hands with chlorine. As Dr Semmelweis grew older he got even angrier and eventually quite "strange". This was either the immense frustration or possibly a result of another disease like Alzheimer's or syphilis. In 1965, at the age of 47, Dr Semmelweis was committed to a mental asylum. And at the asylum, he was probably beaten since he eventually died of sepsis, a complication of an infection in the bloodstream. The tragic irony is that sepsis is a similar kind of disease that he fought so hard to prevent in women who died from childbed fever. It wasn't until 20 years later with Louis Pasteur's work on germ theory that Dr Semmelweis' work gained acceptance. RIP Dr Semmelweis. 

"""

##############################################################################
# DAY 81 - Challenge on Boston House
#
##############################################################################

"""
Day 81 Goals: what you will make by the end of the day

Welcome to Boston Massachusetts in the 1970s! Imagine you're working for a real estate development company. Your company wants to value any residential project before they start. You are tasked with building a model that can provide a price estimate based on a home's characteristics like:

    The number of rooms

    The distance to employment centres

    How rich or poor the area is

    How many students there are per teacher in local schools etc


Today you will:

    Analyse and explore the Boston house price data

    Split your data for training and testing

    Run a Multivariable Regression

    Evaluate how your model's coefficients and residuals

    Use data transformation to improve your model performance

    Use your model to estimate a property price
"""

"""
Today you've learned

    How to quickly spot relationships in a dataset using Seaborn's .pairplot().

    How to split the data into a training and testing dataset to better evaluate a model's performance.

    How to run a multivariable regression.

    How to evaluate that regression-based on the sign of its coefficients.

    How to analyse and look for patterns in a model's residuals.

    How to improve a regression model using (a log) data transformation.

    How to specify your own values for various features and use your model to make a prediction. 
    
"""