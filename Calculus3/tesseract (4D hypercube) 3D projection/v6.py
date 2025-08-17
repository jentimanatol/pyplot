# duoprism_100_faces_fx.py
# 4D duoprism C10 × C10 (100 rectangular faces) → 3D animated projection
# Adds: f(x) overlay and per-face labels (index or ∞), all toggleable via keys.

import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# -------- 4D helpers --------
def rot4(i, j, theta):
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[i, i] = c; R[i, j] = -s
    R[j, i] = s; R[j, j] =  c
    return R

def project4_to_3(P4, perspective=True, d=4.0):
    if not perspective:
        return P4[:, :3]
    w = np.clip(P4[:, 3], -d + 1e-6, d - 1e-6)
    f = d / (d - w)
    return P4[:, :3] * f[:, None]

# -------- Duoprism geometry C_m × C_n --------
def duoprism_vertices_edges_faces(m=10, n=10):
    th_m = np.linspace(0, 2*np.pi, m, endpoint=False)
    Pm = np.stack([np.cos(th_m), np.sin(th_m)], axis=1)
    th_n = np.linspace(0, 2*np.pi, n, endpoint=False)
    Pn = np.stack([np.cos(th_n), np.sin(th_n)], axis=1)

    V4 = np.array([[xm, ym, xn, yn] for (xm, ym) in Pm for (xn, yn) in Pn], dtype=float)

    def idx(i, j): return i*n + j

    E = []
    for j in range(n):
        for i in range(m):
            E.append((idx(i, j), idx((i+1) % m, j)))         # along m
    for i in range(m):
        for j in range(n):
            E.append((idx(i, j), idx(i, (j+1) % n)))         # along n

    F = []
    for i in range(m):
        i1 = (i + 1) % m
        for j in range(n):
            j1 = (j + 1) % n
            F.append([idx(i, j), idx(i1, j), idx(i1, j1), idx(i, j1)])  # rectangle

    return V4, E, F  # vertices, edges, faces

# -------- Build base shape (100 faces) --------
m, n = 10, 10
V4_base, E, F = duoprism_vertices_edges_faces(m, n)

# Fixed 4D pose (keep 3D frame stationary)
POSE = rot4(0, 3, np.deg2rad(25)) @ rot4(1, 3, np.deg2rad(18)) @ rot4(2, 3, np.deg2rad(10))
V4_pose = V4_base @ POSE.T

# -------- Figure & artists --------
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection="3d")
ax.set_title("Duoprism C10×C10 — 100 faces, with f(x) overlay & face labels")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.set_box_aspect([1, 1, 1])

# Edges
edge_lines = [ax.plot([], [], [], linewidth=0.8)[0] for _ in E]

# Faces (uniform translucent pattern)
faces_collection = Poly3DCollection([], facecolors=(0.15, 0.60, 0.85, 0.22), edgecolors=None)
ax.add_collection3d(faces_collection)

# Face labels (Text3D artists) — created once, updated per frame
face_texts = []
for _ in F:
    # placeholder; will update position & text each frame
    txt = ax.text(0, 0, 0, "", fontsize=7, ha="center", va="center")
    txt.set_visible(False)
    face_texts.append(txt)

# f(x) overlay (2D in-axes text)
fx_string = r"$f(x)=\sin(x)\;+\;\frac{x}{2}$"   # customize the displayed formula here
fx_text_artist = ax.text2D(0.02, 0.96, fx_string, transform=ax.transAxes, fontsize=12, fontweight="bold")
fx_text_artist.set_visible(True)

# Camera box
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-3, 3)

# -------- Animation state & controls --------
running = True
perspective = True
dist = 4.0
omega = np.deg2rad(1.0)          # angular speed (rad/frame)
angles = np.zeros(3)             # (x–w, y–w, z–w)
show_faces = True
show_edges = True
show_labels = True
label_mode = 0                   # 0=index, 1=infinity, 2=off (cycled by 'm')

def reset_view():
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-3, 3)

def on_key(e):
    global running, omega, perspective, show_faces, show_edges, show_labels, label_mode
    if e.key == ' ':
        running = not running
    elif e.key == '+':
        omega = min(np.deg2rad(20), omega * 1.25)
    elif e.key == '-':
        omega = max(np.deg2rad(0.1), omega * 0.8)
    elif e.key == 'o':
        perspective = not perspective
    elif e.key == 'c':
        show_faces = not show_faces
        if not show_faces:
            faces_collection.set_verts([])
    elif e.key == 'l':
        show_labels = not show_labels
        for t in face_texts: t.set_visible(False if not show_labels else True)
    elif e.key == 'm':
        label_mode = (label_mode + 1) % 3  # index → infinity → off
        if label_mode == 2:
            for t in face_texts: t.set_visible(False)
        else:
            for t in face_texts: t.set_visible(show_labels)
    elif e.key == 'x':
        fx_text_artist.set_visible(not fx_text_artist.get_visible())
    elif e.key == 'r':
        reset_view()

fig.canvas.mpl_connect('key_press_event', on_key)

# -------- Helpers --------
def face_centroid(V3, face):
    pts = V3[np.array(face)]
    return pts.mean(axis=0)

# -------- Animation step --------
def update(_):
    global angles
    if running:
        angles += np.array([omega, 0.8*omega, 1.2*omega])

    Rxw = rot4(0, 3, angles[0])
    Ryw = rot4(1, 3, angles[1])
    Rzw = rot4(2, 3, angles[2])

    V4_now = (V4_pose @ Rxw.T) @ Ryw.T @ Rzw.T
    V3 = project4_to_3(V4_now, perspective=perspective, d=dist)

    # Faces
    if show_faces:
        polys = [[V3[i], V3[j], V3[k], V3[l]] for (i, j, k, l) in F]
        faces_collection.set_verts(polys)
    else:
        faces_collection.set_verts([])

    # Edges
    if show_edges:
        for ln, (a, b) in zip(edge_lines, E):
            ln.set_data([V3[a,0], V3[b,0]], [V3[a,1], V3[b,1]])
            ln.set_3d_properties([V3[a,2], V3[b,2]])

    # Labels (index or ∞) at face centroids
    if show_labels and label_mode != 2:
        for idx, (face, txt) in enumerate(zip(F, face_texts), start=1):
            cx, cy, cz = face_centroid(V3, face)
            txt.set_position((cx, cy))
            txt.set_3d_properties(cz)
            if label_mode == 0:
                txt.set_text(str(idx))   # 1..100
            elif label_mode == 1:
                txt.set_text("∞")
            txt.set_visible(True)
    else:
        for t in face_texts:
            t.set_visible(False)

    return edge_lines + [faces_collection] + face_texts + [fx_text_artist]

ani = FuncAnimation(fig, update, interval=16, blit=False)  # ~60 FPS
plt.show()
