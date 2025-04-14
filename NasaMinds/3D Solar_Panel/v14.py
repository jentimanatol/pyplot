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
num_sub_sections = 8  # Subdivide each lip into 8 sections
tilt_angle = np.radians(5)  # Tilt angle per subsection in radians

# Generate each segment subdivided into foldable sections
for i in range(num_segments):
    # Define the base angle for the segment
    angle_start = angles[i]
    angle_end = angles[i + 1]
    sub_angles = np.linspace(angle_start, angle_end, num_sub_sections + 1)  # Subdivide into subsections

    # Generate subsections with progressive tilt
    for j in range(num_sub_sections):
        vertices = [
            [0, 0, 0],  # Center of the panel
            [radius * np.cos(sub_angles[j]), radius * np.sin(sub_angles[j]), j * np.sin(tilt_angle)],  # Edge point 1
            [radius * np.cos(sub_angles[j + 1]), radius * np.sin(sub_angles[j + 1]), (j + 1) * np.sin(tilt_angle)],  # Edge point 2
        ]

        # Add the filled subsection
        subsection = Poly3DCollection([vertices], facecolor="blue", edgecolor="black", alpha=0.8)
        ax.add_collection3d(subsection)

# Set limits for better visualization
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-0.5, 1])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Foldable Octagonal Solar Panel with Subsections for Mars Walker")

# Display the plot
plt.show()