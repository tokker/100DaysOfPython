from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self, player):
        super().__init__(visible=False)
        self.score = 0
        self.penup()
        self.goto(100 * player,100)
        self.color("white")
        self.write(0, align="center", font=("Arial", 90, "bold"))

    def addPoint(self):
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=("Arial", 90, "bold"))

