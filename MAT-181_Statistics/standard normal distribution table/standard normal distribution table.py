import matplotlib.pyplot as plt

# Given data
z_scores = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4]
cumulative_areas = [0.5, 0.5398, 0.5793, 0.6179, 0.6554, 0.6915, 0.7257, 0.758, 0.7881, 0.8159, 0.8413, 0.8643, 0.8849, 0.9032, 0.9192, 0.9332, 0.9452, 0.9554, 0.9641, 0.9713, 0.9772, 0.9821, 0.9861, 0.9893, 0.9918, 0.9938, 0.9953, 0.9965, 0.9974, 0.9981, 0.9987, 0.999, 0.9993, 0.9995, 0.9997]

# Plotting the data
plt.plot(z_scores, cumulative_areas, marker='o')
plt.xlabel('z-scores')
plt.ylabel('Cumulative Area from the Left')
plt.title('Standard Normal (z) Distribution: Cumulative Area from the Left')
plt.grid(True)
plt.show()
