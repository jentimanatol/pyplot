import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Define the parameters of the uniform distribution
lower_bound = 0
upper_bound = 8
height = 0.125  # Height of the uniform density function

# Create x values for plotting
x = np.linspace(-1, 9, 1000)

# Define the uniform density function
def uniform_pdf(x):
    return np.where((x >= lower_bound) & (x <= upper_bound), height, 0)

# Calculate the probability P(X < 2.5)
target = 2.5
probability = (target - lower_bound) * height

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the uniform density function
y = uniform_pdf(x)
plt.plot(x, y, 'b-', linewidth=2)

# Fill the area representing P(X < 2.5)
x_fill = np.linspace(lower_bound, target, 100)
y_fill = uniform_pdf(x_fill)
plt.fill_between(x_fill, y_fill, alpha=0.3, color='red')

# Add annotations and labels
plt.grid(True, alpha=0.3)
plt.xlabel('x', fontsize=14)
plt.ylabel('P(x)', fontsize=14)
plt.title('Uniform Density Curve with P(X < 2.5) Highlighted', fontsize=16)

# Add text for probability value
plt.text(4, 0.09, f'P(X < 2.5) = {probability:.3f}', 
         bbox=dict(facecolor='white', alpha=0.8), fontsize=14)

# Add annotations showing the key points
plt.annotate(f'Height = {height}', xy=(upper_bound/2, height), 
             xytext=(upper_bound/2, height + 0.02),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1),
             ha='center', fontsize=12)

plt.annotate(f'x = {target}', xy=(target, 0), 
             xytext=(target, -0.02),
             ha='center', fontsize=12)

# Set axis limits
plt.xlim(-1, 9)
plt.ylim(-0.025, 0.15)

# Show the x-axis values clearly
plt.xticks(np.arange(0, 9))

plt.tight_layout()
plt.show()

# Calculate and print the probability
print(f"Probability that X < 2.5: {probability}")