import matplotlib.pyplot as plt

# Data
customers = [15, 16, 13, 19, 12, 15, 15, 16, 13, 12]

# Create a dot plot
plt.figure(figsize=(8, 5))
for i, value in enumerate(sorted(customers)):
    plt.plot(value, 1, 'ro', markersize=10)  # 'ro' means red circle
plt.yticks([])  # Remove y-axis ticks
plt.xticks(range(12, 20))  # Set x-axis ticks from 12 to 19
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add grid lines
plt.xlabel('Number of Customers')
plt.title('Dot Plot of Customers per Day')
plt.legend(['Customers'], loc='upper right')  # Add legend
plt.show()