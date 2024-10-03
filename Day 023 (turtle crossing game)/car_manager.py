from turtle import Turtle
import random

WEST = 180
Y_RANGE = []

class CarManager():
    def __init__(self):
        self.cars = []
        for i in range(-240, 270):
            if i % 60 == 0:
                Y_RANGE.append(i)
        print(Y_RANGE)
    
    def add_car(self):
        car = Turtle()
        car.penup()
        car.seth(WEST)
        car.speed(0)
        car.shape("square")
        car.shapesize(stretch_len=random.randint(3,5))
        car.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "gray", "black", "cyan", "magenta"]))
        goto_x = 330
        furthest_x_car = None
        random_y = random.choice([i for i in range(-240, 260, 60)])
        
        for c in self.cars:
            if abs(c.ycor() - random_y) < 1e-6:
                if furthest_x_car is None or c.xcor() > furthest_x_car.xcor():
                    furthest_x_car = c

        if furthest_x_car is not None:
            goto_x = furthest_x_car.xcor() + furthest_x_car.shapesize()[1] * 10 + car.shapesize()[1] * 10 + 50
            
        car.goto(goto_x, random_y)        
        self.cars.append(car)
    
    def move_cars(self):
        for car in self.cars:
            car.forward(5)
            
    def reset_cars(self):
        for car in self.cars:
            car.goto(1000, 1000)
        self.cars = []
        
        