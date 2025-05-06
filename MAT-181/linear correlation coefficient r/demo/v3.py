# Update: Adding formulas used for correlation calculation in the right_panel

import tkinter as tk
from tkinter import messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Data
data = [
    (5, 64),
    (10, 86),
    (4, 69),
    (6, 86),
    (10, 59),
    (9, 87)
]

# Compute necessary columns
x_vals = [row[0] for row in data]
y_vals = [row[1] for row in data]
x2_vals = [x**2 for x in x_vals]
y2_vals = [y**2 for y in y_vals]
xy_vals = [x*y for x, y in zip(x_vals, y_vals)]

# Sums
n = len(data)
sum_x = sum(x_vals)
sum_y = sum(y_vals)
sum_x2 = sum(x2_vals)
sum_y2 = sum(y2_vals)
sum_xy = sum(xy_vals)

# Compute r
numerator = n * sum_xy - sum_x * sum_y
denominator = np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
r = numerator / denominator

# Tkinter GUI
root = tk.Tk()
root.title("Linear Correlation Coefficient Visualizer")
root.geometry("2400x1350")

# Layout
top_frame = tk.Frame(root, bg="#e6f0ff", padx=10, pady=5)
top_frame.pack(fill=tk.X)

tk.Label(top_frame, text="Linear Correlation Coefficient (r)", bg="#e6f0ff", font=("Arial", 28, "bold")).pack(side=tk.LEFT)

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

left_panel = tk.Frame(main_frame)
left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Matplotlib figure
fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(x_vals, y_vals, color='blue', s=100)
ax.set_title("Scatter Plot: Hours Studied vs Test Scores", fontsize=22)
ax.set_xlabel("Hours Studied", fontsize=18)
ax.set_ylabel("Test Score", fontsize=18)
ax.grid(True)

canvas = FigureCanvasTkAgg(fig, master=left_panel)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

right_panel = tk.Frame(main_frame, bg="#f0f6ff", width=820, padx=30)
right_panel.pack(side=tk.RIGHT, fill=tk.Y)
right_panel.pack_propagate(0)

tk.Label(
    right_panel,
    text="📊 Data and Calculations",
    font=("Helvetica", 28, "bold"),
    bg="#f0f6ff",
    fg="#003366"
).pack(pady=(5, 2))

table_text = "x\t y\t x²\t y²\t xy\n"
for x, y, x2, y2, xy in zip(x_vals, y_vals, x2_vals, y2_vals, xy_vals):
    table_text += f"{x}\t {y}\t {x2}\t {y2}\t {xy}\n"

table_label = tk.Label(
    right_panel,
    text=table_text,
    bg="#f0f6ff",
    justify="left",
    font=("Courier", 20)
)
table_label.pack(pady=(0, 10), padx=5, anchor="w")

summary_text = f"""
Σx = {sum_x}
Σy = {sum_y}
Σx² = {sum_x2}
Σy² = {sum_y2}
Σxy = {sum_xy}
n = {n}

Numerator = n * Σxy - Σx * Σy = {numerator}
Denominator = sqrt([n * Σx² - (Σx)²] *
* [n * Σy² - (Σy)²]) = {denominator:.4f}

r = {r:.4f}
"""

summary_label = tk.Label(
    right_panel,
    text=summary_text,
    bg="#f0f6ff",
    justify="left",
    font=("Courier", 20)
)
summary_label.pack(pady=(0, 10), padx=5, anchor="w")

# Formulas block
tk.Label(
    right_panel,
    text="📐 Formulas Used",
    font=("Helvetica", 26, "bold"),
    bg="#f0f6ff",
    fg="#003366"
).pack(pady=(5, 2))

formulas_label = tk.Label(
    right_panel,
    text=(
        "r = [nΣxy - (Σx)(Σy)] / \n "
        "/sqrt{[nΣx² - (Σx)²][nΣy² - (Σy)²]}\n\n"
        "Where:\n"
        "Σxy = sum of x*y products\n"
        "Σx² = sum of x squared\n"
        "Σy² = sum of y squared\n"
        "n = number of data pairs"
    ),
    bg="#f0f6ff",
    justify="left",
    font=("Courier", 20),
    fg="#2c3e50"
)
formulas_label.pack(pady=(0, 8), padx=5, anchor="w")

root.mainloop()
