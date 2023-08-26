from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from screendivider import ScreenDivider

# Paddle Objects
paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)

# Ball Object
ball = Ball()

# Scoreboard Objects
scoreboard_left = Scoreboard(-190, 260)
scoreboard_right = Scoreboard(190, 260)

# Dividing line
screendivider = ScreenDivider()

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screendivider.dividing_line(goto_x_cor=0, goto_y_cor=-300)


# Moveset
screen.listen()
screen.onkey(key="w", fun=paddle_right.go_up)
screen.onkey(key="s", fun=paddle_right.go_down)
screen.onkey(key="a", fun=paddle_left.go_up)
screen.onkey(key="d", fun=paddle_left.go_down)


while True:
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_from_wall()
        screen.update()
    if ball.xcor() > 380:
        paddle_left.reset_paddles(-350, 0)
        paddle_right.reset_paddles(350, 0)
        ball.reset_ball()
        scoreboard_left.increase_score()

    if ball.xcor() < -380:
        paddle_left.reset_paddles(-350, 0)
        paddle_right.reset_paddles(350, 0)
        ball.reset_ball()
        scoreboard_right.increase_score()

    if (
        ball.distance(paddle_right) < 50
        and ball.xcor() > 325
        or ball.distance(paddle_left) < 50
        and ball.xcor() < -325
    ):
        ball.bounce_from_paddle()

screen.exitonclick()
