# duotorus_tunnel_shaded_4d.py
# Smooth "real tunnel" in 4D (duotorus S1×S1) → 3D, fully colored curved surface.
# Depth-based coloring + 4D rotation yields a tunnel effect.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ---------- 4D helpers ----------
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

# Parametric duotorus in R^4: (cos u, sin u, cos v, sin v)
def duotorus_grid(nu, nv):
    u = np.linspace(0, 2*np.pi, nu, endpoint=False)
    v = np.linspace(0, 2*np.pi, nv, endpoint=False)
    U, V = np.meshgrid(u, v, indexing="ij")    # shapes (nu, nv)
    x = np.cos(U); y = np.sin(U); z = np.cos(V); w = np.sin(V)
    P4 = np.stack([x, y, z, w], axis=-1)       # (nu, nv, 4)
    return U, V, P4

# ---------- Figure & state ----------
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection="3d")
ax.set_title("4D Tunnel (Duotorus) — fully colored curved surface")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.set_box_aspect([1, 1, 1])
ax.set_xlim(-2.4, 2.4); ax.set_ylim(-2.4, 2.4); ax.set_zlim(-2.4, 2.4)

# Animation state
running = True
perspective = True
dist = 3.5
omega = np.deg2rad(1.2)
angles = np.zeros(3)  # (x–w, y–w, z–w)

# Smoothness (grid resolution)
NU, NV = 64, 128          # base grid (higher = smoother)
STRIPS = 48               # how many colored "bands" along v (tunnel direction)

# Pre-tilt to set a nice stationary 3D pose; only 4D rotation changes each frame
POSE = rot4(0, 3, np.deg2rad(28)) @ rot4(1, 3, np.deg2rad(17)) @ rot4(2, 3, np.deg2rad(9))

# Build base grid in 4D
U, V, P4_grid = duotorus_grid(NU, NV)

# A single Poly3DCollection holding all colored quads ("faces") of the tunnel
surface = Poly3DCollection([], edgecolors=None)
ax.add_collection3d(surface)

# ---------- Controls ----------
def reset_view():
    ax.set_xlim(-2.4, 2.4); ax.set_ylim(-2.4, 2.4); ax.set_zlim(-2.4, 2.4)

def on_key(evt):
    global running, omega, perspective, STRIPS
    if evt.key == ' ':
        running = not running
    elif evt.key == '+':
        omega = min(np.deg2rad(25), omega * 1.25)
    elif evt.key == '-':
        omega = max(np.deg2rad(0.1), omega * 0.8)
    elif evt.key == 'o':
        perspective = not perspective
    elif evt.key == ']':
        STRIPS = int(np.clip(STRIPS + 4, 8, 200))
    elif evt.key == '[':
        STRIPS = int(np.clip(STRIPS - 4, 8, 200))
    elif evt.key == 'r':
        reset_view()

fig.canvas.mpl_connect('key_press_event', on_key)

# ---------- Tunnel coloring ----------
def make_tunnel_quads(V3, W4):
    """
    Build tunnel quads and RGBA colors.
    We slice the parameter v into STRIPS bands, and for each band we create
    curved quad strips (no sharp corners) colored by average 4D w (depth).
    """
    # V3, W4 have shape (NU, NV, 3) and (NU, NV), respectively.
    # Index along v (second axis) to form "rings" around the tunnel.
    nv_band = NV // STRIPS
    polys, colors = [], []

    # Normalize w to [0,1] per-frame for depth-based color/alpha
    wmin, wmax = np.min(W4), np.max(W4)
    span = max(wmax - wmin, 1e-9)

    for j0 in range(0, NV, nv_band):
        j1 = (j0 + nv_band) % NV
        # Build NU quads around the ring: (i,j0)->(i+1,j0)->(i+1,j1)->(i,j1)
        for i in range(NU):
            i1 = (i + 1) % NU
            p00 = V3[i,  j0]; p10 = V3[i1, j0]
            p11 = V3[i1, j1]; p01 = V3[i,  j1]
            polys.append([p00, p10, p11, p01])

            # Average w for depth cue
            w_avg = (W4[i, j0] + W4[i1, j0] + W4[i1, j1] + W4[i, j1]) / 4.0
            t = (w_avg - wmin) / span  # 0..1
            # Color mapping: near (t high) → brighter & slightly more opaque
            # base hue roughly teal; modulate brightness & alpha by t
            base = np.array([0.12, 0.55, 0.90])
            rgb = base * (0.65 + 0.35 * t)         # brighten with t
            alpha = 0.14 + 0.20 * t                # 0.14..0.34
            colors.append((*rgb.tolist(), float(alpha)))
    return polys, colors

# ---------- Animation ----------
def animate(_):
    global angles
    if running:
        angles += np.array([omega, 0.8*omega, 1.2*omega])

    # Rotate entire 4D grid (apply fixed pose once, then per-frame rotation)
    Rxw = rot4(0, 3, angles[0])
    Ryw = rot4(1, 3, angles[1])
    Rzw = rot4(2, 3, angles[2])
    R = Rxw @ Ryw @ Rzw

    P4_now = (P4_grid @ POSE.T) @ R.T                      # (NU, NV, 4)
    V3 = project4_to_3(P4_now.reshape(-1, 4), perspective=perspective, d=dist)
    V3 = V3.reshape(NU, NV, 3)
    W4 = P4_now[..., 3]

    polys, cols = make_tunnel_quads(V3, W4)
    surface.set_verts(polys)
    surface.set_facecolor(cols)

    return [surface]

ani = FuncAnimation(fig, animate, interval=16, blit=False)  # ~60 FPS
plt.show()
