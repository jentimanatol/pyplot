import matplotlib.pyplot as plt

# Data
cities = ["Austin/Georgetown, TX", "Oklahoma City, OK", "Rogers, AR", "Kansas City, MO", "Papillion/Bellevue, NE", "Madison, WI", 
          "La Crosse, WI", "Minneapolis, MN", "Fargo, ND", "Winnipeg, MB, Canada", "Saskatoon, SK, Canada"]
change_in_days = [-1.08, 5.83, 11.23, 25.23, 14.58, 14.93, 14.77, 17.75, 21.01, 24.56, 23.72]

# Create the plot
plt.figure(figsize=(10, 6))
plt.barh(cities, change_in_days, color='skyblue')
plt.xlabel('Change in Length of Ragweed Pollen Season (days)')
plt.title('Change in Ragweed Pollen Season (1995-2015)')
plt.grid(True)

# Display the plot
plt.show()
