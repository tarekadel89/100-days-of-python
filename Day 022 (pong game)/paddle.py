from turtle import Turtle
from score import Score

class Paddle(Turtle):
    def __init__(self, paddle_x, score_x):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(paddle_x, 0)
        self.direction = "none"
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.player_score = Score(score_x)
        
    def move_up(self):
        if self.ycor() < 245:
            self.sety(self.ycor() + 20)
    
    def move_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)