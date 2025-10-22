########################################
# Typing SpeedTest
########################################

from tkinter import *
import pandas as pd
import random

# Tk variables
FONT = "courier"
FONT_SIZE = 12
BACKGROUND_COLOR = "#FFFFFF"

# Global variables
timer = 0
current_word_index = 0

# Centre the Tkinter Window On Screen
def centre_window(window, min_width=0, min_height=0):
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

def clear_placeholder(event):
    typing.delete(0, END)
    typing.unbind('<FocusIn>')

def get_words():
    global random_words
    with open('words.txt') as f:
        words = [word.strip() for word in f.readlines()]
        random.shuffle(words)
        return words[:200]

def display_words(start_index):
    global random_words, current_word_index
    words_to_display = random_words[start_index:start_index+18]
    current_position = current_word_index - start_index
    
    if 0 <= current_position < 18:
        words_to_display[current_position] = f"*{words_to_display[current_position]}*"
    
    line1 = " ".join(words_to_display[0:6])
    line2 = " ".join(words_to_display[6:12])
    line3 = " ".join(words_to_display[12:18])
    
    display_text = "\n".join([line1, line2, line3])
    text.config(text=display_text)

def check_word(event):
    global current_word_index
    typed_word = typing.get()   
    correct_word = random_words[current_word_index]
    
    if typed_word == correct_word:
        print("Correct!")
    else:
        print(f"Wrong! You typed '{typed_word}' but it was '{correct_word}'")
    
    typing.delete(0, END)
    
    current_word_index += 1
    if current_word_index % 18 == 0:
        display_words(current_word_index)
    else:
        current_start = (current_word_index // 18) * 18
        display_words(current_start)

# Config Tk
window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20)

##### Shared Widgets #####
your_best = Label(
    window,
    font=(FONT, FONT_SIZE),
    padx=20,
    pady=10,
    text="Your Best: --"
)
your_best.grid(row=0, column=0)

correct_cpm = Label(
    window, 
    font=(FONT, FONT_SIZE),
    padx=20,
    pady=10,
    text="CPM: --"
)
correct_cpm.grid(row=0, column=1)

wpm = Label(
    window, 
    font=(FONT, FONT_SIZE), 
    padx=20,
    pady=10,
    text="WPM: --"
)
wpm.grid(row=0, column=2)

time_left = Label(
    window, 
    font=(FONT, FONT_SIZE), 
    padx=20,
    pady=10,
    text="Time Left: 60"
)
time_left.grid(row=0, column=3)

restart = Button(
    window, 
    font=(FONT, FONT_SIZE), 
    padx=20,
    text="Restart"
)
restart.grid(row=0, column=4)

##### Game Widgets #####
game_frame = Frame(window)
game_frame.grid(row=1, column=0, columnspan=5)

text = Label(
    game_frame, 
    pady=20,
    font=(FONT, FONT_SIZE)
)
text.grid(row=0, column=0)

typing = Entry(
    game_frame,
    font=(FONT, FONT_SIZE)
)
typing.grid(row=1, column=0)
typing.insert(0, "Start Typing Here!")
typing.bind('<FocusIn>', clear_placeholder)
typing.bind('<space>', check_word)
typing.bind('<Return>', check_word) 

##### Results Widgets #####
results_frame = Frame(window)

results = Label(results_frame, font=(FONT, FONT_SIZE), text="Placeholder")

# Initiate Typing
random_words = get_words()
display_words(0)

# Centre and Maintain Window
centre_window(window)
window.mainloop()
