"""
Day Six Content - Functions, Code Blocks and While Loops

Looks like we'll be making a Escape the Maze game
"""

"""
Already used a lot of built-in functions - e.g. print, len, range
"""

print("Hello")
num_char = len("Hello")
print(num_char)

"""
Defining our own function is easy def function_name():
"""
# Defining function
def my_function():
    print("Hello")
    print("Bye")

# Calling function
my_function()


"""
Reeborg's Python
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fselect_collection_en.json&name=Other%20worlds&url=%2Fworlds%2Fmenus%2Fselect_collection_en.json

# Hurdles Game
"""

# define right turn
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# define jump
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# hurdle six times
for step in range(6): # 6 times
    jump()

"""
Reminder -- For Loops

for item in list_of_items:
    do something to each item

for number in range(a, b):
    do something 

While Loops

whilst something_is_true:
    do something
"""

# hurdle while loop example
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1 # decrease by one each time
    print(number_of_hurdles) #

# for the one with the random goal line
while at_goal() != True:
    jump()

# using it't negation (whilst False)
while not at_goal():
    jump()

"""
For loops are great when you want to iterate over something and you need to do something with each thing.
For loops are great when you want to do something in a range.

While loops are best when you just want to do something until the condition changes.
Whilst loops are more dangerous as they can create infinite loops.
"""

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# Hurdles 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Hurdles 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()