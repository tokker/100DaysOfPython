def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2
	
end = False
result = None

while not end:
	if result == None:
		number1 = float(input("What's the first number?: "))
		first_half = number1
	print("+\n-\n*\n/")
	operation = input("Pick an operation: ")
	number2 = float(input("What's the next number?: "))
	if operation == "+":
		result = add(number1, number2)
	elif operation == "-":
		result = subtract(number1, number2)
	elif operation == "*":
		result = multiply(number1, number2)
	elif operation == "/":
		result = divide(number1, number2)
	else:
		result = "Invalid operation"
	print(f"{first_half} {operation} {number2} = {result}")
	number1 = result
	first_half = str(first_half) + " " + str(operation) + " " + str(number2)
	if input(f"Type 'y' to continue calculating with {result}, or type 'n' to end calculation: ") == "n":
		end = True