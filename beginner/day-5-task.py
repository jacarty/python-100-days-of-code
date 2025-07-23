# Create password generator
# Two options. Just ouput in order. Letters. Symbols. Numbers.
# True random order.

# List 1: All letters of the alphabet in upper and lower case
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# List 2: Numbers 0 to 9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List 3: 8 symbols that can be used in passwords
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

import random

print("Welcome to the PyPasswork Generator.")
password_length = int(input("How many characters would you like the password to be?\n"))
number_count = int(input("How many numbers would you like?\n"))
symbol_count = int(input("How many symbols would you like?\n"))

# calculates the number of letters we want
letter_count = password_length - symbol_count - number_count

# create empty list
password = []

for letter in range(0, letter_count):
    random_letter = random.randint(0, 51)
    password.append(letters[random_letter])

for number in range(0, number_count):
    random_number = random.randint(0, 9)
    password.append(numbers[random_number])

for symbol in range(0, symbol_count):
    random_symbol = random.randint(0, 7)
    password.append(symbols[random_symbol])

# simply returns the list
print(f"This is your simple password: {password}")

# randomly returns the list 
random_password = random.sample(password, len(password))
print(f"This is your complex password: {random_password}")

# instructor used shuffle
shuffle_password = password.copy()
random.shuffle(shuffle_password)
print("This is your shuffle password: ", shuffle_password)

# BONUS: Convert to actual password strings
print("\n--- As actual password strings ---")
print("Simple password string: ", ''.join(password))
print("Complex password string: ", ''.join(random_password))
print("Shuffle password string: ", ''.join(shuffle_password))