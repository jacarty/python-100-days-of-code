"""
Day Five Content - For Loops, Range and Code Blocks

Looks like we'll be making a password generator
"""

"""
for item in list_or_items:
    do something for each item
"""

fruits = ["Strawberries", "Grapes", "Peaches"]

for fruit in fruits:
    print(fruit)

### example how to recreate a sum function with for loop
student_scores= [123, 111, 143, 153, 113, 114, 122, 124]

total_exam_scores = sum(student_scores)
print(total_exam_scores)

sum = 0
for score in student_scores:
    sum += score
print(sum)

### example how to recreate a max function with for loop
student_scores= [123, 111, 143, 153, 113, 114, 122, 124]

print(max(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

"""
Range Function

for number in range(a, b):
    print(number)
"""

for number in range(0, 10):
    print(number)

for number in range(0, 10, 2):
    print(number)

# Add up 1 to 100
sum = 0
for number in range(1,101):
    sum += number
print(sum)

# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. 
# These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# e.g. it might start off like this:

#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz

# ...etc

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)