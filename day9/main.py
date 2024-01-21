print("Welcome to the secret auction program.")

bidders = {}
calculate = False
while calculate == False:
	name = input("What is your name?: ")
	bid = int(input("What's your bid?: $"))
	bidders[name] = bid
	if input("Are there any other bidders? Type 'yes' or 'no'.\n") == "no":
		calculate = True

max_bidder = ""
for bidder in bidders:
	if max_bidder == "":
		max_bidder = bidder
	elif bidders[bidder] > bidders[max_bidder]:
		max_bidder = bidder
	
print(f"The winner is {max_bidder} with a bid of ${bidders[max_bidder]}.")
	