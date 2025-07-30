"""
Day 12 Content - Scopoe, Namespaces, Global Variables

The challenge will be a Number Guessing game.

"""

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# enemies inside function: 2
# enemies outside function: 1

"""
Variables declared inside a function have local scope.
They are only seen by other code within the same block of code.
"""
#local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) ## will error as potion_strength is not defined

# global scope variables are available at any level of code
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()  

# There is no Block Scope within Python; the variable has the same scope as it's enclosing function
if 3 > 2:
    a_variable = 10

## Global & Local example two

game_level = 3
enemies = ["skeleton", "zombie", "alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

#####

game_level = 3
enemies = ["skeleton", "zombie", "alien"]

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

#### same as above but the variable has been initialised; above would never print if level 5 or above
#### this one would return ""
game_level = 3
enemies = ["skeleton", "zombie", "alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

    """
Prime Number Checker

Prime numbers are numbers that can only be cleanly divided by themselves and 1. Wikipedia  

You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  It should return True or False.

e.g. 7 is a primer number because it is only divisible by 1 and itself.
But 4 is not a prime number because you can divide it by 1, 2 or 4.
NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.

Example Input 1
73
Example Output 1
True

Example Input 2
75
Example Output 2
False
"""

def is_prime(num):
    
    for x in range(2, num):
        if num % x == 0:
            return("Not prime")
    else:
        return("Prime")

result = is_prime(75)
print(result)

"""
Modifying global scope

They are actually two entirely different variables.

enemies = "skeleton"

def increase_enemies():
    enemies = "zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

enemies inside function: zombie
enemies outside function: skeleton

"""

## Errors as it's looking for the local variable
enemies = 0

def increase_enemies():
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()


## This tells it we're using the global variable enemies
enemies = 0

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()

"""
Modifying global variables is error prone / open to bugs as the global could have been created anywhere in the code
Reading is fine
Below is a better way of doing it
"""

enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1
    

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

"""
Global Constants

use all upper case

URL = a.com
PI = 3.14159
"""

"""
# ASCII art generator https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
"""