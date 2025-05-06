import matplotlib.pyplot as plt

# Data
hours = [5, 10, 4, 6, 10, 9]
scores = [64, 86, 69, 86, 59, 87]

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(hours, scores, color='blue', edgecolor='black')
plt.title("Scatter Plot of Hours Studied vs Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.grid(True)

# Show plot
plt.show()
