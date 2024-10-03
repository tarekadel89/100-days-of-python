from turtle import Turtle

class Score(Turtle):
    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x, 230)
        self.clear()
        self.write(f"{self.score}", align="center", font=("Atari", 48, "normal"))
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=("Atari", 48, "normal"))
