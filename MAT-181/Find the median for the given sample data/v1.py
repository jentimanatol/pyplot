
# Solution:
# The given data is 9, 1, 29, 11, 22, 46, 40, 35
# The data is arranged in ascending order as follows:
# 1, 9, 11, 22, 29, 35, 40, 46
# The median age is the middle value of the data.

# The number of observations is 8, which is even.
# The median age is the average of the middle two values.
# The middle two values are 22 and 29.
# The median age is (22 + 29) / 2 = 51 / 2 = 25.5 years.

# The median age of the passengers is 25.5 years.
# The median age is 25.5 years.

# graph to represent the data
import matplotlib.pyplot as plt
import numpy as np
data = [9, 1, 29, 11, 22, 46, 40, 35]
data.sort()
plt.plot(data, np.zeros_like(data), 'x')
plt.show()
