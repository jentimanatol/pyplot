import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameters for the octagonal solar panel
radius = 1.0  # Radius of the panel
num_segments = 8  # Number of segments (lips)
angles = np.linspace(0, 2 * np.pi, num_segments + 1)  # Divide the circle into segments
num_bends = 5  # Number of fold lines per lip
bend_angle = np.radians(15)  # Angle of bending per fold
panel_width = 0.1  # Width of each panel segment for clarity

# Generate alternating bending lips
for i in range(num_segments):
    # Alternating bending direction (up for odd lips, down for even lips)
    bending_direction = 1 if i % 2 == 0 else -1

    # Define the base angle for the segment
    angle_start = angles[i]
    angle_end = angles[i + 1]

    # Generate the fold points along the lip
    x_points = np.linspace(0, radius, num_bends + 1)  # Points from center to edge
    z_points = np.zeros_like(x_points)  # Initialize Z values
    for j in range(1, len(z_points)):  # Apply the bend progressively
        z_points[j] = z_points[j - 1] + bending_direction * np.tan(bend_angle) * (x_points[j] - x_points[j - 1])

    # Create the two outer edges of the lip
    outer_x = x_points * np.cos((angle_start + angle_end) / 2)  # Angle adjusted for continuity
    outer_y = x_points * np.sin((angle_start + angle_end) / 2)
    outer_z = z_points

    inner_x = outer_x - panel_width * np.sin((angle_start + angle_end) / 2)
    inner_y = outer_y + panel_width * np.cos((angle_start + angle_end) / 2)
    inner_z = outer_z

    # Create the panels between the outer and inner edges
    for j in range(len(x_points) - 1):
        vertices = [
            [outer_x[j], outer_y[j], outer_z[j]],  # Outer edge current point
            [outer_x[j + 1], outer_y[j + 1], outer_z[j + 1]],  # Outer edge next point
            [inner_x[j + 1], inner_y[j + 1], inner_z[j + 1]],  # Inner edge next point
            [inner_x[j], inner_y[j], inner_z[j]],  # Inner edge current point
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
ax.set_title("Alternating Bendable Solar Panel with Seamless Lips")

# Display the plot
plt.show()