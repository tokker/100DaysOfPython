from turtle import Turtle

class Snake:
    def __init__(self, starting_positions):
        self.direction = "right"
        self.ready = True
        self.body_positions = starting_positions
        self.body_squares = []
        self.growing = False
        for i in range(len(starting_positions)):
            t = Turtle("square", visible=False)
            t.color("white")
            t.speed("fastest")
            self.body_squares.append(t)



    def draw_snake(self):
        for i in range(1, len(self.body_positions) + 1):
            self.body_squares[len(self.body_positions) - i].penup()
            self.body_squares[len(self.body_positions) - i].goto(self.body_positions[len(self.body_positions) - i])


    def move_snake(self):
        body_positions2 = []
        if self.direction == "up":
            body_positions2.append((self.body_positions[0][0], self.body_positions[0][1] + 20))
        elif self.direction == "down":
            body_positions2.append((self.body_positions[0][0], self.body_positions[0][1] - 20))
        elif self.direction == "left":
            body_positions2.append((self.body_positions[0][0] - 20, self.body_positions[0][1]))
        elif self.direction == "right":
            body_positions2.append((self.body_positions[0][0] + 20, self.body_positions[0][1]))
        if body_positions2[0][0] > 280:
            body_positions2.append((body_positions2[0][0] - 580, body_positions2[0][1]))
            body_positions2.pop(0)
        if body_positions2[0][0] < -280:
            body_positions2.append((body_positions2[0][0] + 580, body_positions2[0][1]))
            body_positions2.pop(0)
        if body_positions2[0][1] > 280:
            body_positions2.append((body_positions2[0][0], body_positions2[0][1] - 580))
            body_positions2.pop(0)
        if body_positions2[0][1] < -280:
            body_positions2.append((body_positions2[0][0], body_positions2[0][1] + 580))
            body_positions2.pop(0)
        for i in range(len(self.body_positions) - 1):
            body_positions2.append(self.body_positions[i])
        if self.growing:
            body_positions2.append(self.body_positions[len(self.body_positions) - 1])
            self.growing = False
            t = Turtle("square", visible=False)
            t.goto(self.body_positions[len(self.body_positions) - 1])
            t.showturtle()
            t.color("white")
            t.speed("fastest")
            self.body_squares.append(t)
        self.body_positions = body_positions2
        self.ready = True

    def move_up(self):
        if self.direction != "down" and self.ready:
            self.direction = "up"
            self.ready = False


    def move_down(self):
        if self.direction != "up" and self.ready:
            self.direction = "down"
            self.ready = False


    def move_left(self):
        if self.direction != "right" and self.ready:
            self.direction = "left"
            self.ready = False


    def move_right(self):
        if self.direction != "left" and self.ready:
            self.direction = "right"
            self.ready = False

