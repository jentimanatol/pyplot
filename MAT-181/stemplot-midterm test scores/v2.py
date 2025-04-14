
import matplotlib.pyplot as plt

# Data
scores = [85, 77, 93, 91, 74, 65, 68, 97, 88, 59, 74, 83, 85, 72, 63, 79]

# Sort the data
scores_sorted = sorted(scores)

# Create a stemplot
stems = [score // 10 for score in scores_sorted]  # Extract stems (tens digit)
leaves = [score % 10 for score in scores_sorted]  # Extract leaves (units digit)

# Plot the stemplot
plt.figure(figsize=(8, 5))
plt.yticks(range(min(stems), max(stems) + 1))  # Set y-axis to show stems
plt.xticks([])  # Hide x-axis ticks
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines

# Plot each leaf
for stem, leaf in zip(stems, leaves):
    plt.text(0.1, stem, str(leaf), va='center', ha='left', fontsize=12)

# Add labels and title
plt.ylabel('Stem (Tens Digit)')
plt.xlabel('Leaves (Units Digit)')
plt.title('Stemplot of Midterm Test Scores')
plt.show()