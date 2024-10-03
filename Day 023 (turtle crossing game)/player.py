from turtle import Turtle

NORTH = 90

class Player(Turtle):
    def __init__(self, y):
        super().__init__()
        self.color("black")
        self.speed(0)
        self.penup()
        self.reset_position(y)
        self.shape("turtle")
        self.seth(NORTH)
    
    def detect_collision(self, cars):
        for car in cars:
            if abs(self.ycor() - car.ycor()) < 25:
                if self.xcor() + 10 > car.xcor() - car.shapesize()[1] * 10 and self.xcor() - 10 < car.xcor() + car.shapesize()[1] * 10:
                    return True
        return False
    
    def completed_level(self):
        if self.ycor() >= 270:
            return True
        
    def move_up(self):
        self.forward(10)
    
    def move_down(self):
        if self.ycor() >= -270:
            self.backward(10)
    
    def move_left(self):
        if self.xcor() > -275:
            self.goto(self.xcor()-10, self.ycor())
        
    def move_right(self):
        if self.xcor() < 275:
            self.goto(self.xcor()+10, self.ycor())
    
    def reset_position(self, y):
        self.goto(0, y)