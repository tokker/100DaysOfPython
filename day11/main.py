import random 

def draw_card(player_cards):
	index = random.randint(0, len(cards)-1)
	player_cards.append(cards[index])
	cards.pop(index)
	for i in range(len(player_cards)):
		if sum(player_cards) > 21 and player_cards[i] == 11:
			player_cards[i] = 1
	return player_cards

end = False

while not end:
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	user_cards = []
	computer_cards = []
	user_cards = draw_card(user_cards)
	user_cards = draw_card(user_cards)
	computer_cards = draw_card(computer_cards)
	computer_cards = draw_card(computer_cards)
	print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
	if computer_cards[0] == 1:
		print(f"Computer's first card: {computer_cards[1]}")
	else:
		print(f"Computer's first card: {computer_cards[0]}")
	end_draw = False
	if(sum(computer_cards) == 21 or sum(user_cards) == 21):
		end_draw = True
	while not end_draw:
		if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
			user_cards = draw_card(user_cards)
			print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
			if computer_cards[0] == 1:
				print(f"Computer's first card: {computer_cards[1]}")
			else:
				print(f"Computer's first card: {computer_cards[0]}")
			if sum(user_cards) >= 21:
				end_draw = True
		else:
			end_draw = True
	if(sum(user_cards) < 21):
		while sum(computer_cards) < 17:
			computer_cards = draw_card(computer_cards)
	print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
	print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
	if sum(computer_cards) > 21 or (sum(computer_cards) < sum(user_cards) and sum(user_cards) <= 21):
		print("You win!")
	elif sum(computer_cards) == sum(user_cards) and sum(computer_cards) != 21:
		print("Draw!")
	else:
		print("You lose!")
	if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "n":
		end = True
		
	