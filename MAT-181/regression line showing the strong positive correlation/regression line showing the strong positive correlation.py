import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Mock data (replace with actual bear measurements)
chest_size = np.random.normal(40, 5, 54)  # Mean chest size ~40 inches
weight = 100 + 5 * chest_size + np.random.normal(0, 10, 54)  # Simulated linear relationship

# Plot
plt.figure(figsize=(10, 6))
sns.regplot(x=chest_size, y=weight, color='#4c72b0', line_kws={'color': '#dd8452'})
plt.title(f"Bear Weight vs. Chest Size (r = {0.968:.3f}, p < 0.001)", fontweight='bold')
plt.xlabel("Chest Size (inches)")
plt.ylabel("Weight (lbs)")
plt.grid(True, alpha=0.3)
plt.show()