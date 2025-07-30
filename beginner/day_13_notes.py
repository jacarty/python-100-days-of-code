"""
Day 13 Content - Debugging

The challenge will be a Number Guessing game.
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