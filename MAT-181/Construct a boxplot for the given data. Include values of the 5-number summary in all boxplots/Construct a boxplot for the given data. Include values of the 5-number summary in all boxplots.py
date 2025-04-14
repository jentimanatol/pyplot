import matplotlib.pyplot as plt

# Ages of the 35 members
ages = [15, 16, 18, 18, 18, 19, 20, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 24, 25, 25, 26, 27, 27, 28, 29, 29, 30, 31, 31, 33, 34, 35, 39, 42, 48]

#print the sorted ages

ages.sort()
print(ages)

# ages length
n = len(ages)
print(n)


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

# Show the plot
plt.show()
