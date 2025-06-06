import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameters for the octagonal solar panel
radius = 1.0  # Radius of the octagonal panel
num_segments = 8  # Number of segments (lips)
angles = np.linspace(0, 2 * np.pi, num_segments + 1)  # Divide the circle into 8 parts

# Generate each segment
for i in range(num_segments):
    # Define the vertices of each triangular segment
    vertices = [
        [0, 0, 0],  # Center of the solar panel
        [radius * np.cos(angles[i]), radius * np.sin(angles[i]), 0],  # Edge point 1
        [radius * np.cos(angles[i + 1]), radius * np.sin(angles[i + 1]), 0],  # Edge point 2
    ]
    # Add the filled triangular segment
    segment = Poly3DCollection([vertices], facecolor="blue", edgecolor="black", alpha=0.8)
    ax.add_collection3d(segment)

# Set view limits for better visualization
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([0, 1])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Foldable Octagonal Solar Panel for Mars Walker")

# Display plot
plt.show()