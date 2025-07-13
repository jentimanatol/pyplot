import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the endpoints of the line segment
P = np.array([-5, -5, -3])
Q = np.array([-2, -4, -7])

# Parameter t from 0 to 1
t = np.linspace(0, 1, 100)

# Vector-valued function: r(t) = P + t*(Q - P)
r_t = P.reshape(3, 1) + (Q - P).reshape(3, 1) * t

# Extract x, y, z coordinates
x, y, z = r_t[0], r_t[1], r_t[2]

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the line segment
ax.plot(x, y, z, label='Line Segment from P to Q', color='blue')

# Mark points P and Q
ax.scatter(*P, color='red', s=100, label='Point P (t=0)')
ax.scatter(*Q, color='green', s=100, label='Point Q (t=1)')

# Label axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of Line Segment from P to Q')
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.show()
