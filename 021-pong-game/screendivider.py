from turtle import Turtle


class ScreenDivider(Turtle):
    def __init__(self):
        super().__init__()

    def dividing_line(self, goto_x_cor, goto_y_cor):
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(goto_x_cor, goto_y_cor)
        self.setheading(90)
        for _ in range(15):
            self.penup()
            self.forward(20)
            self.pendown()
            self.forward(20)
