"""
INTERMEDIATE PYTHON SUMMARY
============================

A comprehensive summary of intermediate Python concepts covered in Days 16-31.
This file covers OOP, GUI programming, file handling, and data analysis with external libraries.
"""

# ========================================
# 1. OBJECT-ORIENTED PROGRAMMING (OOP)
# ========================================

"""
Core OOP Concepts:
- Classes: Blueprints for creating objects
- Objects: Instances created from classes
- Attributes: Variables that belong to objects (what they have)
- Methods: Functions that belong to objects (what they do)
- Constructor: __init__ method that initializes objects
"""

# Basic Class Structure
class Car:
    """Example class demonstrating OOP fundamentals."""
    
    def __init__(self, make, model, year):
        """Constructor - runs when object is created."""
        self.make = make          # Instance attribute
        self.model = model        # Instance attribute  
        self.year = year          # Instance attribute
        self.odometer = 0         # Default attribute
    
    def drive(self, miles):
        """Method - what the object can do."""
        self.odometer += miles
        return f"Drove {miles} miles. Total: {self.odometer}"
    
    def get_info(self):
        """Method to return car information."""
        return f"{self.year} {self.make} {self.model}"

# Creating and using objects
my_car = Car("Toyota", "Camry", 2022)
print(my_car.get_info())
print(my_car.drive(100))


# ========================================
# 2. CLASS INHERITANCE
# ========================================

"""
Inheritance allows classes to inherit attributes and methods from parent classes.
- super().__init__() calls the parent class constructor
- Child classes can override parent methods
- Child classes can extend parent functionality
"""

class Animal:
    """Parent class."""
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    """Child class inheriting from Animal."""
    def __init__(self):
        super().__init__()  # Call parent constructor
    
    def breathe(self):
        """Override parent method and extend it."""
        super().breathe()  # Call parent method
        print("doing this underwater.")
    
    def swim(self):
        """New method specific to Fish."""
        print("moving in water.")

# Using inheritance
nemo = Fish()
nemo.breathe()  # Uses overridden method
print(nemo.num_eyes)  # Inherited attribute


# ========================================
# 3. TURTLE GRAPHICS
# ========================================

"""
Turtle module provides a visual way to learn programming.
Key concepts:
- Creating turtle objects
- Moving and drawing
- Event listeners for user input
- Screen management
"""

from turtle import Turtle, Screen
import random

def turtle_example():
    """Demonstrate basic turtle graphics."""
    # Setup
    tim = Turtle()
    screen = Screen()
    screen.colormode(255)
    
    # Configure turtle
    tim.shape("turtle")
    tim.speed("fastest")
    tim.width(3)
    
    # Random color function
    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)
    
    # Draw a square
    for _ in range(4):
        tim.forward(100)
        tim.right(90)
        tim.color(random_color())
    
    # Event listener example
    def move_forward():
        tim.forward(10)
    
    screen.listen()
    screen.onkey(move_forward, "space")
    screen.exitonclick()


# ========================================
# 4. GUI WITH TKINTER
# ========================================

"""
Tkinter is Python's standard GUI library.
Key widgets:
- Label: Display text
- Button: Clickable buttons
- Entry: Single-line text input
- Text: Multi-line text input
- Canvas: Drawing area
"""

from tkinter import *
from tkinter import messagebox

def tkinter_example():
    """Basic Tkinter GUI example."""
    
    # Window setup
    window = Tk()
    window.title("My GUI")
    window.config(padx=20, pady=20)
    
    # Label
    label = Label(text="Hello, Tkinter!")
    label.config(font=("Arial", 24))
    label.grid(column=0, row=0)
    
    # Entry
    entry = Entry(width=30)
    entry.insert(0, "Enter text here")
    entry.grid(column=0, row=1)
    
    # Button with callback
    def button_clicked():
        text = entry.get()
        label.config(text=text)
        messagebox.showinfo("Info", f"You entered: {text}")
    
    button = Button(text="Click Me", command=button_clicked)
    button.grid(column=0, row=2)
    
    window.mainloop()


# ========================================
# 5. FUNCTION ARGUMENTS (*args and **kwargs)
# ========================================

"""
Advanced function parameter handling:
- *args: Variable number of positional arguments (tuple)
- **kwargs: Variable number of keyword arguments (dictionary)
- Can combine regular parameters, *args, and **kwargs
"""

# *args example - unlimited positional arguments
def add_numbers(*args):
    """Add any number of arguments."""
    total = 0
    for num in args:
        total += num
    return total

result = add_numbers(1, 2, 3, 4, 5)  # Can pass any number of arguments

# **kwargs example - unlimited keyword arguments
def build_profile(**kwargs):
    """Build a profile from keyword arguments."""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

user = build_profile(name="Alice", age=25, city="NYC")

# Combining all types
def complex_function(required, default="default", *args, **kwargs):
    """Function with all parameter types."""
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

complex_function("needed", "custom", 1, 2, 3, extra="value", more="data")


# ========================================
# 6. FILE HANDLING
# ========================================

"""
Working with files:
- Opening files with open()
- Reading and writing modes
- Context managers (with statement)
- Automatic file closing
"""

# Reading files
def read_file_example():
    """Different ways to read files."""
    
    # Basic file reading (must close manually)
    file = open("data.txt")
    contents = file.read()
    file.close()
    
    # Using context manager (recommended)
    with open("data.txt") as file:
        contents = file.read()
        # File automatically closes after this block
    
    # Reading lines into a list
    with open("data.txt") as file:
        lines = file.readlines()  # List of lines
    
    return contents

# Writing files
def write_file_example():
    """Different file writing modes."""
    
    # Write mode (overwrites existing content)
    with open("output.txt", mode="w") as file:
        file.write("New content")
    
    # Append mode (adds to existing content)
    with open("output.txt", mode="a") as file:
        file.write("\nAdditional content")
    
    # Creating new file if it doesn't exist
    with open("new_file.txt", mode="w") as file:
        file.write("This creates a new file")


# ========================================
# 7. CSV AND PANDAS
# ========================================

"""
Working with structured data:
- CSV module for basic CSV operations
- Pandas for advanced data analysis
- DataFrames and Series
- Data manipulation and analysis
"""

import csv
import pandas as pd

def csv_example():
    """Basic CSV operations."""
    
    # Reading CSV with csv module
    with open("data.csv") as file:
        data = csv.reader(file)
        for row in data:
            print(row)  # Each row is a list
    
    # Reading CSV with pandas
    df = pd.read_csv("data.csv")
    print(df.head())  # First 5 rows
    
    # Accessing columns
    temperatures = df["temp"].to_list()
    
    # Filtering data
    hot_days = df[df.temp > 25]
    
    # Creating new DataFrame
    data_dict = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["NYC", "LA", "Chicago"]
    }
    new_df = pd.DataFrame(data_dict)
    
    # Saving to CSV
    new_df.to_csv("output.csv", index=False)
    
    # Statistical operations
    mean_temp = df["temp"].mean()
    max_temp = df["temp"].max()
    
    return df


# ========================================
# 8. ERROR HANDLING AND EXCEPTIONS
# ========================================

"""
Robust error handling:
- try/except blocks for catching errors
- Multiple except clauses for different errors
- else clause for success case
- finally clause for cleanup
- Raising custom exceptions
"""

def error_handling_example():
    """Comprehensive error handling."""
    
    try:
        # Code that might raise an exception
        file = open("data.txt")
        data = file.read()
        number = int(data)
        result = 10 / number
        
    except FileNotFoundError:
        print("File not found, creating new file")
        file = open("data.txt", "w")
        file.write("10")
        
    except ValueError as error:
        print(f"Invalid data format: {error}")
        
    except ZeroDivisionError:
        print("Cannot divide by zero")
        
    else:
        # Runs only if no exception occurred
        print(f"Success! Result: {result}")
        
    finally:
        # Always runs, even if there was an error
        if 'file' in locals():
            file.close()
            print("File closed")

# Raising custom exceptions
def validate_age(age):
    """Example of raising exceptions."""
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True


# ========================================
# 9. JSON DATA HANDLING
# ========================================

"""
Working with JSON:
- Reading JSON files
- Writing JSON files
- Converting between Python objects and JSON
- Updating JSON data
"""

import json

def json_example():
    """JSON file operations."""
    
    # Python dictionary to JSON
    data = {
        "name": "Alice",
        "age": 25,
        "hobbies": ["reading", "coding", "hiking"]
    }
    
    # Write JSON to file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    
    # Read JSON from file
    with open("data.json", "r") as file:
        loaded_data = json.load(file)
    
    # Update JSON file
    try:
        with open("data.json", "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    
    # Update data
    existing_data["new_field"] = "new_value"
    
    # Write back
    with open("data.json", "w") as file:
        json.dump(existing_data, file, indent=4)
    
    return loaded_data


# ========================================
# 10. LIST AND DICTIONARY COMPREHENSIONS
# ========================================

"""
Concise ways to create lists and dictionaries:
- List comprehensions: [expression for item in iterable if condition]
- Dictionary comprehensions: {key: value for item in iterable if condition}
- Nested comprehensions
"""

# List comprehensions
numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers]
even_squared = [n**2 for n in numbers if n % 2 == 0]

# Dictionary comprehensions
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}

# Conditional comprehensions
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
passed = {name: score for name, score in scores.items() if score >= 80}

# Nested comprehensions (use sparingly for readability)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]


# ========================================
# 11. IMPORTANT PYTHON CONCEPTS
# ========================================

"""
Additional important concepts from intermediate section:
"""

# Tuples - Immutable sequences
coordinates = (10, 20)  # Cannot be changed after creation
# coordinates[0] = 15  # This would raise an error

# Slicing - Extract portions of sequences
text = "Hello, World!"
print(text[0:5])    # "Hello"
print(text[::2])    # "Hlo ol!" (every 2nd character)
print(text[::-1])   # "!dlroW ,olleH" (reversed)

# Import variations
import math                    # Import entire module
from math import pi, sqrt      # Import specific items
from math import *             # Import everything (avoid)
import numpy as np            # Import with alias

# PascalCase vs snake_case
class MyClass:         # Classes use PascalCase
    def my_method():   # Methods/functions use snake_case
        pass

MY_CONSTANT = 100     # Constants use UPPER_SNAKE_CASE


# ========================================
# 12. COMPLETE PROJECT EXAMPLE
# ========================================

"""
Password Manager - Demonstrates multiple concepts together
"""

from tkinter import *
from tkinter import messagebox
import json
import random
import string

class PasswordManager:
    """Complete password manager application."""
    
    def __init__(self):
        """Initialize the password manager."""
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=20, pady=20)
        
        self.setup_ui()
        
    def setup_ui(self):
        """Create the user interface."""
        # Website entry
        Label(text="Website:").grid(row=0, column=0)
        self.website_entry = Entry(width=35)
        self.website_entry.grid(row=0, column=1, columnspan=2)
        self.website_entry.focus()
        
        # Email entry
        Label(text="Email:").grid(row=1, column=0)
        self.email_entry = Entry(width=35)
        self.email_entry.grid(row=1, column=1, columnspan=2)
        self.email_entry.insert(0, "user@email.com")
        
        # Password entry
        Label(text="Password:").grid(row=2, column=0)
        self.password_entry = Entry(width=21)
        self.password_entry.grid(row=2, column=1)
        
        # Buttons
        Button(text="Generate", command=self.generate_password).grid(row=2, column=2)
        Button(text="Add", width=36, command=self.save_password).grid(row=3, column=1, columnspan=2)
        Button(text="Search", width=15, command=self.search_password).grid(row=0, column=3)
    
    def generate_password(self):
        """Generate a strong random password."""
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(16))
        
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
    
    def save_password(self):
        """Save password to JSON file."""
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if not website or not password:
            messagebox.showwarning("Warning", "Please fill all fields!")
            return
        
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }
        
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        
        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)
        
        self.website_entry.delete(0, END)
        self.password_entry.delete(0, END)
        messagebox.showinfo("Success", "Password saved!")
    
    def search_password(self):
        """Search for a saved password."""
        website = self.website_entry.get()
        
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
                
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo("Not Found", f"No details for {website}")
                
        except FileNotFoundError:
            messagebox.showinfo("Error", "No data file found")
    
    def run(self):
        """Start the application."""
        self.window.mainloop()


# ========================================
# 13. KEY TAKEAWAYS
# ========================================

"""
INTERMEDIATE PYTHON KEY CONCEPTS:

1. Object-Oriented Programming
   - Think in terms of objects with attributes and methods
   - Use inheritance to avoid code duplication
   - Encapsulate related functionality in classes

2. GUI Development
   - Event-driven programming model
   - Separation of UI and logic
   - User input validation and feedback

3. File and Data Handling
   - Always use context managers (with statement)
   - Choose appropriate data format (CSV, JSON, etc.)
   - Handle exceptions gracefully

4. External Libraries
   - Pandas for data analysis
   - Tkinter for GUI applications
   - Learn to read documentation

5. Advanced Functions
   - Use *args and **kwargs for flexible functions
   - Understand scope and namespaces
   - Write pure functions when possible

6. Error Handling
   - Anticipate potential errors
   - Provide helpful error messages
   - Use try/except appropriately

7. Code Organization
   - Separate data from logic
   - Use modules for code organization
   - Follow naming conventions consistently

8. Best Practices
   - Write self-documenting code
   - Use type hints when helpful
   - Test edge cases
   - Keep functions focused on single tasks
"""

if __name__ == "__main__":
    print("🐍 Python Intermediate Concepts Summary")
    print("=" * 40)
    print("This file summarizes key concepts from Days 16-31:")
    print("- Object-Oriented Programming")
    print("- GUI Development with Tkinter")
    print("- File Handling and Data Processing")
    print("- External Libraries (Turtle, Pandas)")
    print("- Advanced Function Concepts")
    print("\nExplore each section for detailed examples and explanations!")