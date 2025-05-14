import matplotlib.pyplot as plt

# Data
weight_intervals = [(5+7)/2, (8+10)/2, (11+13)/2, (14+16)/2, (17+19)/2, (20+22)/2]
frequencies = [2, 9, 18, 13, 4, 1]

# Plot the frequency polygon
plt.plot(weight_intervals, frequencies, marker='o', linestyle='-', color='b')
plt.title('Frequency Polygon of Weight Loss in the First Month of a Diet Program')
plt.xlabel('Weight (lb)')
plt.ylabel('Frequency')
plt.grid(True)

# Add legend
legend_text = 'Weight (lb): 5-7, 8-10, 11-13, 14-16, 17-19, 20-22\nFrequency: 2, 9, 18, 13, 4, 1'
plt.legend([legend_text], loc='upper right')

# Show the plot
plt.show()
