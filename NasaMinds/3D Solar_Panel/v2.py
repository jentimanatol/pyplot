import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Sputnik body: Sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 0.3 * np.outer(np.cos(u), np.sin(v))
y = 0.3 * np.outer(np.sin(u), np.sin(v))
z = 0.3 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, color='silver', alpha=0.8)

# Solar panel: Rectangle
panel_vertices = [
    [-0.6, -0.1, 0],  # Bottom-left
    [-0.6, 0.1, 0],   # Top-left
    [-1.2, 0.1, 0],   # Top-right
    [-1.2, -0.1, 0]   # Bottom-right
]
panel_faces = [panel_vertices]
panel = Poly3DCollection(panel_faces, edgecolor='k', alpha=0.9)
panel.set_facecolor([(0.1, 0.6, 0.8)])  # Light blue for the panel
ax.add_collection3d(panel)

# Antennas: Lines
antenna_length = 1.5
antenna_coords = [
    [[0, 0, 0], [antenna_length, 0, -0.5]],   # Antenna 1
    [[0, 0, 0], [-antenna_length, 0, -0.5]],  # Antenna 2
    [[0, 0, 0], [0, antenna_length, -0.5]],   # Antenna 3
    [[0, 0, 0], [0, -antenna_length, -0.5]]   # Antenna 4
]

for coords in antenna_coords:
    x_line, y_line, z_line = zip(*coords)
    ax.plot(x_line, y_line, z_line, color='black', linewidth=1)

# Set limits for a better view
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-1, 1])

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set title
ax.set_title('3D Model of Sputnik with Solar Antenna')

# Show the plot
plt.show()