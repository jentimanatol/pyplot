# tesseract_gui.py
# Tkinter GUI + Matplotlib 3D: animated 4D tesseract rotation
# Buttons: Speed –  and  Speed +

import itertools
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# -----------------------------
# 4D math helpers
# -----------------------------
def rot4(i, j, theta):
    """4×4 rotation matrix for a rotation by theta in the (i, j) plane."""
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[i, i] = c; R[i, j] = -s
    R[j, i] = s; R[j, j] =  c
    return R

def project4_to_3(P4, perspective=True, d=3.0):
    """Project Nx4 -> Nx3 (simple perspective or orthographic)."""
    if perspective:
        w = P4[:, 3]
        factor = d / (d - w)
        return P4[:, :3] * factor[:, None]
    else:
        return P4[:, :3]

# Build tesseract vertices (±1, ±1, ±1, ±1) and edges (Hamming distance 1)
V4_base = np.array(list(itertools.product([-1, 1], repeat=4)), dtype=float)
edges = []
for i in range(len(V4_base)):
    for j in range(i + 1, len(V4_base)):
        if np.sum(np.abs(V4_base[i] - V4_base[j])) == 2:
            edges.append((i, j))

# -----------------------------
# GUI App
# -----------------------------
class TesseractApp:
    def __init__(self, root):
        self.root = root
        root.title("4D Tesseract Rotation — Speed +/-")

        # State
        self.speed_deg = 1.5   # degrees per frame (will change with buttons)
        self.perspective = True
        self.distance = 3.0
        self.running = True

        # Figure
        self.fig = plt.Figure(figsize=(7, 7))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_title("Tesseract (4D hypercube) → 3D projection")
        self.ax.set_xlabel("x"); self.ax.set_ylabel("y"); self.ax.set_zlabel("z")
        self.ax.set_box_aspect([1, 1, 1])

        # Create line artists for each edge
        self.lines = []
        # initial positions
        V3 = project4_to_3(V4_base.copy(), perspective=self.perspective, d=self.distance)
        for (a, b) in edges:
            xs = [V3[a, 0], V3[b, 0]]
            ys = [V3[a, 1], V3[b, 1]]
            zs = [V3[a, 2], V3[b, 2]]
            line, = self.ax.plot(xs, ys, zs, linewidth=1)
            self.lines.append(line)
        self.ax.scatter(V3[:, 0], V3[:, 1], V3[:, 2], s=25)

        # Embed canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=3, padx=8, pady=8)

        # Controls
        self.btn_slow = ttk.Button(root, text="Speed –", command=self.slower)
        self.btn_fast = ttk.Button(root, text="Speed +", command=self.faster)
        self.btn_pause = ttk.Button(root, text="Pause/Resume", command=self.toggle)

        self.btn_slow.grid(row=1, column=0, padx=6, pady=6, sticky="ew")
        self.btn_pause.grid(row=1, column=1, padx=6, pady=6, sticky="ew")
        self.btn_fast.grid(row=1, column=2, padx=6, pady=6, sticky="ew")

        self.lbl = ttk.Label(root, text=self._speed_text())
        self.lbl.grid(row=2, column=0, columnspan=3, pady=(0, 8))

        # Animation angles (rotate in x–w, y–w, z–w per frame)
        self.angles = np.array([0.0, 0.0, 0.0])  # radians

        # Kick off animation
        self._animate()

    def _speed_text(self):
        return f"Speed: {self.speed_deg:.2f}°/frame (use Speed – / Speed +)"

    def slower(self):
        self.speed_deg = max(0.1, self.speed_deg * 0.8)  # clamp to > 0
        self.lbl.config(text=self._speed_text())

    def faster(self):
        self.speed_deg = min(20.0, self.speed_deg * 1.25)
        self.lbl.config(text=self._speed_text())

    def toggle(self):
        self.running = not self.running

    def _animate(self):
        if self.running:
            # increment angles (convert speed to radians)
            step = np.deg2rad(self.speed_deg)
            # Different rates on each plane to avoid periodic locking
            self.angles += np.array([step, 0.7 * step, 1.3 * step])

            Rxw = rot4(0, 3, self.angles[0])
            Ryw = rot4(1, 3, self.angles[1])
            Rzw = rot4(2, 3, self.angles[2])

            V4r = (V4_base @ Rxw.T) @ Ryw.T @ Rzw.T
            V3 = project4_to_3(V4r, perspective=self.perspective, d=self.distance)

            # Update edge lines
            for line, (a, b) in zip(self.lines, edges):
                line.set_data([V3[a, 0], V3[b, 0]], [V3[a, 1], V3[b, 1]])
                line.set_3d_properties([V3[a, 2], V3[b, 2]])

            self.canvas.draw_idle()

        # schedule next frame
        self.root.after(16, self._animate)  # ~60 FPS target

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    TesseractApp(root)
    root.mainloop()
