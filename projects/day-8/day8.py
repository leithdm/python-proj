def caesarCipherEncryptor(string, key):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	encrypted_string = ""
	for character in string:
		position = alphabet.index(character)
		new_position = position + key
		if new_position > 25:
			new_position = new_position % 26
		new_letter = alphabet[new_position]
		encrypted_string += new_letter
	return encrypted_string


print(caesarCipherEncryptor("xyz", 2))