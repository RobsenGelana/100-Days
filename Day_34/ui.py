from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.config(bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.true_image = PhotoImage(file='~/Desktop/100Days/Day_34/images/true.png')
        self.true = Button()
        self.true.config(image=self.true_image)
        self.true.grid(row=3, column=0)
        self.false_image = PhotoImage(file='~/Desktop/100Days/Day_34/images/false.png')
        self.false = Button()
        self.false.config(image=self.false_image)
        self.false.grid(row=3, column=1)


        
        self.window.mainloop()