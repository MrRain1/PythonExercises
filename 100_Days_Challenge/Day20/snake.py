import turtle

class Snake:
    def __init__(self):
        self.segments = []
              
        for index in range(3):
            self.add_segment((-index*20, 0))
        
        self.head = self.segments[0]
            
    def turnLeft(self):
        self.head.seth(self.head.heading() + 90)
     
    def turnRight(self):
        self.head.seth(self.head.heading() - 90)
        
    def moveSnakeFwd(self):
        for index in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[index-1].xcor()
            new_y = self.segments[index-1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.head.forward(20)  
        
    def add_segment(self, position):
        new_body = turtle.Turtle(shape= "square")
        new_body.penup()
        new_body.color("white")
        new_body.goto((position))
        self.segments.append(new_body)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())