from turtle import Screen, Turtle
import time
from snake import Snake


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
while True:
    snake.draw_snake()
    snake.move_snake()
    time.sleep(0.1)

screen.exitonclick()