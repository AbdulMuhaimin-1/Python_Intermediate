# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as recipients:
    name_of_recipients = recipients.readlines()
for each_name in range(len(name_of_recipients)):
    name = name_of_recipients[each_name]

    with open("./Input/Letters/starting_letter.txt") as letter:
        content = letter.read()
        new_content = content.replace("[name]", name.strip())

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
        new_letter.write(new_content)












    # letter = open("./Input/Letters/starting_letter.txt", mode="r")
    # content = letter.read()
    # new_content = content.replace("[name]", name.strip())
    # letter.close()
    #
    # new_letter = open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w")
    # new_letter.write(new_content)









# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp