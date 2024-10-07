from turtle import Turtle

class Score():
    def __init__(self):
        self.score_text = Turtle()
        self.score_text.hideturtle()
        self.score_text.speed(0)
        self.score_text.color("white")
        self.score_text.penup()
        with open("Day 020_021 (snake game)\high_score.txt", "r") as file:
            self.high_score = int(file.read())
    
    def update_score(self):
        self.score += 1
        self.score_text.clear()
        self.score_text.write(f"Score: {self.score}, high score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
    
    def game_over(self):
        self.score_text.goto(0, 0)
        if self.score > self.high_score:
            self.high_score = self.score
            self.score_text.write(f"Congratulation!\n", align="center", font=("Courier", 24, "normal"))
            self.score_text.write(f"New high score of {self.high_score}!", align="center", font=("Courier", 24, "normal"))
            with open("Day 020_021 (snake game)\high_score.txt", "w") as file:
                file.write(str(self.score))
            return 2
        else:
            self.score_text.write(f"Game Over! Final Score: {self.score}", align="center", font=("Courier", 24, "normal"))
            return 1

        
    def hide_score(self):
        self.score_text.clear()
    
    def reset_score(self):
        self.score = 0
        self.score_text.goto(0,260)
        self.score_text.write(f"Score: {self.score}, high score: {self.high_score}", align="center", font=("Courier", 24, "normal"))