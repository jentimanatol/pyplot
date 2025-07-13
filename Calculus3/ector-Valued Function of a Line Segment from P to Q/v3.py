import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from mpl_toolkits.mplot3d import Axes3D


def parse_point(entry_text):
    try:
        x, y, z = map(float, entry_text.strip().split())
        return np.array([x, y, z])
    except ValueError:
        raise ValueError("Please enter three space-separated numbers.")


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


def on_draw():
    try:
        P = parse_point(entry_P.get())
        Q = parse_point(entry_Q.get())
        plot_line_segment(P, Q)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))


# GUI Window
root = tk.Tk()
root.title("3D Line Segment Visualizer")

tk.Label(root, text="Enter Point P (x y z):").grid(row=0, column=0, padx=5, pady=5)
entry_P = tk.Entry(root, width=30)
entry_P.grid(row=0, column=1, padx=5, pady=5)
entry_P.insert(0, "-5 -5 -3")  # Default

tk.Label(root, text="Enter Point Q (x y z):").grid(row=1, column=0, padx=5, pady=5)
entry_Q = tk.Entry(root, width=30)
entry_Q.grid(row=1, column=1, padx=5, pady=5)
entry_Q.insert(0, "-2 -4 -7")  # Default

btn_draw = tk.Button(root, text="Draw Line", command=on_draw)
btn_draw.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
