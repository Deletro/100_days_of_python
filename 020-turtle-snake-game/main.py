from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)


def self_collide():
    for segment in snake.segments:
        if snake.head.distance(segment) < 10 and segment != snake.head:
            return True
    return False


def wall_collide():
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        return True
    return False


game_active = True
while game_active:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if wall_collide() or self_collide():
        scoreboard.game_over()
        game_active = False

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

screen.exitonclick()
