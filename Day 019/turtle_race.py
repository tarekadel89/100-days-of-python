import turtle as t
import random

WIDTH = 500
HEIGHT = 400
PADDING = 20
TURTLE_COLORS = ["red", "green", "blue", "yellow", "purple", "orange"]
MY_TURTLES = []

my_screen = t.Screen()
my_screen.setup(width=WIDTH, height=HEIGHT)

user_choice = my_screen.textinput("Turtle Choice", "Choose your turtle from rainbow colors:")
while user_choice not in TURTLE_COLORS:
    user_choice = my_screen.textinput("Turtle Choice", "Invalid! Choose your turtle from rainbow colors")

def create_turtles():
    y_pos = -100
    for color in TURTLE_COLORS:
        y_pos += 30
        new_turtle = t.Turtle()
        new_turtle.color(color)
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.goto(-WIDTH / 2 + PADDING, y_pos)
        MY_TURTLES.append(new_turtle)

def check_winner():
    for turtle in MY_TURTLES:
        if turtle.xcor() >= WIDTH / 2 - PADDING:
            return turtle
    return "none"

def move_turtles_randomly():
    for turtle in MY_TURTLES:
        turtle.forward(random.randint(0, 10))

def check_user_won(winner):
    text_turtle = t.Turtle(visible=False)
    text_turtle.penup()
    text_turtle.goto(0, HEIGHT / 2 - 40)
    
    winner.goto(0, HEIGHT / 2 - 60)
    if winner.color()[0] == user_choice:
        text_turtle.write(f"Congrats! The {winner.color()[0]} turtle wins!", align="center", font=("Arial", 18, "bold"))
    else:
        text_turtle.write(f"Sorry! The {winner.color()[0]} turtle wins!", align="center", font=("Arial", 18, "bold"))

create_turtles()
winner_turtle = "none"
while(winner_turtle == "none"):
    move_turtles_randomly()
    winner_turtle = check_winner()

check_user_won(winner_turtle)

my_screen.mainloop() 