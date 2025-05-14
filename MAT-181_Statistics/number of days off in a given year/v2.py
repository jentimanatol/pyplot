
import matplotlib.pyplot as plt

# Define the edges of the bins
bins = [0, 2, 5, 8, 11, 14, 17]

# Frequencies
frequencies = [10, 1, 7, 7, 1, 4]

# Create the histogram
plt.hist([0]*frequencies[0] + [3]*frequencies[1] + [7]*frequencies[2] + [10]*frequencies[3] + [13]*frequencies[4] + [16]*frequencies[5], bins=bins, edgecolor='black')

# Add titles and labels
plt.title('Histogram of Days Off for Police Detectives')
plt.xlabel('Days Off')
plt.ylabel('Frequency')

# Set x-axis ticks to bin edges
plt.xticks(bins)

# Display the histogram
plt.show()
