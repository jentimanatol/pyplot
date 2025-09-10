import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------- geometry helpers ----------
def circle_from_three_points(p1, p2, p3, eps=1e-10):
    """Return (h, k, r2) for the unique circle through three non-collinear points."""
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3

    # Check collinearity (area * 2)
    det = x1*(y2 - y3) - y1*(x2 - x3) + (x2*y3 - x3*y2)
    if abs(det) < eps:
        raise ValueError("Points are (almost) collinear; unique circle does not exist.")

    # Solve linear system for center (h, k)
    a = 2*(x2 - x1)
    b = 2*(y2 - y1)
    c = x2**2 + y2**2 - x1**2 - y1**2

    d = 2*(x3 - x1)
    e = 2*(y3 - y1)
    f = x3**2 + y3**2 - x1**2 - y1**2

    denom = a*e - b*d
    if abs(denom) < eps:
        raise ValueError("Numerical issue; points nearly collinear.")

    h = (c*e - b*f) / denom
    k = (a*f - c*d) / denom
    r2 = (x1 - h)**2 + (y1 - k)**2
    return h, k, r2

# ---------- plotting ----------
def make_figure(points, circle_params=None):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Draw circle if available
    if circle_params is not None:
        h, k, r2 = circle_params
        r = np.sqrt(max(r2, 0))
        t = np.linspace(0, 2*np.pi, 400)
        ax.plot(h + r*np.cos(t), k + r*np.sin(t))
        ax.set_title(f"Circle: (x-{h:.2f})² + (y-{k:.2f})² = {r2:.2f}")
    else:
        ax.set_title("Add points (3 needed to define a circle)")

    # Draw points
    if points:
        xs, ys = zip(*points)
        ax.scatter(xs, ys, s=80)
        for (x, y) in points:
            ax.text(x + 0.15, y, f"({x:g},{y:g})", fontsize=9)

    ax.axhline(0, color="black", lw=1)
    ax.axvline(0, color="black", lw=1)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    return fig

# ---------- GUI ----------
class CircleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle through Points")

        # Defaults: show their circle at startup
        self.default_points = [(-1, 3), (-4, 6), (2, 2)]
        self.points = self.default_points.copy()
        self.defaults_active = True  # first user "Add Point" clears defaults

        # Controls
        ctrl = tk.Frame(root)
        ctrl.pack(pady=8)

        tk.Label(ctrl, text="x:").grid(row=0, column=0)
        self.ex = tk.Entry(ctrl, width=8)
        self.ex.insert(0, "0")
        self.ex.grid(row=0, column=1, padx=(2, 8))

        tk.Label(ctrl, text="y:").grid(row=0, column=2)
        self.ey = tk.Entry(ctrl, width=8)
        self.ey.insert(0, "0")
        self.ey.grid(row=0, column=3, padx=(2, 8))

        # Always says "Add Point"
        self.btn_add = tk.Button(ctrl, text="Add Point", command=self.add_point)
        self.btn_add.grid(row=0, column=4, padx=6)

        tk.Button(ctrl, text="Clear All", command=self.clear_all).grid(row=0, column=5, padx=6)
        tk.Button(ctrl, text="Reset Defaults", command=self.reset_defaults).grid(row=0, column=6, padx=6)

        # Listbox to show current points (the 3 in use)
        self.listbox = tk.Listbox(root, width=32, height=5)
        self.listbox.pack(pady=(0, 8))

        # Initial plot
        self.figure = None
        self.canvas = None
        self.refresh_listbox()
        self.redraw()

    def current_circle(self):
        if len(self.points) == 3:
            try:
                return circle_from_three_points(self.points[0], self.points[1], self.points[2])
            except ValueError:
                return None
        return None

    def redraw(self):
        circ = self.current_circle()
        fig = make_figure(self.points, circ)

        if self.canvas is None:
            self.figure = fig
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
            self.canvas.get_tk_widget().pack()
        else:
            self.figure = fig
            self.canvas.figure = self.figure
        self.canvas.draw()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for p in self.points:
            self.listbox.insert(tk.END, f"({p[0]}, {p[1]})")

    def add_point(self):
        # Read user input
        try:
            x = float(self.ex.get())
            y = float(self.ey.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Enter numeric x and y.")
            return

        # First add clears defaults
        if self.defaults_active:
            self.points = []
            self.defaults_active = False

        # Append and keep only the latest three points
        self.points.append((x, y))
        if len(self.points) > 3:
            self.points = self.points[-3:]

        # Auto-compute and draw the circle as soon as we have 3 points
        self.refresh_listbox()
        self.redraw()

    def clear_all(self):
        self.points = []
        self.defaults_active = False
        self.refresh_listbox()
        self.redraw()

    def reset_defaults(self):
        self.points = self.default_points.copy()
        self.defaults_active = True
        self.refresh_listbox()
        self.redraw()

if __name__ == "__main__":
    root = tk.Tk()
    app = CircleApp(root)
    root.mainloop()
