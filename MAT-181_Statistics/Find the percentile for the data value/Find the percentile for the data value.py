'''
Find the percentile for the data value.
Data set: 12 18 42 24 12 30 54 54 66 18 18 54 36 6 54;
data value: 42
'''

# Solution:

# Given data set
data_set = [12, 18, 42, 24, 12, 30, 54, 54, 66, 18, 18, 54, 36, 6, 54]

# Given data value
data_value = 42

# Sort the data set
data_set.sort()

# Find the index of the data value

index = data_set.index(data_value)

# Find the percentile

percentile = (index / len(data_set)) * 100

# Display the percentile

print("The percentile for the data value is:", percentile)



