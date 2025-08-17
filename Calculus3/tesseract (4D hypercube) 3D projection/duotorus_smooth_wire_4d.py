# duotorus_smooth_wire_4d.py
# Smooth 4D duotorus (S1 x S1 in R^4) → 3D projection with curved wireframe.
# No flat faces; no corners—just smooth iso-u and iso-v curves under 4D rotation.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ---------------- 4D math helpers ----------------
def rot4(i, j, theta):
    """4x4 rotation in (i,j) plane by angle theta (radians)."""
    R = np.eye(4)
    c, s = np.cos(theta), np.sin(theta)
    R[i, i] = c;  R[i, j] = -s
    R[j, i] = s;  R[j, j] =  c
    return R

def project4_to_3(P4, perspective=True, d=3.5):
    """Project Nx4 → Nx3 using simple perspective via w (or orthographic)."""
    if not perspective:
        return P4[:, :3]
    w = np.clip(P4[:, 3], -d + 1e-6, d - 1e-6)
    f = d / (d - w)
    return P4[:, :3] * f[:, None]

# Parametric duotorus in R^4: (cos u, sin u, cos v, sin v)
def duotorus_grid(nu, nv):
    u = np.linspace(0, 2*np.pi, nu, endpoint=False)
    v = np.linspace(0, 2*np.pi, nv, endpoint=False)
    U, V = np.meshgrid(u, v, indexing="ij")  # shapes (nu, nv)
    x = np.cos(U); y = np.sin(U); z = np.cos(V); w = np.sin(V)
    # stack into (nu*nv, 4)
    P4 = np.stack([x, y, z, w], axis=-1).reshape(-1, 4)
    return U, V, P4

# ---------------- Figure & state ----------------
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection="3d")
ax.set_title("Smooth duotorus (S¹×S¹ in 4D) — curved wireframe, 4D rotation")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.set_box_aspect([1, 1, 1])
ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5); ax.set_zlim(-2.5, 2.5)

# Animation state
running = True
perspective = True
dist = 3.5
omega = np.deg2rad(1.2)      # base angular speed
angles = np.zeros(3)         # (x–w, y–w, z–w)

# Smoothness / density (number of iso-curves and points per curve)
n_iso_u = 24     # number of constant-u curves
n_iso_v = 24     # number of constant-v curves
pts_per_curve = 200

# Pre-tilt pose (fixed) so frame stays stationary in 3D
POSE = rot4(0, 3, np.deg2rad(30)) @ rot4(1, 3, np.deg2rad(18)) @ rot4(2, 3, np.deg2rad(12))

# Prepare artists: lists of Line3D objects for iso-u and iso-v families
iso_u_lines = [ax.plot([], [], [], linewidth=1.0)[0] for _ in range(n_iso_u)]
iso_v_lines = [ax.plot([], [], [], linewidth=1.0)[0] for _ in range(n_iso_v)]

def reset_view():
    ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5); ax.set_zlim(-2.5, 2.5)

def rebuild_lines():
    """Recreate line artists if smoothness changed."""
    global iso_u_lines, iso_v_lines
    # Remove old lines from axes
    for ln in iso_u_lines + iso_v_lines:
        ln.remove()
    # Recreate with new counts
    iso_u_lines = [ax.plot([], [], [], linewidth=1.0)[0] for _ in range(n_iso_u)]
    iso_v_lines = [ax.plot([], [], [], linewidth=1.0)[0] for _ in range(n_iso_v)]
    fig.canvas.draw_idle()

def on_key(evt):
    global running, omega, perspective, n_iso_u, n_iso_v
    if evt.key == ' ':
        running = not running
    elif evt.key == '+':
        omega = min(np.deg2rad(25), omega * 1.25)
    elif evt.key == '-':
        omega = max(np.deg2rad(0.1), omega * 0.8)
    elif evt.key == 'o':
        perspective = not perspective
    elif evt.key == ']':
        n_iso_u = min(n_iso_u + 2, 120); n_iso_v = min(n_iso_v + 2, 120); rebuild_lines()
    elif evt.key == '[':
        n_iso_u = max(n_iso_u - 2, 4);   n_iso_v = max(n_iso_v - 2, 4);   rebuild_lines()
    elif evt.key == 'r':
        reset_view()

fig.canvas.mpl_connect('key_press_event', on_key)

def compute_curves(angles_now):
    """
    Build the smooth iso-curves after 4D rotation.
    Returns lists of (X, Y, Z) arrays for plotting.
    """
    # Build rotations for this frame
    Rxw = rot4(0, 3, angles_now[0])
    Ryw = rot4(1, 3, angles_now[1])
    Rzw = rot4(2, 3, angles_now[2])
    R = Rxw @ Ryw @ Rzw

    # ----- Constant-u curves (u fixed, v varies) -----
    u_vals = np.linspace(0, 2*np.pi, n_iso_u, endpoint=False)
    v_vals = np.linspace(0, 2*np.pi, pts_per_curve)
    cu, su = np.cos(u_vals), np.sin(u_vals)
    cv, sv = np.cos(v_vals), np.sin(v_vals)

    iso_u_xyz = []
    for (cu_i, su_i) in zip(cu, su):
        # Curve in 4D: [(cu_i, su_i, cos v, sin v)] for v in v_vals
        P4 = np.stack([
            np.full_like(v_vals, cu_i),
            np.full_like(v_vals, su_i),
            cv,
            sv
        ], axis=-1)  # shape (N,4)
        # Apply fixed pose then per-frame 4D rotation
        P4 = (P4 @ POSE.T) @ R.T
        P3 = project4_to_3(P4, perspective=perspective, d=dist)
        iso_u_xyz.append((P3[:, 0], P3[:, 1], P3[:, 2]))

    # ----- Constant-v curves (v fixed, u varies) -----
    v_vals2 = np.linspace(0, 2*np.pi, n_iso_v, endpoint=False)
    u_vals2 = np.linspace(0, 2*np.pi, pts_per_curve)
    cu2, su2 = np.cos(u_vals2), np.sin(u_vals2)
    cv2, sv2 = np.cos(v_vals2), np.sin(v_vals2)

    iso_v_xyz = []
    for (cv_j, sv_j) in zip(cv2, sv2):
        # Curve in 4D: [(cos u, sin u, cv_j, sv_j)] for u in u_vals2
        P4 = np.stack([
            cu2,
            su2,
            np.full_like(u_vals2, cv_j),
            np.full_like(u_vals2, sv_j)
        ], axis=-1)
        P4 = (P4 @ POSE.T) @ R.T
        P3 = project4_to_3(P4, perspective=perspective, d=dist)
        iso_v_xyz.append((P3[:, 0], P3[:, 1], P3[:, 2]))

    return iso_u_xyz, iso_v_xyz

def animate(_frame):
    global angles
    if running:
        angles += np.array([omega, 0.8*omega, 1.2*omega])

    iso_u_xyz, iso_v_xyz = compute_curves(angles)

    # Update iso-u lines
    for ln, (X, Y, Z) in zip(iso_u_lines, iso_u_xyz):
        ln.set_data(X, Y)
        ln.set_3d_properties(Z)

    # Update iso-v lines
    for ln, (X, Y, Z) in zip(iso_v_lines, iso_v_xyz):
        ln.set_data(X, Y)
        ln.set_3d_properties(Z)

    return iso_u_lines + iso_v_lines

ani = FuncAnimation(fig, animate, interval=16, blit=False)  # ~60 FPS
plt.show()
