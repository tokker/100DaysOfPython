import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if playerChoice == 0:
	print(rock)
elif playerChoice == 1:
	print(paper)
else:
	print(scissors)
print("\nComputer chose:\n")
computerChoice = random.randint(0,2)
if computerChoice == 0:
	print(rock)
elif computerChoice == 1:
	print(paper)
else:
	print(scissors)
if playerChoice == computerChoice:	
	print("It's a draw")
elif (playerChoice == 0 and computerChoice == 1) or (playerChoice == 1 and computerChoice == 2) or (playerChoice == 2 and computerChoice == 0):
	print("You lose")
else:
	print("You win")
	