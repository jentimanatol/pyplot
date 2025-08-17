# tesseract_4d_animation.py
# Animate a 4D tesseract (hypercube) rotating in 4D and projected to 3D.

import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ----- 4D helpers -----
def rot4(i, j, theta):
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[i, i] = c; R[i, j] = -s
    R[j, i] = s; R[j, j] =  c
    return R

def project4_to_3(P4, perspective=True, d=3.5):
    if not perspective:
        return P4[:, :3]
    w = np.clip(P4[:, 3], -d + 1e-6, d - 1e-6)
    f = d / (d - w)
    return P4[:, :3] * f[:, None]

# Vertices (±1, ±1, ±1, ±1)
V4 = np.array(list(itertools.product([-1, 1], repeat=4)), dtype=float)

# Edges (Hamming distance 1)
edges = []
for a in range(len(V4)):
    for b in range(a + 1, len(V4)):
        if np.sum(np.abs(V4[a] - V4[b])) == 2:
            edges.append((a, b))

# Pre-tilt for a nice fixed stance (doesn't change during animation)
R_fixed = rot4(0, 3, np.deg2rad(35)) @ rot4(1, 3, np.deg2rad(22)) @ rot4(2, 3, np.deg2rad(15))
V4_fixed = V4 @ R_fixed.T

# ----- Figure -----
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.set_title("Tesseract (4D hypercube) — 4D rotation → 3D projection")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.set_box_aspect([1, 1, 1])

# Artists for edges
lines = []
for _ in edges:
    line, = ax.plot([], [], [], linewidth=1)  # no explicit color
    lines.append(line)

# State
perspective = True
dist = 3.5
running = True
speed = np.deg2rad(1.4)  # radians per frame (base)
theta = np.zeros(3)      # angles for xw, yw, zw planes

def on_key(event):
    global running, speed, perspective
    if event.key == '+':
        speed = min(np.deg2rad(25), speed * 1.25)
    elif event.key == '-':
        speed = max(np.deg2rad(0.1), speed * 0.8)
    elif event.key == 'p':
        running = not running
    elif event.key == 'o':
        perspective = not perspective

fig.canvas.mpl_connect('key_press_event', on_key)

# Initial limits
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-3, 3)

def update(_frame):
    global theta
    if running:
        theta += np.array([speed, 0.8*speed, 1.2*speed])  # rotate in xw, yw, zw

    Rxw = rot4(0, 3, theta[0])
    Ryw = rot4(1, 3, theta[1])
    Rzw = rot4(2, 3, theta[2])

    V4_now = (V4_fixed @ Rxw.T) @ Ryw.T @ Rzw.T
    V3 = project4_to_3(V4_now, perspective=perspective, d=dist)

    for line, (a, b) in zip(lines, edges):
        line.set_data([V3[a,0], V3[b,0]], [V3[a,1], V3[b,1]])
        line.set_3d_properties([V3[a,2], V3[b,2]])
    return lines

ani = FuncAnimation(fig, update, interval=16, blit=False)  # ~60 FPS
plt.show()
