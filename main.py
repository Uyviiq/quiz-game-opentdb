from data import questions
from question_model import Question
from quiz_brain import QuizBrain
from termcolor import colored


question_bank = []
question_data = questions()
for item in question_data:
    q = item["question"]
    a = item["correct_answer"]
    ob_question = Question(q,a) 
    question_bank.append(ob_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(colored("you completed the quiz",color="blue"))
print(f"your final score is {colored(quiz.score,color="red")}/{colored(quiz.question_number,color="red")}")