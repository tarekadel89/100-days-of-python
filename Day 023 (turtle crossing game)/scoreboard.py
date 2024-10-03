from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(-280, 270)
        self.score = 0
        self.speed = 0.25
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.score += 1 
        self.speed -= self.speed * .1
        self.clear()
        self.write(f"Level: {self.score}", align="Left", font=("Courier", 18, "normal"))
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()