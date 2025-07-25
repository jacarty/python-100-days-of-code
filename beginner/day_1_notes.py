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