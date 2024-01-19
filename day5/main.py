#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
categories = []
if nr_letters > 0:
	categories.append("letters")
if nr_symbols > 0:
	categories.append("symbols")
if nr_numbers > 0:
	categories.append("numbers")


for i in range(0,nr_letters + nr_symbols + nr_numbers):
	categoriy = categories[random.randint(0,len(categories)-1)]
	if categoriy == "letters": 
		password += letters[random.randint(0,len(letters)-1)]
		nr_letters -= 1
		if nr_letters == 0:
			categories.remove("letters")
	elif categoriy == "numbers":
		password += numbers[random.randint(0,len(numbers)-1)]
		nr_numbers -= 1
		if nr_numbers == 0:
			categories.remove("numbers")
	else:
		password += symbols[random.randint(0,len(symbols)-1)]
		nr_symbols -= 1
		if nr_symbols == 0:
			categories.remove("symbols")

print(f"Your password is: {password}")