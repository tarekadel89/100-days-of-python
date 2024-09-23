from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))
    
quiz = Quiz(question_bank)    

while quiz.still_has_questions():
    current_question = quiz.get_question()
    user_answer = input(f"Q.{quiz.question_number+1} {current_question.text} [true/false]? ").title()
    while user_answer not in ["True", "False"]:
        print("Invalid input. Please enter 'true' or 'false'.")
        user_answer = input(f"{current_question.text} [true/false]? ").title()
    if(quiz.check_answer(current_question, user_answer)):
        print(f"Correct! Current score: {quiz.score}")
    else:
        print(f"Wrong! The correct answer is {current_question.answer}. Current score: {quiz.score}")