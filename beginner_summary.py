"""
BEGINNER PYTHON SUMMARY
=======================

A comprehensive summary of Python fundamentals covered in Days 1-13 of the 100 Days of Code course.
This file distills key concepts, best practices, and provides examples for complex topics.
"""

# ========================================
# 1. BASIC OUTPUT AND INPUT
# ========================================

"""
Key Concepts:
- print() function for output
- input() function for user input
- String concatenation with +
- f-strings for formatted output
"""

# Basic output
print("Hello, World!")

# String concatenation
name = "Python"
print("Hello, " + name + "!")

# f-strings (preferred method)
age = 25
print(f"I am {age} years old")

# User input
user_name = input("What's your name? ")
print(f"Nice to meet you, {user_name}!")


# ========================================
# 2. DATA TYPES AND TYPE CONVERSION
# ========================================

"""
Four main data types:
1. String (str) - Text data
2. Integer (int) - Whole numbers
3. Float (float) - Decimal numbers
4. Boolean (bool) - True/False
"""

# Data type examples
text = "Hello"          # String
whole_number = 42       # Integer
decimal = 3.14159       # Float
is_true = True          # Boolean

# Type checking
print(type(text))       # <class 'str'>
print(type(whole_number))  # <class 'int'>

# Type conversion
number_string = "123"
actual_number = int(number_string)  # Convert string to int
text_number = str(42)               # Convert int to string

# Complex example: BMI Calculator
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {round(bmi, 2)}")


# ========================================
# 3. MATHEMATICAL OPERATIONS
# ========================================

"""
Basic operators:
+ Addition
- Subtraction  
* Multiplication
/ Division (returns float)
// Floor division (returns int)
** Exponentiation
% Modulo (remainder)

PEMDAS order: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
"""

# Mathematical examples
result1 = 10 + 5        # 15
result2 = 10 / 3        # 3.333...
result3 = 10 // 3       # 3 (floor division)
result4 = 10 % 3        # 1 (remainder)
result5 = 2 ** 3        # 8 (2 to the power of 3)

# Assignment operators
score = 0
score += 10             # score = score + 10
score *= 2              # score = score * 2

# Modulo examples (useful for checking odd/even)
def is_even(number):
    return number % 2 == 0

print(f"Is 10 even? {is_even(10)}")  # True
print(f"Is 7 even? {is_even(7)}")    # False


# ========================================
# 4. CONDITIONAL STATEMENTS
# ========================================

"""
Comparison operators:
== Equal to
!= Not equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

Logical operators:
and - All conditions must be true
or  - At least one condition must be true
not - Reverses the boolean value
"""

# Basic if/else
temperature = 25
if temperature > 20:
    print("It's warm outside")
else:
    print("It's cold outside")

# if/elif/else chain
grade = 85
if grade >= 90:
    print("A grade")
elif grade >= 80:
    print("B grade")
elif grade >= 70:
    print("C grade")
else:
    print("Below C grade")

# Logical operators example
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")
elif age >= 18 and not has_license:
    print("Need to get license first")
else:
    print("Too young to drive")

# Complex conditional example: Ticket pricing
def calculate_ticket_price(age, wants_photo=False):
    """Calculate roller coaster ticket price based on age and photo option."""
    if age < 3:
        price = 0
    elif age <= 12:
        price = 5
    elif age <= 18:
        price = 7
    elif 45 <= age <= 55:  # Midlife crisis discount!
        price = 0
    else:
        price = 12
    
    if wants_photo:
        price += 3
    
    return price

# Test the function
print(f"Price for 10-year-old with photo: ${calculate_ticket_price(10, True)}")


# ========================================
# 5. LISTS AND LIST OPERATIONS
# ========================================

"""
Lists are ordered collections that can hold multiple items.
- Use square brackets []
- Items are indexed starting from 0
- Can contain mixed data types
- Are mutable (can be changed)
"""

# Creating and accessing lists
fruits = ["apple", "banana", "orange", "grape"]
print(fruits[0])        # "apple" (first item)
print(fruits[-1])       # "grape" (last item)

# List methods
fruits.append("kiwi")           # Add to end
fruits.insert(1, "mango")      # Insert at position 1
fruits.remove("banana")        # Remove specific item
fruits.extend(["peach", "plum"])  # Add multiple items

# List operations
print(len(fruits))              # Get length
print("apple" in fruits)        # Check if item exists

# Nested lists example
shopping_list = [
    ["milk", "eggs", "bread"],      # Dairy/Bakery
    ["apples", "bananas", "oranges"], # Fruits
    ["chicken", "beef", "fish"]     # Meat
]
print(shopping_list[1][0])      # "apples" (first fruit)

# List with random selection
import random
random_fruit = random.choice(fruits)
print(f"Today's special: {random_fruit}")


# ========================================
# 6. LOOPS
# ========================================

"""
Two main types:
1. For loops - iterate over sequences or ranges
2. While loops - repeat while condition is true
"""

# For loop with list
students = ["Alice", "Bob", "Charlie"]
for student in students:
    print(f"Hello, {student}")

# For loop with range
for number in range(1, 6):  # 1, 2, 3, 4, 5
    print(f"Count: {number}")

# For loop with step
for number in range(0, 11, 2):  # 0, 2, 4, 6, 8, 10
    print(number)

# While loop example
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

# Complex loop example: FizzBuzz
def fizz_buzz(limit):
    """Print numbers 1 to limit, but replace multiples of 3 with 'Fizz', 
    multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'."""
    for number in range(1, limit + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# Nested loops example: Multiplication table
def multiplication_table(size=10):
    """Generate a multiplication table."""
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print(f"{i * j:3}", end=" ")  # Format with 3 spaces
        print()  # New line after each row


# ========================================
# 7. FUNCTIONS
# ========================================

"""
Functions help organize code and avoid repetition.
Types:
1. Functions without parameters
2. Functions with parameters
3. Functions with return values
4. Functions with default parameters
"""

# Basic function
def greet():
    print("Hello from a function!")

# Function with parameters
def greet_person(name, greeting="Hello"):
    """Greet a person with a custom greeting."""
    print(f"{greeting}, {name}!")

# Function with return value
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

# Function with multiple returns
def analyze_number(num):
    """Analyze if a number is positive, negative, or zero, and if it's even or odd."""
    if num == 0:
        return "zero", "neither"
    elif num > 0:
        sign = "positive"
    else:
        sign = "negative"
    
    parity = "even" if num % 2 == 0 else "odd"
    return sign, parity

# Using the functions
greet()
greet_person("Alice")
greet_person("Bob", "Hi")

area = calculate_area(5, 10)
print(f"Area: {area}")

sign, parity = analyze_number(-6)
print(f"The number is {sign} and {parity}")

# Advanced function example: Password strength checker
def check_password_strength(password):
    """Check password strength based on various criteria."""
    strength = 0
    feedback = []
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters")
    
    if any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter")
    
    if any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter")
    
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("Include at least one number")
    
    strength_levels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]
    return strength_levels[min(strength, 4)], feedback


# ========================================
# 8. DICTIONARIES
# ========================================

"""
Dictionaries store key-value pairs.
- Use curly braces {}
- Keys must be unique
- Values can be any data type
- Are mutable
"""

# Basic dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

# Accessing and modifying
print(student["name"])              # "Alice"
student["age"] = 21                 # Update value
student["graduated"] = False        # Add new key-value pair

# Dictionary methods
print(student.get("height", "Unknown"))  # Get with default value
print(student.keys())               # Get all keys
print(student.values())             # Get all values

# Looping through dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Nested dictionary example: Student database
students_db = {
    "alice": {
        "full_name": "Alice Johnson",
        "grades": {"math": 95, "science": 87, "english": 92},
        "attendance": 0.96
    },
    "bob": {
        "full_name": "Bob Smith",
        "grades": {"math": 78, "science": 84, "english": 89},
        "attendance": 0.89
    }
}

# Calculate average grade for a student
def calculate_average_grade(student_data):
    """Calculate the average grade for a student."""
    grades = list(student_data["grades"].values())
    return sum(grades) / len(grades)

alice_avg = calculate_average_grade(students_db["alice"])
print(f"Alice's average grade: {alice_avg:.1f}")


# ========================================
# 9. SCOPE AND GLOBAL VARIABLES
# ========================================

"""
Scope determines where variables can be accessed:
- Global scope: Available everywhere
- Local scope: Only within the function
- Best practice: Avoid modifying global variables directly
"""

# Global variable
game_score = 0

def increase_score(points):
    """Increase score by returning new value (recommended approach)."""
    return game_score + points

def reset_game():
    """Reset game using global keyword (use sparingly)."""
    global game_score
    game_score = 0

# Better approach: Pass and return values
def update_score(current_score, points):
    """Update score by passing and returning values."""
    return current_score + points

# Example usage
game_score = update_score(game_score, 100)
print(f"Current score: {game_score}")

# Constants (by convention, use ALL_CAPS)
MAX_LIVES = 3
WINNING_SCORE = 1000


# ========================================
# 10. ERROR HANDLING AND DEBUGGING
# ========================================

"""
Common debugging techniques:
1. Print statements to track values
2. Check data types with type()
3. Use try/except for error handling
4. Read error messages carefully
"""

# Try/except example
def safe_divide(a, b):
    """Safely divide two numbers with error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Please provide numbers only!")
        return None

# Input validation example
def get_positive_number(prompt):
    """Get a positive number from user with validation."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

# Debugging example with print statements
def debug_function(numbers):
    """Example function with debug prints."""
    print(f"Input: {numbers}")
    print(f"Input type: {type(numbers)}")
    
    total = 0
    for i, num in enumerate(numbers):
        print(f"Processing item {i}: {num}")
        total += num
    
    print(f"Final total: {total}")
    return total


# ========================================
# 11. PUTTING IT ALL TOGETHER: MINI PROJECT
# ========================================

def number_guessing_game():
    """A complete number guessing game demonstrating multiple concepts."""
    import random
    
    # Game settings
    MAX_ATTEMPTS = 7
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    
    # Initialize game state
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0
    guessed_numbers = []
    
    print("🎯 Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it!")
    
    while attempts < MAX_ATTEMPTS:
        try:
            # Get user input
            guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
            
            # Validate input
            if guess < MIN_NUMBER or guess > MAX_NUMBER:
                print(f"Please guess between {MIN_NUMBER} and {MAX_NUMBER}")
                continue
            
            if guess in guessed_numbers:
                print("You already guessed that number!")
                continue
            
            # Process guess
            attempts += 1
            guessed_numbers.append(guess)
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("📈 Too low!")
            else:
                print("📉 Too high!")
            
            # Show remaining attempts
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                print(f"Attempts remaining: {remaining}")
                print(f"Previous guesses: {sorted(guessed_numbers)}")
            
        except ValueError:
            print("Please enter a valid number!")
    
    else:
        print(f"\n😔 Game Over! The number was {secret_number}")
        print(f"Your guesses: {sorted(guessed_numbers)}")


# ========================================
# 12. BEST PRACTICES SUMMARY
# ========================================

"""
KEY PROGRAMMING PRINCIPLES LEARNED:

1. DRY (Don't Repeat Yourself)
   - Use functions to avoid code duplication
   - Create reusable components

2. Clear Naming
   - Use descriptive variable names
   - Follow snake_case convention for variables/functions
   - Use UPPER_CASE for constants

3. Code Organization
   - Group related functionality together
   - Use comments to explain complex logic
   - Break large problems into smaller functions

4. Error Handling
   - Validate user input
   - Use try/except for potential errors
   - Provide helpful error messages

5. Testing and Debugging
   - Test edge cases
   - Use print statements for debugging
   - Read error messages carefully

6. Data Structure Choice
   - Lists for ordered collections
   - Dictionaries for key-value relationships
   - Consider the operations you need to perform

7. Loop Selection
   - For loops when you know the number of iterations
   - While loops when condition-based repetition is needed
   - Be careful to avoid infinite loops
"""

if __name__ == "__main__":
    print("🐍 Python Beginner Concepts Summary")
    print("=" * 40)
    print("This file contains examples of all major concepts")
    print("from the first 13 days of Python learning.")
    print("\nUncomment the line below to play the number guessing game!")
    
    # Uncomment to play the game:
    # number_guessing_game()