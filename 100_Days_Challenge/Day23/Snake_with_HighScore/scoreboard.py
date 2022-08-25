from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = int(self.readHighScore())
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.drawBoundary()
        self.updateScore()       
    
    def updateScore(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score}\tHigh Score: {self.highScore}", align=ALIGNMENT, font= FONT)
    
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()
    
    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font= FONT)    
        
    def drawBoundary(self):
        self.penup()
        self.goto(-250, -250)
        self.pendown()
        for edge in range(4):
            self.fd(250+250)
            self.left(90)
        self.penup()
        
    def setHighScore(self):
        if self.score > self.highScore:
            with open("./high_score.txt", "w") as file:
                file.write(str(self.score))
                
    def readHighScore(self):
        with open("./high_score.txt") as file:
            return file.read()