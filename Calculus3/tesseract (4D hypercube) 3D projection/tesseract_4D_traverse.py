# tesseract_4D_traverse.py
# Keep the 3D frame stationary; move the tesseract in 4D to create
# (1) a "tunnel" traversal (enter via one cube face, exit via the opposite)
# (2) a single-cell "pulse" (one cube face minimizes → maximizes)

import itertools
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------- 4D helpers ----------------
def rot4(i, j, theta):
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[i, i] = c; R[i, j] = -s
    R[j, i] = s; R[j, j] =  c
    return R

def project4_to_3(P4, perspective=True, d=5.0):
    if perspective:
        w = P4[:, 3]
        # keep away from d to avoid blow-ups
        w = np.clip(w, -d+1e-3, d-1e-3)
        factor = d / (d - w)
        return P4[:, :3] * factor[:, None]
    else:
        return P4[:, :3]

# 16 vertices of a tesseract: (±1, ±1, ±1, ±1)
V4_base = np.array(list(itertools.product([-1, 1], repeat=4)), dtype=float)

# Edges (Hamming distance 1)
edges = []
for i in range(len(V4_base)):
    for j in range(i + 1, len(V4_base)):
        if np.sum(np.abs(V4_base[i] - V4_base[j])) == 2:
            edges.append((i, j))

# 24 square faces (for coloring)
index_of = {tuple(v): k for k, v in enumerate(V4_base)}
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

# 8 cube cells: fix one coordinate to ±1, vary the other three.
# We'll index them as (dim, sign), where dim in {0:x,1:y,2:z,3:w}, sign in {-1,+1}
def build_cells():
    cells = []  # list of lists of vertex indices (each 8 verts)
    for dim in range(4):
        for sign in (-1, 1):
            group = []
            for v in V4_base:
                if v[dim] == sign:
                    group.append(index_of[tuple(v)])
            cells.append((dim, sign, group))
    return cells

cells = build_cells()  # 8 cubes

# Pre-rotate once to choose a nice, stationary 3D stance (no per-frame spin)
# You can tweak these angles to set the fixed pose.
R_fixed = rot4(0, 3, np.deg2rad(40)) @ rot4(1, 3, np.deg2rad(28)) @ rot4(2, 3, np.deg2rad(18))
V4_fixed = V4_base @ R_fixed.T

# ---------------- GUI app ----------------
class TesseractTraverseApp:
    def __init__(self, root):
        self.root = root
        root.title("4D Tesseract — Stationary 3D Frame, 4D Motion Traverse")

        # State
        self.running = True
        self.speed_deg = 1.2        # "phase speed" for the motion
        self.phase = 0.0            # animation phase (radians)
        self.mode = tk.StringVar(value="Tunnel (w-translate)")
        self.cell_idx = tk.IntVar(value=0)  # which cell to pulse
        self.show_faces_var = tk.BooleanVar(value=True)
        self.distance = 5.0
        self.perspective = True

        # Figure / axes
        self.fig = plt.Figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_title("Tesseract — 4D traverse (stationary 3D frame)")
        self.ax.set_xlabel("x"); self.ax.set_ylabel("y"); self.ax.set_zlabel("z")
        self.ax.set_box_aspect([1,1,1])

        # Canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=6, padx=8, pady=8)

        # Controls row 1
        ttk.Button(root, text="Speed –", command=self.slower).grid(row=1, column=0, padx=6, pady=6, sticky="ew")
        ttk.Button(root, text="Pause/Resume", command=self.toggle).grid(row=1, column=1, padx=6, pady=6, sticky="ew")
        ttk.Button(root, text="Speed +", command=self.faster).grid(row=1, column=2, padx=6, pady=6, sticky="ew")
        ttk.Checkbutton(root, text="Show faces", variable=self.show_faces_var, command=self._redraw_now)\
            .grid(row=1, column=3, padx=6, pady=6)

        ttk.Label(root, text="Mode:").grid(row=1, column=4, sticky="e")
        ttk.OptionMenu(root, self.mode, self.mode.get(),
                       "Tunnel (w-translate)",
                       "Face pulse (one cell)")\
            .grid(row=1, column=5, sticky="ew", padx=6)

        # Controls row 2
        ttk.Label(root, text="Pulse cell (dim, sign):").grid(row=2, column=0, columnspan=2, sticky="e", padx=6)
        self.cell_menu = ttk.Combobox(root, state="readonly",
                                      values=[f"{i}: dim={d} {'+' if s>0 else '-'}1" for i,(d,s,_) in enumerate(cells)],
                                      width=22)
        self.cell_menu.current(0)
        self.cell_menu.bind("<<ComboboxSelected>>", self._on_cell_change)
        self.cell_menu.grid(row=2, column=2, columnspan=2, sticky="ew", padx=6)
        self.speed_lbl = ttk.Label(root, text=self._speed_text()); self.speed_lbl.grid(row=2, column=4, columnspan=2, padx=6)

        # Artists
        self.edge_lines = []
        self.face_collection = None
        self.vertex_scatter = None

        # Init artists
        self._init_artists()

        # Animate
        self._animate()

    # ------------- UI callbacks -------------
    def _on_cell_change(self, _evt):
        self.cell_idx.set(int(self.cell_menu.get().split(":")[0]))

    def slower(self):
        self.speed_deg = max(0.1, self.speed_deg * 0.8)
        self.speed_lbl.config(text=self._speed_text())

    def faster(self):
        self.speed_deg = min(30.0, self.speed_deg * 1.25)
        self.speed_lbl.config(text=self._speed_text())

    def toggle(self):
        self.running = not self.running

    def _speed_text(self):
        return f"Speed: {self.speed_deg:.2f} (phase units)"

    # ------------- drawing setup -------------
    def _init_artists(self):
        V3 = project4_to_3(V4_fixed, perspective=self.perspective, d=self.distance)
        # faces
        self._rebuild_faces(V3)
        # edges
        for (a,b) in edges:
            ln, = self.ax.plot([V3[a,0], V3[b,0]],
                               [V3[a,1], V3[b,1]],
                               [V3[a,2], V3[b,2]], linewidth=1)
            self.edge_lines.append(ln)
        # vertices
        self.vertex_scatter = self.ax.scatter(V3[:,0], V3[:,1], V3[:,2], s=12)

    def _rebuild_faces(self, V3):
        if self.face_collection is not None:
            self.face_collection.remove()
            self.face_collection = None
        if not self.show_faces_var.get():
            self.canvas.draw_idle()
            return
        polys = [[V3[i], V3[j], V3[k], V3[l]] for (i,j,k,l) in square_faces]
        # light transparent colors
        cmap = plt.cm.get_cmap("tab20")
        cols = [(cmap((i % 20)/19.0)[0:3] + (0.22,)) for i in range(len(polys))]
        self.face_collection = Poly3DCollection(polys, facecolors=cols, edgecolors=None)
        self.ax.add_collection3d(self.face_collection)

    def _redraw_now(self):
        # force an immediate refresh using current phase
        self._update_frame(force_redraw=True)

    # ------------- motion models -------------
    def _apply_motion(self, V4):
        """
        Keep 3D pose fixed (R_fixed is already applied).
        Apply 4D motion to V4 in one of two ways:
        - Tunnel: translate all vertices along w
        - Face pulse: translate only one cell's vertices along w
        """
        phase = self.phase
        V4m = V4.copy()

        if self.mode.get().startswith("Tunnel"):
            # Smooth traverse along w: enter via one face, exit via the other
            # amplitude chosen to avoid w near d
            A = 1.6
            w_shift = A * np.sin(phase)
            V4m[:, 3] += w_shift

        else:
            # Face pulse: pick one cube cell and push/pull only that cell in w
            A = 1.8
            _, _, verts = cells[self.cell_idx.get()]
            pulse = A * np.sin(phase)
            V4m[verts, 3] += pulse

        return V4m

    # ------------- per-frame update -------------
    def _update_frame(self, force_redraw=False):
        # Update phase
        if self.running or force_redraw:
            self.phase += np.deg2rad(self.speed_deg)

        # 4D motion (no extra 3D rotation; frame stays fixed)
        V4m = self._apply_motion(V4_fixed)
        V3 = project4_to_3(V4m, perspective=self.perspective, d=self.distance)

        # Update faces
        if self.show_faces_var.get():
            self._rebuild_faces(V3)
        elif self.face_collection is not None:
            self.face_collection.remove()
            self.face_collection = None

        # Update edges
        for ln, (a,b) in zip(self.edge_lines, edges):
            ln.set_data([V3[a,0], V3[b,0]], [V3[a,1], V3[b,1]])
            ln.set_3d_properties([V3[a,2], V3[b,2]])

        # Update vertices
        self.vertex_scatter._offsets3d = (V3[:,0], V3[:,1], V3[:,2])

        self.canvas.draw_idle()

    def _animate(self):
        if self.running:
            self._update_frame()
        else:
            # still refresh occasionally to honor UI changes
            self._update_frame(force_redraw=True)
        self.root.after(16, self._animate)  # ~60 FPS

# ------------- run -------------
if __name__ == "__main__":
    root = tk.Tk()
    TesseractTraverseApp(root)
    root.mainloop()
