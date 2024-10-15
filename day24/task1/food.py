from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.shape("circle")
        self.penup()
        self.shapesize(0.75, 0.75)
        self.color("red")
        self.speed("fastest")
        self.randomPosition()
        self.showturtle()

    def randomPosition(self):
        self.goto(random.randint(-14, 14) * 20, (random.randint(-14, 13) * 20))
