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