from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
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
        self.true.config(image=true_image)
        self.true.grid(row=3, column=0)
        false_image = PhotoImage(file='~/Desktop/100Days/Day_34/images/false.png')
        self.false = Button()
        self.false.config(image=false_image)
        self.false.grid(row=3, column=1)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)