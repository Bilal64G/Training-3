import numpy as np
import matplotlib.pyplot as plt
import os

def mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    C = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    Z = np.zeros_like(C, dtype=np.complex128)
    img = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] ** 2 + C[mask]
        img[mask] = i

    return img

def plot_mandelbrot(output_path):
    width, height = 800, 800
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    max_iter = 100

    print("Generating Mandelbrot set...")
    img = mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.figure(figsize=(8, 8))
    plt.imshow(img, extent=[x_min, x_max, y_min, y_max], cmap='inferno')
    plt.axis('off')
    plt.title("Mandelbrot Set")
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()
    print(f"Saved Mandelbrot image to {output_path}")

# Save the Mandelbrot image
plot_mandelbrot('output/fractal.png')
