from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 2
        self.y_move = 2
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_from_wall(self):
        self.y_move *= -1

    def bounce_from_paddle(self):
        self.x_move *= -1

    def reset_ball(self):
        self.reset()
        self.create_ball()
