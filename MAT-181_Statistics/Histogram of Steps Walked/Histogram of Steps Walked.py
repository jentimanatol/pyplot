import matplotlib.pyplot as plt

# Step data (in thousands of steps)
steps_walked = [3, 4, 5, 4, 7, 6, 8, 5, 3, 6, 4, 7, 5, 6, 9, 3, 6, 5, 6, 4]

# Create histogram with bin intervals: [3-4], [5-6], [7-8], [9-10]
plt.figure(figsize=(8, 6))
plt.hist(steps_walked, bins=[3, 5, 7, 9, 11], edgecolor='black', alpha=0.7, color='skyblue')

# Add labels and title
plt.xlabel('Steps Walked (in thousands)')
plt.ylabel('Frequency (Number of People)')
plt.title('Histogram of Steps Walked Per Day')

# Set x-axis labels to correspond to the intervals
plt.xticks([4, 6, 8, 10], ['3-4', '5-6', '7-8', '9-10'])

# Display grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
