# brand_new_tesseract_anim.py
# Completely new implementation: 4D tesseract → 3D animated projection
# with colored square faces and wireframe edges.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from itertools import product, combinations

# -------------------------------
# 4D math & geometry (new names)
# -------------------------------
def R4_plane(a, b, ang):
    """4×4 rotation in the (a,b) plane by angle ang (radians)."""
    M = np.eye(4)
    c, s = np.cos(ang), np.sin(ang)
    M[a, a] = c;  M[a, b] = -s
    M[b, a] = s;  M[b, b] =  c
    return M

def proj_4d_to_3d(P, use_persp=True, cam_w=3.5):
    """Project Nx4 → Nx3. Perspective uses w for a simple divide."""
    if not use_persp:
        return P[:, :3]
    w = np.clip(P[:, 3], -cam_w + 1e-6, cam_w - 1e-6)
    scale = cam_w / (cam_w - w)
    return P[:, :3] * scale[:, None]

def tesseract_vertices():
    """16 vertices at (±1, ±1, ±1, ±1)."""
    return np.array(list(product([-1, 1], repeat=4)), dtype=float)

def tesseract_edges(V):
    """Pairs of indices that differ in exactly one coordinate."""
    idx = np.arange(len(V))
    pairs = []
    for i in idx:
        for j in idx[i+1:]:
            if np.sum(np.abs(V[i] - V[j])) == 2:  # one flip of ±1
                pairs.append((i, j))
    return pairs

def tesseract_square_faces(V):
    """
    Return list of faces, each as 4 vertex indices.
    For each choice of 2 varying coords, fix the other 2 to ±1.
    """
    faces = []
    coords = [0, 1, 2, 3]
    # map vertex tuple to index
    lut = {tuple(v): k for k, v in enumerate(V)}
    for a, b in combinations(coords, 2):       # vary a,b; fix the rest
        c, d = [x for x in coords if x not in (a, b)]
        for sc in (-1, 1):
            for sd in (-1, 1):
                # corners in (a,b): (-,-), (+,-), (+,+), (-,+)
                poly = []
                for sa, sb in [(-1,-1),(1,-1),(1,1),(-1,1)]:
                    v = [0,0,0,0]
                    v[a] = sa; v[b] = sb; v[c] = sc; v[d] = sd
                    poly.append(lut[tuple(v)])
                faces.append(poly)
    return faces  # 24 quads

# -------------------------------
# Build base shape & pre-pose
# -------------------------------
V4_base = tesseract_vertices()
E = tesseract_edges(V4_base)
F = tesseract_square_faces(V4_base)

# A fixed “nice” orientation: tip the shape into w slightly
POSE = R4_plane(0, 3, np.deg2rad(32)) @ R4_plane(1, 3, np.deg2rad(19)) @ R4_plane(2, 3, np.deg2rad(11))
V4_pose = V4_base @ POSE.T

# -------------------------------
# Figure & artists
# -------------------------------
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.set_title("Tesseract (4D hypercube) — brand-new 4D rotation visualizer")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.set_box_aspect([1, 1, 1])

# Edge artists
edge_lines = [ax.plot([], [], [], linewidth=1)[0] for _ in E]

# Face artist (single Poly3DCollection we update each frame)
face_collection = Poly3DCollection([], edgecolors=None, alpha=0.25)
ax.add_collection3d(face_collection)

# Camera box
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-3, 3)

# -------------------------------
# Animation state & controls
# -------------------------------
running = True
omega = np.deg2rad(1.5)  # base angular speed (rad/frame)
angles = np.zeros(3)     # (xw, yw, zw)
persp = True
cam_w = 3.5
show_faces = True
show_edges = True

def reset_view():
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-3, 3)

def on_key(evt):
    global running, omega, persp, show_faces, show_edges
    if evt.key == ' ':
        running = not running
    elif evt.key == '+':
        omega = min(np.deg2rad(25), omega * 1.25)
    elif evt.key == '-':
        omega = max(np.deg2rad(0.1), omega * 0.8)
    elif evt.key == 'o':
        persp = not persp
    elif evt.key == 'f':
        show_faces = not show_faces
        if not show_faces:
            face_collection.set_verts([])
    elif evt.key == 'e':
        show_edges = not show_edges
        for ln in edge_lines:
            ln.set_visible(show_edges)
    elif evt.key == 'r':
        reset_view()

fig.canvas.mpl_connect('key_press_event', on_key)

# -------------------------------
# Helpers for face coloring
# -------------------------------
def build_face_polys_and_colors(V4_now, V3_now):
    """
    Create 3D polygons and RGBA colors.
    Color/alpha encodes average w of each face (near vs far in 4D).
    """
    polys = []
    w_avg = []
    for face in F:
        idx = np.array(face)
        polys.append([V3_now[i] for i in idx])
        w_avg.append(float(np.mean(V4_now[idx, 3])))

    w_avg = np.array(w_avg)
    if np.ptp(w_avg) < 1e-9:  # fixed for NumPy 2.0+
        t = np.zeros_like(w_avg)
    else:
        t = (w_avg - w_avg.min()) / np.ptp(w_avg)

    # Map t ∈ [0,1] to color/alpha (near = higher alpha)
    base = np.array([0.12, 0.55, 0.90])   # teal-ish
    alphas = 0.12 + 0.22 * t              # 0.12..0.34
    colors = [(*base, float(a)) for a in alphas]
    return polys, colors

# -------------------------------
# Animation step
# -------------------------------
def animate(_):
    global angles
    if running:
        angles += np.array([omega, 0.8*omega, 1.2*omega])  # rotate in x–w, y–w, z–w

    Rxw = R4_plane(0, 3, angles[0])
    Ryw = R4_plane(1, 3, angles[1])
    Rzw = R4_plane(2, 3, angles[2])
    V4_now = (V4_pose @ Rxw.T) @ Ryw.T @ Rzw.T

    V3 = proj_4d_to_3d(V4_now, use_persp=persp, cam_w=cam_w)

    # Faces
    if show_faces:
        polys, cols = build_face_polys_and_colors(V4_now, V3)
        face_collection.set_verts(polys)
        face_collection.set_facecolor(cols)
    else:
        face_collection.set_verts([])

    # Edges
    if show_edges:
        for ln, (i, j) in zip(edge_lines, E):
            ln.set_data([V3[i, 0], V3[j, 0]], [V3[i, 1], V3[j, 1]])
            ln.set_3d_properties([V3[i, 2], V3[j, 2]])
    return edge_lines + [face_collection]

# -------------------------------
# Run animation
# -------------------------------
ani = FuncAnimation(fig, animate, interval=16, blit=False)  # ~60 FPS
plt.show()
