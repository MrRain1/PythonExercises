# spirograpgh

import turtle as trt

from random import randint

LINE_WIDTH = 1
DRAW_SPEED = 0
TURT_SHAPE = "arrow"
CIRCLE_RADIUS = 150

tturt = trt.Turtle()
tturt.shape(TURT_SHAPE)
tturt.width(LINE_WIDTH)
tturt.speed(DRAW_SPEED)


trt.colormode(255)

def randColor():
    return randint(0, 255)

def randAngle():
    return randint(0, 360)

for angle in range(0, 360, 3):
    tturt.setheading(angle)
    tturt.color(randColor(), randColor(), randColor())
    tturt.circle(CIRCLE_RADIUS)
    
screen = trt.Screen()
screen.exitonclick()