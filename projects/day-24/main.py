PLACEHOLDER = "[name]"

# absolute path
with open("./Input/Names/invited_names.txt") as names_file:
    # return all lines in the file as a list, where each line is an item in list object
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # remove spaces at start and end of string
        stripped_name = name.strip()
        # replace will replace a specified phrase with another specified phrase
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

