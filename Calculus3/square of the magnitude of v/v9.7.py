import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import messagebox

# Helper function to parse vector input
def parse_vector(entry):
    try:
        return np.array([float(x.strip()) for x in entry.get().split(',')])
    except:
        messagebox.showerror("Invalid input", "Please enter a valid vector (e.g., 1, 2, 3)")
        return None

# Function to visualize a single vector
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

# Operations
def dot_product():
    u = parse_vector(entry_u)
    v = parse_vector(entry_v)
    if u is not None and v is not None:
        result = np.dot(u, v)
        messagebox.showinfo("Dot Product", f"u · v = {result}")
        visualize_vector(u, "u vector")
        visualize_vector(v, "v vector")

def u_dot_u():
    u = parse_vector(entry_u)
    if u is not None:
        result = np.dot(u, u)
        messagebox.showinfo("u · u", f"u · u = {result}")
        visualize_vector(u, "u vector")

def norm_v_squared():
    v = parse_vector(entry_v)
    if v is not None:
        result = np.dot(v, v)
        messagebox.showinfo("||v||²", f"||v||² = {result}")
        visualize_vector(v, "v vector")

def scalar_mult_uv_v():
    u = parse_vector(entry_u)
    v = parse_vector(entry_v)
    if u is not None and v is not None:
        result = np.dot(u, v) * v
        visualize_vector(result, "(u · v)v")

def dot_u_3v():
    u = parse_vector(entry_u)
    v = parse_vector(entry_v)
    if u is not None and v is not None:
        result = np.dot(u, 3 * v)
        messagebox.showinfo("u · (3v)", f"u · (3v) = {result}")
        visualize_vector(3 * v, "3v vector")

def visualize_all():
    u = parse_vector(entry_u)
    v = parse_vector(entry_v)
    if u is not None and v is not None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        origin = [0, 0, 0]
        ax.quiver(*origin, *u, color='blue', label='u', arrow_length_ratio=0.1)
        ax.quiver(*origin, *v, color='green', label='v', arrow_length_ratio=0.1)
        ax.quiver(*origin, *(np.dot(u, v) * v), color='purple', label='(u·v)v', arrow_length_ratio=0.1)
        ax.quiver(*origin, *(3 * v), color='orange', label='3v', arrow_length_ratio=0.1)
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.set_zlim([-10, 10])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        ax.set_title("Vector Visualizations")
        plt.tight_layout()
        plt.show()

# --- NEW: External visualize all vectors ---
def visualize_all_external():
    u = parse_vector(entry_u)
    v = parse_vector(entry_v)
    if u is not None and v is not None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        origin = [0, 0, 0]
        ax.quiver(*origin, *u, color='blue', label='u', arrow_length_ratio=0.13, linewidth=2)
        ax.quiver(*origin, *v, color='green', label='v', arrow_length_ratio=0.13, linewidth=2)
        ax.quiver(*origin, *(np.dot(u, v) * v), color='purple', label='(u·v)v', arrow_length_ratio=0.13, linewidth=2)
        ax.quiver(*origin, *(3 * v), color='orange', label='3v', arrow_length_ratio=0.13, linewidth=2)
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.set_zlim([-10, 10])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        ax.set_title("All Vectors (external 3D window)")
        plt.tight_layout()
        plt.show()

# GUI setup
root = tk.Tk()
root.title("Vector Operations Visualizer")

tk.Label(root, text="Enter vector u (e.g. 2, -3, 4):").pack()
entry_u = tk.Entry(root)
entry_u.insert(0, "2, -3, 4")
entry_u.pack()

tk.Label(root, text="Enter vector v (e.g. 0, 6, 5):").pack()
entry_v = tk.Entry(root)
entry_v.insert(0, "0, 6, 5")
entry_v.pack()

tk.Button(root, text="Compute u · v", command=dot_product).pack(pady=2)
tk.Button(root, text="Compute u · u", command=u_dot_u).pack(pady=2)
tk.Button(root, text="Compute ||v||²", command=norm_v_squared).pack(pady=2)
tk.Button(root, text="Visualize (u · v)v", command=scalar_mult_uv_v).pack(pady=2)
tk.Button(root, text="Compute u · (3v)", command=dot_u_3v).pack(pady=2)
tk.Button(root, text="Visualize All Vectors", command=visualize_all).pack(pady=5)
# --- NEW BUTTON ---
tk.Button(root, text="Visualize All Vectors (external 3D window)", command=visualize_all_external, bg="#175bba", fg="white").pack(pady=7)

root.mainloop()
