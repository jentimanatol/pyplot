import numpy as np
import matplotlib.pyplot as plt

# Create a grid of x and y values
x = np.linspace(-4, 4, 400)
y = np.linspace(-4, 4, 400)
X, Y = np.meshgrid(x, y)

# Compute Z = 3x^2 + y^2
Z = 3 * X**2 + Y**2

# Create the contour plot for level curves c = 1 to 5
fig, ax = plt.subplots()
contours = ax.contour(X, Y, Z, levels=[1, 2, 3, 4, 5], colors='black')
ax.clabel(contours, inline=True, fontsize=8)
ax.set_title('Level Curves of $z = 3x^2 + y^2$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal')

plt.grid(True)
plt.show()
