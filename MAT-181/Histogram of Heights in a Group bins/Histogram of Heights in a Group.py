import matplotlib.pyplot as plt
import numpy as np

# New sample height data in inches (converted from feet & inches)
height_data = [59, 60, 60, 61, 62, 63, 64, 65, 66, 66, 67, 68, 69, 70, 70, 71, 
               72, 73, 73, 74, 75, 76, 76, 77, 78, 79, 80, 81, 82, 83, 83, 84, 85]

# Define bins (grouping heights into 3-inch intervals)
bins = [58, 61, 64, 67, 70, 73, 76, 79, 82, 85,88]  # 3-inch bin size

# Create histogram
plt.figure(figsize=(8, 6))
plt.hist(height_data, bins=bins, edgecolor="black", alpha=0.7, color="skyblue")

# Labels and title
plt.xlabel("Height (inches)")
plt.ylabel("Number of People")
plt.title("Histogram of Heights in a Group")
plt.xticks(bins)  # Set x-axis labels to match bin edges
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
