"""
Question Attributes:

Text - question text
Answer - the answer to question

new_q = Question("2+3=5", "True")

text = "2+3=5"
answer = "True"
new_q = Question("2+3=5", "True")

Question Class with an __init__ will have the two attributes; test and answer attribute
"""

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
