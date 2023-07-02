from question_model import Question
from data import q_and_a
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank=[]
for i in range(len(q_and_a)):
    question_bank.append(Question(q_and_a[i]["text"],q_and_a[i]["answer"]))

quiz = QuizBrain(question_bank)
quiz_ui=QuizInterface(quiz)
