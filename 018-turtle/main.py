import turtle
import colorgram
import random

DOT_SIZE = 20
DOT_DISTANCE = 50

DOT_ROW = 10
DOT_COLUMN = 10


def get_picture_colors():
    colors = colorgram.extract("image.jpg", 30)

    transformed_colors = []

    for color in colors:
        rgb_r = color.rgb.r
        rgb_g = color.rgb.g
        rgb_b = color.rgb.b
        rgb_color = (rgb_r, rgb_g, rgb_b)
        transformed_colors.append(rgb_color)


turtle_colors = [
    (202, 164, 110),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]


akos = turtle.Turtle()
turtle.colormode(255)


def draw_config():
    akos.penup()
    akos.hideturtle()
    akos.setheading(200)
    akos.forward(300)
    akos.setheading(0)
    akos.speed("fastest")


def draw_row():
    for _ in range(DOT_ROW):
        akos.dot(DOT_SIZE, random.choice(turtle_colors))
        akos.forward(DOT_DISTANCE)


def draw_all():
    for _ in range(DOT_COLUMN):
        draw_row()
        akos.left(90)
        akos.forward(DOT_DISTANCE)
        akos.left(90)
        akos.forward(DOT_ROW * DOT_DISTANCE)
        akos.setheading(0)


draw_config()
draw_all()

my_screen = turtle.Screen()

print(my_screen.canvheight)
my_screen.exitonclick()
