from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UserInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            bg= THEME_COLOR, 
            padx=20, 
            pady=20)

        self.score = Label()
        self.score.config(
            bg=THEME_COLOR, 
            fg="white", 
            text="Score: ")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(
            150, 125, 
            width=275, # wraps text
            text="Question Text",
            font=("ariel", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)
    
        self.check_button = Button(command=self.check_button)
        # doesn't need self as not being used anywhere else in the Class
        check_image = PhotoImage(file="./images/true.png") 
        self.check_button.config(image=check_image, highlightthickness=0, bd=0)
        self.check_button.grid(column=0, row=2)

        self.cross_button = Button(command=self.cross_button)
        cross_image = PhotoImage(file="./images/false.png")
        self.cross_button.config(image=cross_image, highlightthickness=0, bd=0)
        self.cross_button.grid(column=1, row=2)

        self.get_next_question()
        self.centre_window(self.window)
        self.window.mainloop()

    def centre_window(self, window, min_width=0, min_height=0):
        """Centre window with minimum size but allow growth for content"""
        # Update to calculate widget sizes
        window.update_idletasks()
        # get required size for content
        req_width = window.winfo_reqwidth()
        req_height = window.winfo_reqheight()
        # use larger of minimum or required
        width = max(min_width, req_width)
        height = max(min_height, req_height)
        # get screen dimensions
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        # calculate position
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        # set screen location
        window.geometry(f"{width}x{height}+{x}+{y}")

    def get_next_question(self):
        self.canvas(bg="white")
        if self.quiz.still_has_questions:
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def cross_button(self):
        check_answer = self.quiz.check_answer("True")
        self.give_feedback(check_answer)

    def check_button(self):
        self.give_feedback(self.quiz.check_answer("False")) # same as above

    def give_feedback(self, check_answer):
        if check_answer:
            self.canvas(bg="green")
        else:
            self.canvas(bg="red")
        self.window.after(1000, self.get_next_question)
