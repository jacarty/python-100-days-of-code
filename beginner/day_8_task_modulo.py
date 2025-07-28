
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(encode_or_decode, original_text, shift_amount):
    
    output_text = ""

    # by multiplying by -1 it reverse positive to negative in the next line
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for each_letter in original_text:

        # find position of original letter
        original_position = alphabet.index(each_letter)
        # calculate new position from end
        new_position = (original_position + shift_amount) % len(alphabet)
        # add new letter to new word
        output_text +=  alphabet[new_position]

    # clever use of variable with d at end    
    print(f"This is your {encode_or_decode}d word: {output_text}")


caeser(encode_or_decode=direction, original_text=text, shift_amount=shift)
