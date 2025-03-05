'''Find the mean for the given sample data. Unless indicated otherwise, round your answer to one more decimal place
 than is present in the original data values.
 1)
 The weights (in pounds) of six dogs are listed below. Find the mean weight. 
26 12 100 45 126 84'''


# Solution
# Mean = sum of all the values / number of values
# Mean = (26 + 12 + 100 + 45 + 126 + 84) / 6
# Mean = 393 / 6
# Mean = 65.5
# Therefore, the mean weight of the dogs is 65.5 pounds.


#Macke a grafical representation of the data
import matplotlib.pyplot as plt

# Data
dogs = [26, 12, 100, 45, 126, 84]
x = range(1, 7)

# Plot
plt.bar(x, dogs)
plt.xlabel('Dog')

plt.ylabel('Weight (pounds)')
plt.title('Weights of six dogs')
plt.show()

