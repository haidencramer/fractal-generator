import numpy as np
from PIL import Image
import matplotlib.cm as cm

def generate_julia(c, width=1920, height=1080, filename="static/latest_fractal.png", zoom=1.0):
    # Adjust coordinates based on zoom (smaller range = higher zoom)
    # Default range is -1.5 to 1.5. Zoom 2.0 makes it -0.75 to 0.75
    x_range = 1.5 / zoom
    y_range = 1.0 / zoom
    
    x = np.linspace(-x_range, x_range, width)
    y = np.linspace(-y_range, y_range, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    
    # Increase iterations for fine-detail filaments (spiciness level: high)
    max_iter = 256 
    counts = np.zeros(Z.shape, dtype=float)
    
    # Escape time with smooth coloring logic
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + c
        counts[mask] += 1
    
    # Logarithmic scaling makes the "fuzzier" edges look much sharper
    counts = np.log(counts + 1)
    color_mapped = cm.magma(counts / np.log(max_iter + 1))
    
    img_data = (color_mapped[:, :, :3] * 255).astype(np.uint8)
    Image.fromarray(img_data).save(filename)
    print(f"High-detail fractal saved (Zoom: {zoom}x)")