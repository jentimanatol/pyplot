import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mu = 100  # Mean IQ score
sigma = 15  # Standard deviation

# Create the range of x values (IQ scores) from -4σ to +4σ
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Calculate the corresponding y values for the normal distribution
y = norm.pdf(x, mu, sigma)

# Define the x value of interest (IQ score of 110)
x_value = 110

# Calculate the z-score for x = 110
z = (x_value - mu) / sigma

# Calculate the cumulative area to the left of the z-score
area = norm.cdf(z)

# Plotting the normal distribution
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\mu = 100, \sigma = 15$', color='blue', lw=2)

# Shading the area under the curve up to x = 110
plt.fill_between(x, 0, y, where=(x <= x_value), color='skyblue', alpha=0.5, label=f'Area up to x = {x_value}')

# Mark the x_value (IQ score of 110) with a red vertical line
plt.axvline(x_value, color='red', linestyle='--', label=f'x = {x_value}')

# Add text annotations
plt.text(x_value + 3, 0.02, f'Z = {z:.2f}', fontsize=12, color='red')
plt.text(x_value + 3, 0.025, f'Area = {area:.4f} (~{area*100:.2f}%)', fontsize=12, color='red')

# Add a label for the area formula
plt.text(mu - 3, 0.025, r'$\text{Area} = P(Z \leq z) = P\left(\frac{x - \mu}{\sigma} \right)$', fontsize=12, color='black')

# Title and labels
plt.title('Normal Distribution Curve: Area Under the Curve', fontsize=16)
plt.xlabel('IQ Score', fontsize=14)
plt.ylabel('Probability Density', fontsize=14)

# Show grid and legend
plt.grid(True)
plt.legend()

# Save the plot as an image in the same directory
#plt.savefig('normal_distribution_area.png', dpi=300)


# Save the plot as an image in the same directory
plt.savefig('normal_distribution_area.jpg', dpi=300)



# Show the plot
plt.show()
