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
Lose = False

with open("high_score.txt") as hs_file:
    hs = hs_file.read()
sc = ScoreBoard(int(hs))

screen.tracer(0)

while not Lose:
    time.sleep(0.1)
    if snake.body_positions[0] == food.pos():
        food.randomPosition()
        snake.growing = True
        sc.addPoint()
    screen.update()
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
is_high_score = ""
if sc.score > sc.high_score:
    is_high_score = "\nIt's a new high score!"
    with open("high_score.txt", "w") as hs_file:
        hs_file.write(str(sc.score))
game_over.write("Game over!\nYour score: " + str(sc.score) + is_high_score, align="center", font=("Arial", 32, "bold"))


screen.exitonclick()




