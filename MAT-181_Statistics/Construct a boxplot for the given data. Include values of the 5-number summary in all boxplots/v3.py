import matplotlib.pyplot as plt

# Ages of the 35 members
ages = [15, 16, 18, 18, 18, 19, 20, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 24, 25, 25, 26, 27, 27, 28, 29, 29, 30, 31, 31, 33, 34, 35, 39, 42, 48]

# Sorting the ages
ages.sort()

# Length of the ages list
n = len(ages)

# Creating the boxplot
plt.boxplot(ages, vert=False, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='black'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'),
            flierprops=dict(marker='o', color='black', markersize=5))

# Adding labels and title
plt.xlabel('Age')
plt.title('Boxplot of Ages of Track and Field Team Members')

# Adding 5-number summary text
plt.text(15, 1.1, f'Min: {min(ages)}', verticalalignment='center', horizontalalignment='left')
plt.text(20, 1.1, f'Q1: {20}', verticalalignment='center', horizontalalignment='left')
plt.text(24, 1.1, f'Median: {24}', verticalalignment='center', horizontalalignment='left')
plt.text(30, 1.1, f'Q3: {30}', verticalalignment='center', horizontalalignment='left')
plt.text(48, 1.1, f'Max: {max(ages)}', verticalalignment='center', horizontalalignment='left')

# Adding detailed legend description directly in the graph
legend_text = ('Sorted ages: [15, 16, 18, 18, 18, 19, 20, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 24, 25, 25, 26, 27, 27, 28, 29, 29, 30, 31, 31, 33, 34, 35, 39, 42, 48]\n'
               'Number of ages: ' + str(n) + '\n'
               'Data sorted using: ages.sort()')
plt.text(10, -0.5, legend_text, verticalalignment='center', horizontalalignment='left', bbox=dict(facecolor='white', alpha=0.5))

# Show the plot
plt.show()
