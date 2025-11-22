"""
Better way of doing the colours
"""

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from PIL import Image
import base64
from io import BytesIO

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def image_analysis(image, num_colors, delta):
    """
    Two-stage color extraction:
    1. Initial quantization to reduce color space
    2. Merge similar colors from quantized palette
    """
    img = image
    
    # Stage 1: Quantize to reduce color space (more colors than needed)
    # Use 3-4x the target colors for initial reduction
    initial_colors = num_colors * 4
    img_palette = img.convert('P', palette=Image.ADAPTIVE, colors=initial_colors)
    
    palette = img_palette.getpalette()
    colors = [tuple(palette[i:i+3]) for i in range(0, initial_colors*3, 3)]
    
    pixel_data = np.array(img_palette)
    unique, counts = np.unique(pixel_data, return_counts=True)
    
    # Get color frequencies
    color_counts = [(colors[unique[i]], counts[i]) for i in range(len(unique))]
    
    # Stage 2: Merge similar colors
    merged = []
    used = set()
    
    # Sort by frequency first (most common colors first)
    color_counts.sort(key=lambda x: x[1], reverse=True)
    
    for i, (color1, count1) in enumerate(color_counts):
        if i in used:
            continue
        
        # Start cluster
        cluster_count = count1
        cluster_colors = [color1]
        used.add(i)
        
        # Find similar colors to merge
        for j, (color2, count2) in enumerate(color_counts):
            if j in used:
                continue
            
            # Calculate RGB distance
            distance = np.sqrt(sum((c1 - c2)**2 for c1, c2 in zip(color1, color2)))
            
            if distance <= delta:
                cluster_colors.append(color2)
                cluster_count += count2
                used.add(j)
        
        # Use average color for cluster
        avg_color = tuple(int(np.mean([c[i] for c in cluster_colors])) 
                         for i in range(3))
        merged.append((avg_color, cluster_count))
    
    # Sort merged colors by frequency
    merged.sort(key=lambda x: x[1], reverse=True)
    
    # Take top N
    top_colors_data = merged[:num_colors]
    
    total_pixels = pixel_data.size
    
    result = {
        'colors': [
            {
                'rgb': [int(color[0]), int(color[1]), int(color[2])],
                'count': int(count),
                'percentage': round((float(count) / total_pixels) * 100, 2),
                'hex': f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            }
            for color, count in top_colors_data
        ]
    }
    
    return result
