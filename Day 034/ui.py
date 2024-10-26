import tkinter as tk
from tkinter import ttk
from quiz_brain import Quiz

THEME_COLOR = "#375363"

class TriviaInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.quiz = Quiz()
        self.curr_question = None
        
        self.true_image = tk.PhotoImage(file="Day 034/images/true.png")
        self.false_image = tk.PhotoImage(file="Day 034/images/false.png")
        
        self.title("Trivia Quiz")
        self.configure(padx=20, pady=20)
        self.configure(background=THEME_COLOR)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
            
        # First row: Score label (right column)
        self.score_label = ttk.Label(
            self,
            text="Score: 0",
            font=("Arial", 10),
            foreground="white",
            background=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1, sticky="E", padx=10, pady=10)
        
        self.feedback_label = ttk.Label(
            self,
            text="",  # Empty initially
            font=("Arial", 16, "bold"),
            foreground="white",
            background=THEME_COLOR
        )
        self.feedback_label.grid(row=0, column=0, sticky="W", padx=10, pady=10)
        
        # Second row: Question canvas (spans both columns)
        self.question_canvas = tk.Canvas(
            self,
            height=250,
            width=300,
            bg="white",
            highlightthickness=1,
            highlightbackground="gray"
        )
        self.question_canvas.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="NSEW",
            padx=10,
            pady=10
        )
        
        # Create a text item on the canvas for the question
        self.question_text = self.question_canvas.create_text(
            150,  # x position (center)
            100,  # y position.
            text="Question will appear here",
            justify='center',
            font=("Arial", 14),
            width=280  # max width for text wrapping
        )
        
        # Third row: Button frame
        button_frame = tk.Frame(
            self,
            bg=THEME_COLOR  # Match main window background
        )
        button_frame.grid(row=2, column=0, columnspan=2, sticky="NSEW")
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        # True and False buttons
        # Note: Replace 'true_image' and 'false_image' with your actual PhotoImage objects
        self.true_button = ttk.Button(
            button_frame,
            image=self.true_image,
            text="True",  # Temporary text, replace with image
            command=self.true_pressed
        )
        self.true_button.grid(row=0, column=0, padx=20, pady=20)
        
        self.false_button = ttk.Button(
            button_frame,
            image=self.false_image,
            text="False",  # Temporary text, replace with image
            command=self.false_pressed
        )
        self.false_button.grid(row=0, column=1, padx=20, pady=20)
        self.set_question()
            
    def set_question(self):
        """Update the question text on the canvas"""
        if(self.quiz.still_has_questions()):
            self.curr_question = self.quiz.get_question()
            self.question_canvas.itemconfig(self.question_text, text=f"Q.{self.quiz.question_number+1} {self.curr_question.text}")
        else:
            self.end_quiz()
    
    def update_score(self):
        """Update the score label"""
        self.score_label.config(text=f"Score: {self.quiz.score}")
    
    def true_pressed(self):
        is_answer_correct = self.quiz.check_answer(self.curr_question, 'True')
        if(is_answer_correct):
            self.update_score()
        self.show_feedback(is_answer_correct)
    
    def false_pressed(self):
        is_answer_correct = self.quiz.check_answer(self.curr_question, 'False')
        if(is_answer_correct):
            self.update_score()
        self.show_feedback(is_answer_correct)
        
    def show_feedback(self, is_correct):
        # Change canvas color
        original_color = self.question_canvas["bg"]
        self.question_canvas["bg"] = "green" if is_correct else "red"
    
        # Show feedback text
        self.feedback_label["text"] = "Correct!" if is_correct else "Wrong!"
        
        self.question_canvas.itemconfig(self.question_text, fill="white")
    
        # Reset after 1 second
        self.after(1500, lambda: self.reset_feedback(original_color))
    
    def reset_feedback(self, original_color):
        self.question_canvas["bg"] = original_color
        self.feedback_label["text"] = ""
        self.question_canvas.itemconfig(self.question_text, fill="black")
        self.set_question()
        
    
    def end_quiz(self):
        self.question_canvas.itemconfig(self.question_text, text=f"No more questions. You've completed the quiz!\nFinal score {self.quiz.score}")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.after(3000, self.end_quiz)  # End the quiz after 3 seconds
