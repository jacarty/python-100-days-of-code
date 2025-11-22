########################################
# Typing SpeedTest
########################################

from tkinter import *
import pandas as pd
import random

############################
###### Tk variables ########
############################
FONT = "courier"
FONT_SIZE = 14
BACKGROUND_COLOR = "#FFFFFF"

############################
##### Global variables #####
############################
current_word_index = 0
timer_running = False
elapsed_time = 0
correct_words = 0
incorrect_words = 0
total_chars = 0
mistakes = []
backspace_count = 0 

# Centre the Tkinter Window On Screen
def centre_window(window, min_width=850, min_height=400):
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
    """Clear Typing Box placeholder text"""
    typing.delete(0, END)
    typing.unbind('<FocusIn>')

def count_down(count):
    """Timer - One Minute Countdown"""
    global elapsed_time
    elapsed_time = 60 - count
    time_left.config(text=f"Time Left: {count}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        end_test()

def start_timer(event):
    """Start timer when key is pressed"""
    global timer_running
    if not timer_running:
        timer_running = True
        count_down(60)
        typing.unbind('<KeyPress>')

def restart_test():
    """Reset all metrics and start new test"""
    global current_word_index, timer_running, elapsed_time, correct_words, incorrect_words, mistakes, random_words, backspace_count
    
    current_word_index = 0
    timer_running = False
    elapsed_time = 0
    correct_words = 0
    incorrect_words = 0
    mistakes = []
    backspace_count = 0

    random_words = get_words()
    
    correct_cpm.config(text="CPM: --")
    wpm.config(text="WPM: --")
    time_left.config(text="Time Left: 60")
    
    results_frame.grid_forget()
    game_frame.grid(row=1, column=0, columnspan=5)
    
    # Reset entry box
    typing.delete(0, END)
    typing.focus_set()  # Put cursor in the box ready to type
    
    # Rebind timer (don't need FocusIn anymore)
    typing.bind('<KeyPress>', start_timer)
    
    # Display first words
    display_words(0)

def end_test(speedster=False):
    """Results screen generation and metrics"""
    # Hide game frame, show results frame
    game_frame.grid_forget()
    results_frame.grid(row=1, column=0, columnspan=5)
    
    total_words = correct_words + incorrect_words
    cpm_final = total_chars
    wpm_final = correct_words  
    
    best_wpm = load_best_score()
    if wpm_final > best_wpm:
        save_best_score(wpm_final)
        your_best.config(text=f"Your Best: {wpm_final}")

    if total_words > 0:
        edit_rate = round(backspace_count / total_words, 2)
    else:
        edit_rate = 0

    results_text = ""

    if speedster:
        results_text += f"Wow! Your results are insanely fast at 200+ words minute! Your fingers must be on fire 🔥\n\n"
    results_text += f"Your score: {cpm_final} CPM (that is {wpm_final} WPM)\n\n"
    results_text += f"In reality, you typed {total_words} words, "
    results_text += f"but you made {incorrect_words} mistakes, "
    results_text += f"which were not counted in the corrected scores.\n\n"
    results_text += f"Your edit rate: {edit_rate} backspaces per word\n\n"
    
    if mistakes:
        results_text += "Your mistakes were:\n"
        for typed, correct in mistakes:
            results_text += f'    Instead of "{correct}", you typed "{typed}".\n'
        
    results.config(text=results_text)

def track_backspace(event):
    """Track backspace usage"""
    global backspace_count
    backspace_count += 1

def update_stats():
    """Track and update metrics"""
    global correct_words, incorrect_words, elapsed_time, total_chars
    
    cpm = total_chars
    
    if elapsed_time > 0:
        wpm_value = round((correct_words / elapsed_time) * 60)
    else:
        wpm_value = 0
    
    correct_cpm.config(text=f"CPM: {cpm}")
    wpm.config(text=f"WPM: {wpm_value}")

def load_best_score():
    """Load best WPM from file, return 0 if file doesn't exist"""
    try:
        with open('best_score.txt', 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0

def save_best_score(wpm):
    """Save WPM to file"""
    with open('best_score.txt', 'w') as file:
        file.write(str(wpm))

def get_words():
    """Create a list of 200 random workds"""
    global random_words
    with open('words.txt') as f:
        words = [word.strip() for word in f.readlines()]
        random.shuffle(words)
        return words[:200]

def display_words(start_index):
    """Create three lines of six words"""
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
    """Check if the typed word is correct"""
    global current_word_index, correct_words, incorrect_words, mistakes, total_chars
    typed_word = typing.get().strip()
    correct_word = random_words[current_word_index]
    
    if typed_word == correct_word:
        correct_words += 1
        total_chars += len(correct_word)
    else:
        incorrect_words += 1
        mistakes.append((typed_word, correct_word))
        print(f"Wrong! You typed '{typed_word}' but it was '{correct_word}'")
    
    typing.delete(0, END)
    
    current_word_index += 1

    update_stats()

    if current_word_index >= 200:
        end_test(speedster=True)
    else:
        if current_word_index % 18 == 0:
            display_words(current_word_index)
        else:
            current_start = (current_word_index // 18) * 18
            display_words(current_start)

############################
# Config Tk
############################

window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20)

############################
###### Shared Widgets ######
############################
your_best = Label(window, font=(FONT, FONT_SIZE), padx=20, pady=10, text="Your Best: --")
your_best.grid(row=0, column=0)

correct_cpm = Label(window, font=(FONT, FONT_SIZE), padx=20, pady=10, text="CPM: --")
correct_cpm.grid(row=0, column=1)

wpm = Label(window, font=(FONT, FONT_SIZE), padx=20, pady=10, text="WPM: --")
wpm.grid(row=0, column=2)

time_left = Label(window, font=(FONT, FONT_SIZE), padx=20, pady=10, text="Time Left: 60")
time_left.grid(row=0, column=3)

restart = Button(window, font=(FONT, FONT_SIZE), padx=20, text="Restart", command=restart_test)
restart.grid(row=0, column=4)

############################
###### Game Widgets ########
############################
game_frame = Frame(window)
game_frame.grid(row=1, column=0, columnspan=5)

text = Label(game_frame, pady=75, font=(FONT, FONT_SIZE))
text.grid(row=0, column=0)

typing = Entry(game_frame, font=(FONT, FONT_SIZE))
typing.grid(row=1, column=0)
typing.insert(0, "Start Typing Here!")
typing.bind('<FocusIn>', clear_placeholder)
typing.bind('<KeyPress>', start_timer)
typing.bind('<space>', check_word)
typing.bind('<Return>', check_word) 
typing.bind('<BackSpace>', track_backspace)

############################
##### Results Widgets ######
############################
results_frame = Frame(window)

results = Label(results_frame, font=(FONT, FONT_SIZE), text="Placeholder", wraplength=700, justify=LEFT)
results.grid(row=0, column=0, padx=20, pady=20, sticky='w') # sticky is align west

############################
# Initiate Typing
############################
random_words = get_words()
display_words(0)

############################
# Best Score
############################
best_wpm = load_best_score()
your_best.config(text=f"Your Best: {best_wpm}")

############################
# Centre and Maintain Window
############################
centre_window(window)
window.mainloop()
