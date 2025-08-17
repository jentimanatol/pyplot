# duoprism_100_faces.py
# 4D duoprism C10 × C10 (100 rectangular faces) → 3D animated projection
# Faces all share the SAME color/pattern (uniform translucent fill).

import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ---------- 4D helpers ----------
def rot4(i, j, theta):
    """Return 4×4 rotation matrix in plane (i, j) by angle theta (radians)."""
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[i, i] = c; R[i, j] = -s
    R[j, i] = s; R[j, j] =  c
    return R

def project4_to_3(P4, perspective=True, d=4.0):
    """Project Nx4 → Nx3 using simple perspective via w (or orthographic if off)."""
    if not perspective:
        return P4[:, :3]
    w = np.clip(P4[:, 3], -d + 1e-6, d - 1e-6)
    f = d / (d - w)
    return P4[:, :3] * f[:, None]

# ---------- Duoprism geometry (C_m × C_n) ----------
def duoprism_vertices_edges_faces(m=10, n=10):
    """
    C_m × C_n embedded in 4D as (cos(2πi/m), sin(2πi/m), cos(2πj/n), sin(2πj/n)).
    Returns:
      V4: (m*n, 4) vertices
      E:  list of edge index pairs
      F:  list of rectangular faces (each 4 vertex indices) -> total m*n faces
    """
    theta_m = np.linspace(0, 2*np.pi, m, endpoint=False)
    Pm = np.stack([np.cos(theta_m), np.sin(theta_m)], axis=1)  # (m,2)

    theta_n = np.linspace(0, 2*np.pi, n, endpoint=False)
    Pn = np.stack([np.cos(theta_n), np.sin(theta_n)], axis=1)  # (n,2)

    # Cartesian product → 4D vertices (x, y, u, v)
    V4 = np.array([[xm, ym, xn, yn] for (xm, ym) in Pm for (xn, yn) in Pn], dtype=float)

    def idx(i, j): return i*n + j

    # Edges along m (wrap) and along n (wrap)
    E = []
    for j in range(n):
        for i in range(m):
            E.append((idx(i, j), idx((i + 1) % m, j)))
    for i in range(m):
        for j in range(n):
            E.append((idx(i, j), idx(i, (j + 1) % n)))

    # Rectangular faces: (i,j) → (i+1,j) → (i+1,j+1) → (i,j+1)
    F = []
    for i in range(m):
        i1 = (i + 1) % m
        for j in range(n):
            j1 = (j + 1) % n
            F.append([idx(i, j), idx(i1, j), idx(i1, j1), idx(i, j1)])

    return V4, E, F

# ---------- Build the 100-face shape ----------
m, n = 10, 10  # 10×10 => 100 rectangular faces
V4_base, E, F = duoprism_vertices_edges_faces(m, n)

# Fixed pose so the 3D frame is stationary (just 4D motion)
POSE = rot4(0, 3, np.deg2rad(25)) @ rot4(1, 3, np.deg2rad(18)) @ rot4(2, 3, np.deg2rad(10))
V4_pose = V4_base @ POSE.T

# ---------- Figure & artists ----------
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.set_title("Duoprism C10 × C10 — 100 faces, uniform pattern")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.set_box_aspect([1, 1, 1])
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-3, 3)

# Edges
edge_lines = [ax.plot([], [], [], linewidth=0.8)[0] for _ in E]

# Faces: one Poly3DCollection with UNIFORM color/pattern
faces_collection = Poly3DCollection([], facecolors=(0.15, 0.6, 0.85, 0.22), edgecolors=None)
ax.add_collection3d(faces_collection)

# ---------- Animation state ----------
running = True
perspective = True
dist = 4.0
# Rotate in three independent 4D planes to create depth motion
omega = np.deg2rad(1.0)  # base angular speed
angles = np.zeros(3)     # (x–w, y–w, z–w)

def on_key(e):
    global running, omega, perspective
    if e.key == ' ':
        running = not running
    elif e.key == '+':
        omega = min(np.deg2rad(20), omega * 1.25)
    elif e.key == '-':
        omega = max(np.deg2rad(0.1), omega * 0.8)
    elif e.key == 'o':
        perspective = not perspective
    elif e.key == 'r':
        ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-3, 3)

fig.canvas.mpl_connect('key_press_event', on_key)

# ---------- Animation step ----------
def update(_):
    global angles
    if running:
        angles += np.array([omega, 0.8*omega, 1.2*omega])

    Rxw = rot4(0, 3, angles[0])
    Ryw = rot4(1, 3, angles[1])
    Rzw = rot4(2, 3, angles[2])

    V4_now = (V4_pose @ Rxw.T) @ Ryw.T @ Rzw.T
    V3 = project4_to_3(V4_now, perspective=perspective, d=dist)

    # Update faces (uniform color/pattern)
    polys = [[V3[i], V3[j], V3[k], V3[l]] for (i, j, k, l) in F]
    faces_collection.set_verts(polys)

    # Update edges
    for ln, (a, b) in zip(edge_lines, E):
        ln.set_data([V3[a, 0], V3[b, 0]], [V3[a, 1], V3[b, 1]])
        ln.set_3d_properties([V3[a, 2], V3[b, 2]])

    return edge_lines + [faces_collection]

ani = FuncAnimation(fig, update, interval=16, blit=False)  # ~60 FPS
plt.show()
