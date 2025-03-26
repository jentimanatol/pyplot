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
num_bends = 8  # Number of fold lines (perpendicular bends within a single lip)
bend_angle = np.radians(5)  # Fold angle per section in radians (5 degrees)
panel_width = 0.1  # Thickness of each panel for clarity

# Generate each segment with perpendicular bending
for i in range(num_segments):
    # Define the base angle for the segment
    angle_start = angles[i]
    angle_end = angles[i + 1]
    segment_center_angle = (angle_start + angle_end) / 2  # Center angle of the lip

    # Generate the fold points along the lip
    x_points = np.linspace(0, radius, num_bends + 1)  # Points from center to edge
    z_points = np.zeros_like(x_points)  # Initialize Z values
    for j in range(1, len(z_points)):  # Apply the bend progressively
        z_points[j] = z_points[j - 1] + np.tan(bend_angle) * (x_points[j] - x_points[j - 1])

    # Create the two outer edges of the lip
    outer_x = x_points * np.cos(segment_center_angle)
    outer_y = x_points * np.sin(segment_center_angle)
    outer_z = z_points

    inner_x = outer_x - panel_width * np.sin(segment_center_angle)
    inner_y = outer_y + panel_width * np.cos(segment_center_angle)
    inner_z = outer_z

    # Create the panels between the outer and inner edges
    for j in range(len(x_points) - 1):
        vertices = [
            [outer_x[j], outer_y[j], outer_z[j]],       # Outer edge current point
            [outer_x[j + 1], outer_y[j + 1], outer_z[j + 1]],  # Outer edge next point
            [inner_x[j + 1], inner_y[j + 1], inner_z[j + 1]],  # Inner edge next point
            [inner_x[j], inner_y[j], inner_z[j]],       # Inner edge current point
        ]
        # Add the filled panel
        panel = Poly3DCollection([vertices], facecolor="blue", edgecolor="black", alpha=0.8)
        ax.add_collection3d(panel)

# Set limits for better visualization
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1, 1])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Foldable Octagonal Solar Panel with Perpendicular Bends")

# Display the plot
plt.show()