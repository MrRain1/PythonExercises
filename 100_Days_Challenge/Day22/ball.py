from turtle import Turtle
from random import randint

class newBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.ballSpeed = 1
        self.penup()
        self.color("white")
        self.speed(self.ballSpeed)
        self.x_move = 10
        self.y_move = 10
        
    def launchBall(self):
        rand_x_direction = randint(-self.x_move, self.x_move)
        rand_y_direction = randint(-self.y_move, self.y_move)
        self.goto(x= rand_x_direction, y = rand_y_direction)
        
    def moveBall(self):
        self.goto(x= self.xcor() + self.x_move, y= self.ycor() + self.y_move)
        
    def bounce(self):
        self.y_move *=-1
        
    def ballReset(self):
        self.speed(0)
        self.goto(0,0)
        self.bouncePaddle()
        self.bounce()
        self.ballSpeed = 1 
        self.speed(self.ballSpeed)
        
    def bouncePaddle(self):
        self.x_move *= -1
        self.addSpeed()
        
    def addSpeed(self):
        if self.ballSpeed < 5:
            self.ballSpeed += 1
            self.speed(self.ballSpeed)