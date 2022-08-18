# random walk

import turtle as trt
from random import randint

LINE_LENGHT = 20
LINE_WIDTH = 8
MAX_LEN = 500
TURT_SHAPE = "arrow"
ANGLES = [0 , 90, 180, 270]


tturt = trt.Turtle()
tturt.shape(TURT_SHAPE)
tturt.width(LINE_WIDTH)
tturt.speed(0)

screen = trt.Screen()
screen.colormode(255)

def randColor():
    return randint(0, 255)

def randAngle():
    return ANGLES[randint(0, len(ANGLES) - 1)]

for _ in range(MAX_LEN):
    tturt.pencolor(randColor(), randColor(), randColor())
    tturt.setheading(randAngle())
    tturt.fd(LINE_LENGHT)

screen.exitonclick()