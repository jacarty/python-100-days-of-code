"""
Working with local files and directories
"""

# Open, read and close a file
# You need to rememeber to close to free up memory
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Using with method closes files when you've finished with it
with open("my_file.txt") as f:
    contents = f.read()
    print(contents)

# Writing to a file; w overwrites the content
with open("my_file.txt", mode="w") as f:
    contents = f.write("My text.")

# Writing to a file; a appends
with open("my_file.txt", mode="a") as f:
    contents = f.write("\nAdditional text.")
    print(contents)

# Writing to a file that doesn't exist, creates it.
with open("new_file.txt", mode="a") as f:
    contents = f.write("Hello, this is a new file with text.")
    print(contents)

# Related to files
# import OS
import os
# Show current working directory
print("Current working directory:", os.getcwd())
# List files in current directory
print("Files in current directory:", os.listdir())


"""
Instructor Mail Merge
"""

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

