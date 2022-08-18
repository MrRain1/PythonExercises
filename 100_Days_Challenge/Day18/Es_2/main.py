# draw a dashed line on the screen

import turtle

GAP = 10
SOLID_LINE = 10

tturtle = turtle.Turtle()

line_length = int(input("Insert the lenght of the line: "))

for counter in range(int(line_length/20)):
    
    tturtle.pendown()
    tturtle.forward(SOLID_LINE)
    tturtle.penup()
    tturtle.forward(GAP)
    

screen = turtle.Screen()
screen.exitonclick()