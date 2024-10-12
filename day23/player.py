from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed("fastest")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
        self.finish_line = FINISH_LINE_Y
        self.starting_position = STARTING_POSITION

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

