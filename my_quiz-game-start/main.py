from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_options = question["option_answers"]
    new_question = Question(question_text, question_answer, question_options)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("Congrats!, You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
