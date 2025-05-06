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
root.geometry("2400x1200")

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

Numerator = {numerator}
Denominator = {denominator:.4f}
r = {r:.4f}


formula used:
r = (n * Σxy - Σx * Σy) / sqrt([n * Σx² - (Σx)²] * [n * Σy² - (Σy)²])

where:
n = number of data points
Σx = sum of x values
Σy = sum of y values
Σx² = sum of x² values
Σy² = sum of y² values
Σxy = sum of x*y values

sqrt = square root

# r = linear correlation coefficient
# r = 1 indicates a perfect positive linear relationship
# r = -1 indicates a perfect negative linear relationship
# r = 0 indicates no linear relationship
# r = 0.8 indicates a strong positive linear relationship
# r = -0.8 indicates a strong negative linear relationship
# r = 0.5 indicates a moderate positive linear relationship
# r = -0.5 indicates a moderate negative linear relationship
# r = 0.2 indicates a weak positive linear relationship
# r = -0.2 indicates a weak negative linear relationship
# r = 0 indicates no linear relationship
# r = 0.1 indicates a very weak positive linear relationship
# r = -0.1 indicates a very weak negative linear relationship
# r = 0.3 indicates a weak positive linear relationship
# r = -0.3 indicates a weak negative linear relationship
# r = 0.4 indicates a moderate positive linear relationship
# r = -0.4 indicates a moderate negative linear relationship
# r = 0.6 indicates a strong positive linear relationship
# r = -0.6 indicates a strong negative linear relationship
# r = 0.7 indicates a strong positive linear relationship
# r = -0.7 indicates a strong negative linear relationship
# r = 0.9 indicates a very strong positive linear relationship
# r = -0.9 indicates a very strong negative linear relationship
# r = 0.95 indicates a very strong positive linear relationship
# r = -0.95 indicates a very strong negative linear relationship
# r = 0.99 indicates a very strong positive linear relationship
# r = -0.99 indicates a very strong negative linear relationship
# r = 0.999 indicates a very strong positive linear relationship
# r = -0.999 indicates a very strong negative linear relationship



"""

summary_label = tk.Label(
    right_panel,
    text=summary_text,
    bg="#f0f6ff",
    justify="left",
    font=("Courier", 20)
)
summary_label.pack(pady=(0, 10), padx=5, anchor="w")

root.mainloop()
