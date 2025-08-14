"""
Question Attributes:

Text - question text
Answer - the answer to question

new_q = Question("2+3=5", "True")

text = "2+3=5"
answer = "True"
new_q = Question("2+3=5", "True")
"""

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for key in question_data:
    question = key["question"]
    answer = key["correct_answer"]
    new_q = Question(q_text=question, q_answer=answer)
    question_bank.append(new_q)

# simply prints a list of the question objects
# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    quiz.final_score()
