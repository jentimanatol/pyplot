from scipy.stats import norm

# Right-tail area
right_area = 0.0694
left_area = 1 - right_area

# Compute the z-score
z = norm.ppf(left_area)
print(f"Z-score: {z:.2f}")  # Output: Z-score: 1.48
