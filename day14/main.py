import random
import game_data

last_index = random.randint(0, len(game_data.data) - 1)
index = last_index
loose = False
score = 0

while not loose:
	while last_index == index:
		index = random.randint(0, len(game_data.data)-1)
	print("Compare A: " + game_data.data[last_index]['name'] + ", " + game_data.data[last_index]['description'] + ", from " + game_data.data[last_index]['country'] + "\n")
	print("Against B: " + game_data.data[index]['name'] + ", " + game_data.data[index]['description'] + ", from " + game_data.data[index]['country'])
	choice = input("Who has more followers? Type 'A' or 'B': ")
	if choice == 'A':
		if game_data.data[last_index]['follower_count'] > game_data.data[index]['follower_count']:
			score += 1
			last_index = index
		else:
			loose = True
	elif choice == 'B':
		if game_data.data[last_index]['follower_count'] < game_data.data[index]['follower_count']:
			score += 1
			last_index = index
		else:
			loose = True
	print(f"Your score is {score}")
	print("\n")
print(f"You loose, your score is {score}")
