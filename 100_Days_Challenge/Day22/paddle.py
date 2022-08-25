from turtle import Turtle

HALF_SCREEN_HEIGTH = 600/2 


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.actualWidth = self.shapesize()[0] * 20
        self.penup()
        self.goto(position)

    
    def moveUp(self):
        if self.ycor() < HALF_SCREEN_HEIGTH - self.actualWidth/2:
            self.goto(x = self.xcor() , y = self.ycor() + 20)
        
    def moveDown(self):
        if self.ycor() > -(HALF_SCREEN_HEIGTH - self.actualWidth/2):    
            self.goto(x = self.xcor() , y = self.ycor() - 20)