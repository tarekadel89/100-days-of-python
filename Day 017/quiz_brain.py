import os

class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        if os.name == 'nt':  # Check if the system is Windows
            os.system('cls')  # Use cls command on Windows
        else:
            os.system('clear')  # Use clear command on other systems
        print("Welcome to the Quiz")
    
    def get_question(self):
        return self.question_list[self.question_number]
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, question, answer):
        self.question_number += 1
        if question.answer == answer:
            self.score += 1
            return True
        return False
