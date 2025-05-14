import matplotlib.pyplot as plt

# Data set
data = [12, 18, 42, 24, 12, 30, 54, 54, 66, 18, 18, 54, 36, 6, 54]
data.sort()

# Positions of the data values
positions = range(1, len(data) + 1)

# Value to highlight
highlight_value = 42
highlight_position = data.index(42) + 1

# Create the bar chart
plt.bar(positions, data, color='skyblue', label='Data Values')

# Highlight the specific value
plt.bar(highlight_position, highlight_value, color='orange', label='Highlighted Value (42)')

# Add labels and title
plt.xlabel('Position in Data Set')
plt.ylabel('Value')
plt.title('Bar Chart of Data Set with Highlighted Value')

# Add a legend
plt.legend()

# Show the plot
plt.show()
