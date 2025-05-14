import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data Preparation
data = {
    "Category": ["Max Temperature", "Min Temperature", "Avg Temperature", "Precipitation", "Snowfall", "Snow Depth", "HDD (base 65)", "CDD (base 65)"],
    "Observed": ["M", "M", "M", "M", "M", "M", "M", "M"],
    "Normal": [54, 37, 45.6, 0.11, 0.1, "-", 20, 0],
    "Record Highest": [79, 57, 68.0, 1.41, 2.6, 8, 38, 3],
    "Record Lowest": [33, 19, 27.0, 0.00, 0.0, 0, 0, 0]
}

month_to_date = {
    "Category": ["Avg Max Temperature", "Avg Min Temperature", "Avg Temperature", "Total Precipitation", "Total Snowfall", "Max Snow Depth", "Total HDD (base 65)", "Total CDD (base 65)"],
    "Observed": [57.3, 36.0, 46.7, 0.70, 0.0, 0, 162, 0],
    "Normal": [53.0, 35.7, 44.4, 1.06, 1.0, "-", 207, 0],
    "Record Highest": [67.0, 46.8, 56.4, 3.56, 13.7, 8, 394, 4],
    "Record Lowest": [30.9, 19.8, 25.4, "T", 0.0, 0, 88, 0]
}

year_to_date = {
    "Category": ["Avg Max Temperature", "Avg Min Temperature", "Avg Temperature", "Total Precipitation", "Total Snowfall (since July 1)", "Max Snow Depth (since July 1)", "Total HDD (since July 1)", "Total CDD (since Jan 1)"],
    "Observed": [46.6, 30.7, 38.7, 5.49, 14.9, 6, 2902, 0],
    "Normal": [47.4, 31.6, 39.5, 6.54, 12.7, "-", 3129, 0],
    "Record Highest": [54.7, 37.9, 46.3, 13.07, 56.1, 22, 4008, 4],
    "Record Lowest": [38.7, 24.6, 31.9, 2.21, 0.1, 0, 2535, 0]
}

# Convert to DataFrames
df_daily = pd.DataFrame(data)
df_month_to_date = pd.DataFrame(month_to_date)
df_year_to_date = pd.DataFrame(year_to_date)

# Plotting
def plot_summary(df, title):
    df_melted = df.melt(id_vars=["Category"], var_name="Type", value_name="Value")
    df_melted['Value'] = pd.to_numeric(df_melted['Value'], errors='coerce')
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Category", y="Value", hue="Type", data=df_melted)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.ylabel("Value")
    plt.xlabel("Category")
    plt.legend(title="Type")
    plt.tight_layout()
    plt.show()

# Visualize Daily Data
plot_summary(df_daily, "Daily Weather Data Summary")

# Visualize Month-to-Date Data
plot_summary(df_month_to_date, "Month-to-Date Weather Data Summary")

# Visualize Year-to-Date Data
plot_summary(df_year_to_date, "Year-to-Date Weather Data Summary")