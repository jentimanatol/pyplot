import matplotlib.pyplot as plt

# Data
days_absent = [0, 2, 3, 4, 2, 3, 4, 6, 7, 2, 3, 4, 6, 9, 8]

# Create a dot plot
plt.figure(figsize=(8, 5))
for i, value in enumerate(sorted(days_absent)):
    plt.plot(value, 1, 'bo', markersize=10)  # 'bo' means blue circle
plt.yticks([])  # Remove y-axis ticks
plt.xticks(range(0, 10))  # Set x-axis ticks from 0 to 9
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add grid lines
plt.xlabel('Days Absent')
plt.title('Dot Plot of Days Absent')
plt.legend(['Days Absent'], loc='upper right')  # Add legend
plt.show()