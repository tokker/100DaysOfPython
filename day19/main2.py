from turtle import Turtle, Screen
import random

def move_forward(t):
	distance = random.randint(1, 5)
	t.forward(distance)
	
screen = Screen()
screen.setup(500,400)
bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for i in range(6):
	turtles.append(Turtle(shape="turtle"))
	turtles[i].color(colors[i])
	turtles[i].penup()
	turtles[i].goto(-230, -100 + i*50)

win = False
while not win:
	for i in range(6):
		move_forward(turtles[i])
		if turtles[i].xcor() >= 230:
			win = True
			if bet == colors[i]:
				print(f"You've won! The {colors[i]} turtle is the winner!")
			else:
				print(f"You've lost! The {colors[i]} turtle is the winner!")
			break
		
screen.exitonclick()


