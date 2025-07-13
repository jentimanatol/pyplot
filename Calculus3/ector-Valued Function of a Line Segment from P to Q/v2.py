# line_segment_visualizer.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_point_input(prompt):
    try:
        raw = input(f"{prompt} (format: x y z): ")
        x, y, z = map(float, raw.strip().split())
        return np.array([x, y, z])
    except ValueError:
        print("❌ Invalid input. Please enter 3 space-separated numbers.")
        exit()

def plot_line_segment(P, Q):
    t = np.linspace(0, 1, 100)
    r_t = P.reshape(3, 1) + (Q - P).reshape(3, 1) * t
    x, y, z = r_t[0], r_t[1], r_t[2]

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='Line Segment', color='blue')
    ax.scatter(*P, color='red', s=100, label='Point P (t=0)')
    ax.scatter(*Q, color='green', s=100, label='Point Q (t=1)')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Line Segment Visualizer')
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("📐 3D Line Segment Visualizer")
    P = get_point_input("Enter Point P")
    Q = get_point_input("Enter Point Q")
    plot_line_segment(P, Q)
