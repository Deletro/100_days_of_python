from turtle import Turtle
import random

COLORS = ["red", "yellow", "orange", "purple", "green", "cyan", "pink", "blue"]
MOVE_DISTANCE_INCREASER = 10


class CarManager(Turtle):
    def __init__(self):
        self.car_list = []
        self.move_distance = 10

    def create_car(self):
        self.car = Turtle()
        self.car.hideturtle()
        self.car.penup()
        self.car.goto(600, random.randint(-250, 250))
        self.car.showturtle()
        self.car.shape("square")
        self.car.shapesize(stretch_len=2, stretch_wid=1)
        self.car.color(random.choice(COLORS))
        self.car.setheading(180)
        self.car_list.append(self.car)

    def move_car(self):
        for car in self.car_list:
            car.forward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_DISTANCE_INCREASER
