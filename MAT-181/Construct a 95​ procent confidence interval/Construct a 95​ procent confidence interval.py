''' requrenemt 

Listed below are the amounts of net worth​ (in millions of​ dollars) of the ten wealthiest celebrities in a country. Construct a 95​% confidence interval. What does the result tell us about the population of all​ celebrities? Do the data appear to be from a normally distributed population as​ required? 240 215 187 172 164 163 152 152 152 152



answer: Because the ten wealthiest celebrities are not a representative​ sample, this​ doesn't provide any information about the population of all celebrities. Your answer is correct.B. We are 95​% confident that the interval from ​$


question : Do the data appear to be from a normally distributed population as​ required? Choose the correct answer.
answer : 
​No, because there is a systematic pattern that is not a straight line pattern.


'''



import matplotlib.pyplot as plt
import numpy as np

# Data from the question
net_worths = [240, 215, 187, 172, 164, 163, 152, 152, 152, 152]

# Calculate sample mean and standard deviation
mean_net_worth = np.mean(net_worths)
std_dev_net_worth = np.std(net_worths, ddof=1)

# Confidence Interval Limits for 95% confidence level
lower_limit = 153.2
upper_limit = 196.6

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the net worths of each celebrity
plt.bar(range(len(net_worths)), net_worths, color='skyblue', label='Net Worth (Millions)')

# Add a horizontal line for the mean
plt.axhline(mean_net_worth, color='red', linestyle='--', label=f'Mean Net Worth: {mean_net_worth:.1f} million')

# Highlight the confidence interval
plt.axhspan(lower_limit, upper_limit, color='yellow', alpha=0.3, label=f'95% Confidence Interval: [{lower_limit}, {upper_limit}] million')

# Add labels and title
plt.xlabel('Celebrity Index', fontsize=12)
plt.ylabel('Net Worth (Millions)', fontsize=12)
plt.title('Net Worth of the Ten Wealthiest Celebrities', fontsize=14, fontweight='bold')

# Add informational text in the top-right corner
info_text = (
    f"Sample Size (n): {len(net_worths)}\n"
    f"Sample Mean: {mean_net_worth:.1f} million\n"
    f"Sample Standard Deviation: {std_dev_net_worth:.1f} million\n"
)

plt.text(0.95, 0.95, info_text, fontsize=10, bbox=dict(facecolor='lightyellow', alpha=0.8),
         transform=plt.gca().transAxes, verticalalignment='top', horizontalalignment='right')

# Add legend
plt.legend(loc='upper left')

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
