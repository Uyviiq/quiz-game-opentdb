class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list) 
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}.(True/False/something else according to the question)?: ").strip()
        correct_answer = current_question.answer
        self.check_answer(user_answer,correct_answer)
    def check_answer(self,answer,correct):
        if answer.lower() == correct.lower():
            print("You got it right")
            self.score +=1
        else:
            print("that's wrong")
        print(f"the answer is {correct}")
        print(f"Your score is {self.score}/{self.question_number}\n")