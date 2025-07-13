import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_user_input():
    print("🎯 3D Parametric Line Visualizer")
    print("--------------------------------")
    try:
        point_input = input("Enter the point (x y z): ").strip()
        vector_input = input("Enter the direction vector (a b c): ").strip()
        x0, y0, z0 = map(float, point_input.split())
        a, b, c = map(float, vector_input.split())
        return (x0, y0, z0), (a, b, c)
    except ValueError:
        print("❌ Invalid input format. Use space-separated numbers like: 2 8 5")
        exit()

def plot_parametric_line(point, direction):
    x0, y0, z0 = point
    a, b, c = direction

    # Parameter t for the line
    t = np.linspace(-10, 10, 100)
    x = x0 + a * t
    y = y0 + b * t
    z = z0 + c * t

    # Another point when t = 1
    x1, y1, z1 = x0 + a, y0 + b, z0 + c

    # Create 3D plot
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(x, y, z, label='Parametric Line', color='blue')
    ax.scatter([x0], [y0], [z0], color='red', s=100, label='Given Point (P)')
    ax.scatter([x1], [y1], [z1], color='green', s=100, label='Another Point (t=1)')
    ax.quiver(x0, y0, z0, a, b, c, length=3, color='purple', arrow_length_ratio=0.1, label='Direction Vector')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('🧭 3D Parametric Line Visualization')
    ax.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    point, direction = get_user_input()
    plot_parametric_line(point, direction)
