import matplotlib.pyplot as plt
import numpy as np
import os

def koch_snowflake(order, scale=10):
    def koch_curve(p1, p2, order):
        if order == 0:
            return [p1, p2]
        else:
            p1 = np.array(p1)
            p2 = np.array(p2)
            delta = p2 - p1
            p3 = p1 + delta / 3
            p5 = p1 + delta * 2 / 3
            angle = np.pi / 3
            rotation = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
            p4 = p3 + rotation.dot(p5 - p3)
            return (koch_curve(p1, p3, order - 1) +
                    koch_curve(p3, p4, order - 1)[1:] +
                    koch_curve(p4, p5, order - 1)[1:] +
                    koch_curve(p5, p2, order - 1)[1:])

    height = np.sqrt(3) / 2 * scale
    p1 = [0, 0]
    p2 = [scale, 0]
    p3 = [scale / 2, height]

    side1 = koch_curve(p1, p2, order)
    side2 = koch_curve(p2, p3, order)
    side3 = koch_curve(p3, p1, order)

    return side1 + side2[1:] + side3[1:]

def plot_koch(order, output_path):
    points = koch_snowflake(order)
    x, y = zip(*points)
    plt.figure(figsize=(8, 8))
    plt.plot(x, y)
    plt.title(f'Koch Snowflake (Order {order})')
    plt.axis('equal')
    plt.axis('off')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()

# Save the output to a file
print("Generating Koch snowflake...")
plot_koch(order=4, output_path='output/fractal.png')
print("✅ Fractal image saved to output/fractal.png")
print("✅ Done.")

