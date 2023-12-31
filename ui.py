import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
true_img = "images/true.png"
false_img = "images/false.png"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = self.quiz.score
        
        self.window = tkinter.Tk()
        self.window.title="Quizzler"
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        
        self.label = tkinter.Label(text=f"Score: {self.score}",font=('Arial',15,'normal'), fg="white", bg=THEME_COLOR)
        self.label.grid(column=1,row=0)
        
        self.canvas = tkinter.Canvas(width=300,height=250)
        self.question_text = self.canvas.create_text(150, 125, text='Some question text', 
                                                     fill=THEME_COLOR, font=('Arial',16,'italic'),
                                                     width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=25)
        
        correct_img = tkinter.PhotoImage(file="images/true.png")
        self.correct_btn = tkinter.Button(image=correct_img,
                                          highlightthickness=0,
                                          width=100, height=100,
                                          command=self.pick_true
                                          )
        self.correct_btn.grid(column=0,row=2)
        
        false_img = tkinter.PhotoImage(file="images/false.png") 
        self.false_btn = tkinter.Button(image=false_img,
                                        highlightthickness=0,
                                        width=100,height=100,
                                        command=self.pick_wrong
                                        )
        self.false_btn.grid(column=1,row=2)

        self.get_next_question()


        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have finished the quiz.")
            self.correct_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
    def pick_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
    
    def pick_wrong(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)