from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.level = 1
        self.penup()
        self.goto(-280,250)
        self.color("black")
        self.write("Level: 1", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write("Level: " + str(self.level), align="left", font=FONT)


