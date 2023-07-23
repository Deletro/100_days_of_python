from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

# TODO: Etch a Sketch game with turtle[W=move foward, S=move backward, A=turning left, D= turning right, C=clear the table]


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.back(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def screen_clearer():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=screen_clearer)
screen.exitonclick()
