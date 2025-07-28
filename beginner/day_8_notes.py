"""
Day Eight Content - Functions with Inputs

The challenge will be Caeser cypher
"""

"""
Standard function

def my_function():
    do this
    then this
    finally this

my_function()
"""

# create function called greet and give it three things to print
# define
def greet():
    print("Hello!")
    print("I'm the greet function.")
    print("Hope you're having a good day?")

# call
greet()

"""
Function that allows for Inputs

def my_function(something):
    do this
    then this
    finally this

my_function()
"""

# create function called greet with input and give it three things to print
# define function and parameter
def greet_with_name(name):
    print(f"Hello {name}!")
    print("I'm the greet function.")
    print("Hope you're having a good day?")

# call with argument
greet_with_name("James")

"""
Life in Weeks

I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, 
if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.

Where x is replaced with the actual calculated number of weeks the input age has left until age 90.


**Warning** The function must be called life_in_weeks for the tests to pass. 
Also the output must have the same punctuation and spelling as the example. Including the full stop!

Example Input
56


Example Output
You have 1768 weeks left.
"""

def life_in_weeks(current_age):
    years_remaining = 90 - current_age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")

life_in_weeks(X)

"""
Multiple Inputs Example

Default way is to use Positional Argument, i.e. just take the input order and use. 

Keyword arg
"""

def greet_with(name, location):
    print(F"Hi {name}, I understand you're from {location}?")

greet_with("James", "Hove")

greet_with("Hove", "James")

"""
Multiple Inputs Example

Keyword arg always ties the parameter to the argument
"""

def greet_with(name, location):
    print(F"Hi {name}, I understand you're from {location}?")

greet_with(location="Hove", name="James")

"""
Love Calculator
💪 This is a difficult challenge! 💪 
You are going to write a function called calculate_love_score() that tests the compatibility between two names.  
To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 

Total = 5 

L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 
Total = 3 

Love Score = 53

Example Input 
calculate_love_score("Kanye West", "Kim Kardashian")
Example Output
42
"""


### I've seemingly overcomplicated this and reflected on why strings would be better
###

def calculate_love_score(name1, name2):
    
    combined_names = []
    true_list = ["t", "r", "u", "e" ]
    love_list = ["l", "o", "v", "e"]
    score_one = 0
    score_two = 0

    # add each letter of the names to a list; remove spaces; lower as added
    for index, each_char in enumerate(name1+name2):
        if each_char == " ":
            continue
        else: 
            combined_names.append(each_char.lower())
        print(combined_names)

    # lookup each letter vs the two lists
    for each_char in combined_names:

        if each_char in true_list:
            score_one += 1
            print(score_one)

        if each_char in love_list:
            score_two += 1
            print(score_two)

    print(f"Your love score is {score_one}{score_two}")

calculate_love_score("Kanye West", "Kim Kardashian")

"""
Instructor 

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
        
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
        
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
            
    score = int(str(first_digit) + str(second_digit))
    print(score)
        
calculate_love_score("Kanye West", "Kim Kardashian")

"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text, shift_amount):
    # print(original_text)
    # print(shift_amount)

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

    cipher_word = ""
    
    # rather than double the alphabet
    # instructor did below modulo to get the remainder
    # remainder is the correct offset 0-25
    # 35 % 26 = 9 (example of Z offset 9)
    # example letter 1 offset 20
    # 11 (12th letter) % 26 = 5 which is F
    # this would work for any list - modulo the list length
    # new_position %= len(alphabet)

    # double the alphabet list to allow for offset of up to 25 chars (TODO 4)
    cipher_alphabet = alphabet * 2

    for each_letter in original_text:
        # find position of original letter
        original_position = alphabet.index(each_letter)
        # calculate new position
        new_position = original_position + shift_amount
        # add new letter to new word
        cipher_word +=  cipher_alphabet[new_position]
    
    print(f"This is your encoded word: {cipher_word}")

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    "Please retry"

"""
    Note on ABOVE
    rather than double the alphabet
    instructor did below modulo to get the remainder
    remainder is the correct offset 0-25
    35 % 26 = 9 (example of Z offset 9)
    this would work for any list - modulo the list length
    new_position %= len(alphabet)
"""