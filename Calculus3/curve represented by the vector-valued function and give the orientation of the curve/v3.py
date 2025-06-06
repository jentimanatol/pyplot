import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter t
t = np.linspace(-5, 5, 100)

# Vector-valued function r(t) = (t+1, 3t-1, 2t)
x = t + 1
y = 3 * t - 1
z = 2 * t



# Fix index error by adjusting the arrow indices to avoid out-of-bounds
arrow_indices = np.linspace(0, len(t) - 2, 10, dtype=int)

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the curve
ax.plot(x, y, z, label='r(t)', color='blue')

# Orientation arrows
for i in arrow_indices:
    ax.quiver(x[i], y[i], z[i], x[i+1]-x[i], y[i+1]-y[i], z[i+1]-z[i],
              color='red', arrow_length_ratio=0.2)

# Axes lines
max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0
mid_x = (x.max()+x.min()) * 0.5
mid_y = (y.max()+y.min()) * 0.5
mid_z = (z.max()+z.min()) * 0.5

# Plot coordinate axes with labels
ax.plot([mid_x - max_range, mid_x + max_range], [mid_y, mid_y], [mid_z, mid_z], 'k--')
ax.plot([mid_x, mid_x], [mid_y - max_range, mid_y + max_range], [mid_z, mid_z], 'k--')
ax.plot([mid_x, mid_x], [mid_y, mid_y], [mid_z - max_range, mid_z + max_range], 'k--')

# Set labels
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

# Set ticks for better readability
ax.set_xticks(np.arange(int(x.min()), int(x.max())+1, 2))
ax.set_yticks(np.arange(int(y.min()), int(y.max())+1, 5))
ax.set_zticks(np.arange(int(z.min()), int(z.max())+1, 5))

ax.set_title('Plot of r(t) = (t+1)i + (3t−1)j + 2tk with Orientation')
ax.legend()
plt.tight_layout()
plt.show()
