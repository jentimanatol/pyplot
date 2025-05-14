import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.offsetbox import AnchoredText

# Define the parameters of the uniform distribution
a = 6  # Lower bound (minimum weight loss)
b = 12  # Upper bound (maximum weight loss)
height = 1/(b-a)  # Height of PDF

# Create x values for plotting
x = np.linspace(4, 14, 1000)

# Define the uniform density function
def uniform_pdf(x, a, b):
    return np.where((x >= a) & (x <= b), height, 0)

# Create a sample range to calculate probability for
c = 8  # Lower bound of sample range
d = 10  # Upper bound of sample range
prob_range = (d-c)/(b-a)  # Probability of the range

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the uniform density function
y = uniform_pdf(x, a, b)
ax.plot(x, y, 'b-', linewidth=2)

# Fill the area representing the total distribution
ax.fill_between(x, uniform_pdf(x, a, b), color='skyblue', alpha=0.3, label='Total distribution')

# Fill the area representing the probability range
x_fill = np.linspace(c, d, 100)
y_fill = uniform_pdf(x_fill, a, b)
ax.fill_between(x_fill, y_fill, color='red', alpha=0.5, label=f'P({c} ≤ X ≤ {d})')

# Add annotations and labels
ax.grid(True, alpha=0.3)
ax.set_xlabel('Weight Loss (pounds)', fontsize=12)
ax.set_ylabel('Probability Density', fontsize=12)
ax.set_title('Uniform Distribution of Weight Loss (6-12 pounds)', fontsize=14)

# Set axis limits
ax.set_xlim(4, 14)
ax.set_ylim(-0.02, height + 0.05)

# Show the x-axis values clearly
ax.set_xticks(np.arange(4, 15, 1))

# Create a string with the formulas and calculations for the legend
formula_text = (
    r"$f(x) = \frac{1}{b-a}$ for $a \leq x \leq b$" + "\n"
    r"$f(x) = \frac{1}{12-6} = \frac{1}{6} \approx 0.167$" + "\n\n"
    r"$P(c \leq X \leq d) = \frac{d-c}{b-a}$" + "\n"
    f"$P({c} \\leq X \\leq {d}) = \\frac{{{d}-{c}}}{{{b}-{a}}} = \\frac{{{d-c}}}{{{b-a}}} = {prob_range:.3f}$"
)

# Add a text box with the formulas
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(13, 0.11, formula_text, transform=ax.transData, fontsize=10,
        verticalalignment='center', bbox=props)

# Add probability calculation to the plot
prob_text = f"P({c} ≤ X ≤ {d}) = {prob_range:.3f}"
ax.annotate(prob_text, xy=((c+d)/2, height/2), xytext=((c+d)/2, height+0.02),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1),
            ha='center', fontsize=10)

# Annotate key points
ax.annotate(f"a = {a}", xy=(a, 0), xytext=(a, -0.01),
            ha='center', fontsize=10)
ax.annotate(f"b = {b}", xy=(b, 0), xytext=(b, -0.01),
            ha='center', fontsize=10)
ax.annotate(f"c = {c}", xy=(c, height), xytext=(c, height+0.01),
            ha='center', fontsize=10)
ax.annotate(f"d = {d}", xy=(d, height), xytext=(d, height+0.01),
            ha='center', fontsize=10)
ax.annotate(f"height = 1/(b-a) = {height:.3f}", xy=((a+b)/2, height), 
            xytext=((a+b)/2, height+0.03),
            ha='center', fontsize=10)

# General case formulas section
general_text = (
    "General Uniform Distribution Formulas:\n"
    r"$\mu = \frac{a+b}{2} = \frac{6+12}{2} = 9$ pounds" + "\n"
    r"$\sigma = \frac{b-a}{\sqrt{12}} = \frac{6}{\sqrt{12}} \approx 1.73$ pounds"
)

# Add general formulas
ax.text(5, 0.05, general_text, fontsize=10, bbox=dict(facecolor='lightgreen', alpha=0.5))

plt.tight_layout()
plt.show()

# Calculate and print all relevant statistics
mean = (a + b) / 2
std_dev = (b - a) / np.sqrt(12)
print(f"Distribution parameters:")
print(f"  Range: [{a}, {b}] pounds")
print(f"  PDF height: {height:.4f}")
print(f"  Mean (μ): {mean:.2f} pounds")
print(f"  Standard deviation (σ): {std_dev:.2f} pounds")
print(f"\nProbability calculations:")
print(f"  P({c} ≤ X ≤ {d}) = {prob_range:.4f}")