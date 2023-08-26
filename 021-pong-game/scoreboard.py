from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, goto_x_cor, goto_y_cor):
        super().__init__()
        self.score = 0
        self.create_scoreboard()
        self.goto(goto_x_cor, goto_y_cor)
        self.update_scoreboard()

    def create_scoreboard(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.write(
            f"Score: {self.score}",
            move=False,
            align="center",
            font=("Arial", 24, "normal"),
        )

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"{self.score}",
            move=False,
            align="center",
            font=("Arial", 30, "normal"),
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


# kellene egy bal és egy jobb scoreboard ami azt nézi ha x-en minuszba ér falat a labda
# akkor a jobb oldali scoreboard kap pontot, és ez forditva
