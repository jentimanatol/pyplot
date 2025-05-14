'''requarement :
 In a survey, 26 voters were asked their ages. The results are shown below. Construct a histogram to represent the
 data (with 5 classes beginning with a lower class limit of 20 and a class width of 10). What is the approximate age
 at the center?
 43 56 28 63 67 66 52 48 37 51 40 60 62 
66 45 21 35 49 32 53 61 53 69 31 48 59

'''
import matplotlib.pyplot as plt

# Data
ages = [43, 56, 28, 63, 67, 66, 52, 48, 37, 51, 40, 60, 62,
        66, 45, 21, 35, 49, 32, 53, 61, 53, 69, 31, 48, 59]
bins = [20, 30, 40, 50, 60, 70]

# Create the histogram
plt.hist(ages, bins=bins, edgecolor='black', alpha=0.7)
plt.grid(axis='y', linestyle='--')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution of Voters')

# Calculate the median (approximate age at the center)
sorted_ages = sorted(ages)
median_age = (sorted_ages[len(sorted_ages)//2 - 1] + sorted_ages[len(sorted_ages)//2]) / 2

# Add a label with all data and the median age
data_label = f"Ages: {', '.join(map(str, sorted_ages))}\nMedian Age: {median_age:.1f}"
plt.text(20, 8, data_label, fontsize=9, bbox=dict(facecolor='white', alpha=0.8))

# Show the plot
plt.show()