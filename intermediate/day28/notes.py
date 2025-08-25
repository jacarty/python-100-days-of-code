"""
Building a Pomodoro App with Tkinter

The Pomodoro Technique
A time management method that breaks work into focused intervals, traditionally 25 minutes long, separated by short breaks.

Basic Flow:
Work (25 min) → Break (5 min) → Work (25 min) → Break (5 min) → 
Work (25 min) → Break (5 min) → Work (25 min) → Long Break (15-30 min)

Key Steps:
-- Choose a task to work on
-- Set timer for 25 minutes
-- Work with full focus until timer rings
-- Take a short break (5 minutes)

Repeat - After 4 pomodoros, take a longer break

The technique helps maintain focus, prevents burnout, and makes large tasks feel more manageable by breaking them into smaller, timed chunks.

"""

# https://colorhunt.co/


#######################################################################
#
# Dynamic Datatyping
# We're changing the Variable from Int to Str
# This isn't possible in all languages 
#
# https://stackoverflow.com/questions/11328920/is-python-strongly-typed
#
#######################################################################

def count_down(count):
    # timer function; 1s (1000ms)

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec == f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)



"""

Pomodoro Application

"""

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps

    reps += 1

    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    work_min = WORK_MIN * 60

    # 8th round
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    # 2nd, 4th and 6th round
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)
    # 1st, 3rd, 5th, 7th round
    else:
        count_down(work_min)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    # timer function; 1s (1000ms)

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

def center_window(window, min_width=200, min_height=200):
    """Center window with minimum size but allow growth for content"""
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

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, fg=GREEN, font=("FONT_NAME", 30, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.config(
    bg=YELLOW, 
    activebackground=YELLOW,
    highlightbackground=YELLOW,
    highlightcolor=YELLOW
)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(
    bg=YELLOW, 
    activebackground=YELLOW,
    highlightbackground=YELLOW,
    highlightcolor=YELLOW
)
reset_button.grid(column=2, row=2)

checkmarks = Label()
checkmarks.config(bg=YELLOW, fg=GREEN, font=("FONT_NAME", 16, "bold"))
checkmarks.grid(column=1, row=3)

canvas = Canvas(width=220, height=250, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="tomato.png")
canvas.create_image(110, 125, image=bg_image)
timer_text = canvas.create_text(110, 140, text="00:00", fill="white", font=("FONT_NAME", 16, "bold"))
canvas.grid(column=1, row=1)

center_window(window)
window.mainloop()