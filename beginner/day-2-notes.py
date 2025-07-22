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