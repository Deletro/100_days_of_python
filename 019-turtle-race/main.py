from turtle import Turtle, Screen
import random

COLORS = ["Red", "Cyan", "Blue", "Green", "Gray"]
START_POSITIONS = [-200, -100, 0, 100, 200]


def to_the_start(turtle_name, coordinate_x, coordinate_y):
    turtle_name.penup()
    turtle_name.goto(coordinate_x, coordinate_y)


def lets_race(turtle):
    for _ in range(1):
        turtle.forward(random.randint(0, 10))


turtle_list = []

for idx in range(5):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(COLORS[idx])
    to_the_start(turtle, -600, START_POSITIONS[idx])
    turtle_list.append(turtle)
    turtle.speed("fastest")

screen = Screen()

game_active = True
player_tipp = screen.textinput(
    title="Guess a color!", prompt="Guess who will be the winner color?"
).lower()

while game_active:
    for turtle in turtle_list:
        lets_race(turtle)
        turtle_position = turtle.pos()

        if turtle_position[0] >= 570:
            print(f"The winner is the {turtle.pencolor()} turtle!!")
            if player_tipp == turtle.pencolor().lower():
                print("You Win")
            else:
                print("You Lose")
            game_active = False
            break


screen.exitonclick()
