from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, player):
        super().__init__(visible=False)
        self.player = player
        self.shape("square")
        self.penup()
        self.shapesize(0.8, 4)
        self.color("white")
        self.speed(300)
        self.goto(480 * player, 0)
        self.left(90)
        self.showturtle()

    def move_up(self):
        if self.ycor() < 220:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -220:
            self.back(20)

    def start(self):
        self.hideturtle()
        self.goto(480 * self.player, 0)
        self.showturtle()