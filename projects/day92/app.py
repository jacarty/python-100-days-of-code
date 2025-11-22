from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from PIL import Image
import base64
from io import BytesIO

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def image_analysis(image, num_colors, delta):
    img = image
    top_colors = num_colors
    sensitivity = delta

    # Quantise image
    img_palette = img.convert('P', palette=Image.ADAPTIVE, colors=sensitivity)

    # Create palette for comparison and conver to tuple
    palette = img_palette.getpalette()
    colors = [tuple(palette[i:i+3]) for i in range(0, sensitivity*3, 3)]

    # Conver image to numpy array and count how many pixels use each palette index
    pixel_data = np.array(img_palette)
    unique, counts = np.unique(pixel_data, return_counts=True)

    # Sort by frequency and create list by frequency
    sorted_indices = np.argsort(-counts)
    most_frequent = [(colors[unique[i]], counts[i]) for i in sorted_indices]
    
    # Calculate total pixels for percentage calculations
    total_pixels = pixel_data.size

    # Return JSON for page
    result = {
        'colors': [
            {
                'rgb': [int(color[0]), int(color[1]), int(color[2])],
                'count': int(count),
                'percentage': round((float(count) / total_pixels) * 100, 2),
                'hex': f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            }
            for color, count in most_frequent[:top_colors]
        ]
    }
    
    return result

#######################################
# Home Page
#######################################
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if image file is present
        if 'image' not in request.files:
            return render_template("index.html", error="No image file uploaded")
        
        file = request.files['image']
        
        if file.filename == '':
            return render_template("index.html", error="No image selected")
        
        # Get form parameters
        num_colors = int(request.form.get('num_colors', 10))
        delta = int(request.form.get('delta', 24))
        
        # Validate parameters
        num_colors = max(2, min(20, num_colors))
        delta = max(1, min(255, delta))
        
        try:
            # Open and process image
            image = Image.open(file.stream)
            
            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Convert image to base64 for preview/display
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            image_data = f"data:image/png;base64,{img_str}"
            
            # Run analysis
            results = image_analysis(image, num_colors, delta)
            
            # Pass data directly to results template
            return render_template("results.html", 
                                 results=results, 
                                 image_data=image_data,
                                 num_colors=num_colors,
                                 delta=delta)
        
        except Exception as e:
            return render_template("index.html", error=f"Error processing image: {str(e)}")
    
    return render_template("index.html")

#######################################
# Init App
#######################################
if __name__ == '__main__':
    app.run(debug=True)