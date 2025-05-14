import matplotlib.pyplot as plt
import numpy as np

# Provided data
z_scores = np.array([0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09,
                     0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1,
                     1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2,
                     2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3,
                     3.1, 3.2, 3.3, 3.4, 3.5])
cumulative_areas = np.array([0.5, 0.504, 0.508, 0.512, 0.516, 0.5199, 0.5239, 0.5279, 0.5319, 0.5359,
                             0.5398, 0.5793, 0.6179, 0.6554, 0.6915, 0.7257, 0.758, 0.7881, 0.8159, 0.8413,
                             0.8643, 0.8849, 0.9032, 0.9192, 0.9332, 0.9452, 0.9554, 0.9641, 0.9713, 0.9772,
                             0.9821, 0.9861, 0.9893, 0.9918, 0.9938, 0.9953, 0.9965, 0.9974, 0.9981, 0.9987,
                             0.999, 0.9993, 0.9995, 0.9997, 0.9999])

# Create the plot
plt.plot(z_scores, cumulative_areas, marker='o', linestyle='-', color='blue')

# Add labels and title
plt.xlabel('Z-Scores')
plt.ylabel('Cumulative Area from the Left')
plt.title('Standard Normal (z) Distribution')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()
