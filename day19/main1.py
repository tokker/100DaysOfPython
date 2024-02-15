from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forward():
	t.forward(10)
	
def move_backward():
	t.backward(10)
	
def move_left():
	t.left(10)
	
def move_right():
	t.right(10)

def clear():
	t.home()
	t.clear()
	

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()