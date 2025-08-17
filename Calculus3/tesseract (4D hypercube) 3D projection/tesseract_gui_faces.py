# tesseract_gui_faces.py
# Tkinter GUI + Matplotlib 3D: animated 4D tesseract rotation
# Buttons: Speed – / Speed +
# Toggle: Show/Hide colored faces (24 squares)

import itertools
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------- 4D helpers ----------
def rot4(i, j, theta):
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[i, i] = c; R[i, j] = -s
    R[j, i] = s; R[j, j] =  c
    return R

def project4_to_3(P4, perspective=True, d=3.0):
    if perspective:
        w = P4[:, 3]
        factor = d / (d - w)
        return P4[:, :3] * factor[:, None]
    else:
        return P4[:, :3]

# Vertices of the tesseract (±1 in each coordinate)
V4_base = np.array(list(itertools.product([-1, 1], repeat=4)), dtype=float)

# Map 4D point -> index for quick lookup
index_of = {tuple(v): i for i, v in enumerate(V4_base)}

# Edges (Hamming distance 1)
edges = []
for i in range(len(V4_base)):
    for j in range(i + 1, len(V4_base)):
        if np.sum(np.abs(V4_base[i] - V4_base[j])) == 2:
            edges.append((i, j))

# 24 square faces: fix two coordinates (dims a,b) to ±1; vary the other two
def build_square_faces():
    faces = []  # each face is a list of 4 vertex indices (consistent order)
    dims = [0, 1, 2, 3]
    for a in range(4):
        for b in range(a + 1, 4):
            c, d = [x for x in dims if x not in (a, b)]
            for sa in (-1, 1):
                for sb in (-1, 1):
                    v = [0, 0, 0, 0]
                    # base corners in (c,d): (-,-), (+,-), (+,+), (-,+)
                    corners = []
                    for sc, sd in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
                        v[a] = sa; v[b] = sb; v[c] = sc; v[d] = sd
                        corners.append(index_of[tuple(v)])
                    faces.append(corners)
    return faces

square_faces = build_square_faces()

# ---------- GUI ----------
class TesseractApp:
    def __init__(self, root):
        self.root = root
        root.title("4D Tesseract Rotation — colored faces")

        # State
        self.speed_deg = 1.5
        self.running = True
        self.perspective = True
        self.distance = 3.0
        self.show_faces_var = tk.BooleanVar(value=True)

        # Figure/axes
        self.fig = plt.Figure(figsize=(7.5, 7.5))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_title("Tesseract (4D hypercube) — 3D projection with colored faces")
        self.ax.set_xlabel("x"); self.ax.set_ylabel("y"); self.ax.set_zlabel("z")
        self.ax.set_box_aspect([1, 1, 1])

        # Embed canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=4, padx=8, pady=8)

        # Controls
        ttk.Button(root, text="Speed –", command=self.slower).grid(row=1, column=0, padx=6, pady=6, sticky="ew")
        ttk.Button(root, text="Pause/Resume", command=self.toggle).grid(row=1, column=1, padx=6, pady=6, sticky="ew")
        ttk.Button(root, text="Speed +", command=self.faster).grid(row=1, column=2, padx=6, pady=6, sticky="ew")
        ttk.Checkbutton(root, text="Show faces", variable=self.show_faces_var).grid(row=1, column=3, padx=6, pady=6)

        self.lbl = ttk.Label(root, text=self._speed_text())
        self.lbl.grid(row=2, column=0, columnspan=4, pady=(0, 8))

        # Artists: edges + (optional) faces
        self.edge_lines = []
        self.face_collection = None

        # Initialize with base position
        self.angles = np.zeros(3)  # radians for x–w, y–w, z–w
        self._init_artists()
        self._animate()

    # --- UI handlers ---
    def _speed_text(self): return f"Speed: {self.speed_deg:.2f}°/frame"
    def slower(self): self._set_speed(max(0.1, self.speed_deg * 0.8))
    def faster(self): self._set_speed(min(30.0, self.speed_deg * 1.25))
    def _set_speed(self, s): self.speed_deg = s; self.lbl.config(text=self._speed_text())
    def toggle(self): self.running = not self.running

    # --- drawing setup ---
    def _init_artists(self):
        V3 = project4_to_3(V4_base, perspective=self.perspective, d=self.distance)

        # Faces (colored, translucent)
        self._rebuild_faces(V3)

        # Edges
        for (a, b) in edges:
            line, = self.ax.plot([V3[a,0], V3[b,0]],
                                 [V3[a,1], V3[b,1]],
                                 [V3[a,2], V3[b,2]], linewidth=1)
            self.edge_lines.append(line)

        # Vertices (small markers to help depth perception)
        self.ax.scatter(V3[:,0], V3[:,1], V3[:,2], s=12)

    def _rebuild_faces(self, V3):
        if self.face_collection is not None:
            self.face_collection.remove()
            self.face_collection = None
        if not self.show_faces_var.get():
            self.canvas.draw_idle()
            return

        # Build list of face polygons in 3D
        polys = []
        for face in square_faces:
            polys.append([V3[idx] for idx in face])

        # Color map for 24 faces
        cmap = plt.cm.get_cmap("tab20")
        face_colors = [cmap((i % 20) / 19.0) for i in range(len(polys))]
        # add alpha
        face_colors = [(r, g, b, 0.25) for (r, g, b, a) in face_colors]

        self.face_collection = Poly3DCollection(polys, facecolors=face_colors, edgecolors=None)
        self.ax.add_collection3d(self.face_collection)

    # --- animation loop ---
    def _animate(self):
        if self.running:
            step = np.deg2rad(self.speed_deg)
            self.angles += np.array([step, 0.7*step, 1.3*step])

            Rxw = rot4(0, 3, self.angles[0])
            Ryw = rot4(1, 3, self.angles[1])
            Rzw = rot4(2, 3, self.angles[2])

            V4r = (V4_base @ Rxw.T) @ Ryw.T @ Rzw.T
            V3 = project4_to_3(V4r, perspective=self.perspective, d=self.distance)

            # Update faces (rebuild to keep polygons correct)
            if self.show_faces_var.get():
                self._rebuild_faces(V3)
            elif self.face_collection is not None:
                self.face_collection.remove()
                self.face_collection = None

            # Update edges
            for line, (a, b) in zip(self.edge_lines, edges):
                line.set_data([V3[a,0], V3[b,0]], [V3[a,1], V3[b,1]])
                line.set_3d_properties([V3[a,2], V3[b,2]])

            self.canvas.draw_idle()

        # schedule next frame (~60 FPS)
        self.root.after(16, self._animate)

# ---- run app ----
if __name__ == "__main__":
    root = tk.Tk()
    TesseractApp(root)
    root.mainloop()
