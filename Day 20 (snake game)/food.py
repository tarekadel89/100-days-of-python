from turtle import Turtle
import random

class Food():
    def __init__(self):
        self.food = Turtle()
        self.food.speed(0)
        self.food.penup()
        self.food.shape("circle")
        self.food.color("blue")
        
    def move(self):
        self.food.goto(random.randint(-280,280), random.randint(-280, 250))
        self.x_coord = self.food.xcor()
        self.y_coord = self.food.ycor()
    
    def hide_food(self):
        self.food.goto(1000, 1000)