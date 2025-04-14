import matplotlib.pyplot as plt

# Data
weights = [144, 152, 142, 151, 160, 152, 131, 164, 141, 153, 140,
           144, 175, 156, 147, 133, 172, 159, 135, 159, 148, 171]

# Create a stemplot
plt.figure(figsize=(8, 6))
markerline, stemlines, baseline = plt.stem(weights, basefmt=" ", linefmt="C0-", markerfmt="C0o")

# Customize the plot
plt.title('Stem-and-Leaf Plot of Varsity Football Team Weights', fontsize=16)
plt.xlabel('Weight (lbs)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Add a legend
plt.legend([markerline], ['Weights'], loc='upper right')

# Show the plot
plt.show()