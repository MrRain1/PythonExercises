import turtle
import time

screen = turtle.Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

INITIAL_LENGTH = 3
SNAKE_SPEED = 0
gameFlag = True

snakeBody = []

def initializeSnake():
    for index in range(INITIAL_LENGTH):
        new_body = turtle.Turtle(shape= "square")
        new_body.penup()
        new_body.speed(SNAKE_SPEED)
        new_body.color("white")
        new_body.setpos(x= 0-index*20, y= 0)
        snakeBody.append(new_body)

def addBodyPart():
    snake_length = len(snakeBody)
    new_body = turtle.Turtle(shape= "square")
    new_body.penup()
    new_body.speed(SNAKE_SPEED)
    new_body.color("white")
    new_body.setposition(x= snakeBody[snake_length-1].xcor() - 20 , y= snakeBody[snake_length-1].ycor())
    snakeBody.append(new_body)

def turnLeft():
    snakeBody[0].seth(snakeBody[0].heading() + 90)

def turnRight():
    snakeBody[0].seth(snakeBody[0].heading() - 90)

def exitGame():
    global gameFlag
    gameFlag = False


screen.listen()
screen.onkey(key="Left", fun= turnLeft)
screen.onkey(key="Right", fun= turnRight)
screen.onkey(key="c", fun= exitGame)

initializeSnake()


while(gameFlag):
    screen.update()
    time.sleep(0.15)
    for index in range(len(snakeBody)-1, 0, -1):
        new_x = snakeBody[index-1].xcor()
        new_y = snakeBody[index-1].ycor()
        snakeBody[index].goto(new_x, new_y)
    snakeBody[0].forward(20)    
        

screen.exitonclick()