from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-420, 265)
        self.write(
            f"Level: {self.level}",
            move=False,
            align="center",
            font=("Courier", 24, "normal"),
        )

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(
            f"Level: {self.level}",
            move=False,
            align="center",
            font=("Courier", 24, "normal"),
        )

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(
            f"GAME OVER",
            move=False,
            align="center",
            font=("Courier", 36, "normal"),
        )
