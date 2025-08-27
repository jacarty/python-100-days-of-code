"""
Errors, Exceptions and Saving JSON Data

try:

except:

else:

finallly:

"""

######
# File Example
######

# would fail if file doesn't exist
# with open("a_file.txt") as f:
#     f.read()

# try this
try:
    f = open("a_file.txt")
    a_dict = {"key" : "value"}
    print(a_dict["ads"])
# error specific
except FileNotFoundError:
    print("There was an error opening, creating file")
    f = open("a_file.txt", "w")
    f.write("Hello")
# error specific that's captured
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist.")
# run if the try succeeds
else:
    content = f.read()
    print(content)
# happens regardless if the code succeeds or fails
finally:
    f.close()
    print("The file was closed.")

    # allows you to raise an error and message
    raise TypeError("This is an error I made up.")

######
# Realk Example
# Valid code but nonsense result
######

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)

"""
IndexError Handling

Issue 

We've got some buggy code. Try running the code. The code will crash and give you an IndexError.
This is because we're looking through the list of fruits for an index that is out of range. 


Objective 

Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie". 


IMPORTANT: The exception handling should NOT allow each fruit to be printed when there is an exception. e.g. it should not print out Apple pie, Pear pie and Orange pie, when there is an exception it should only print "Fruit pie".  
"""

fruits = ["Apple", "Pear", "Orange"]
     
# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")
     
make_pie(4)



"""
KeyError Handling

We've got some buggy code, try running the code. The code will crash and give you a KeyError.
This is because some of the posts in the facebook_posts don't have any "Likes". 

Objective 
Use what you've learnt about exception handling to prevent the program from crashing.
"""

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
 
    total_likes = 0
    for post in posts:
      try:
        total_likes = total_likes + post['Likes']
      except KeyError:
        pass 
    
    return total_likes
 
 
count_likes(facebook_posts)



############
# Mine
############

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

while True:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, please only enter letters of the alphabet.")
        continue
    else:
        print(output_list)
        break

""""
JSON
"""

########
# JSON file to read
########
# dict = dictionary to pass in (serialise)
# file_name is output
# indent=4 is number spaces to add (for readability)
json.dump(dict, file_names, indent=4)

########
# JSON file name to load
########
# outputs back to dictionary (deserialise)
json.load(file_name)

########
# update a JSON file
########
# read old data from file
data = json.load(data_file)
# update old data with new data
json.update(dict)
# write file back
json.dump(data, file_name, indent=4)

