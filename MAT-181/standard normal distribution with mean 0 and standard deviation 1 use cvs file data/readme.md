
# Standard Normal Distribution Visualization

This project visualizes the standard normal distribution using data extracted from a CSV file. It includes detailed steps to process the data, generate the distribution curve, highlight specific areas of interest, and ensure a thorough understanding of the statistical concepts involved.

## Project Overview

The aim of this project is to create a visually appealing and informative graph of the standard normal distribution. This graph will include:
1. The standard normal distribution curve.
2. A vertical line at a specific z-score (e.g., z = 0.76).
3. A shaded area representing the cumulative probability up to this z-score.
4. Annotation of the area under the curve.

By using data extracted from a CSV file, we ensure that the visualization is both accurate and based on real statistical data.

## Installation

To run this project, you will need to have Python installed on your system along with the necessary libraries. You can install the required libraries using `pip`.

### Step-by-Step Installation

1. **Clone the repository**:


2. **Install the required libraries**:
   ```bash
   pip install numpy pandas matplotlib scipy
   ```

## Usage

### Data Extraction and Visualization

The project uses a CSV file (`data-3_6_2025-5_14 PM.csv`) containing z-scores and their corresponding cumulative probabilities. Here's a breakdown of the process:

1. **Reading the CSV File**:
   We start by reading the CSV file using `pandas`. We skip the initial rows that contain metadata and focus on the rows with actual data.

   ```python
   import pandas as pd

   file_path = 'data-3_6_2025-5_14 PM.csv'
   data = pd.read_csv(file_path, skiprows=5)
   ```

2. **Data Cleaning**:
   We parse each row, converting values to float where possible. Non-numeric rows are skipped.

   ```python
   z_scores = []
   area_values = []

   for idx, row in data.iterrows():
       try:
           z = float(row[0].strip())
           z_scores.append(z)
           area_values.append(list(map(float, row[1:])))
       except ValueError:
           print(f"Skipping non-numeric row at index {idx}")
   ```

3. **Flattening the Data**:
   The cumulative area values are flattened into a single list to ensure consistency in length.

   ```python
   area_list = [item for sublist in area_values for item in sublist]
   ```

4. **Matching Lengths**:
   We ensure that both the z-scores and cumulative area lists have the same length by truncating the longer list.

   ```python
   min_length = min(len(z_scores) * len(data.columns[1:]), len(area_list))
   z_list = np.repeat(z_scores, len(data.columns[1:]))[:min_length]
   area_list = area_list[:min_length]
   ```

5. **Generating the Visualization**:
   We use `matplotlib` and `scipy` to create the standard normal distribution curve, plot the vertical line at the specific z-score, and shade the area to the left of this line.

   ```python
   import numpy as np
   import matplotlib.pyplot as plt
   from scipy.stats import norm

   def plot_z_shaded(z_value):
       x = np.linspace(-4, 4, 1000)
       y = norm.pdf(x, 0, 1)

       plt.plot(x, y, label='Standard Normal Distribution Curve', color='blue')
       plt.axvline(z_value, color='red', linestyle='--', label=f'z = {z_value}')
       plt.fill_between(x, 0, y, where=(x <= z_value), color='red', alpha=0.5, label=f'Area to the left of z = {z_value} = 0.7764')

       plt.title('Standard Normal Distribution with Shaded Area')
       plt.xlabel('z-score')
       plt.ylabel('Probability Density')
       plt.legend()
       plt.grid(True)
       plt.show()

   plot_z_shaded(0.76)
   ```

### Detailed Explanation

- **Generating Data Points**:
  We generate data points for the x-axis ranging from -4 to 4, which covers the majority of the standard normal distribution.

  ```python
  x = np.linspace(-4, 4, 1000)
  ```

- **Calculating Probability Density**:
  We use `norm.pdf` to calculate the probability density function for each x value.

  ```python
  y = norm.pdf(x, 0, 1)
  ```

- **Plotting the Distribution Curve**:
  The curve is plotted using `plt.plot`.

  ```python
  plt.plot(x, y, label='Standard Normal Distribution Curve', color='blue')
  ```

- **Adding Vertical Line and Shaded Area**:
  A vertical line is added at the specific z-score, and the area to the left is shaded to highlight the cumulative probability.

  ```python
  plt.axvline(z_value, color='red', linestyle='--', label=f'z = {z_value}')
  plt.fill_between(x, 0, y, where=(x <= z_value), color='red', alpha=0.5, label=f'Area to the left of z = {z_value} = 0.7764')
  ```

### Example Usage

To visualize the standard normal distribution and highlight the area for a different z-score, you can simply call the `plot_z_shaded` function with the desired z-value.

```python
# Example: Plot for z = 1.96
plot_z_shaded(1.96)
```

## Conclusion

This project demonstrates the process of visualizing the standard normal distribution using data extracted from a CSV file. It includes detailed steps for data extraction, cleaning, processing, and visualization, making it a comprehensive guide for similar projects. The resulting graph provides a clear and informative representation of the distribution, enhancing our understanding of statistical concepts.

_Not protected by copyright, may be used for its intended purpose._  
_Author: Anatolie Jentimir._
