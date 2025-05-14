import matplotlib.pyplot as plt
import numpy as np

# Data
midpoints = [1, 4, 7, 10, 13, 16]
frequencies = [10, 1, 7, 7, 1, 4]

# Calculate the bin edges for the histogram
bin_width = 3
bin_edges = np.arange(0, 18, bin_width)

# Create the histogram
plt.hist(midpoints, bins=bin_edges, weights=frequencies, edgecolor='black', align='mid')

# Labels and title
plt.xlabel('Class Midpoints')
plt.ylabel('Frequency')
plt.title('Histogram of Days Off for Police Detectives')

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for better visualization
plt.show()
