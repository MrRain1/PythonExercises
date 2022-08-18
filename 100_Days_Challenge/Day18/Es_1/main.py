# draw a square on the screen

import turtle

tturtle = turtle.Turtle()

square_length = float(input("Insert the edge lenght of the square: "))
for counter in range(4):
    tturtle.forward(square_length)
    print(tturtle.position())
    tturtle.left(90)

screen = turtle.Screen()
screen.exitonclick()