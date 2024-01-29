from turtle import Turtle, Screen
import random
import colorgram

image_colors = colorgram.extract("dots.jpg", 30)
colors = []
for i in range(3, 30):
    colors.append(image_colors[i].rgb)

screen = Screen()
screen.setup(500,500,0,0)
screen.colormode(255)

t = Turtle()
t.speed(10000)

for i in range(10):
    for j in range(10):
        t.penup()
        t.goto(-200+j * 40, -200+i * 40)
        t.pendown()
        t.pencolor(colors[random.randint(0, len(colors)-1)])
        t.dot(20)

screen.exitonclick()
