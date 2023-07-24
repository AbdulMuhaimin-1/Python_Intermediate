# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# is_text = True
# while is_text:
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError as error_message:
#         print(f"Sorry, {error_message} not acceptable, only letters in the alphabet are acceptable please.")
#     else:
#         print(output_list)
#         is_text = False


def nato_alphabet():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as error_message:
        print(f"Sorry, {error_message} not acceptable, only letters in the alphabet are acceptable please.")
        nato_alphabet()
    else:
        print(output_list)


nato_alphabet()
