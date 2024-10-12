import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "space")

game_is_on = True
while game_is_on:
    if player.ycor() > player.finish_line:
        player.goto(player.starting_position)
        car_manager.increase_speed()
        scoreboard.increase_level()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.cars:
        if player.ycor() - 20 < car.ycor() < player.ycor() + 20 and -30 < car.xcor() < 30:
            game_is_on = False
    time.sleep(0.1)
    screen.update()

game_over = Turtle(visible=False)
game_over.penup()
game_over.goto(0, 0)
game_over.color("black")
game_over.write("Game over.", align="center", font=("Courier", 48, "bold"))

screen.exitonclick()
