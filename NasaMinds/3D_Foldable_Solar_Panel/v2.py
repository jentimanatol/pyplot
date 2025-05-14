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
bend_angle = np.radians(10)  # Angle of bending per trapezoid (10 degrees)

# Generate each segment with trapezoidal bends
for i in range(num_segments):
    # Alternating bending direction for each lip
    bending_direction = 1 if i % 2 == 0 else -1

    # Define the angles for the segment
    angle_start = angles[i]
    angle_end = angles[i + 1]

    # Generate trapezoids along the lip
    for j in range(num_trapezoids):
        inner_radius = j * (radius / num_trapezoids)  # Inner radius of the trapezoid
        outer_radius = (j + 1) * (radius / num_trapezoids)  # Outer radius of the trapezoid

        # Define Z offsets for bending (up/down alternates for continuity)
        inner_z = bending_direction * j * np.tan(bend_angle)
        outer_z = bending_direction * (j + 1) * np.tan(bend_angle)

        # Define the vertices of the trapezoid
        vertices = [
            [inner_radius * np.cos(angle_start), inner_radius * np.sin(angle_start), inner_z],  # Bottom-left
            [outer_radius * np.cos(angle_start), outer_radius * np.sin(angle_start), outer_z],  # Top-left
            [outer_radius * np.cos(angle_end), outer_radius * np.sin(angle_end), outer_z],  # Top-right
            [inner_radius * np.cos(angle_end), inner_radius * np.sin(angle_end), inner_z],  # Bottom-right
        ]

        # Add the filled trapezoid
        trapezoid = Poly3DCollection([vertices], facecolor="blue", edgecolor="black", alpha=0.8)
        ax.add_collection3d(trapezoid)

# Set limits for better visualization
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1, 1])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Alternating Trapezoidal Solar Panel with Seamless Lips")

# Display the plot
plt.show()