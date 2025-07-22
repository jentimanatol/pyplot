import scipy.integrate as spi
import numpy as np

f = lambda t: np.sqrt(4*t**2 + 25/(4*t) + 4/(t**6))
result, _ = spi.quad(f, 1, 4)
print(round(result, 2))
# Save the plot as a PNG file
print("The integral result is:", result)
