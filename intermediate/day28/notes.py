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