from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for idx in range(3):
            self.create_segment(idx * -20, 0)

    def extend(self):
        tail_x = self.segments[-1].xcor()
        tail_y = self.segments[-1].ycor()
        self.create_segment(tail_x, tail_y)

    def create_segment(self, x, y):
        turtle = Turtle()
        turtle.color("white")
        turtle.penup()
        turtle.shape("square")
        turtle.goto(x, y)
        self.segments.append(turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
