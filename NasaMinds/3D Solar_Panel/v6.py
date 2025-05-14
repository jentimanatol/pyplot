import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import numpy as np

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Mars walker base: Circle
theta = np.linspace(0, 2 * np.pi, 100)
x_base = 0.3 * np.cos(theta)
y_base = 0.3 * np.sin(theta)
z_base = np.zeros_like(theta)
ax.plot(x_base, y_base, z_base, color="brown", label="Base")

# Foldable antenna limbs (6 limbs radiating outward)
antenna_length = [0.5, 1.0, 1.5]  # Lengths of foldable segments
limb_angles = np.linspace(0, 2 * np.pi, 6, endpoint=False)  # Angles for 6 limbs

for angle in limb_angles:
    x_limb = [0]  # Start at the base center
    y_limb = [0]
    z_limb = [0]

    for length in antenna_length:
        x_limb.append(length * np.cos(angle))
        y_limb.append(length * np.sin(angle))
        z_limb.append(length * 0.1)  # Slight upward tilt for limbs

    ax.plot(x_limb, y_limb, z_limb, color="blue", linewidth=2, label="Foldable limb")

# Set limits for better view
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-1, 1])

# Set labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Title
ax.set_title("Mars Walker with 6-Limb Foldable Antenna")

# Show plot
plt.legend()
plt.show()