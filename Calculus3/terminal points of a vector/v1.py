import matplotlib.pyplot as plt

# Define points
A = (2, 0)
B = (5, 3)
dx = B[0] - A[0]
dy = B[1] - A[1]

# Plot
plt.figure(figsize=(6, 6))
plt.quiver(A[0], A[1], dx, dy, angles='xy', scale_units='xy', scale=1, color='blue', label='Vector v')
plt.scatter(*A, color='red', label='Initial Point A (2, 0)')
plt.scatter(*B, color='green', label='Terminal Point B (5, 3)')

# Axes setup
plt.xlim(0, 7)
plt.ylim(-1, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.title("Directed Line Segment from A to B")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.legend()
plt.show()
