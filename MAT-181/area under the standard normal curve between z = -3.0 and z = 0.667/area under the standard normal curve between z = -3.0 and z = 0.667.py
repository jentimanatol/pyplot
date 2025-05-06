import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Parameters of the normal distribution (Wechsler IQ scores)
mu = 100       # mean
sigma = 15     # standard deviation

# Range for the x-axis
x = np.linspace(40, 160, 500)
y = stats.norm.pdf(x, mu, sigma)

# Values for the shaded area
x_fill = np.linspace(55, 110, 500)
y_fill = stats.norm.pdf(x_fill, mu, sigma)

# Z-scores
z_55 = (55 - mu) / sigma  # = -3.0
z_110 = (110 - mu) / sigma  # ≈ 0.667

# Area under the curve between 55 and 110
area = stats.norm.cdf(110, mu, sigma) - stats.norm.cdf(55, mu, sigma)

# Plotting the normal distribution curve
plt.figure(figsize=(12, 6))
plt.plot(x, y, label='Normal Distribution (μ=100, σ=15)', color='black')
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.6, label=f'Shaded Area ≈ {area:.4f}')

# Add vertical lines for 55 and 110
plt.axvline(55, color='blue', linestyle='--')
plt.axvline(110, color='blue', linestyle='--')

# Add text box with formulas and calculations
legend_text = (
    "Formulas and Calculations:\n"
    "z = (X - μ) / σ\n"
    "z(55) = (55 - 100) / 15 = -3.0\n"
    "z(110) = (110 - 100) / 15 ≈ 0.667\n"
    "P(55 < X < 110) ≈ Φ(0.667) - Φ(-3.0)\n"
    "≈ 0.7475 - 0.0013 = 0.7462"
)

plt.text(125, 0.015, legend_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# Labels and title
plt.title("Shaded Area Under Normal Distribution Curve for IQ Scores (55 to 110)")
plt.xlabel("IQ Score")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("printscreen.png", dpi=300)

plt.show()
