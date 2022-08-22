import turtle
import time
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

gameFlag = True

ssnake = snake.Snake()
ffood = food.Food()
sscoreboard = scoreboard.Scoreboard()


def exitGame():
    global gameFlag
    gameFlag = False

screen.listen()
screen.onkey(key="Left", fun= ssnake.turnLeft)
screen.onkey(key="Right", fun= ssnake.turnRight)
screen.onkey(key="c", fun= exitGame)

while(gameFlag):
    screen.update()
    time.sleep(0.1)
    ssnake.moveSnakeFwd()
    
    if ssnake.head.distance(ffood) < 20:
        ffood.refresh()
        ssnake.extend()
        sscoreboard.increaseScore()
        sscoreboard.drawBoundary()
    
    if ssnake.head.xcor() < -250 or ssnake.head.xcor() > 250 or ssnake.head.ycor() < -250 or ssnake.head.ycor() > 250:
        exitGame()
        sscoreboard.gameOver()
    
    for segment in ssnake.segments[1:]:
        if ssnake.head.distance(segment) < 10:
            exitGame()
            sscoreboard.gameOver()
    
screen.exitonclick()