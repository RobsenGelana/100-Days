from tkinter import *
THEME_COLOR = "#375362"
FONT = ('Ariel', 20, 'normal')


class QuizInterface:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,  bg='white')
        self.question_text = self.canvas.create_text(150, 125,text="Question Text", fill=THEME_COLOR, font=('Arial', 20, 'normal'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file='~/Desktop/100Days/Day_34/images/true.png')
        self.true = Button()
        self.true.config(image=true_image)
        self.true.grid(row=3, column=0)
        false_image = PhotoImage(file='~/Desktop/100Days/Day_34/images/false.png')
        self.false = Button()
        self.false.config(image=false_image)
        self.false.grid(row=3, column=1)


        
        self.window.mainloop()