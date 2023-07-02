class QuizBrain:
    def __init__(self,question_list):
        self.question_list=question_list
        self.question_number=0
        self.score=0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1 
        self.correct_answer = current_question.answer
        return f"Q.{self.question_number}: {current_question.text}"  

    def still_has_questions(self):
        if self.question_number>=len(self.question_list):
            self.question_number=0
            return False
        else:
            return True
        
    def check_answer(self,user_answer):
        if user_answer.lower() == self.correct_answer.lower():
            self.score+=1
            return True
        else:
            return False