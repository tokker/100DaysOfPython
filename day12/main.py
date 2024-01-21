import random

attempts = 10
win = False

number = random.randint(1,100)
print("Welome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
if input("Choose a difficulty. Type 'easy' or 'hard': ") == "hard":
	attempts = 5
while attempts > 0 and not win:
	print(f"You have {attempts} attempts remaining to guess the number.")
	guess = int(input("Make a guess: "))
	if guess == number:
		win = True
	elif guess > number:
		print("Too high.")
		attempts -= 1
	else:
		print("Too low.")
		attempts -= 1
if win:
	print(f"You got it! The answer was {number}.")
else:
	print("You've run out of guesses, you lose.")
