import matplotlib.pyplot as plt
import numpy as np

# Ages of the 35 members
ages = [15, 16, 18, 18, 18, 19, 20, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 24, 25, 25, 
        26, 27, 27, 28, 29, 29, 30, 31, 31, 33, 34, 35, 39, 42, 48]

# Sorting the ages
ages.sort()

# Computing quartiles
Q1 = np.percentile(ages, 25)
Median = np.median(ages)
Q3 = np.percentile(ages, 75)
Min = min(ages)
Max = max(ages)

# Creating the boxplot
plt.figure(figsize=(10, 6))  # Adjust figure size for better readability
plt.boxplot(ages, vert=False, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='black'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'),
            flierprops=dict(marker='o', color='black', markersize=5))

# Adding labels and title
plt.xlabel('Age')
plt.title('Boxplot of Ages of Track and Field Team Members')

# Adding 5-number summary text with adjusted positions
plt.text(Min, 1.05, f'Min: {Min}', verticalalignment='center', horizontalalignment='left')
plt.text(Q1, 1.1, f'Q1: {Q1:.1f}', verticalalignment='center', horizontalalignment='left')
plt.text(Median, 1.15, f'Median: {Median}', verticalalignment='center', horizontalalignment='left')
plt.text(Q3, 1.1, f'Q3: {Q3:.1f}', verticalalignment='center', horizontalalignment='left')
plt.text(Max, 1.05, f'Max: {Max}', verticalalignment='center', horizontalalignment='left')

# Adding the sorted ages as text inside the plot area
sorted_ages_text = f"Sorted ages:\n{ages}"
plt.text(ages[0], -0.5, sorted_ages_text, verticalalignment='center', horizontalalignment='left',
         fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# Adjust y-limits to ensure text visibility
plt.ylim(-1, 2)  

# Show the plot
plt.show()
