import matplotlib.pyplot as plt
import numpy as np

# Circle equation: (x - h)^2 + (y - k)^2 = r^2
h, k, r = 3, 10, np.sqrt(65)

# Default points
default_points = [(-1, 3), (-4, 6), (2, 2)]

# Ask user for additional points
print("Enter extra points (x,y) one by one, or press Enter to stop.")
extra_points = []
while True:
    user_input = input("Enter point as x,y (or just Enter to finish): ")
    if user_input.strip() == "":
        break
    try:
        x, y = map(float, user_input.split(","))
        extra_points.append((x, y))
    except:
        print("Invalid format. Please enter as x,y (example: 2.5,3)")

# Create circle points for plotting
theta = np.linspace(0, 2*np.pi, 400)
x_vals = h + r * np.cos(theta)
y_vals = k + r * np.sin(theta)

# Plot circle
plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, 'r-', label=f"Circle: (x-{h})² + (y-{k})² = {r**2:.0f}")

# Plot default points
for (x, y) in default_points:
    plt.scatter(x, y, color="blue", s=80, zorder=5)
    plt.text(x+0.2, y, f"({x},{y})", fontsize=9, color="blue")

# Plot extra user points
for (x, y) in extra_points:
    plt.scatter(x, y, color="green", s=80, zorder=5)
    plt.text(x+0.2, y, f"({x},{y})", fontsize=9, color="green")

# Axis formatting
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True, linestyle="--", alpha=0.6)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Circle through (-1,3), (-4,6), (2,2)")
plt.legend()
plt.show()
