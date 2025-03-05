import numpy as np

# Data for men aged 20-29
data_20_29 = [117, 122, 129, 118, 131, 123]

# Data for men aged 60-69
data_60_69 = [130, 153, 141, 125, 164, 139]

# Function to calculate mean, standard deviation and CV
def calculate_statistics(data):
    mean = np.mean(data)
    deviations = [(x - mean) for x in data]
    squared_deviations = [(x - mean) ** 2 for x in data]

    print(f'sum of squared deviations: {np.sum(squared_deviations)}')
    std_dev = np.sqrt(np.sum(squared_deviations) / (len(data) - 1))
    print(f'std_dev: {std_dev}')
    cv = (std_dev / mean) * 100

    # Print intermediate calculations
    print(f"Data: {data}")
    print(f"Mean: {mean:.2f}")
    print("Deviations from mean:", deviations)
    print("Squared deviations:", squared_deviations)
    print(f"Standard Deviation: {std_dev:.2f}")
    print(f"Coefficient of Variation: {cv:.1f}%")
    print()
    
    return mean, std_dev, cv

# Calculations for men aged 20-29
print("Men aged 20-29:")
mean_20_29, std_dev_20_29, cv_20_29 = calculate_statistics(data_20_29)

# Calculations for men aged 60-69
print("Men aged 60-69:")
mean_60_69, std_dev_60_69, cv_60_69 = calculate_statistics(data_60_69)
