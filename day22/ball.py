from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1, 1)
        self.color("white")
        self.speed("fastest")
        self.degree = random.randint(0, 360)
        self.left(self.degree)

    def move_forward(self):
        self.forward(10)
        if self.ycor() > 245 or self.ycor() < -245:
            self.right(self.degree)
            self.degree = 360 - self.degree
            self.left(self.degree)

    def start(self):
        self.goto(0,0)
        self.right(self.degree)
        self.degree = random.randint(0, 360)
        self.left(self.degree)
