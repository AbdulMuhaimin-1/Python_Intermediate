import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    # print(value)
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # print(row)
    # Access row.student or row.score
    pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name:").upper()
name_phonetic_code_word = [alphabet_dict[letter] for letter in name]
print(name_phonetic_code_word)
