import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Circle equation: (x - h)^2 + (y - k)^2 = r^2
h, k, r = 3, 10, np.sqrt(65)

# Default points
points = [(-1, 3), (-4, 6), (2, 2)]

# --- Plotting Function ---
def plot_circle():
    fig, ax = plt.subplots(figsize=(6,6))
    
    # Circle points
    theta = np.linspace(0, 2*np.pi, 400)
    x_vals = h + r * np.cos(theta)
    y_vals = k + r * np.sin(theta)
    
    # Plot circle
    ax.plot(x_vals, y_vals, 'r-', label=f"Circle: (x-{h})² + (y-{k})² = {r**2:.0f}")
    
    # Plot points
    for (x, y) in points:
        ax.scatter(x, y, color="blue", s=80)
        ax.text(x+0.2, y, f"({x},{y})", fontsize=9, color="blue")
    
    # Axes
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Circle through default points")
    ax.legend()
    
    return fig

# --- GUI Functions ---
def add_point():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        points.append((x, y))
        redraw()
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for x and y.")

def redraw():
    fig = plot_circle()
    canvas.figure = fig
    canvas.draw()

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Circle Plotter")

# Input fields
frame = tk.Frame(root)
frame.pack(side=tk.TOP, pady=10)

tk.Label(frame, text="x:").grid(row=0, column=0)
entry_x = tk.Entry(frame, width=8)
entry_x.grid(row=0, column=1)

tk.Label(frame, text="y:").grid(row=0, column=2)
entry_y = tk.Entry(frame, width=8)
entry_y.grid(row=0, column=3)

btn_add = tk.Button(frame, text="Add Point", command=add_point)
btn_add.grid(row=0, column=4, padx=10)

# Matplotlib plot in Tkinter
fig = plot_circle()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Run GUI
root.mainloop()
