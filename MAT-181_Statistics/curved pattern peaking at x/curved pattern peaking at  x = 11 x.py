import numpy as np
import matplotlib.pyplot as plt

# Given data
x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y = [9.15, 8.13, 8.74, 8.77, 9.26, 8.09, 6.13, 3.11, 9.14, 7.27, 4.74]

# Scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='#4c72b0', s=100, edgecolor='black')
plt.title("Scatterplot of X vs. Y (Nonlinear Pattern)", fontweight='bold')
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, alpha=0.3)
plt.show()