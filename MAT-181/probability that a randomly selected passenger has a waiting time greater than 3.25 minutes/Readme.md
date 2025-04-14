# Distribution Visualization Project

This project visualizes both the normal and uniform distribution curves using Python and Matplotlib. It includes calculations and visualizations for specific probability scenarios.

## Project Description

This project contains:
- Visualization of a normal distribution curve.
- Visualization of a uniform distribution curve with highlighted probabilities.
- Detailed explanations and calculations for probability scenarios.

## Installation

To run this project, you'll need to have Python installed on your system. You can install the necessary libraries using `pip`.

### 1. Clone this repository:

### 2. Install the required libraries:
```bash
pip install numpy matplotlib scipy
```

## Usage

### Normal Distribution Visualization
To visualize the normal distribution curve, run the following Python script:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate data points for the x-axis
x = np.linspace(-4, 4, 1000)

# Calculate the corresponding y values for a standard normal distribution
y = norm.pdf(x, 0, 1)

# Create the plot
plt.plot(x, y, label='Normal Distribution', color='blue')

# Add titles and labels
plt.title('Normal Distribution Curve')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
```

### Uniform Distribution Visualization
To visualize the uniform distribution curve and the probability that a randomly selected passenger has a waiting time greater than 3.25 minutes, run the following Python script:

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the uniform distribution
a = 0
b = 8
x = 3.25

# Generate data points for the x-axis
x_values = np.linspace(a, b, 1000)

# Calculate the probability density function (PDF)
pdf = [1 / (b - a) for _ in x_values]

# Create the plot
plt.figure(figsize=(12, 8))
plt.plot(x_values, pdf, label='Uniform Distribution (0 to 8 minutes)', color='blue')
plt.fill_between(x_values, 0, pdf, where=(x_values > x), color='red', alpha=0.5, label=f'P(X > {x}) = 0.594')

# Add vertical line at x = 3.25
plt.axvline(x, color='green', linestyle='--', label=f'x = {x} minutes')

# Add text annotations for the requirements and initial setup
plt.text(0.5, 0.12, f'Requirements: \n- Uniform distribution between 0 and 8 minutes\n- Find the probability that a passenger has a waiting time greater than 3.25 minutes', 
         fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Add text annotations for the calculations
plt.text(6.5, 0.1, f'P(X > {x}) = (8 - {x}) / (8 - 0)\n= {round(8 - x, 3)} / 8\n= 0.594', 
         fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Add title, labels, and legend
plt.title('Uniform Distribution of Waiting Times for Subway Departure', fontsize=16)
plt.xlabel('Waiting Time (minutes)', fontsize=14)
plt.ylabel('Probability Density', fontsize=14)
plt.legend(fontsize=12)

# Add grid for better visualization
plt.grid(True)

# Show the plot
plt.show()
```

_Not protected by copyright, may be used for its intended purpose._  
_Author: Anatolie Jentimir._
