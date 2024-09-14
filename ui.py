#We're going to create our user interface in tkinter but we're going to do it inside a class.
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:  #Pascal Case

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window= Tk()   #self.whatever makes whatever a property of this class
        self.window.title("Quizzler")     #window is an object of the tkinter class Tk

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text = 'Score:0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg='white') #canvas allows us to layer graphics on top of it:-)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=f"text goes here",
            fill=THEME_COLOR,
            font = ("Arial", 20, "italic")
        )
        #whenever we add an image or we add something to the canvas,we always have to provide a position as
        #the first two arguments.And that is the tuple that represents the X and Y position of the text.

        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file='images/false.png')
        true_img = PhotoImage(file='images/true.png')

        self.false_button = Button(image=false_img, highlightthickness=0, command= self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.true_button = Button(image=true_img, highlightthickness=0, command = self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()  #a never ending loop. Gets confused if near a while loop
                                #cannot use time module with this function either.
                                #if time delay is needed must use tkinter window.after()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score:{self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state='disabled') #keyword argument state allows us to disable or turn off buttons
            self.false_button.config(state='disabled')
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        #self.give_feedback(self.quiz.check_answer("True"))
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        #self.give_feedback(self.quiz.check_answer("False"))
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg='green') #milliseconds
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question) #milliseconds