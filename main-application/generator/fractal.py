import numpy as np
from PIL import Image
import matplotlib.cm as cm

def generate_julia(c, width=1920, height=1080, filename="static/latest_fractal.png", zoom=1.0):
    # 1. Force integer types to prevent the 'str' TypeError
    width = int(width)   
    height = int(height)
    
    # 2. Set up coordinate space
    x_range = 1.5 / zoom
    y_range = (1.5 * height / width) / zoom  # Maintains aspect ratio
    
    x = np.linspace(-x_range, x_range, width)
    y = np.linspace(-y_range, y_range, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    
    max_iter = 256 
    counts = np.zeros(Z.shape, dtype=float)
    
    # 3. Optimized iteration loop
    # Uses a context manager to ignore the 'overflow' warnings from Z**2
    with np.errstate(over='ignore', invalid='ignore'):
        for i in range(max_iter):
            mask = np.abs(Z) <= 2
            Z[mask] = Z[mask]**2 + c
            counts[mask] += 1
    
    # 4. Coloring Logic
    counts = np.log(counts + 1)
    normalized_counts = counts / np.log(max_iter + 1)
    color_mapped = cm.magma(normalized_counts)
    
    # 5. Convert to RGB and save
    img_data = (color_mapped[:, :, :3] * 255).astype(np.uint8)
    Image.fromarray(img_data).save(filename)
    print(f"Success: High-detail fractal saved to {filename}")