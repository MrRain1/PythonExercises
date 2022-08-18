from colors import color_data
import turtle as trt    
from random import randint

# paint a 10x10 grid of points spaced by 50 from wach other
#  and of size 20

# grid parameters
ROWS = 15
COLS = 15
DOT_SIZE = 20
DOT_SPACING = 50

# turtle apperence parameters
LINE_WIDTH = 1
DRAW_SPEED = 0
TURT_SHAPE = "arrow"

trt.colormode(255)

# initialize turtle object
tturt = trt.Turtle()
tturt.shape(TURT_SHAPE)
tturt.width(LINE_WIDTH)
tturt.speed(DRAW_SPEED)


def randColor():
    return color_data[randint(0, len(color_data)-1)]

for col_index in range(COLS):
    tturt.penup()
    tturt.setx(-400 + col_index * DOT_SPACING)
    
    for row_index in range(ROWS):
        tturt.sety(-400 + row_index * DOT_SPACING)
        tturt.pendown()
        tturt.dot(DOT_SIZE, randColor())
        tturt.penup()



screen = trt.Screen()
screen.exitonclick()

