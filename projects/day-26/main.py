import pandas
# Program to convert any word to a NATO Alphabet

#1. Create a dictionary in format: {"A": "Alfa", "B": "Bravo"...}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row['letter']:row['code'] for (index, row) in data.iterrows()}
# 2. User types in a word [e.g. "Enter a word: Thomas]
# and when user hits enter, retrieve a list ['Tango', 'Hotel', 'Oscar', 'Mike', 'Alfa', 'Sierra']
word = input("Enter a word: ").upper()
result = [new_dict[letter] for letter in word]
print(result)