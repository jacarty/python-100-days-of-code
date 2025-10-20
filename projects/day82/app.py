"""
Assignment: Text to Morse Code Converter
A text-based Python program to convert Strings into Morse Code.

"""

from morse_code import morse_code

#############################################################
# Input
#############################################################

message = input("""
############################################################################
########################### Morse Code Generator ###########################
############################################################################
   
Hi there!
Please enter the word or phrase you would like to convert to Morse Code.
Note: Only Letters, Numbers, Punctuation and Spaces are valid.
Enter your phrase: """
).lower()

#############################################################
# Function
#############################################################

def converter(message):

    # Check for invalid characters
    invalid_chars = [char for char in message if char not in morse_code]
    if invalid_chars:
        return f"\nInvalid character(s): {', '.join(set(invalid_chars))} \nPlease try again."
    
    # Convert
    encoded = [morse_code[char] for char in message]
    return f"\nHere is your encoded message:\n\n{' '.join(encoded)}\n"


#############################################################
# Init
#############################################################

if __name__ == "__main__":
    output = converter(message)
    print(output)
