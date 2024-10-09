import pandas as pd
import re

def validate_input(user_input):
    return bool(re.match("^[A-Z]*$", user_input))

data = pd.read_csv("Day 026/nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row["code"] for (index, row) in data.iterrows()}

another_word = "y"

while another_word == "y":
    user_input = input("Enter a word to generate the nato equivalents: ").upper()
    while not validate_input(user_input):
        print("Invalid input. Please enter only letters.")
        user_input = input("Enter a word to generate the nato equivalents: ").upper()

    nato_equivalents = [nato_dict.get(letter, "Invalid letter") for letter in user_input]
    print(nato_equivalents)
    another_word = input("Do you want to try another word? (y/n): ").lower()
    
print("Ok, goodbye!")  