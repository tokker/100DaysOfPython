from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake(starting_positions)

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

snake.draw_snake()
for t in snake.body_squares:
    t.showturtle()
food = Food()
sc = ScoreBoard()
Lose = False

while not Lose:
    time.sleep(0.1)
    if snake.body_positions[0] == food.pos():
        food.randomPosition()
        snake.growing = True
        sc.addPoint()
    snake.move_snake()
    snake.draw_snake()
    for i in range(1, len(snake.body_positions)):
        if snake.body_positions[0] == snake.body_positions[i]:
            Lose = True

sc.clear()
game_over = Turtle(visible=False)
game_over.penup()
game_over.goto(0, 0)
game_over.color("white")
game_over.write("Game over!\nYour score: " + str(sc.score), align="center", font=("Arial", 48, "bold"))

screen.exitonclick()




