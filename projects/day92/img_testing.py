import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('./static/images/default.png')
# num_colors = request.form.get('sensitivity', default=10, type=int)
palette_colors = 20
top_colors = 5

# Quantize to palette
img_palette = img.convert('P', palette=Image.ADAPTIVE, colors=palette_colors)

# Show the original and quantised side-by-side
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
# ax1.imshow(img)
# ax1.set_title('Original')
# ax1.axis('off')
# ax2.imshow(img_palette)
# ax2.set_title(f'Quantized ({palette_colors} colors)')
# ax2.axis('off')
# plt.tight_layout()
# plt.show()

# Get the palette colors new image (as a flat list) & create a LIST of tuples
palette = img_palette.getpalette()
colors = [tuple(palette[i:i+3]) for i in range(0, palette_colors*3, 3)]

# Convert quantised image into numpy array & count the indices
pixel_data = np.array(img_palette)
unique, counts = np.unique(pixel_data, return_counts=True) # tuple unpacking

# Sort by frequency
sorted_indices = np.argsort(-counts)  # negative for descending
most_frequent = [(colors[unique[i]], counts[i]) for i in sorted_indices]

# print("Most frequent colors:")
# for color, count in most_frequent[:top_colors]:  # return top_colours
#     print(f"RGB{color}: {count} pixels")

# Return RBG and HEX values
result = {
    'colors': [
        {'rgb': color, 'count': count, 
         'hex': f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'}
        for color, count in most_frequent[:top_colors]
    ]
}