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