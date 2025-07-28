from day_8_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caeser(encode_or_decode, original_text, shift_amount):

    output_word = ""
    cipher_alphabet = alphabet * 2

    # set to negative number for decode and add 26 to move backwards
    if encode_or_decode == "decode":
        shift_amount *= -1 + 26

    for each_letter in original_text:
   
        # check if it's a letter
        if each_letter in alphabet:
            # find position of original letter
            original_position = alphabet.index(each_letter)
            # calculate new position
            new_position = original_position + shift_amount
            # add new letter to new word
            output_word +=  cipher_alphabet[new_position]

        # if it's a character that isn't in the alphabet just add it, e.g. space or special character
        else:
            output_word +=  each_letter
        
    print(f"This is your {encode_or_decode}d word: {output_word}")

continue_cipher = True

while continue_cipher:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(encode_or_decode=direction, original_text=text, shift_amount=shift)

    want_to_continue = input("If you want to continue type 'yes'. Otherwise type 'no'.\n").lower()

    if want_to_continue == "yes":
        continue
    if want_to_continue == "no":
        continue_cipher = False
        print("Goodbye.")
