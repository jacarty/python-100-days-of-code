"""
Flashcard Project

https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists

https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish

https://github.com/hermitdave/FrequencyWords/tree/master/content/2018

"""


from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("./data/spanish_words_to_learn.csv")
    spanish_list = df.to_dict('records')
except:
    df = pd.read_csv("./data/spanish_words_1k.csv")
    spanish_list = df.to_dict('records')

random_word = {}
flip_timer = None

def known_word():
    global random_word
    spanish_list.remove(random_word)
    
    df = pd.DataFrame(spanish_list)
    df.to_csv("./data/spanish_words_to_learn.csv", index=False)
    generate_card()


def generate_card():
    global random_word, flip_timer
    random_word = random.choice(spanish_list)

    canvas.itemconfig(canvas_image, image=spanish_image)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=random_word["word"], fill="black")

    # cancel any running timer when a new card is generated
    if flip_timer:
        window.after_cancel(flip_timer)

    # set timer
    flip_timer = window.after(3000, flip_card)


def flip_card():
    english_word = random_word['translation']

    canvas.itemconfig(canvas_image, image=english_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")


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

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
spanish_image = PhotoImage(file="./images/card_front.png")
english_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(410, 263, image=spanish_image)
card_title = canvas.create_text(400, 120, font=("ariel", 35, "italic"))
card_word = canvas.create_text(400, 263, font=("ariel", 60, "italic"))
canvas.grid(column=0, columnspan=2, row=0)

cross_button = Button(command=generate_card)
cross_image = PhotoImage(file="./images/wrong.png")
cross_button.config(image=cross_image, highlightthickness=0, bd=0)
cross_button.grid(column=0, row=1)

check_button = Button(command=known_word)
check_image = PhotoImage(file="./images/right.png")
check_button.config(image=check_image, highlightthickness=0, bd=0)
check_button.grid(column=1, row=1)

centre_window(window)
generate_card()
window.mainloop()