import matplotlib.pyplot as plt
import numpy as np
import math

# Quiz scores
scores = [50, 15, 31, 27, 11, 42, 71]

sum_scores = sum(scores)

# Step 1: Calculate the mean
mean_score = sum(scores) / len(scores)

# Step 2: Calculate the squared differences from the mean
squared_differences = [(score - mean_score) ** 2 for score in scores]

# Step 3: Find the average of the squared differences (variance)
variance = sum(squared_differences) / len(scores)

# Step 4: Take the square root of the variance to find the standard deviation
standard_deviation = math.sqrt(variance)

# Round the standard deviation to one more decimal place than the original data
standard_deviation = round(standard_deviation, 1)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.hist(scores, bins=np.arange(10, 81, 10), edgecolor='black', color='skyblue')
plt.xlabel('Quiz Scores')
plt.ylabel('Frequency')
plt.title('Distribution of Christine\'s Quiz Scores')

# Adding the mean and standard deviation to the plot
plt.axvline(mean_score, color='red', linestyle='dashed', linewidth=1)
plt.text(mean_score + 1, 2, f'Mean: {mean_score:.1f}', color='red')
plt.axvline(mean_score + standard_deviation, color='green', linestyle='dashed', linewidth=1)
plt.text(mean_score + standard_deviation + 1, 2, f'+1 SD: {mean_score + standard_deviation:.1f}', color='green')
plt.axvline(mean_score - standard_deviation, color='green', linestyle='dashed', linewidth=1)
plt.text(mean_score - standard_deviation - 15, 2, f' .                -1 SD: {mean_score - standard_deviation:.1f}', color='green')

plt.show()
