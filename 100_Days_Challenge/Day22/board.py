from turtle import Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600

ALIGNMENT = "center"
FONT = ("Courier", 32, "bold")

class newBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreP1 = 0
        self.scoreP2 = 0
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color("white")
        self.updateScore()
        
    def updateScore(self):
        self.goto(x= 0, y = SCREEN_HEIGTH/2 - 100)
        self.clear()
        self.write(f"{self.scoreP2}\t{self.scoreP1}", align=ALIGNMENT, font=FONT)
        
    def addPointP1(self):
        self.scoreP1+=1
        self.updateScore()
    
    def addPointP2(self):
        self.scoreP2+=1
        self.updateScore()