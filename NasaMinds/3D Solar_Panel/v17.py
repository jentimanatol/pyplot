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
num_trapezoids = 5  # Number of trapezoids per lip
bend_angle_parallel = np.radians(5)  # Fold angle parallel
bend_angle_perpendicular = np.radians(5)  # Fold angle perpendicular

# Generate each segment with trapezoidal bends
for i in range(num_segments):
    # Define the base angle for the segment
    angle_start = angles[i]
    angle_end = angles[i + 1]
    segment_center_angle = (angle_start + angle_end) / 2  # Center angle of the lip

    # Create the trapezoids along the lip
    for j in range(num_trapezoids):
        inner_radius = j * (radius / num_trapezoids)  # Inner radius of trapezoid
        outer_radius = (j + 1) * (radius / num_trapezoids)  # Outer radius of trapezoid

        # Define the tilt for the trapezoid
        inner_z_offset = j * np.tan(bend_angle_parallel)  # Parallel fold
        outer_z_offset = (j + 1) * np.tan(bend_angle_parallel)  # Parallel fold
        inner_z_perpendicular = np.tan(j * bend_angle_perpendicular)  # Perpendicular fold
        outer_z_perpendicular = np.tan((j + 1) * bend_angle_perpendicular)  # Perpendicular fold

        # Vertices of the trapezoid
        vertices = [
            [inner_radius * np.cos(angle_start), inner_radius * np.sin(angle_start), inner_z_offset + inner_z_perpendicular],  # Bottom-left
            [outer_radius * np.cos(angle_start), outer_radius * np.sin(angle_start), outer_z_offset + outer_z_perpendicular],  # Top-left
            [outer_radius * np.cos(angle_end), outer_radius * np.sin(angle_end), outer_z_offset - outer_z_perpendicular],  # Top-right
            [inner_radius * np.cos(angle_end), inner_radius * np.sin(angle_end), inner_z_offset - inner_z_perpendicular],  # Bottom-right
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
ax.set_title("Bendable Octagonal Solar Panel with Trapezoidal Sections")

# Display the plot
plt.show()