print("Welcome to the NATO phonetic alphabet project.")

import pandas as pd

nato_phonetic_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
# nato_phonetic_alphabet_dict = {key: values for (key, values) in nato_phonetic_alphabet.items()}
nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}

word = input("Enter a word: ").upper()

output_list = [nato_phonetic_alphabet_dict[letter] for letter in word]
print(output_list)
