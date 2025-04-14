import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameters for the octagonal solar panel
radius = 1.0  # Radius of the panel
num_segments = 8  # Number of lips (segments)
angles = np.linspace(0, 2 * np.pi, num_segments + 1)  # Divide the circle into segments
num_trapezoids = 5  # Number of trapezoids per lip

# Generate each segment with alternating Z-values
for i in range(num_segments):
    # Define the angles for the segment
    angle_start = angles[i]
    angle_end = angles[i + 1]

    # Determine whether this lip has normal or reversed Z-values
    if i % 2 == 0:
        left_small_z, left_big_z = 5, 6
        right_small_z, right_big_z = -5, -6
    else:
        left_small_z, left_big_z = -5, -6
        right_small_z, right_big_z = 5, 6

    # Create trapezoids along the lip
    for j in range(num_trapezoids):
        inner_radius = j * (radius / num_trapezoids)  # Inner radius of the trapezoid
        outer_radius = (j + 1) * (radius / num_trapezoids)  # Outer radius of the trapezoid

        # Progressively adjust Z-values for each trapezoid
        inner_left_z = left_small_z + j
        outer_left_z = left_big_z + j
        inner_right_z = right_small_z - j
        outer_right_z = right_big_z - j

        # Vertices of the trapezoid
        vertices = [
            [inner_radius * np.cos(angle_start), inner_radius * np.sin(angle_start), inner_left_z],  # Bottom-left
            [outer_radius * np.cos(angle_start), outer_radius * np.sin(angle_start), outer_left_z],  # Top-left
            [outer_radius * np.cos(angle_end), outer_radius * np.sin(angle_end), outer_right_z],  # Top-right
            [inner_radius * np.cos(angle_end), inner_radius * np.sin(angle_end), inner_right_z],  # Bottom-right
        ]

        # Add the filled trapezoid
        trapezoid = Poly3DCollection([vertices], facecolor="blue", edgecolor="black", alpha=0.8)
        ax.add_collection3d(trapezoid)

# Set limits for better visualization
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-10, 10])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Alternating Tilted Trapezoidal Solar Panels")

# Display the plot
plt.show()