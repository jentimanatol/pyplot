import matplotlib.pyplot as plt
import numpy as np

# Data
n = 987  # Sample size
x = 526  # Number of "yes" responses
confidence_level = 0.90  # Confidence level

# Calculate the sample proportion
p_hat = x / n

# Critical value for 90% confidence level
z_alpha_over_2 = 1.645

# Margin of error
E = z_alpha_over_2 * np.sqrt((p_hat * (1 - p_hat)) / n)

# Confidence interval
lower_bound = p_hat - E
upper_bound = p_hat + E

# Plotting
fig, ax = plt.subplots()

# Bar plot for the sample proportion
ax.bar(1, p_hat, color='blue', width=0.1, label='Sample Proportion')
ax.errorbar(1, p_hat, yerr=E, fmt='o', color='red', label='Confidence Interval (90%)')

# Adding text for the bounds
ax.text(1.1, lower_bound, f'{lower_bound:.3f}', color='green')
ax.text(1.1, upper_bound, f'{upper_bound:.3f}', color='green')

# Formatting the plot
ax.set_xlim(0.9, 1.2)
ax.set_ylim(0, 1)
ax.set_xticks([1])
ax.set_xticklabels(['Proportion'])
ax.set_ylabel('Proportion')
ax.set_title('90% Confidence Interval for Population Proportion')
ax.legend()

# Show the plot
plt.show()
