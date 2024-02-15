from turtle import Turtle

class Snake:
    def __init__(self, starting_positions):
        self.direction = "right"
        self.ready = True
        self.body_positions = starting_positions
        self.body_squares = []
        for i in range(len(starting_positions)):
            t = Turtle("square")
            t.color("white")
            t.speed(100)
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
        for i in range(len(self.body_positions) - 1):
            body_positions2.append(self.body_positions[i])
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
