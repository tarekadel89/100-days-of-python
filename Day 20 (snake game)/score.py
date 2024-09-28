from turtle import Turtle

class Score():
    def __init__(self):
        self.score_text = Turtle()
        self.score_text.hideturtle()
        self.score_text.speed(0)
        self.score_text.color("white")
        self.score_text.penup()
    
    def update_score(self):
        self.score += 1
        self.score_text.clear()
        self.score_text.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
    
    def game_over(self):
        self.score_text.goto(0, 0)
        self.score_text.write(f"Game Over! Final Score: {self.score}", align="center", font=("Courier", 24, "normal"))
        
    def hide_score(self):
        self.score_text.clear()
    
    def reset_score(self):
        self.score = 0
        self.score_text.goto(0,260)
        self.score_text.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))