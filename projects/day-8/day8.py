import math
from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True

def encrypt(text, shift, direction):
    cipher_string = " "
    for character in text:
        position = alphabet.index(character)
        if direction == 'encode':
            new_position = position + shift
            if new_position > 25:
                new_position = 25 - (position)
            new_letter = alphabet[new_position]
            cipher_string += new_letter
        elif direction == 'decode':
            new_position = position - shift
            if new_position < 0:
                new_position = 25 - (position)
            new_letter = alphabet[new_position]
            cipher_string += new_letter
    print(cipher_string)

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift, direction)
    result = input("Type 'y' if you want to go again. Otherwise type 'n'.\n")
    if result == 'n':
        should_continue = False
        print("Goodbye")

