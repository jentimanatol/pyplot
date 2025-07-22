import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Symbolic t values
t_vals = np.linspace(0, 2*np.pi, 400)

# Parametric definitions
x_t = np.cos(t_vals)
y_t = np.sin(t_vals)

# Function definition
def f(x, y):
    return 8*x**2 + 9*x*y - 13*y**2

z_t = f(x_t, y_t)

# Derivatives for chain rule
def df_dx(x, y):
    return 16*x + 9*y

def df_dy(x, y):
    return 9*x - 26*y

def dx_dt(t):
    return -np.sin(t)

def dy_dt(t):
    return np.cos(t)

# Evaluate at t = π/4
t_eval = np.pi / 4
x_eval = np.cos(t_eval)
y_eval = np.sin(t_eval)
z_eval = f(x_eval, y_eval)

dfdx_val = df_dx(x_eval, y_eval)
dfdy_val = df_dy(x_eval, y_eval)
dxdt_val = dx_dt(t_eval)
dydt_val = dy_dt(t_eval)

# Apply chain rule
dzdt = dfdx_val * dxdt_val + dfdy_val * dydt_val

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
X = np.linspace(-1, 1, 100)
Y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
ax.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis', edgecolor='none', label='f(x, y)')

# Parametric curve on surface
ax.plot(x_t, y_t, z_t, color='red', label=r'$\vec{r}(t)$ path on surface')

# Point at t = π/4
ax.scatter(x_eval, y_eval, z_eval, color='black', s=80, label=r'$t = \frac{\pi}{4}$')
ax.text(x_eval, y_eval, z_eval + 10, f'dz/dt = {dzdt:.1f}', fontsize=12, color='black')

# Labels and formatting
ax.set_title(r"Chain Rule: $\frac{dz}{dt} = \frac{\partial f}{\partial x} \cdot \frac{dx}{dt} + \frac{\partial f}{\partial y} \cdot \frac{dy}{dt}$", fontsize=14)
ax.set_xlabel("x(t) = cos(t)")
ax.set_ylabel("y(t) = sin(t)")
ax.set_zlabel("z = f(x, y)")
ax.view_init(elev=30, azim=135)
ax.legend()

plt.tight_layout()
plt.show()
