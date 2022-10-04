from cgitb import text
from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) :
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,  bg='white')
        self.question_text = self.canvas.create_text(150, 125,
                                                    width=280,
                                                    text="Question Text", 
                                                    fill=THEME_COLOR, 
                                                    font=('Arial', 20, 'normal'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file='~/Desktop/100Days/Day_34/images/true.png')
        self.true = Button()
        self.true.config(image=true_image, command=self.check_true)
        self.true.grid(row=3, column=0)
        false_image = PhotoImage(file='~/Desktop/100Days/Day_34/images/false.png')
        self.false = Button()
        self.false.config(image=false_image, command=self.check_false)
        self.false.grid(row=3, column=1)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of questions")
        
    def check_true(self):
        #is_right = self.quiz.check_answer('True')
        self.give_feedback(self.quiz.check_answer('True'))

    def check_false(self):
       # is_right = self.quiz.check_answer('False')
        self.give_feedback(self.quiz.check_answer('False'))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
        