import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Rover base: Circle
theta = np.linspace(0, 2 * np.pi, 100)
x_base = 0.3 * np.cos(theta)
y_base = 0.3 * np.sin(theta)
z_base = np.zeros_like(theta)
ax.plot(x_base, y_base, z_base, color="brown", label="Rover Base")

# Parameters for solar panel limbs
panel_length = 1.0  # Length of each panel segment
panel_width = 0.2   # Width of each panel
num_limbs = 8       # Number of solar panel limbs
angles = np.linspace(0, 2 * np.pi, num_limbs, endpoint=False)  # Limb angles

# Create solar panels
for angle in angles:
    # Base of the panel (fixed to rover)
    base_x = [0]  # Starting point at the rover center
    base_y = [0]
    base_z = [0]

    # Panel vertices (rectangles extending outward)
    panel_vertices = [
        [base_x[0], base_y[0], base_z[0]],  # Center (Base connection)
        [panel_length * np.cos(angle), panel_length * np.sin(angle), 0.1],  # Bottom-left corner of panel
        [panel_length * np.cos(angle) - panel_width * np.sin(angle), panel_length * np.sin(angle) + panel_width * np.cos(angle), 0.1],  # Top-left corner of panel
        [panel_length * np.cos(angle) - panel_width * np.sin(angle), panel_length * np.sin(angle) + panel_width * np.cos(angle), 0.3],  # Top-right corner
    ]

    # Adding filled panel (fully solid limb)
    panel = Poly3DCollection([panel_vertices], facecolor="blue", edgecolor="black", alpha=0.8)
    ax.add_collection3d(panel)

# Set limits for better view
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-1, 1])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("8-Limb Foldable Solar Panel System for Mars Curiosity")

# Show plot
plt.legend()
plt.show()