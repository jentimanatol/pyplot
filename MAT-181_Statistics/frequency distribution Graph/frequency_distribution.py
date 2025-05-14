import matplotlib.pyplot as plt

# Data: Age ranges and corresponding frequencies
age_ranges = ['10-19', '20-29', '30-39', '40-49', '50-59']
frequencies = [5, 11, 8, 10, 3]

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(age_ranges, frequencies, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Age Range')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Ages for Auditioning')

# Display grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart
plt.show()
