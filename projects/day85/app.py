########################################
# Watermark Image
########################################

from tkinter import *
from tkinter import filedialog
from PIL import Image

FONT = "courier"
FONT_SIZE = 10

background_image = None
foreground_image = None 

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

def upload_background(event=None):
    """Upload background image"""
    # Import global var
    global background_image
    # File to upload
    filename = filedialog.askopenfilename(
        title="Select Background Image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )

    # Update label
    if filename:
        background_image = Image.open(filename)
        print('Background selected:', filename)
        background_label.config(text=f"✓ {filename.split('/')[-1]}")

        # Enable apply button if both images are loaded
        if background_image and foreground_image:
            apply_button.config(state='normal')

def upload_foreground(event=None):
    """Upload foreground image"""    
    # Import global var
    global foreground_image
    filename = filedialog.askopenfilename(
        title="Select Watermark Image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )

    # Update label
    if filename:
        foreground_image = Image.open(filename)
        print('Watermark selected:', filename)
        foreground_label.config(text=f"✓ {filename.split('/')[-1]}")

        # Enable apply button if both images are loaded
        if background_image and foreground_image:
            apply_button.config(state='normal')

def apply_watermark():
    """Resize the watermark and overlay on background"""
    # Import global vars
    global background_image, foreground_image
    
    if background_image is None:
        print("Please upload a background image first!")
        return
    
    if foreground_image is None:
        print("Please upload a watermark image first!")
        return
    
    # Resize and create watermark imaage
    scale = 0.10
    new_width = int(background_image.width * scale)
    new_height = int(foreground_image.height * (new_width / foreground_image.width))
    resized_foreground = foreground_image.resize((new_width, new_height))

    # Convert to RGBA if it doesn't have alpha channel
    if resized_foreground.mode != 'RGBA':
        resized_foreground = resized_foreground.convert('RGBA')

    # Create a copy so we don't modify the original
    final_image = background_image.copy()

    # Convert background to RGBA too
    if final_image.mode != 'RGBA':
        final_image = final_image.convert('RGBA')

    # Place in bottom-right with 30px padding
    position = (
        final_image.width - resized_foreground.width - 30,
        final_image.height - resized_foreground.height - 30
    )

    # New final image with Watemark
    final_image.paste(resized_foreground, position, resized_foreground)
    final_image.show()

    # Save option
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
    )
    if save_path:
        final_image.save(save_path)
        print(f"Saved to: {save_path}")

# Config Tk
window = Tk()
window.title("Image Watermark Tool")
window.config(padx=20, pady=20)

# Background Image Button
background_button = Button(
    window, 
    text='Upload Background', 
    font=(FONT, FONT_SIZE),
    command=upload_background
)
background_button.pack(pady=5)

# Background Image Label
background_label = Label()
background_label.config(
    text="No Background Provided", 
    font=(FONT, FONT_SIZE)
)
background_label.pack()

# Foreground Image Button
foreground_button = Button(
    window, 
    text='Upload Watermark', 
    font=(FONT, FONT_SIZE),
    command=upload_foreground
)
foreground_button.pack(pady=5)

# Foreground Image Label
foreground_label = Label()
foreground_label.config(
    text="No Watermark Provided", 
    font=(FONT, FONT_SIZE)
)
foreground_label.pack()

# Apply Button
apply_button = Button(
    window, 
    text='Apply Watermark',
    font=(FONT, FONT_SIZE),
    command=apply_watermark,
    state='disabled'
)
apply_button.pack(pady=15)

# Centre and Maintain Window
centre_window(window)
window.mainloop()
