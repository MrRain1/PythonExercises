import turtle
from random import randint

screen = turtle.Screen()
screen.setup(width= 500, height= 400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
winner = ""

exitFlag = False
TURTLE_NUMBERS = len(colors)


def randomFwd():
    return randint(10, 20)

def checkFinishLine():
    global winner
    global exitFlag
    for index in range(TURTLE_NUMBERS):
        if turtles[index].xcor() >= 230:
            winner = turtles[index]
            exitFlag = True

def initializeTurtle():
    for index in range(TURTLE_NUMBERS):
        new_turtle = turtle.Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[index])
        new_turtle.goto(x= -230, y= -70 + index*30)
        turtles.append(new_turtle)

def advancePosition():
    global exitFlag
    
    for index in range(TURTLE_NUMBERS):
        turtles[index].forward(randomFwd())

def userInput():
    correct_flag = True
    
    while(correct_flag):
        user_in = screen.textinput(title= "Turtle Bet", prompt= "Which turtle will win the race? Enter a color:").lower()
        if user_in in colors:
            correct_flag = False
        else:
            print("Invalid input")
    
    return user_in
    
initializeTurtle()
user_bet = userInput()

while(not exitFlag):
    advancePosition()
    checkFinishLine()
    
if user_bet in winner.color():
    print("Congrats! You won the bet!")
else:
    print(f"Sorry the winner was the {winner.pencolor()} turtle")


screen.exitonclick()