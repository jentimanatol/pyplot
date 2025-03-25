import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameters for the octagonal solar panel
radius = 1.0  # Radius of the octagonal panel
num_segments = 8  # Number of segments (lips)
angles = np.linspace(0, 2 * np.pi, num_segments + 1)  # Divide the circle into segments
tilt_angle = np.radians(45)  # Tilt angle in radians

# Generate each segment with foldable tilt
for i in range(num_segments):
    # Define the vertices of the tilted segment
    if i % 2 == 0:  # Every other segment tilts upward
        vertices = [
            [0, 0, 0],  # Center of the solar panel
            [radius * np.cos(angles[i]), radius * np.sin(angles[i]), radius * np.sin(tilt_angle)],  # Edge 1 (tilted up)
            [radius * np.cos(angles[i + 1]), radius * np.sin(angles[i + 1]), -radius * np.sin(tilt_angle)],  # Edge 2 (tilted down)
        ]
    else:  # Alternate segments tilt downward
        vertices = [
            [0, 0, 0],  # Center of the solar panel
            [radius * np.cos(angles[i]), radius * np.sin(angles[i]), -radius * np.sin(tilt_angle)],  # Edge 1 (tilted down)
            [radius * np.cos(angles[i + 1]), radius * np.sin(angles[i + 1]), radius * np.sin(tilt_angle)],  # Edge 2 (tilted up)
        ]

    # Add the tilted triangular segment
    segment = Poly3DCollection([vertices], facecolor="blue", edgecolor="black", alpha=0.8)
    ax.add_collection3d(segment)

# Set view limits for better visualization
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1, 1])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Partially Folded Concave Octagonal Solar Panel")

# Display the plot
plt.show()