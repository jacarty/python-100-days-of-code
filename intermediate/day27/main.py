from tkinter import *

def center_window(window, min_width=0, min_height=0):
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

def button_clicked():
    """Create a button"""
    print("I got clicked")
    calc = round((float(miles_entry.get()) * 1.609), 2)
    calc_label.config(text=calc)

# create Window and centre in screen
window = Tk()
window.title("Distance Converter")
center_window(window)
window.config(padx=10, pady=10)

# entry box
miles_entry = Entry()
miles_entry.config(width=10)
miles_entry.insert(END,string="0")
miles_entry.grid(column=1, row=0)

# miles label
miles_label = Label(text="Miles")
miles_label.config(font=("courier", 12))
miles_label.grid(column=2, row=0)

# equals to label
equals_label = Label(text="Is equal to")
equals_label.config(font=("courier", 12))
equals_label.grid(column=0, row=1)

# km label
calc_label = Label(text="0")
calc_label.config(font=("courier", 12))
calc_label.grid(column=1, row=1)

# label4
km_label = Label(text="KM")
km_label.config(font=("courier", 12))
km_label.grid(column=2, row=1)

# button
calc_button = Button(text="Calculate", command=button_clicked)
calc_button.config(font=("courier", 12))
calc_button.grid(column=1, row=2)

# centre window
center_window(window)
# keep alive
window.mainloop()
