"""
Lists and Dictionary Comprehensions

The project is to spell things using the Phonetic Alphabet

Regular
new_list = [new_item for item in list]
new_list = [letter for letter in string]
new_list = [number for number in range()]

Conditional 
new_list = [new_item for item in list if test]

"""

###############
# for loop example adding one to each number in list 
###############

numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1 
    new_list.append(add_1)

print(new_list)
# [2, 3, 4]


###############
# with list comprehension
###############

# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)
# [2, 3, 4]

###############
# String example
# new_list = [letter for letter in list]
###############

name = "James"
list = [letter for letter in name]
print(list)
# ['J', 'a', 'm', 'e', 's']

###############
# double the number in range
# new_list = [number for number in range()]
###############

list = [n * 2 for n in range(1,5)]
print(list)
# [2, 4, 6, 8]

###############
# conditional list comprehension
# new_list = [new_item for item in list if test]
# only add names of four letter to new list
###############

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)
# ['Alex', 'Beth', 'Dave']

###############
# Make names over 5 letters all upper case
###############

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
# ['CAROLINE', 'ELEANOR', 'FREDDIE']

"""
Squaring Numbers

You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared. 

e.g. 4 * 4 = 16
4 squared equals 16.
**DO NOT** modify the List numbers directly. Try to use List Comprehension instead of a Loop. 

Target Output 
[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]  
"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)


"""
Filtering Even Numbers

In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.   

First, use list comprehension to convert the list_of_strings to a list of integers called numbers.   
Then use list comprehension again to create a new list called result.
This new list should only contain the even numbers from the list numbers. 
Again, try to use Python's List Comprehension instead of a Loop.   
"""

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(s) for s in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)

"""
Data Overlap

💪 This exercise is HARD 💪 

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
You are going to create a list called result which contains the numbers that are common in both files. 
e.g. if file1.txt contained: 

1 
2 
3

and file2.txt contained: 

2
3
4

result = [2, 3]

IMPORTANT:  The output should be a list of integers and not strings! 
"""

with open("./file1.txt") as file1:
    f1_data = file1.readlines()
with open("./file2.txt") as file2:
    f2_data = file2.readlines()

result = [int(num) for num in f1_data if num in f2_data]

print(result)


## Mine
with open("./file1.txt") as file1:
    f1_data = [line.strip() for line in file1.readlines()]
with open("./file2.txt") as file2:
    f2_data = [line.strip() for line in file2.readlines()]


result = [int(num) for num in set(f1_data) & set(f2_data)]

print(result)


"""
When to use each approach:


missed_states = [state for state in data.state if state not in correct_states]
missed_states = list(set(data.state) - set(correct_states))


########
# Use list comprehension when:
########

# You need to preserve order
missed_states = [state for state in data.state if state not in correct_states]

# You need to transform data while filtering
missed_states_upper = [state.upper() for state in data.state if state not in correct_states]

# You have more complex conditions
missed_states = [state for state in data.state 
                 if state not in correct_states and len(state) > 5]
########
# Use sets when:
########

# Simple difference operations
missed_states = list(set(data.state) - set(correct_states))

# Need intersection
common_states = list(set(states1) & set(states2))

# Need union
all_states = list(set(states1) | set(states2))

"""

###########
###########
# Dictionary Comprehension
# new_dict = {"new_key":"new_vaule" for item in list}
#
# new_dict = {"new_key":"new_vaule" for (key, value) in dict.items()}
###########
###########

########
# Assign random score to student 
########
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)


########
# Assign random score to student 
# Assign student with score over 60 to pass list
########
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

# You have to call the items method on the dictionary
passed_students = {student:score for (student, score) in student_scores.items() if score > 60}
print(passed_students)

"""
Dictionary Comprehension 1

You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.   

Try to use Dictionary Comprehension instead of a Loop. 

To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8. 
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result = {word:len(word) for word in words}
print(result)
# {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

"""
Dictionary Comprehension 2

You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. 

To convert temp_c into temp_f use this formula: 

(temp_c * 9/5) + 32 = temp_f 
"""

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:((temp * 9/5) + 32) for (day, temp) in weather_c.items()}

print(weather_f)
# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}

"""
Loops and Pandas Dataframe
"""

student_dict = {
    "student": ["Angela", "Alan", "James", "Katie"],
    "score": [55, 37, 86, 90],
}

for key, value in student_dict.items():
    print(key)
    print(value)
    
    # student
    # ['Angela', 'Alan', 'James', 'Katie']
    # score
    # [55, 37, 86, 90]

"""
Loops and Pandas Dataframe

"""

student_dict = {
    "student": ["Angela", "Alan", "James", "Katie"],
    "score": [55, 37, 86, 90],
}

# looping through dictionary
for (key, value) in student_dict.items():
    print(key)
    print(value)
#   student  score
# 0  Angela     55
# 1    Alan     37
# 2   James     86
# 3   Katie     90

##########
# Dataframe
##########

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

##########
# looping though dataframe
##########

for (key, value) in student_data_frame.items():
    print(key)
    print(value)
#   student  score
# 0  Angela     55
# 1    Alan     37
# 2   James     86
# 3   Katie     90
# student
# 0    Angela
# 1      Alan
# 2     James
# 3     Katie

##########
# looping though dataframe rows 
##########
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row)

for (index, row) in student_data_frame.iterrows():
    print(row.student)

for (index, row) in student_data_frame.iterrows():
    if row.student == "James":
        print(row.score)

"""
Final Challenge
"""
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

df = pd.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

user_word = input("Enter a word for conversion: ").upper()
nato_output = [nato_dict[code] for code in user_word]
print(nato_output)

# JAMES
# ['Juliet', 'Alfa', 'Mike', 'Echo', 'Sierra']