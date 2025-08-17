# 4D hypercube (tesseract) -> 3D projection plot
# Edit the angles below to see different projections.
import numpy as np
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ---- Parameters you can tweak ----
angle_xw = np.deg2rad(25)  # rotation in x–w plane
angle_yw = np.deg2rad(35)  # rotation in y–w plane
angle_zw = np.deg2rad(15)  # rotation in z–w plane
perspective = True         # True -> perspective; False -> orthographic
d = 3.0                    # perspective distance (bigger -> weaker perspective)
# ----------------------------------

# Generate 16 vertices of a 4D hypercube (±1 in each coordinate)
verts4 = np.array(list(itertools.product([-1, 1], repeat=4)), dtype=float)  # (16,4)

# Build rotation matrices in 4D for planes xw, yw, zw
def rot4_xw(theta):
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[0,0], R[0,3] = c, -s
    R[3,0], R[3,3] = s,  c
    return R

def rot4_yw(theta):
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[1,1], R[1,3] = c, -s
    R[3,1], R[3,3] = s,  c
    return R

def rot4_zw(theta):
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[2,2], R[2,3] = c, -s
    R[3,2], R[3,3] = s,  c
    return R

# Apply combined rotation
R = rot4_xw(angle_xw) @ rot4_yw(angle_yw) @ rot4_zw(angle_zw)
verts4_rot = verts4 @ R.T  # shape (16,4)

# Project 4D -> 3D
if perspective:
    # simple perspective divide using w
    w = verts4_rot[:, 3]
    factor = d / (d - w)  # avoid divide by zero if w==d
    verts3 = verts4_rot[:, :3] * factor[:, None]
else:
    # orthographic: just drop w
    verts3 = verts4_rot[:, :3]

# Determine edges: connect vertices that differ by exactly one coordinate
edges = []
for i in range(len(verts4)):
    for j in range(i+1, len(verts4)):
        if np.sum(np.abs(verts4[i] - verts4[j])) == 2:  # differs by one coordinate (from -1 to 1 -> |diff|=2)
            edges.append((i, j))

# Plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Draw edges
for i, j in edges:
    xs = [verts3[i,0], verts3[j,0]]
    ys = [verts3[i,1], verts3[j,1]]
    zs = [verts3[i,2], verts3[j,2]]
    ax.plot(xs, ys, zs, linewidth=1)

# Draw vertices
ax.scatter(verts3[:,0], verts3[:,1], verts3[:,2], s=30)

# Labels & formatting
ax.set_title("Tesseract (4D hypercube) → 3D projection")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_box_aspect([1,1,1])

plt.show()
