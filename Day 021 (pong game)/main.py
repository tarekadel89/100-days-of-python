from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

PLAYER1_STARTING_X = -435
PLAYER1_SCORE_x = -40

PLAYER2_STARTING_X = 428
PLAYER2_SCORE_x = 40

## Screen initialization
my_screen = Screen()
my_screen.setup(width=900, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong Game")
my_screen.tracer(0)

# Players initialization
player1 = Paddle(PLAYER1_STARTING_X,PLAYER1_SCORE_x)
player2 = Paddle(PLAYER2_STARTING_X,PLAYER2_SCORE_x)
ball = Ball()

#drawing the middle line
middle_line = Turtle()
middle_line.color("white")
middle_line.penup()
middle_line.goto(0,285)
middle_line.hideturtle()
middle_line.pensize(3)
middle_line.seth(270)
for i in range(29):
    middle_line.pendown()
    middle_line.forward(10)
    middle_line.penup()
    middle_line.forward(10)
    
# event listeners
my_screen.listen()
my_screen.onkeypress(player1.move_up, "w")
my_screen.onkeypress(player1.move_down, "s")
my_screen.onkeypress(player2.move_up, "Up")
my_screen.onkeypress(player2.move_down, "Down")


while True:
    ball.move(player1, player2)
    if ball.xcor() > 440:
        player1.player_score.update_score()
        ball.reset()
    if ball.xcor() < -440:
        player2.player_score.update_score()
        ball.reset()
    my_screen.update()
    time.sleep(ball.speed)