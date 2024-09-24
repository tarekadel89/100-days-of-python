import turtle as t


my_turtle = t.Turtle()
my_screen = t.Screen()

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def turn_counter_clockwise():
    my_turtle.seth(my_turtle.heading() + 10)

def turn_clockwise():
    my_turtle.seth(my_turtle.heading() - 10)
    
def clear_screen():
    my_turtle.penup()
    my_turtle.clear()
    my_turtle.home()
    my_turtle.pendown()

    
my_screen.listen()
my_screen.onkey(fun= move_forward, key='w')
my_screen.onkey(fun= move_backward, key='s')
my_screen.onkey(fun= turn_counter_clockwise, key='a')
my_screen.onkey(fun= turn_clockwise, key='d')
my_screen.onkey(fun= clear_screen, key='c')







my_screen.mainloop() 