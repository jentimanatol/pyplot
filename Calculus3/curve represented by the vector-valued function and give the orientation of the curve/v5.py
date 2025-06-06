import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter t values
t = np.linspace(-10, 10, 100)

# Define r(t) components
x = t + 1
y = 3 * t - 1
z = 2 * t

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the vector-valued curve
ax.plot(x, y, z, color='blue', label=r'$\vec{r}(t)$')

# Draw axes arrows manually and place number labels directly on axes
for i in range(-10, 11, 5):
    if i != 0:
        ax.text(i, 0, 0, f'{i}', color='black')  # x-axis labels
        ax.text(0, i, 0, f'{i}', color='black')  # y-axis labels
        ax.text(0, 0, i, f'{i}', color='black')  # z-axis labels

# Add arrows for axes
arrow_length = 12
ax.quiver(0, 0, 0, arrow_length, 0, 0, color='black', arrow_length_ratio=0.05)
ax.quiver(0, 0, 0, 0, arrow_length, 0, color='black', arrow_length_ratio=0.05)
ax.quiver(0, 0, 0, 0, 0, arrow_length, color='black', arrow_length_ratio=0.05)

# Add axis labels at the end of arrows
ax.text(arrow_length, 0, 0, 'x', color='black', fontsize=12)
ax.text(0, arrow_length, 0, 'y', color='black', fontsize=12)
ax.text(0, 0, arrow_length, 'z', color='black', fontsize=12)

# Set limits
ax.set_xlim([-12, 12])
ax.set_ylim([-12, 12])
ax.set_zlim([-12, 12])

# Remove ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Show plot
plt.tight_layout()
plt.show()
