import matplotlib.pyplot as plt

# Data
scores = [85, 77, 93, 91, 74, 65, 68, 97, 88, 59, 74, 83, 85, 72, 63, 79]

# Sort the data
scores_sorted = sorted(scores)

# Extract stems and leaves
stems = [score // 10 for score in scores_sorted]  # Tens digit
leaves = [score % 10 for score in scores_sorted]  # Units digit

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Hide axes
ax.axis('off')

# Plot stems and leaves
y_offset = 0.1  # Vertical spacing
for stem, leaf in zip(stems, leaves):
    ax.text(0.1, stem + y_offset, str(stem), va='center', ha='right', fontsize=12, color='blue')  # Stem
    ax.text(0.2, stem + y_offset, '|', va='center', ha='center', fontsize=12, color='black')  # Separator
    ax.text(0.3, stem + y_offset, str(leaf), va='center', ha='left', fontsize=12, color='red')  # Leaf

# Add title
ax.set_title('Stemplot of Midterm Test Scores', fontsize=14, pad=20)

# Show the plot
plt.show()