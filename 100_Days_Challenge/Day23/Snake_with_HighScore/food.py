from turtle import Turtle 
from random import randint
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("red")
        self.speed(0)
        self.refresh()
    
    def refresh(self):
        positionX = randint(-250, 250)
        positionY = randint(-250,250)
        self.goto(positionX, positionY)