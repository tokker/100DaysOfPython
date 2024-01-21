def encrypt(text, shift):
	text2 = []
	for letter in text:
		if letter in alphabet:
			index = alphabet.index(letter)
			index += shift%26
			if index > 25:
				index -= 26
			text2.append(alphabet[index])
		else:
			text2.append(letter)
	return "".join(text2)

def decrypt(text, shift):
	text2 = []
	for letter in text:
		if letter in alphabet:
			index = alphabet.index(letter)
			index -= shift%26
			text2.append(alphabet[index])
		else:
			text2.append(letter)
	return "".join(text2)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end = False

while not end:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	if direction == "encode":
		result = encrypt(text, shift)
	else:
		result = decrypt(text, shift)
	print(f"Here is the result: {result}")
	if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n") == "no":
		end = True