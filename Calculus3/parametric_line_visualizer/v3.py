import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import messagebox

def visualize_line():
    try:
        # Get user input
        x0 = float(entry_x.get())
        y0 = float(entry_y.get())
        z0 = float(entry_z.get())
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "❌ Please enter valid numbers in all fields.")
        return

    # Define parametric line
    t = np.linspace(-10, 10, 100)
    x = x0 + a * t
    y = y0 + b * t
    z = z0 + c * t

    # Compute another point on the line (t = 1)
    x1, y1, z1 = x0 + a, y0 + b, z0 + c

    # Plotting
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='Parametric Line', color='blue')
    ax.scatter([x0], [y0], [z0], color='red', s=100, label='Given Point (P)')
    ax.scatter([x1], [y1], [z1], color='green', s=100, label='Another Point (t=1)')
    ax.quiver(x0, y0, z0, a, b, c, length=3, color='purple', arrow_length_ratio=0.1, label='Direction Vector')

    # Labeling
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('📈 3D Parametric Line Visualizer')
    ax.legend()
    plt.tight_layout()
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("🎓 Parametric Line Visualizer")

# Instruction Text
instruction = (
    "📚 This interactive tool helps you visualize a parametric line in 3D space.\n"
    "🟢 Enter a point that the line passes through (x₀, y₀, z₀), and a direction vector (a, b, c).\n"
    "The app will plot the line, mark key points, and show the direction.\n\n"
    "🎯 Use this to better understand parametric equations in Calculus III."
)
tk.Label(root, text=instruction, justify="left", wraplength=500, fg="darkblue").grid(row=0, column=0, columnspan=4, pady=10)

# Input Labels
tk.Label(root, text="🔺 Point on the Line (x₀, y₀, z₀):").grid(row=1, column=0, sticky="w")
entry_x = tk.Entry(root, width=7); entry_x.grid(row=1, column=1)
entry_y = tk.Entry(root, width=7); entry_y.grid(row=1, column=2)
entry_z = tk.Entry(root, width=7); entry_z.grid(row=1, column=3)

tk.Label(root, text="➡️ Direction Vector (a, b, c):").grid(row=2, column=0, sticky="w")
entry_a = tk.Entry(root, width=7); entry_a.grid(row=2, column=1)
entry_b = tk.Entry(root, width=7); entry_b.grid(row=2, column=2)
entry_c = tk.Entry(root, width=7); entry_c.grid(row=2, column=3)

# Visualize Button
tk.Button(root, text="🎨 Visualize Line", command=visualize_line, bg="lightgreen", fg="black").grid(row=3, column=0, columnspan=4, pady=15)

# Footer
tk.Label(root, text="Created for Calculus 3 Students by Your Friendly Python Visualizer 🐍", fg="gray").grid(row=4, column=0, columnspan=4, pady=10)

# Run the App
root.mainloop()
