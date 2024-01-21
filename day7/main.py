import random
import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
	  |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
	  |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
	  |
	  |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
	  |
	  |
=========''', '''
  +---+
  |   |
  O   |
  |   |
	  |
	  |
=========
''', '''
  +---+
  |   |
  O   |
	  |
	  |
	  |
=========
''', '''
  +---+
  |   |
	  |
	  |
	  |
	  |
=========
''']

word_list = word_list.word_list

chosen_word = word_list[random.randint(0,len(word_list)-1)]
word_letters = []
for letter in chosen_word:
	word_letters.append("_")

print(' '.join(word_letters))
player_win = False
player_lives = 6
while not player_win and player_lives > 0:
	guessed_letter = input("\nGuess a letter: ").lower()
	letter_in_word = False
	for i in range(0, len(chosen_word)):
		if chosen_word[i] == guessed_letter:
			word_letters[i] = guessed_letter
			letter_in_word = True
	print(' '.join(word_letters))	
	if letter_in_word == False:
		player_lives -= 1
	if "_" not in word_letters:
		player_win = True
	print(stages[player_lives])
if(player_lives == 0):
	print(f"You lose, the word was {chosen_word}.")
else:
	print("You win!")