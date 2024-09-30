from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.reset()
        
    def move(self, paddle1, paddle2):
        self.forward(10)
        if self.ycor() >= 290 or self.ycor() <= -285:
            self.seth(-self.heading())
        elif (self.xcor() <= -415 and self.distance(paddle1) < 50) or (self.xcor() >= 410 and self.distance(paddle2) < 50):
            self.seth(180 - self.heading())
            self.speed -= self.speed * 0.1
    
    def reset(self):
        self.goto(0, 0)
        heading_angle = random.choice([45, 135, 225, 315])
        self.seth(heading_angle)
        self.speed = 0.08