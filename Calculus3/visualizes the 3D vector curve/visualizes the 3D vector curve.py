import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter t from 1 to 4
t = np.linspace(1, 4, 400)

# Vector function components
x = t**2
y = 5 * np.sqrt(t)
z = -1 / t**2

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='blue', linewidth=2, label=r"$\vec{r}(t)$")

# Mark endpoints
ax.scatter(x[0], y[0], z[0], color='green', s=50, label='t = 1 (Start)')
ax.scatter(x[-1], y[-1], z[-1], color='red', s=50, label='t = 4 (End)')

# Axes labels
ax.set_xlabel("x = $t^2$")
ax.set_ylabel("y = $5\\sqrt{t}$")
ax.set_zlabel("z = $-\\frac{1}{t^2}$")
ax.set_title("3D Visualization of Curve $\mathbf{r}(t)$ from $t=1$ to $t=4$")
ax.legend()
ax.grid(True)

# Better 3D view angle
ax.view_init(elev=30, azim=135)

plt.tight_layout()
plt.show()
