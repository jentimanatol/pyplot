import matplotlib.pyplot as plt

# Simulated height data (in inches) based on a real distribution
height_data = [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 
               73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]  

# Frequency distribution (number of people for each height range)
frequency = [2, 1, 3, 2, 4, 5, 6, 7, 8, 7, 6, 5, 6, 5, 4, 
             3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]

# Plot histogram
plt.figure(figsize=(8, 6))
plt.bar(height_data, frequency, width=1.5, edgecolor="black", alpha=0.7)

# Labels and title
plt.xlabel("Height (inches)")
plt.ylabel("Number of People")
plt.title("Histogram of Heights in a Group")
plt.xticks(range(58, 84, 2))  # Setting x-axis labels at every 2-inch interval
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
