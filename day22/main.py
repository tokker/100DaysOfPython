from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard


screen = Screen()
screen.setup(1000, 500)
screen.bgcolor("black")
screen.title("Pong Game")

screenDrawer = Turtle(visible=False)
screenDrawer.penup()
screenDrawer.color("white")
screenDrawer.speed("fastest")
screenDrawer.goto(0, 240)
screenDrawer.right(90)
screenDrawer.pensize(3)
for i in range(24):
    screenDrawer.pendown()
    screenDrawer.forward(8)
    screenDrawer.penup()
    screenDrawer.forward(12)

paddle1 = Paddle(-1)
paddle2 = Paddle(1)

screen.listen()
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")

ball = Ball()
p1_sc = ScoreBoard(-1)
p2_sc = ScoreBoard(1)
player1_points = 0
player2_points = 0

while not (player1_points == 5 or player2_points == 5):
    time.sleep(0.004)
    ball.move_forward()
    if ball.xcor() < -470:
        if ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50:
            ball.right(ball.degree)
            ball.degree = (ball.ycor() - paddle1.ycor()) * 90 / 50
            ball.left(ball.degree)
        else:
            player2_points +=1
            ball.start()
            paddle1.start()
            paddle2.start()
            p2_sc.addPoint()
            time.sleep(0.5)
    if ball.xcor() > 470:
        if ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50:
            ball.right(ball.degree)
            ball.degree = (paddle2.ycor() - ball.ycor()) * 90 / 50 - 180
            ball.left(ball.degree)
        else:
            player1_points += 1
            ball.start()
            paddle1.start()
            paddle2.start()
            p1_sc.addPoint()
            time.sleep(0.5)

if player1_points == 5:
    winner = "Left player"
else:
    winner = "Right player"
game_over = Turtle(visible=False)
game_over.penup()
game_over.goto(0, -100)
game_over.color("white")
game_over.write(f"Game over!\n{winner} won", align="center", font=("Arial", 48, "bold"))

screen.exitonclick()




