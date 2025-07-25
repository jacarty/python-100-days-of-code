"""
1 - Create a greeting for your program
2 - Ask the user for the name of the city they grew up in and store as a variable
3 - Ask the user for the name of their pet and store as a variable
4 - Combine the city and pet names to show them their band name
5 - Make sure the input cursor shows on a new line
"""

print("Hello, and welcome to the Band Name Generator!")
city = input("Firstly, please enter the name of the city you grew up in?\n")
pet_name = input("Now, please enter the name of of your first pet?\n")
print("Congratulations; your band name is " + city + " " + pet_name)