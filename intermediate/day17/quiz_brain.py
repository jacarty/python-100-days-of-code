"""
Ask the questions
Check if the answer was correct
Check if we're at the end of the quiz

Class QuizBrain

attributes:
question_number = 0
questions_list

methods:
next_question()

Q.1 question (true/false)
"""

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0
        #print(self.question_list[question_number])

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # above is a slicker way of doing below - it will return True or False
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def next_question(self):
        for question in self.question_list:
            current_question = self.question_list[self.question_number]

            # print(vars(current_question)) # returns full dictionary
            # print(current_question.text)  # returns the text value
            # print(f"Q{self.question_number +1}: {current_question.text} True/False?: ")

            self.question_number += 1 # doing this first avoids +1 on the question number in next line
            user_answer = input(f"Q{self.question_number}: {current_question.text} True/False?: ")
            correct_answer = current_question.answer
            # print(user_answer)
            # print(correct_answer)

            self.check_answer(user_answer, correct_answer)
            
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Oops. You got it wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score} out of {self.question_number}")
        print("\n") # purely for readability

    def final_score(self):
        print("You've completed the Quiz!")
        print(f"Your score was: {self.score}/{self.question_number}")
