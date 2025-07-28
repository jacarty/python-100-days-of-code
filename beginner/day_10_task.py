from day_10_art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2
    
def multiply(n1, n2):
    return n1 * n2
    
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)
first_number = float(input("What's the first number?: "))
keep_calculating = True

while keep_calculating:

    ## instuctor used this to print the symbols
    #for symbol in operations:
    #    print(symbol)

    calc_type = input("Operator options are: + - * /\nWhich would you like?: ")
    second_number = float(input("What's the second number?: "))

    # looks up the calc_type in the operations dictionary to return the function name
    my_operator = operations[calc_type]

    # uses the output of above (function name) and then inputs the two numbers
    output = my_operator(first_number, second_number)

    # prints the function output
    print(f"{first_number} + {calc_type} + {second_number} = {output}")

    continue_calc = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation, or anything else to quit:\n").lower()

    if continue_calc == "y":
        first_number = output
    elif continue_calc == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        first_number = float(input("What's the first number?: "))
    else:
        quit()


"""
INSTRUCTOR
import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
"""