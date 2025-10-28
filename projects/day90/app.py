########################################
# The Most Dangerous Writing App
########################################

from tkinter import *

############################
###### Tk variables ########
############################
FONT = "courier"
FONT_SIZE = 14
BACKGROUND_COLOR = "#1a1a2e"

############################
##### Global variables #####
############################
word_count = 0
timer_running = False
elapsed_time = 0
target_word_count = 250
danger_timer = None
typing_stopped_seconds = 0

############################
# Functions
############################

def centre_window(window, min_width=900, min_height=600):
    """Centre window with minimum size but allow growth for content"""
    window.update_idletasks()
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def show_typing_frame():
    """Hide setup frame and show typing frame"""
    global target_word_count
    target_word_count = int(word_count_var.get())
    setup_frame.grid_forget()
    typing_frame.grid(row=0, column=0, columnspan=5, sticky='nsew', padx=40, pady=40)
    typing.delete("1.0", END) 
    typing.focus_set()

def show_setup_frame():
    """Hide other frames and show setup frame"""
    typing_frame.grid_forget()
    results_frame.grid_forget()
    setup_frame.grid(row=0, column=0, columnspan=5, sticky='nsew')

def check_typing_stopped():
    """Check if user has stopped typing for more than 5 seconds"""
    global typing_stopped_seconds, danger_timer
    
    typing_stopped_seconds += 1
    time_remaining = 5 - typing_stopped_seconds
    time_left.config(text=f"Time: {time_remaining}s")
    
    if typing_stopped_seconds >= 5:
        # User stopped typing for 5 seconds - delete all text!
        typing.delete("1.0", END)
        typing.insert("1.0", "You stopped typing! Your work has been lost.\n\nStart over!")
        typing.config(state=DISABLED)
        window.after(3000, restart_test)
    else:
        danger_timer = window.after(1000, check_typing_stopped)

def reset_typing_timer(event):
    """Reset the danger timer whenever user types"""
    global typing_stopped_seconds, danger_timer, timer_running
    
    if not timer_running:
        timer_running = True
    
    # Update word count
    content = typing.get("1.0", END).strip()
    words = len(content.split()) if content else 0
    current_words.config(text=f"Words: {words}")
    
    # Check if target reached
    if words >= target_word_count:
        # Target reached - stop the countdown!
        if danger_timer:
            window.after_cancel(danger_timer)
            danger_timer = None
        save_button.config(state=NORMAL, bg="#4CAF50", fg="#1a1a2e")
        current_words.config(fg="#4CAF50")  # Green color to show success
        time_left.config(text="Complete!", fg="#4CAF50")
    else:
        # Target not reached - continue countdown
        typing_stopped_seconds = 0
        time_left.config(text=f"Time: 5s", fg="#E57373")
        save_button.config(state=DISABLED, bg="#666666", fg="#1a1a2e")
        current_words.config(fg="white")
        
        # Cancel existing timer and start new one
        if danger_timer:
            window.after_cancel(danger_timer)
        danger_timer = window.after(1000, check_typing_stopped)

def restart_test():
    """Reset all metrics and start new test"""
    global timer_running, word_count, typing_stopped_seconds, danger_timer
    
    if danger_timer:
        window.after_cancel(danger_timer)
    
    timer_running = False
    word_count = 0
    typing_stopped_seconds = 0
    
    typing.config(state=NORMAL)
    typing.delete("1.0", END)
    current_words.config(text="Words: 0", fg="white")
    time_left.config(text="Time: 5s")
    save_button.config(state=DISABLED, bg="#666666")
    show_setup_frame()

def save_work():
    """Save the current text to a file"""
    content = typing.get("1.0", END).strip()
    if content:
        try:
            with open("dangerous_writing_output.txt", "w") as f:
                f.write(content)
            results.config(text=f"✓ Successfully saved {len(content.split())} words!")
            typing_frame.grid_forget()
            results_frame.grid(row=0, column=0, columnspan=5, sticky='nsew')
        except Exception as e:
            results.config(text=f"Error saving: {str(e)}")

############################
# Config Tk
############################

window = Tk()
window.title("The Most Dangerous Writing App")
window.config(padx=0, pady=0, bg=BACKGROUND_COLOR)

# Configure grid to expand properly
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

############################
####### Setup Frame ########
############################

setup_frame = Frame(window, bg=BACKGROUND_COLOR)
setup_frame.grid(row=0, column=0, columnspan=5, sticky='nsew')

# Configure setup frame grid
for i in range(7):
    setup_frame.grid_rowconfigure(i, weight=1)
for i in range(3):
    setup_frame.grid_columnconfigure(i, weight=1)

# Icon (using canvas to draw nested squares like the reference image)
icon_canvas = Canvas(setup_frame, width=120, height=120, bg=BACKGROUND_COLOR, highlightthickness=0)
icon_canvas.grid(row=0, column=0, columnspan=3, pady=(40, 10))
icon_canvas.create_rectangle(20, 20, 100, 100, outline="#E57373", width=8)
icon_canvas.create_rectangle(35, 35, 85, 85, outline="#E57373", width=6)
icon_canvas.create_rectangle(45, 45, 75, 75, fill="#E57373", outline="")

# Title - "The Most"
title_label = Label(
    setup_frame, 
    text="The Most", 
    font=(FONT, 40, "bold"), 
    bg=BACKGROUND_COLOR, 
    fg="white"
)
title_label.grid(row=1, column=0, columnspan=3, pady=(0, 5))

# "Dangerous" in red/pink
dangerous_label = Label(
    setup_frame, 
    text="Dangerous", 
    font=(FONT, 40, "bold"), 
    bg=BACKGROUND_COLOR, 
    fg="#E57373"
)
dangerous_label.grid(row=2, column=0, columnspan=3, pady=(0, 5))

# "Writing App"
app_label = Label(
    setup_frame, 
    text="Writing App", 
    font=(FONT, 40, "bold"), 
    bg=BACKGROUND_COLOR, 
    fg="white"
)
app_label.grid(row=3, column=0, columnspan=3, pady=(0, 30))

# Warning message
warning_label = Label(
    setup_frame,
    text="Don't stop typing or your work will be lost!",
    font=(FONT, 14),
    bg=BACKGROUND_COLOR,
    fg="#CCCCCC"
)
warning_label.grid(row=4, column=0, columnspan=3, pady=(0, 30))

# Word count selection frame
selection_frame = Frame(setup_frame, bg="#2d2d44", pady=20, padx=40)
selection_frame.grid(row=5, column=0, columnspan=3, pady=20)

word_count_label = Label(
    selection_frame,
    text="Minutes / Words",
    font=(FONT, 11),
    bg="#2d2d44",
    fg="#888888"
)
word_count_label.grid(row=0, column=0, columnspan=5, pady=(0, 15))

# Word count variable
word_count_var = StringVar(window)
word_count_var.set("250")  # default value

# Create radio-button style selection (matching the reference image)
word_options = [("150", 150), ("250", 250), ("500", 500), ("750", 750), ("1337", 1337)]
for idx, (text, value) in enumerate(word_options):
    rb = Radiobutton(
        selection_frame,
        text=text,
        variable=word_count_var,
        value=str(value),
        font=(FONT, 13),
        bg="#2d2d44",
        fg="white",
        selectcolor="#1a1a2e",
        activebackground="#2d2d44",
        activeforeground="white",
        indicatoron=True,
        borderwidth=0,
        highlightthickness=0
    )
    rb.grid(row=1, column=idx, padx=15)
    if text == "150":
        rb.select()  # Select first option by default visually

# Start button
start_button = Button(
    setup_frame,
    text="Start Writing",
    font=(FONT, 16, "bold"),
    bg="#D8D8D8",
    fg="#1a1a2e",
    padx=60,
    pady=18,
    command=show_typing_frame,
    relief=FLAT,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    activebackground="#C0C0C0",
    activeforeground="#1a1a2e"
)
start_button.grid(row=6, column=0, columnspan=3, pady=40)

############################
###### Typing Frame ########
############################

typing_frame = Frame(window, bg=BACKGROUND_COLOR)

# Configure typing frame to expand
typing_frame.grid_columnconfigure(0, weight=1)
typing_frame.grid_columnconfigure(4, weight=1)
typing_frame.grid_rowconfigure(1, weight=1)

# Stats bar at top
stats_frame = Frame(typing_frame, bg=BACKGROUND_COLOR)
stats_frame.grid(row=0, column=0, columnspan=5, sticky='ew', pady=(0, 20))
stats_frame.grid_columnconfigure(0, weight=1)
stats_frame.grid_columnconfigure(1, weight=1)

current_words = Label(
    stats_frame, 
    font=(FONT, 16), 
    text="Words: 0", 
    bg=BACKGROUND_COLOR, 
    fg="white"
)
current_words.grid(row=0, column=0, sticky='w')

time_left = Label(
    stats_frame, 
    font=(FONT, 16), 
    text="Time: 5s", 
    bg=BACKGROUND_COLOR, 
    fg="#E57373"
)
time_left.grid(row=0, column=1, sticky='e')

typing = Text(
    typing_frame, 
    font=(FONT, 16), 
    wrap=WORD, 
    bg="#2d2d44", 
    fg="white", 
    insertbackground="white", 
    relief=FLAT,
    padx=20,
    pady=20,
    borderwidth=0,
    highlightthickness=0
)
typing.grid(row=1, column=0, columnspan=5, sticky='nsew')
typing.bind('<KeyPress>', reset_typing_timer)

# Action buttons frame
button_frame = Frame(typing_frame, bg=BACKGROUND_COLOR)
button_frame.grid(row=2, column=0, columnspan=5, pady=(20, 0))

save_button = Button(
    button_frame,
    text="Save & Finish",
    font=(FONT, 12, "bold"),
    bg="#666666",
    fg="#1a1a2e",
    padx=20,
    pady=10,
    command=save_work,
    relief=FLAT,
    cursor="hand2",
    borderwidth=0,
    state=DISABLED,
    disabledforeground="#555555"
)
save_button.pack(side=LEFT, padx=10)

restart_button_typing = Button(
    button_frame,
    text="Start Over",
    font=(FONT, 12, "bold"),
    bg="#D8D8D8",
    fg="#1a1a2e",
    padx=20,
    pady=10,
    command=restart_test,
    relief=FLAT,
    cursor="hand2",
    borderwidth=0,
    highlightthickness=0,
    activebackground="#C0C0C0",
    activeforeground="#1a1a2e"
)
restart_button_typing.pack(side=LEFT, padx=10)

############################
##### Results Frame ########
############################
results_frame = Frame(window, bg=BACKGROUND_COLOR)
results_frame.grid_rowconfigure(0, weight=1)
results_frame.grid_columnconfigure(0, weight=1)

results = Label(
    results_frame, 
    font=(FONT, 18), 
    text="", 
    bg=BACKGROUND_COLOR, 
    fg="white",
    pady=40
)
results.grid(row=0, column=0)

restart_button = Button(
    results_frame,
    text="Start Over",
    font=(FONT, 14, "bold"),
    bg="#E57373",
    fg="white",
    padx=40,
    pady=15,
    command=restart_test,
    relief=FLAT,
    cursor="hand2",
    borderwidth=0
)
restart_button.grid(row=1, column=0, pady=20)

############################
# Centre and Maintain Window
############################
centre_window(window)
window.mainloop()
