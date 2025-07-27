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