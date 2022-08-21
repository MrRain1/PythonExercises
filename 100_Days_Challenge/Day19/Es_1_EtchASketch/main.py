from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def turnRight():
    newHeading= tim.heading() - 10
    tim.seth(newHeading)

def turnLeft():
    newHeading= tim.heading() + 10
    tim.seth(newHeading)

def turnBack():
    tim.back(10)

def clearScreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Left", fun=turnLeft)
screen.onkey(key="Right", fun=turnRight)
screen.onkey(key="Down", fun=turnBack)
screen.onkey(key="c", fun=clearScreen)
screen.exitonclick()