################################################
# Gave Claude App.py and it suggested this flair
################################################

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageEnhance

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

def calculate_position(bg_width, bg_height, fg_width, fg_height, position_choice, padding=30):
    """Calculate watermark position based on user selection"""
    positions = {
        "top-left": (padding, padding),
        "top-right": (bg_width - fg_width - padding, padding),
        "bottom-left": (padding, bg_height - fg_height - padding),
        "bottom-right": (bg_width - fg_width - padding, bg_height - fg_height - padding),
        "center": ((bg_width - fg_width) // 2, (bg_height - fg_height) // 2)
    }
    return positions.get(position_choice, positions["bottom-right"])

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
    
    # Get user settings
    scale = scale_var.get()
    opacity = opacity_var.get()
    position_choice = position_var.get()
    
    # Resize watermark based on scale
    new_width = int(background_image.width * scale)
    new_height = int(foreground_image.height * (new_width / foreground_image.width))
    resized_foreground = foreground_image.resize((new_width, new_height))

    # Convert to RGBA if it doesn't have alpha channel
    if resized_foreground.mode != 'RGBA':
        resized_foreground = resized_foreground.convert('RGBA')

    # Apply opacity
    alpha = resized_foreground.split()[3]  # Get alpha channel
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    resized_foreground.putalpha(alpha)

    # Create a copy so we don't modify the original
    final_image = background_image.copy()

    # Convert background to RGBA too
    if final_image.mode != 'RGBA':
        final_image = final_image.convert('RGBA')

    # Calculate position based on user selection
    position = calculate_position(
        final_image.width, 
        final_image.height,
        resized_foreground.width,
        resized_foreground.height,
        position_choice
    )

    # Apply watermark
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
window.title("Image Watermark Tool - Enhanced")
window.config(padx=20, pady=20)

# ===== BACKGROUND IMAGE SECTION =====
background_button = Button(
    window, 
    text='Upload Background', 
    font=(FONT, FONT_SIZE),
    command=upload_background
)
background_button.pack(pady=5)

background_label = Label()
background_label.config(
    text="No Background Provided", 
    font=(FONT, FONT_SIZE)
)
background_label.pack()

# ===== FOREGROUND IMAGE SECTION =====
foreground_button = Button(
    window, 
    text='Upload Watermark', 
    font=(FONT, FONT_SIZE),
    command=upload_foreground
)
foreground_button.pack(pady=5)

foreground_label = Label()
foreground_label.config(
    text="No Watermark Provided", 
    font=(FONT, FONT_SIZE)
)
foreground_label.pack()

# ===== SEPARATOR =====
separator1 = Frame(window, height=2, bd=1, relief=SUNKEN)
separator1.pack(fill=X, padx=5, pady=10)

# ===== WATERMARK SIZE CONTROL =====
size_label = Label(window, text="Watermark Size", font=(FONT, FONT_SIZE, "bold"))
size_label.pack(pady=(10, 5))

scale_var = DoubleVar(value=0.10)
scale_slider = Scale(
    window, 
    from_=0.05, 
    to=0.5, 
    resolution=0.05, 
    orient=HORIZONTAL,
    variable=scale_var,
    length=300,
    font=(FONT, FONT_SIZE)
)
scale_slider.pack()

scale_info = Label(window, text="(5% to 50% of background width)", font=(FONT, 8))
scale_info.pack()

# ===== OPACITY CONTROL =====
opacity_label = Label(window, text="Watermark Opacity", font=(FONT, FONT_SIZE, "bold"))
opacity_label.pack(pady=(10, 5))

opacity_var = DoubleVar(value=1.0)
opacity_slider = Scale(
    window,
    from_=0.1,
    to=1.0,
    resolution=0.1,
    orient=HORIZONTAL,
    variable=opacity_var,
    length=300,
    font=(FONT, FONT_SIZE)
)
opacity_slider.pack()

opacity_info = Label(window, text="(0.1 = very transparent, 1.0 = solid)", font=(FONT, 8))
opacity_info.pack()

# ===== POSITION CONTROL =====
position_label = Label(window, text="Watermark Position", font=(FONT, FONT_SIZE, "bold"))
position_label.pack(pady=(10, 5))

position_var = StringVar(value="bottom-right")
positions = [
    ("Top Left", "top-left"), 
    ("Top Right", "top-right"),
    ("Center", "center"),
    ("Bottom Left", "bottom-left"), 
    ("Bottom Right", "bottom-right")
]

position_frame = Frame(window)
position_frame.pack()

for text, value in positions:
    rb = Radiobutton(
        position_frame, 
        text=text, 
        variable=position_var, 
        value=value,
        font=(FONT, FONT_SIZE)
    )
    rb.pack(anchor=W)

# ===== SEPARATOR =====
separator2 = Frame(window, height=2, bd=1, relief=SUNKEN)
separator2.pack(fill=X, padx=5, pady=10)

# ===== APPLY BUTTON =====
apply_button = Button(
    window, 
    text='Apply Watermark',
    font=(FONT, FONT_SIZE + 2, "bold"),
    command=apply_watermark,
    state='disabled',
    bg='#4CAF50',
    fg='white',
    padx=20,
    pady=10
)
apply_button.pack(pady=15)

# Centre and Maintain Window
centre_window(window)
window.mainloop()