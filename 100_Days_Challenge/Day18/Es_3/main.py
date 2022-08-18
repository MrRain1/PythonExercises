# draw polygons with different colors

import turtle as trt
from random import randint

LINE_LENGHT = 100
LINE_WIDTH = 3
TURT_SHAPE = "arrow"
MAX_SIZE = 11

def randColor():
    return randint(0, 255)

screen = trt.Screen()
screen.colormode(255)

tturt = trt.Turtle()
tturt.shape(TURT_SHAPE)
tturt.width(LINE_WIDTH)
tturt.speed(10)


for edge_number in range(3, MAX_SIZE):
    tturt.pencolor(randColor(), randColor(), randColor())
    for edge in range (1, edge_number+1):
        tturt.fd(LINE_LENGHT)
        tturt.right(360/edge_number)    


screen.exitonclick()