import matplotlib.pyplot as plt
import numpy as np

# Data
friends = ['H1', 'H2', 'H3', 'H4', 'H5']
heights = [62, 69, 71, 66, 72]

# Calculations
mean_height = np.mean(heights)
deviations = [height - mean_height for height in heights]
squared_deviations = [dev**2 for dev in deviations]
sum_of_squares = sum(squared_deviations)
variance = sum_of_squares / (len(heights) - 1)
std_deviation = np.sqrt(variance)

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.bar(friends, heights, color='skyblue')

# Adding labels and title
plt.xlabel('Friends')
plt.ylabel('Height (inches)')
plt.title('Height of Friends and Statistical Information')

# Mean line
plt.axhline(y=mean_height, color='r', linestyle='--', label=f'Mean Height: {mean_height:.2f} inches')

# Informational text location 
plt.text(-0.1, min(heights) - 70, f'Mean Height: {mean_height:.2f} inches, Standard Deviation: {std_deviation:.2f} inches', color='red')

# Adding values on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval}', ha='center', va='bottom')

# Show plot
plt.legend()
plt.grid(True)
plt.show()
