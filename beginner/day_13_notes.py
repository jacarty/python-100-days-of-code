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
