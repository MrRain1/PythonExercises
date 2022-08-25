from ball import newBall
from turtle import Screen
from paddle import Paddle
from board import newBoard

def exitGame():
    global game_Flag
    game_Flag = False
game_Flag = True

screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer()

scoreBoard = newBoard()

screen.onkey(key = "e", fun = exitGame)

player_1 = Paddle((350,0))
player_2 = Paddle((-350,0))
ball = newBall()

screen.onkey(key = "Up", fun = player_1.moveUp)
screen.onkey(key = "Down", fun = player_1.moveDown)


screen.onkey(key = "w", fun = player_2.moveUp)
screen.onkey(key = "s", fun = player_2.moveDown)


while game_Flag:
    screen.update()
    ball.moveBall()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
    if ball.distance(player_1) < 50 and ball.xcor() > 320 or (ball.distance(player_2) < 50 and ball.xcor() < -320):
        ball.bouncePaddle()
    
    if ball.xcor() > 380:
        scoreBoard.addPointP2()
        ball.ballReset()
 
    if ball.xcor() < -380:
        scoreBoard.addPointP1()
        ball.ballReset()
        
    
    
screen.exitonclick()