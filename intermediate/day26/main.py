# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

df = pd.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

user_word = input("Enter a word for conversion: ").upper()
nato_output = [nato_dict[code] for code in user_word]
print(nato_output)

# JAMES
# ['Juliet', 'Alfa', 'Mike', 'Echo', 'Sierra']