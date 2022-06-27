from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class GraficalInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score.grid(row=0, column=1, pady=30)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="hello", font=("verdana", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20)

        true_image = PhotoImage(file="true.png")
        false_image = PhotoImage(file="false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button_function)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button_function)
        self.true_button.grid(row=2, column=0, pady=20)
        self.false_button.grid(row=2, column=1)

        self.getnext()

        self.window.mainloop()

    def getnext(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        txt = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=txt)

    def true_button_function(self):
        answer = self.quiz.check_answer("true")
        self.feedback(answer)

    def false_button_function(self):
        answer = self.quiz.check_answer("false")
        self.feedback(answer)

    def feedback(self, feedback):
        print(feedback)
        if feedback:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.getnext)

