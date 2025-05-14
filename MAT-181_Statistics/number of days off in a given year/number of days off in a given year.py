
'''requarement: 
Provide an appropriate response.
 1)The frequency table below shows the number of days off in a given year for 30 police detectives.
 Days off Frequency
 0-2 10
 3-5 1
 6-8 7
 9-11 7
 12-14 1
 15-17 4
 Construct a histogram. Use the class midpoints for the horizontal scale. Does the result appear to be a normal
 distribution? Why or why not?'''


import matplotlib.pyplot as plt

# Define the edges of the bins
bins = [0, 2, 5, 8, 11, 14, 17]

# Frequencies
frequencies = [10, 1, 7, 7, 1, 4]

# Create the histogram
plt.hist([0]*frequencies[0] + [3]*frequencies[1] + [7]*frequencies[2] + [10]*frequencies[3] + [13]*frequencies[4] + [16]*frequencies[5], bins=bins, edgecolor='black')

# Add titles and labels
plt.title('Histogram of Days Off for Police Detectives')
plt.xlabel('Days Off')
plt.ylabel('Frequency')

# Display the histogram
plt.show()


