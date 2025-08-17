# hyper_shapes.py
# Visualize a 4D tesseract (hypercube) and a C16×C4 duoprism via 3D projection.

import itertools
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# -----------------------------
# Utility: simple 4D rotations
# -----------------------------
def rot4(i, j, theta):
    """Return a 4×4 rotation matrix in the (i,j) plane by angle theta."""
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[i, i] = c; R[i, j] = -s
    R[j, i] = s; R[j, j] =  c
    return R

def project4_to_3(P4, perspective=True, d=3.0):
    """
    Project Nx4 -> Nx3.
    perspective=True uses x,y,z times d/(d-w).
    perspective=False just drops w.
    """
    if perspective:
        w = P4[:, 3]
        factor = d / (d - w)
        return P4[:, :3] * factor[:, None]
    else:
        return P4[:, :3]

def draw_edges(ax, V3, edges, lw=1):
    for a, b in edges:
        ax.plot([V3[a,0], V3[b,0]],
                [V3[a,1], V3[b,1]],
                [V3[a,2], V3[b,2]], linewidth=lw)

# ---------------------------------
# Part A: Tesseract (4D hypercube)
# ---------------------------------
def plot_tesseract(angle_xw=25, angle_yw=35, angle_zw=15,
                   perspective=True, d=3.0, show=True):
    """
    Tesseract = 4D hypercube (16 vertices, 32 edges).
    angle_* are degrees for rotations in x–w, y–w, z–w planes.
    """
    # 1) Vertices in 4D (±1, ±1, ±1, ±1)
    V4 = np.array(list(itertools.product([-1, 1], repeat=4)), dtype=float)

    # 2) Edges connect vertices that differ by exactly one coordinate
    edges = []
    for i in range(len(V4)):
        for j in range(i+1, len(V4)):
            if np.sum(np.abs(V4[i] - V4[j])) == 2:  # -1 -> +1 on one axis
                edges.append((i, j))

    # 3) Rotate in 4D
    Rxw = rot4(0, 3, np.deg2rad(angle_xw))
    Ryw = rot4(1, 3, np.deg2rad(angle_yw))
    Rzw = rot4(2, 3, np.deg2rad(angle_zw))
    V4r = (V4 @ Rxw.T) @ Ryw.T @ Rzw.T

    # 4) Project to 3D
    V3 = project4_to_3(V4r, perspective=perspective, d=d)

    # 5) Plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    draw_edges(ax, V3, edges, lw=1)
    ax.scatter(V3[:,0], V3[:,1], V3[:,2], s=30)
    ax.set_title("Tesseract (4D hypercube) → 3D projection")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
    ax.set_box_aspect([1,1,1])
    if show:
        plt.show()
    return fig, ax

# -------------------------------------------------------
# Part B: “Same pattern” with a 16-gon → C16×C4 duoprism
# -------------------------------------------------------
def plot_duoprism(m=16, n=4, angle_xw=20, angle_yw=30, angle_zw=15,
                  perspective=True, d=4.0, show=True):
    """
    Duoprism C_m × C_n: Cartesian product of two polygons.
    For m=16, n=4 you get 64 vertices and 128 edges.
    """
    # 1) Polygons on unit circles in (x,y) and (u,v)
    theta_m = np.linspace(0, 2*np.pi, m, endpoint=False)
    Pm = np.stack([np.cos(theta_m), np.sin(theta_m)], axis=1)
    theta_n = np.linspace(0, 2*np.pi, n, endpoint=False)
    Pn = np.stack([np.cos(theta_n), np.sin(theta_n)], axis=1)

    # 2) 4D vertices: (x,y,u,v)
    V4 = np.array([[xm, ym, xn, yn] for (xm, ym) in Pm for (xn, yn) in Pn], dtype=float)

    # 3) Edges: along m-cycle and n-cycle
    def idx(i, j): return i*n + j
    edges = []
    # edges along m
    for j in range(n):
        for i in range(m):
            edges.append((idx(i, j), idx((i+1) % m, j)))
    # edges along n
    for i in range(m):
        for j in range(n):
            edges.append((idx(i, j), idx(i, (j+1) % n)))

    # 4) Rotate in 4D (mix x,y,u with v as the “w” axis)
    Rxv = rot4(0, 3, np.deg2rad(angle_xw))
    Ryv = rot4(1, 3, np.deg2rad(angle_yw))
    Ruv = rot4(2, 3, np.deg2rad(angle_zw))
    V4r = (V4 @ Rxv.T) @ Ryv.T @ Ruv.T

    # 5) Project to 3D and plot
    V3 = project4_to_3(V4r, perspective=perspective, d=d)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    draw_edges(ax, V3, edges, lw=1)
    ax.scatter(V3[:,0], V3[:,1], V3[:,2], s=20)
    ax.set_title(f"C{m} × C{n} duoprism → 3D projection\n"
                 f"{m*n} vertices, {2*m*n//1} edges")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
    ax.set_box_aspect([1,1,1])
    if show:
        plt.show()
    return fig, ax

# -------------------
# Quick demo runner
# -------------------
if __name__ == "__main__":
    # 1) Tesseract
    plot_tesseract(angle_xw=25, angle_yw=35, angle_zw=15,
                   perspective=True, d=3.0, show=True)

    # 2) C16 × C4 duoprism (your 16-sides pattern)
    plot_duoprism(m=16, n=4, angle_xw=20, angle_yw=30, angle_zw=15,
                  perspective=True, d=4.0, show=True)
