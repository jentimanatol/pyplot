import matplotlib.pyplot as plt

ages = [43, 56, 28, 63, 67, 66, 52, 48, 37, 51, 40, 60, 62,
        66, 45, 21, 35, 49, 32, 53, 61, 53, 69, 31, 48, 59]
bins = [20, 30, 40, 50, 60, 70]

plt.hist(ages, bins=bins, edgecolor='black', alpha=0.7)
plt.grid(axis='y', linestyle='--')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution of Voters')
plt.show()