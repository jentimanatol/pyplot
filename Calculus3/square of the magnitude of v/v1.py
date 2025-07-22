import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import messagebox

# Default vectors
u = np.array([2, -3, 4])
v = np.array([0, 6, 5])

# Functions for vector operations
def dot_product():
    result = np.dot(u, v)
    messagebox.showinfo("Dot Product", f"u · v = {result}")

def u_dot_u():
    result = np.dot(u, u)
    messagebox.showinfo("u · u", f"u · u = {result}")

def norm_v_squared():
    result = np.dot(v, v)
    messagebox.showinfo("||v||²", f"||v||² = {result}")

def scalar_mult_uv_v():
    scalar = np.dot(u, v)
    result = scalar * v
    visualize_vector(result, title="(u · v)v")

def dot_u_3v():
    result = np.dot(u, 3 * v)
    messagebox.showinfo("u · (3v)", f"u · (3v) = {result}")

# 3D visualization function
def visualize_vector(vector, title="Vector"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='blue', arrow_length_ratio=0.1)
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    plt.tight_layout()
    plt.show()

# GUI setup
root = tk.Tk()
root.title("Vector Operations Visualizer")

tk.Label(root, text="Default Vectors:").pack()
tk.Label(root, text=f"u = {u}").pack()
tk.Label(root, text=f"v = {v}").pack()

tk.Button(root, text="Compute u · v", command=dot_product).pack(pady=2)
tk.Button(root, text="Compute u · u", command=u_dot_u).pack(pady=2)
tk.Button(root, text="Compute ||v||²", command=norm_v_squared).pack(pady=2)
tk.Button(root, text="Visualize (u · v)v", command=scalar_mult_uv_v).pack(pady=2)
tk.Button(root, text="Compute u · (3v)", command=dot_u_3v).pack(pady=2)

root.mainloop()
