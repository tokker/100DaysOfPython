from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for line in range(-6, 7):
            can_create = True
            for car in self.cars:
                if car.ycor() == line * 40 and car.xcor() > 260:
                    can_create = False
            if random.randint(1,50) == 50 and can_create:
                self.cars.append(Car(COLORS[random.randint(0,5)], line))

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - self.move_distance, car.ycor())
            if car.xcor() < -320:
                self.cars.remove(car)

    def increase_speed(self):
        self.move_distance = self.move_distance + MOVE_INCREMENT


class Car(Turtle):
    def __init__(self, color, line):
        super().__init__()
        self.shape("square")
        self.shapesize(2,1)
        self.speed("fastest")
        self.penup()
        self.left(90)
        self.goto(320, line * 40)
        self.color(color)


