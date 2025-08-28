"""
GUI with Tkinter and Functional Arguments
"""
# import
import tkinter

#### Windows

# create a window
window = tkinter.Tk()

# title window
window.title("My GUI Program")
# minimum size (autoscales by default)
window.minsize(width=500, height=300)

#### Labels
my_label = tkinter.Label(text="I am a label", font=("courier", 11, "bold"))
my_label.pack(side="left")

# keep window on screen; has to be at the bottom of program
window.mainloop()

"""
##### Keyword arguments
"""

def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    pass

my_function(a=1, b=2, c=2)    

#### Arguments with default values
def my_function(a=1, b=2, c=3):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    pass

my_function()    

#### Overwrite one value
def my_function(a=1, b=2, c=3):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    pass

my_function(b=4)    

"""
##### Unlimited positional arguments

They get passed in as a Tuple

"""

#print them
def add(*args):
    for n in args:
        print(n)

add(1, 2, 6, 10)

### add them
def add(*args):
    return(sum(args))

print(add(1, 2, 6, 10))

# get one value
def add(*args):
    print(args[1])

add(1, 2, 6, 10)

"""
##### Unlimited positional keyword arguments

They get passed in as a Dictionary

"""
### kwargs
def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    
    print(kwargs["add"])

calculate(add=3, multiply=8)

### with a value and kwargs
def calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply=8)

### create Class with kwargs (kw)
class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Bugait", model="Veyron")
print(my_car.model)

### using get is the way for Classes with optional inputs
### if the value is empty it just returns none
### the key lookup would cause an error if not passed
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")

my_car = Car(make="Bugait", model="Veyron")
print(my_car.colour)


### you can mix all three
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
    # 4 (7, 3, 0) {'x': 10, 'y': 64}
    
all_aboard(4, 7, 3, 0, x=10, y=64)


"""
Examples of widgets

"""

from tkinter import *

def center_window(window, min_width=500, min_height=500):
    """Center window with minimum size but allow growth for content"""
    
    # Get required size for content
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()
    
    # Use larger of minimum or required
    width = max(min_width, req_width)
    height = max(min_height, req_height)
    
    # Get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calculate position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

my_window = Tk()
# show all available methods
# print(dir(my_window))
# give window a title
my_window.title("Distance Converter")
# function to set size and centre on screen
center_window(my_window)



# on screen label
my_label = Label(text="I am a label")
# lots of element can be configured with .config or individually
my_label.config(font=("courier", 12))
# pack always needed to position on screen
my_label.pack()


def button_clicked():
    print("I got clicked")
    # update the label text
    # my_label.config(text="Button was clicked")
    # use the input window text
    my_label.config(text=my_entry.get())

# on screen button
# command defines what happens when clicked; it calls the name of a function
my_button = Button(text="Click me", command=button_clicked)
# pack always needed to position on screen
my_button.pack()


# on screen Entry box
my_entry = Entry()
my_entry.pack()
my_entry.config(width=20)
# default text
my_entry.insert(END, string="enter email")


# multi line Text entry
my_text_entry = Text()
# box size
my_text_entry.config(width=30, height=10)
# start cursor in this box
my_text_entry.focus()
my_text_entry.insert(END, "Some starting text in the box")
print(my_text_entry.get(1.0, END))
my_text_entry.pack()


# spinbox 
def spinbox_used():
    print(my_spinbox.get())

my_spinbox = Spinbox()
my_spinbox.config(from_=0, to=10, width=5, command=spinbox_used)
my_spinbox.pack()


# scale / scroll to set number
def scale_used(value):
    print(value)

# scale / scroll to set number
my_scale = Scale()
my_scale.config(from_=0, to=100, command=scale_used)
my_scale.pack()

# checkbutton
def checkbutton_used():
    # prints 1 in clicked otherwise 0
    print(checked_state.get())

checked_state = IntVar()
my_checkbutton = Checkbutton()
my_checkbutton.config(text="Is On?", variable=checked_state, command=checkbutton_used)
my_checkbutton.pack()

# radio button 
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
my_radiobutton1 = Radiobutton()
my_radiobutton2 = Radiobutton()
my_radiobutton1.config(text="Option1", value=1, variable=radio_state, command=radio_used)
my_radiobutton2.config(text="Option2", value=2, variable=radio_state, command=radio_used)
my_radiobutton1.pack()
my_radiobutton2.pack()

# listbox
def listbox_used(event):
    # gets current selection from listbox
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
my_listbox.config(height=4)
fruits = ["Apple", "Orange", "Pineapple", "Strawberry"]
for item in fruits:
    my_listbox.insert(fruits.index(item), item)
my_listbox.bind("<<ListboxSelect>>", listbox_used)
my_listbox.pack()

# keep window open; last line
my_window.mainloop()


"""
can't mix pack and grid in same program

let Tk order and place on window
my_label.pack()

specific places on window
my_label.place(x=50, y=50)

using grid to divide the window and place
my_label.grid(column=0, row=0)
"""

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
    label.config(text=entry.get())

# create Window and centre in screen
window = Tk()
window.title("Distance Converter")
center_window(window)

# label
label = Label(text="I am a label")
#label.config(font=("courier", 12), padx=20, pady=20)
label.grid(column=0, row=0)

# button one
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# button two
button_2 = Button(text="Button 2")
button_2.grid(column=2, row=0)

# entry box
entry = Entry()
entry.config(width=20)
entry.insert(END, string="enter email")
entry.grid(column=3, row=3)

# centre window
center_window(window, min_width=0, min_height=0)
# keep alive
window.mainloop()

#######################
# miles to KM converter
#######################

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
