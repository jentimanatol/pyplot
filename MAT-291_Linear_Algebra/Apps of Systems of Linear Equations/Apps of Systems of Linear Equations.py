import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial function
def p(x):
    return (1/10)*x**3 + (7/2)*x**2 - (13/5)*x

# Points given
points_x = np.array([-1, 0, 1, 4])
points_y = np.array([6, 0, 1, 52])

# Create a smooth range of x values for the curve
x_vals = np.linspace(-2, 5, 400)
y_vals = p(x_vals)

# Plot the polynomial curve
plt.figure(figsize=(8,6))
plt.plot(x_vals, y_vals, 'r-', label=r"$p(x)=\frac{1}{10}x^3+\frac{7}{2}x^2-\frac{13}{5}x$")

# Plot the given points
plt.scatter(points_x, points_y, color='blue', s=80, zorder=5, label="Given points")

# Annotate the points
for (x, y) in zip(points_x, points_y):
    plt.text(x+0.1, y, f"({x},{y})", fontsize=10)

# Add grid, title, labels
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel("x")
plt.ylabel("p(x)")
plt.title("Polynomial through given points")
plt.legend()
plt.show()
