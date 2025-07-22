import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to plot the points
def plot_points():
    try:
        x1, y1, z1 = float(entry_x1.get()), float(entry_y1.get()), float(entry_z1.get())
        x2, y2, z2 = float(entry_x2.get()), float(entry_y2.get()), float(entry_z2.get())
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        return

    ax.clear()

    # Plot points and vertical lines
    ax.scatter(x1, y1, z1, label=f"A ({x1}, {y1}, {z1})", color='blue')
    ax.scatter(x2, y2, z2, label=f"B ({x2}, {y2}, {z2})", color='red')

    ax.plot([x1, x1], [y1, y1], [0, z1], linestyle='dashed', color='gray')
    ax.plot([x2, x2], [y2, y2], [0, z2], linestyle='dashed', color='gray')

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(0, 10)

    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("3D Coordinate Plot")
    ax.legend()

    ax.grid(False)  # <- No grid

    canvas.draw()
    result_label.config(text="Plot updated successfully.")

# GUI Setup
root = tk.Tk()
root.title("3D Point Plotter")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

# Point A input
ttk.Label(frame, text="Point A (x, y, z):").grid(row=0, column=0, columnspan=3)
entry_x1 = ttk.Entry(frame, width=5)
entry_y1 = ttk.Entry(frame, width=5)
entry_z1 = ttk.Entry(frame, width=5)
entry_x1.insert(0, "7")
entry_y1.insert(0, "5")
entry_z1.insert(0, "3")
entry_x1.grid(row=1, column=0)
entry_y1.grid(row=1, column=1)
entry_z1.grid(row=1, column=2)

# Point B input
ttk.Label(frame, text="Point B (x, y, z):").grid(row=2, column=0, columnspan=3)
entry_x2 = ttk.Entry(frame, width=5)
entry_y2 = ttk.Entry(frame, width=5)
entry_z2 = ttk.Entry(frame, width=5)
entry_x2.insert(0, "-3")
entry_y2.insert(0, "1")
entry_z2.insert(0, "2")
entry_x2.grid(row=3, column=0)
entry_y2.grid(row=3, column=1)
entry_z2.grid(row=3, column=2)

# Plot Button
ttk.Button(frame, text="Plot Points", command=plot_points).grid(row=4, column=0, columnspan=3, pady=10)

# Result Message
result_label = ttk.Label(frame, text="")
result_label.grid(row=5, column=0, columnspan=3)

# Matplotlib Setup
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d')
ax.grid(False)  # no grid at start

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=1, padx=10)

root.mainloop()
