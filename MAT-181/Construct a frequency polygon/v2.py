import matplotlib.pyplot as plt

# Data
mileage_intervals = [(10+14)/2, (15+19)/2, (20+24)/2, (25+29)/2, (30+34)/2]
frequencies = [0, 6, 9, 21, 7]

# Plot the frequency polygon
plt.plot(mileage_intervals, frequencies, marker='o', linestyle='-', color='b')
plt.title('Frequency Polygon of Roundtrip Mileage')
plt.xlabel('Miles')
plt.ylabel('Frequency')
plt.grid(True)

# Add legend
legend_text = 'Miles: 10-14, 15-19, 20-24, 25-29, 30-34\nFrequency: 0, 6, 9, 21, 7'
plt.legend([legend_text], loc='upper left')

# Show the plot
plt.show()
