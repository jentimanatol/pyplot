import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import messagebox

def print_data():
    try:
        x0 = float(entry_x.get())
        y0 = float(entry_y.get())
        z0 = float(entry_z.get())
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        t_val = float(entry_t.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "❌ Please enter valid numbers.")
        return

    x1, y1, z1 = x0 + a * t_val, y0 + b * t_val, z0 + c * t_val

    info = (
        f"📌 Given Point P = ({x0}, {y0}, {z0})\n"
        f"➡️ Direction Vector u = <{a}, {b}, {c}>\n"
        f"🟢 Point on Line (t = {t_val}): ({x1}, {y1}, {z1})\n"
        f"🧮 Parametric Equations:\n"
        f"  x(t) = {x0} + {a}t\n"
        f"  y(t) = {y0} + {b}t\n"
        f"  z(t) = {z0} + {c}t"
    )

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, info)

def visualize_line():
    try:
        x0 = float(entry_x.get())
        y0 = float(entry_y.get())
        z0 = float(entry_z.get())
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        t_val = float(entry_t.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "❌ Please enter valid numbers.")
        return

    t = np.linspace(-10, 10, 100)
    x = x0 + a * t
    y = y0 + b * t
    z = z0 + c * t

    x1, y1, z1 = x0 + a * t_val, y0 + b * t_val, z0 + c * t_val

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='🟦 Parametric Line', color='blue')
    ax.scatter([x0], [y0], [z0], color='red', s=100, label=f'🔴 Point P ({x0}, {y0}, {z0})')
    ax.scatter([x1], [y1], [z1], color='green', s=100, label=f'🟢 Point (t={t_val}) ({x1}, {y1}, {z1})')
    ax.quiver(x0, y0, z0, a, b, c, length=3, color='purple', arrow_length_ratio=0.1,
              label=f'🟣 Direction Vector <{a}, {b}, {c}>')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('📈 3D Parametric Line Visualization')
    ax.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

# GUI
root = tk.Tk()
root.title("🎓 Parametric Line Visualizer")

description = (
    "📚 Visualize a parametric line in 3D space.\n"
    "🔺 Default point: P = (2, 8, 5)\n"
    "➡️ Default vector: u = ⟨-3, 4, -1⟩\n"
    "⌨️ Enter any value of t (default = 1)\n"
    "📄 'Print Data' shows parametric equations below\n"
    "🎨 'Visualize Line' displays 3D plot"
)
tk.Label(root, text=description, wraplength=500, justify='left', fg='darkblue').grid(row=0, column=0, columnspan=4, pady=10)

# Inputs
tk.Label(root, text="🔺 Point (x₀, y₀, z₀):").grid(row=1, column=0, sticky="w")
entry_x = tk.Entry(root, width=7); entry_x.grid(row=1, column=1); entry_x.insert(0, "2")
entry_y = tk.Entry(root, width=7); entry_y.grid(row=1, column=2); entry_y.insert(0, "8")
entry_z = tk.Entry(root, width=7); entry_z.grid(row=1, column=3); entry_z.insert(0, "5")

tk.Label(root, text="➡️ Vector (a, b, c):").grid(row=2, column=0, sticky="w")
entry_a = tk.Entry(root, width=7); entry_a.grid(row=2, column=1); entry_a.insert(0, "-3")
entry_b = tk.Entry(root, width=7); entry_b.grid(row=2, column=2); entry_b.insert(0, "4")
entry_c = tk.Entry(root, width=7); entry_c.grid(row=2, column=3); entry_c.insert(0, "-1")

tk.Label(root, text="🔢 Value of t:").grid(row=3, column=0, sticky="w")
entry_t = tk.Entry(root, width=7); entry_t.grid(row=3, column=1); entry_t.insert(0, "1")

# Buttons
tk.Button(root, text="📄 Print Data", command=print_data, bg="lightyellow").grid(row=3, column=2)
tk.Button(root, text="🎨 Visualize Line", command=visualize_line, bg="lightgreen").grid(row=3, column=3)

# Output
tk.Label(root, text="🖨️ Parametric Equation Info:").grid(row=4, column=0, columnspan=4, sticky="w", padx=5)
output_text = tk.Text(root, height=8, width=65, wrap="word", borderwidth=2, relief="sunken")
output_text.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

# Footer
tk.Label(root, text="🧮 Calculus 3 Visualizer | Powered by Python & Matplotlib", fg="gray").grid(row=6, column=0, columnspan=4, pady=10)

root.mainloop()
