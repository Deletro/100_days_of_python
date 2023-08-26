from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, goto_x_cor, goto_y_cor):
        super().__init__()
        self.create_paddle()
        self.goto(goto_x_cor, goto_y_cor)

    def create_paddle(self):
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        # self.goto(x=350, y=0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def reset_paddles(self, goto_x_cor, goto_y_cor):
        self.goto(goto_x_cor, goto_y_cor)
