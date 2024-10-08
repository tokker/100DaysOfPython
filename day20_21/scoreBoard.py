from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.write("Your score: 0", align="center", font=("Arial", 12, "bold"))

    def addPoint(self):
        self.score += 1
        self.clear()
        self.write("Your score: " + str(self.score), align="center", font=("Arial", 12, "bold"))

