from turtle import Turtle, Screen
import random
import turtle

TILT_ANGLE = 5
RADIUS_ANGLE = 360

turtle.colormode(255)

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.hideturtle()
my_screen = Screen()

for i in range(int(RADIUS_ANGLE/TILT_ANGLE)):
    my_turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    my_turtle.circle(100)
    my_turtle.setheading(my_turtle.heading()+TILT_ANGLE)
    
my_screen.mainloop()