import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    image = np.empty((height, width))
    
    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            image[i, j] = mandelbrot(c, max_iter)
    
    return image

# Settings
width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 100

mandelbrot_image = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_image, extent=[x_min, x_max, y_min, y_max], cmap='twilight_shifted')
plt.colorbar(label='Iteration count')
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
