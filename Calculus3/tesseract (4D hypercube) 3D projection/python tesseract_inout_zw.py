# tesseract_inout_zw.py
# Stationary 3D frame; 4D rotation in z–w to make the near side grow while
# the far side shrinks (simultaneous in/out), matching the "enter/exit" feel.

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

def project4_to_3(P4, perspective=True, d=5.0):
    if not perspective:
        return P4[:, :3]
    # simple perspective using w as depth-in-4D
    w = np.clip(P4[:, 3], -d + 1e-3, d - 1e-3)
    factor = d / (d - w)
    return P4[:, :3] * factor[:, None]

# ---------- Tesseract geometry ----------
# 16 vertices: (±1, ±1, ±1, ±1)
V4_base = np.array(list(itertools.product([-1, 1], repeat=4)), dtype=float)

# Edges: Hamming distance 1
edges = []
for a in range(len(V4_base)):
    for b in range(a + 1, len(V4_base)):
        if np.sum(np.abs(V4_base[a] - V4_base[b])) == 2:
            edges.append((a, b))

# Faces (24 squares): fix any 2 coords; vary the other 2
index_of = {tuple(v): i for i, v in enumerate(V4_base)}
def build_square_faces():
    faces = []
    dims = [0, 1, 2, 3]
    for a in range(4):
        for b in range(a + 1, 4):
            c, d = [x for x in dims if x not in (a, b)]
            for sa in (-1, 1):
                for sb in (-1, 1):
                    v = [0, 0, 0, 0]
                    quad = []
                    for sc, sd in [(-1,-1),(1,-1),(1,1),(-1,1)]:
                        v[a] = sa; v[b] = sb; v[c] = sc; v[d] = sd
                        quad.append(index_of[tuple(v)])
                    faces.append(quad)
    return faces

square_faces = build_square_faces()

# 8 cube cells: fix one coord to ±1, vary the other three
# We'll especially highlight the two opposite "w cells": w=+1 and w=-1.
cells = []
for dim in range(4):
    for sign in (-1, 1):
        group = [index_of[tuple(v)] for v in V4_base if v[dim] == sign]
        cells.append((dim, sign, group))
# locate w=-1 and w=+1 cells
wminus = next(group for (dim, s, group) in cells if dim == 3 and s == -1)
wplus  = next(group for (dim, s, group) in cells if dim == 3 and s == +1)

# Fixed 4D pose so the 3D frame doesn't rotate; only z–w rotates over time
R_fixed = rot4(0, 3, np.deg2rad(35)) @ rot4(1, 3, np.deg2rad(22))  # x–w, y–w pre-tilt
V4_fixed = V4_base @ R_fixed.T

# ---------- GUI ----------
class InOutZWApp:
    def __init__(self, root):
        self.root = root
        root.title("Tesseract: 4D z–w Rotation (near face grows, far face shrinks)")

        # State
        self.running = True
        self.speed_deg = 1.8     # degrees per frame for z–w rotation
        self.theta = 0.0         # current z–w angle
        self.perspective = True
        self.distance = 5.0
        self.show_faces_var = tk.BooleanVar(value=True)

        # Figure
        self.fig = plt.Figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_title("Stationary 3D frame — pure 4D z–w rotation")
        self.ax.set_xlabel("x"); self.ax.set_ylabel("y"); self.ax.set_zlabel("z")
        self.ax.set_box_aspect([1, 1, 1])

        # Canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=4, padx=8, pady=8)

        # Controls
        ttk.Button(root, text="Speed –", command=self.slower).grid(row=1, column=0, padx=6, pady=6, sticky="ew")
        ttk.Button(root, text="Pause/Resume", command=self.toggle).grid(row=1, column=1, padx=6, pady=6, sticky="ew")
        ttk.Button(root, text="Speed +", command=self.faster).grid(row=1, column=2, padx=6, pady=6, sticky="ew")
        ttk.Checkbutton(root, text="Show faces", variable=self.show_faces_var, command=self._force_draw)\
            .grid(row=1, column=3, padx=6, pady=6)
        self.lbl = ttk.Label(root, text=self._speed_text()); self.lbl.grid(row=2, column=0, columnspan=4)

        # Artists
        self.edge_lines = []
        self.face_collection_near = None
        self.face_collection_far = None
        self.face_collection_mid = None
        self.vertex_scatter = None

        self._init_artists()
        self._animate()

    def _speed_text(self):
        return f"z–w rotation speed: {self.speed_deg:.2f}°/frame"

    def slower(self):
        self.speed_deg = max(0.1, self.speed_deg * 0.8)
        self.lbl.config(text=self._speed_text())

    def faster(self):
        self.speed_deg = min(30.0, self.speed_deg * 1.25)
        self.lbl.config(text=self._speed_text())

    def toggle(self):
        self.running = not self.running

    def _force_draw(self):
        self._update_frame(force=True)

    def _init_artists(self):
        # first draw with theta=0
        V3 = project4_to_3(V4_fixed, perspective=self.perspective, d=self.distance)
        # faces (split into near/far/mid sets for visual clarity)
        self._rebuild_faces_split(V4_fixed, V3)
        # edges
        for (a, b) in edges:
            ln, = self.ax.plot([V3[a,0], V3[b,0]],
                               [V3[a,1], V3[b,1]],
                               [V3[a,2], V3[b,2]], linewidth=1)
            self.edge_lines.append(ln)
        # vertices
        self.vertex_scatter = self.ax.scatter(V3[:,0], V3[:,1], V3[:,2], s=12)

    def _rebuild_faces_split(self, V4_current, V3):
        # Remove old
        for coll in (self.face_collection_near, self.face_collection_far, self.face_collection_mid):
            if coll is not None:
                coll.remove()
        self.face_collection_near = self.face_collection_far = self.face_collection_mid = None
        if not self.show_faces_var.get():
            self.canvas.draw_idle()
            return

        # Classify each face by average current w (near = larger w)
        face_polys_near, face_polys_far, face_polys_mid = [], [], []
        face_ws = []
        for face in square_faces:
            w_avg = float(np.mean(V4_current[np.array(face), 3]))
            face_ws.append((w_avg, face))
        # threshold bands: top third near, bottom third far
        ws = np.array([w for (w, _) in face_ws])
        if len(ws) > 0:
            lo, hi = np.percentile(ws, [33, 67])
        else:
            lo, hi = -1.0, 1.0

        for w_avg, face in face_ws:
            poly = [V3[i] for i in face]
            if w_avg >= hi:
                face_polys_near.append(poly)
            elif w_avg <= lo:
                face_polys_far.append(poly)
            else:
                face_polys_mid.append(poly)

        # Colors: near = stronger, far = fainter, middle = in-between
        self.face_collection_near = Poly3DCollection(face_polys_near, facecolors=(0.1, 0.6, 0.9, 0.30), edgecolors=None)
        self.face_collection_mid  = Poly3DCollection(face_polys_mid,  facecolors=(0.2, 0.7, 0.3, 0.20), edgecolors=None)
        self.face_collection_far  = Poly3DCollection(face_polys_far,  facecolors=(0.7, 0.2, 0.3, 0.12), edgecolors=None)
        self.ax.add_collection3d(self.face_collection_far)
        self.ax.add_collection3d(self.face_collection_mid)
        self.ax.add_collection3d(self.face_collection_near)

    def _update_frame(self, force=False):
        if self.running or force:
            self.theta += np.deg2rad(self.speed_deg)

        # Pure 4D rotation in the z–w plane (index 2 ↔ 3)
        Rzw = rot4(2, 3, self.theta)
        V4_now = V4_fixed @ Rzw.T

        # Project with perspective (near faces swell, far faces shrink)
        V3 = project4_to_3(V4_now, perspective=self.perspective, d=self.distance)

        # Faces (rebuild & classify by current w-average)
        if self.show_faces_var.get():
            self._rebuild_faces_split(V4_now, V3)
        else:
            for coll in (self.face_collection_near, self.face_collection_far, self.face_collection_mid):
                if coll is not None:
                    coll.remove()
            self.face_collection_near = self.face_collection_far = self.face_collection_mid = None

        # Edges
        for ln, (a, b) in zip(self.edge_lines, edges):
            ln.set_data([V3[a,0], V3[b,0]], [V3[a,1], V3[b,1]])
            ln.set_3d_properties([V3[a,2], V3[b,2]])

        # Vertices
        self.vertex_scatter._offsets3d = (V3[:,0], V3[:,1], V3[:,2])

        self.canvas.draw_idle()

    def _animate(self):
        if self.running:
            self._update_frame()
        else:
            self._update_frame(force=True)
        self.root.after(16, self._animate)  # ~60 FPS

# ---- run ----
if __name__ == "__main__":
    root = tk.Tk()
    InOutZWApp(root)
    root.mainloop()
