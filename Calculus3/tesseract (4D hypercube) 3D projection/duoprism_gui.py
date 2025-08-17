# duoprism_gui.py
# Animate a 4D duoprism C_m × C_n (product of two polygons) projected to 3D.
# Controls: sliders for m and n (sides), Rebuild, Speed – / Pause / Speed +, Show faces.

import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---- 4D helpers ----
def rot4(i, j, theta):
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[i, i] = c; R[i, j] = -s
    R[j, i] = s; R[j, j] =  c
    return R

def project4_to_3(P4, perspective=True, d=4.0):
    if perspective:
        w = P4[:, 3]
        factor = d / (d - w)
        return P4[:, :3] * factor[:, None]
    else:
        return P4[:, :3]

# ---- Geometry ----
def duoprism_vertices_edges_faces(m=16, n=4):
    """Vertices (x,y,u,v), edges along m and n, and m*n rectangular faces."""
    theta_m = np.linspace(0, 2*np.pi, m, endpoint=False)
    Pm = np.stack([np.cos(theta_m), np.sin(theta_m)], axis=1)
    theta_n = np.linspace(0, 2*np.pi, n, endpoint=False)
    Pn = np.stack([np.cos(theta_n), np.sin(theta_n)], axis=1)

    verts4 = np.array([[xm, ym, xn, yn] for (xm, ym) in Pm for (xn, yn) in Pn], dtype=float)

    def idx(i, j): return i*n + j

    edges = []
    for j in range(n):
        for i in range(m):
            edges.append((idx(i, j), idx((i+1) % m, j)))       # along m
    for i in range(m):
        for j in range(n):
            edges.append((idx(i, j), idx(i, (j+1) % n)))       # along n

    faces = []
    for i in range(m):
        i1 = (i + 1) % m
        for j in range(n):
            j1 = (j + 1) % n
            faces.append([idx(i, j), idx(i1, j), idx(i1, j1), idx(i, j1)])  # rectangle

    return verts4, edges, faces

# ---- GUI App ----
class DuoprismApp:
    def __init__(self, root):
        self.root = root
        root.title("4D Duoprism C_m × C_n — adjustable sides & animation")

        # State
        self.m = 16
        self.n = 4
        self.speed_deg = 1.0
        self.running = True
        self.perspective = True
        self.distance = 4.0
        self.show_faces_var = tk.BooleanVar(value=True)

        # Figure
        self.fig = plt.Figure(figsize=(7.5, 7.5))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_title("C_m × C_n duoprism — 3D projection")
        self.ax.set_xlabel("x"); self.ax.set_ylabel("y"); self.ax.set_zlabel("z")
        self.ax.set_box_aspect([1, 1, 1])

        # Canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=6, padx=8, pady=8)

        # Sliders
        ttk.Label(root, text="m (sides #1)").grid(row=1, column=0, padx=4, sticky="e")
        self.m_scale = ttk.Scale(root, from_=3, to=64, orient="horizontal", command=self._on_m_change)
        self.m_scale.set(self.m)
        self.m_scale.grid(row=1, column=1, columnspan=2, sticky="ew", padx=4)
        self.m_lbl = ttk.Label(root, text=str(self.m)); self.m_lbl.grid(row=1, column=3, padx=4, sticky="w")

        ttk.Label(root, text="n (sides #2)").grid(row=2, column=0, padx=4, sticky="e")
        self.n_scale = ttk.Scale(root, from_=3, to=64, orient="horizontal", command=self._on_n_change)
        self.n_scale.set(self.n)
        self.n_scale.grid(row=2, column=1, columnspan=2, sticky="ew", padx=4)
        self.n_lbl = ttk.Label(root, text=str(self.n)); self.n_lbl.grid(row=2, column=3, padx=4, sticky="w")

        ttk.Button(root, text="Rebuild", command=self.rebuild).grid(row=1, column=4, rowspan=2, padx=6, pady=2, sticky="ns")

        # Buttons
        ttk.Button(root, text="Speed –", command=self.slower).grid(row=3, column=0, padx=6, pady=6, sticky="ew")
        ttk.Button(root, text="Pause/Resume", command=self.toggle).grid(row=3, column=1, padx=6, pady=6, sticky="ew")
        ttk.Button(root, text="Speed +", command=self.faster).grid(row=3, column=2, padx=6, pady=6, sticky="ew")
        ttk.Checkbutton(root, text="Show faces", variable=self.show_faces_var).grid(row=3, column=3, padx=6, pady=6)
        self.speed_lbl = ttk.Label(root, text=self._speed_text()); self.speed_lbl.grid(row=3, column=4, columnspan=2, padx=6)

        # Geometry & artists
        self.angles = np.zeros(3)
        self.V4, self.edges, self.faces = duoprism_vertices_edges_faces(self.m, self.n)
        self.edge_lines = []
        self.face_collection = None
        self._init_artists()

        # Animate
        self._animate()

    def _on_m_change(self, val): self.m_lbl.config(text=str(int(float(val))))
    def _on_n_change(self, val): self.n_lbl.config(text=str(int(float(val))))
    def slower(self): self.speed_deg = max(0.1, self.speed_deg * 0.8); self.speed_lbl.config(text=self._speed_text())
    def faster(self): self.speed_deg = min(20.0, self.speed_deg * 1.25); self.speed_lbl.config(text=self._speed_text())
    def toggle(self): self.running = not self.running
    def _speed_text(self): return f"Speed: {self.speed_deg:.2f}°/frame"

    def rebuild(self):
        self.m = int(self.m_scale.get()); self.n = int(self.n_scale.get())
        self.V4, self.edges, self.faces = duoprism_vertices_edges_faces(self.m, self.n)
        self._reset_artists()

    def _init_artists(self):
        V3 = project4_to_3(self.V4, perspective=self.perspective, d=self.distance)
        self._rebuild_faces(V3)
        for (a, b) in self.edges:
            line, = self.ax.plot([V3[a,0], V3[b,0]],[V3[a,1], V3[b,1]],[V3[a,2], V3[b,2]], linewidth=1)
            self.edge_lines.append(line)
        self.ax.scatter(V3[:,0], V3[:,1], V3[:,2], s=10)

    def _reset_artists(self):
        self.ax.cla()
        self.ax.set_title("C_m × C_n duoprism — 3D projection")
        self.ax.set_xlabel("x"); self.ax.set_ylabel("y"); self.ax.set_zlabel("z")
        self.ax.set_box_aspect([1, 1, 1])
        self.edge_lines = []
        self.face_collection = None
        self._init_artists()
        self.canvas.draw_idle()

    def _rebuild_faces(self, V3):
        if self.face_collection is not None:
            self.face_collection.remove()
            self.face_collection = None
        if not self.show_faces_var.get():
            return
        polys = [[V3[i], V3[j], V3[k], V3[l]] for (i, j, k, l) in self.faces]
        self.face_collection = Poly3DCollection(polys, alpha=0.15, edgecolors=None)
        self.ax.add_collection3d(self.face_collection)

    def _animate(self):
        if self.running:
            step = np.deg2rad(self.speed_deg)
            self.angles += np.array([step, 0.8*step, 1.2*step])

            Rxv = rot4(0, 3, self.angles[0])
            Ryv = rot4(1, 3, self.angles[1])
            Ruv = rot4(2, 3, self.angles[2])
            V4r = (self.V4 @ Rxv.T) @ Ryv.T @ Ruv.T
            V3 = project4_to_3(V4r, perspective=True, d=4.0)

            if self.show_faces_var.get():
                self._rebuild_faces(V3)
            elif self.face_collection is not None:
                self.face_collection.remove(); self.face_collection = None

            for line, (a, b) in zip(self.edge_lines, self.edges):
                line.set_data([V3[a,0], V3[b,0]], [V3[a,1], V3[b,1]])
                line.set_3d_properties([V3[a,2], V3[b,2]])

            self.canvas.draw_idle()

        self.root.after(16, self._animate)

if __name__ == "__main__":
    root = tk.Tk()
    DuoprismApp(root)
    root.mainloop()
