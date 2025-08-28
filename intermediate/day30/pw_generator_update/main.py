"""

Building a Password Generator with Tkinter

File output format
website | email | password

"""

from tkinter import *
from tkinter import messagebox # need to import message box
import string # used to get letters, digits and punctuation
import pyperclip
import random
import json

FONT = "courier"
FONT_SIZE = 11

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(16))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"""These are the details entered: \n
                                       Website: {website}\n
                                       Email: {email}\n
                                       Password: {password}\n
                                       Is it okay to save?""")

####################
# we could avoid except / else repitition with a function
# being left like this for future readability
####################

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # read data file
                    data = json.load(file)

            except FileNotFoundError:
                print("File not found. Needs to be created.")
                with open("data.json", "w") as file:
                    # saving updated data
                    json.dump(new_data, file, indent=4)

            else:
                # update old data with new data
                data.update(new_data)

                with open("data.json", "w") as file:
                    # saving updated data
                    json.dump(data, file, indent=4)
                
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    # print("search")
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        email_lookup = data[website]["email"]
        pw_lookup = data[website]["password"]

    except FileNotFoundError:
        messagebox.showinfo(title=f"{website}", message="No data file found.")

    except KeyError:
        messagebox.showinfo(title=f"{website}", message="No details exist for the website.")

    else:
        messagebox.showinfo(title=f"{website}", message=f"""Email: {email_lookup}\n
                                                        Password: {pw_lookup}""")

# ---------------------------- UI SETUP ------------------------------- #

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
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(127, 100, image=bg_image)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website:", font=(FONT, FONT_SIZE))
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.config(width=21)
website_entry.focus() # default cursor to this box
website_entry.grid(column=1, row=1)

search_button = Button(command=search_password)
search_button.config(text="Search Password", width=17, font=(FONT, FONT_SIZE))
search_button.grid(column=2, row=1)

email_label = Label()
email_label.config(text="Email/Username:", font=(FONT, FONT_SIZE))
email_label.grid(column=0, row=2)

email_entry = Entry()
email_entry.config(width=42)
email_entry.insert(0, "test@email.com") # default text
email_entry.grid(column=1, columnspan=2, row=2)

password_label = Label()
password_label.config(text="Password:", font=(FONT, FONT_SIZE))
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(command=generate_password)
password_button.config(text="Generate Password", font=(FONT, FONT_SIZE))
password_button.grid(column=2, row=3)

add_button = Button(command=save_password)
add_button.config(text="Add", width=40, font=(FONT, FONT_SIZE))
add_button.grid(column=1, columnspan=2, row=4)

#centre_window(window)
window.mainloop()