from data import question_data
from question_model import Question

class Quiz:
    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.question_list = []
        for q in question_data:
            self.question_list.append(Question(q["question"], q["correct_answer"]))
        
    
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
