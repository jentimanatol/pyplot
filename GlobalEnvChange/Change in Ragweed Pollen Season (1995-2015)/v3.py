import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {
    "Year": list(range(1895, 2024)),
    "Heating Degree Days (colder than 65°F)": [5092, 4661, 4711, 4704, 4842, 4521, 4937, 4748, 4852, 5048, 4942, 4664, 4800, 4556, 4745, 4679, 4596, 5072, 4515, 4802, 4694, 4881, 5268, 4724, 4661, 4884, 4122, 4540, 4662, 5019, 4634, 4858, 4421, 4630, 4789, 4645, 4213, 4542, 4438, 4466, 4747, 4757, 4774, 4291, 4393, 4890, 4449, 4628, 4768, 4674, 4635, 4234, 4729, 4712, 4403, 4654, 4692, 4542, 4232, 4378, 4675, 4540, 4487, 4835, 4533, 4850, 4650, 4781, 4815, 4633, 4628, 4785, 4678, 4766, 4811, 4736, 4623, 4750, 4406, 4464, 4538, 4764, 4636, 4976, 4810, 4718, 4529, 4637, 4642, 4518, 4646, 4274, 4329, 4612, 4662, 4008, 4182, 4392, 4657, 4428, 4465, 4629, 4479, 3949, 4108, 4376, 4156, 4266, 4441, 4260, 4272, 3979, 4211, 4436, 4433, 4429, 4280, 3739, 4444, 4535, 4078, 3879, 3833, 4292, 4327, 3920, 3945, 4268, 3828],
    "Cooling Degree Days (warmer than 65°F)": [1149, 1280, 1209, 1264, 1244, 1315, 1251, 1170, 1010, 1082, 1190, 1198, 1082, 1173, 1138, 1141, 1307, 1110, 1162, 1182, 1072, 1149, 1060, 1205, 1218, 1076, 1348, 1265, 1138, 1077, 1298, 1178, 1138, 1125, 1153, 1244, 1351, 1222, 1359, 1392, 1210, 1382, 1266, 1255, 1328, 1110, 1252, 1168, 1263, 1253, 1174, 1157, 1252, 1223, 1290, 1104, 1194, 1295, 1298, 1300, 1303, 1212, 1211, 1187, 1317, 1200, 1153, 1187, 1208, 1187, 1153, 1144, 1091, 1125, 1192, 1230, 1192, 1157, 1235, 1130, 1175, 1036, 1299, 1245, 1123, 1321, 1221, 1153, 1254, 1230, 1223, 1272, 1280, 1299, 1188, 1290, 1347, 1078, 1232, 1251, 1314, 1223, 1190, 1449, 1329, 1285, 1297, 1401, 1304, 1247, 1409, 1387, 1410, 1299, 1259, 1468, 1482, 1502, 1312, 1298, 1483, 1549, 1418, 1571, 1484, 1503, 1474, 1530, 1444]
}

df = pd.DataFrame(data)

# Create figure and plot space
plt.figure(figsize=(14, 7))

# Plot
plt.plot(df["Year"], df["Heating Degree Days (colder than 65°F)"], label="Heating Degree Days (colder than 65°F)", color="blue", linestyle="-", linewidth=2)
plt.plot(df["Year"], df["Cooling Degree Days (warmer than 65°F)"], label="Cooling Degree Days (warmer than 65°F)", color="red", linestyle="--", linewidth=2)

# Add titles and labels
plt.title("Figure 1. Heating and Cooling Degree Days in the Contiguous 48 States, 1895-2023")
plt.xlabel("Year")
plt.ylabel("Degree Days (Fahrenheit)")
plt.legend(loc="upper right")

# Add grid
plt.grid(True, linestyle="--", alpha=0.7)

# Add creative touches
plt.fill_between(df["Year"], df["Heating Degree Days (colder than 65°F)"], color="blue", alpha=0.1)
plt.fill_between(df["Year"], df["Cooling Degree Days (warmer than 65°F)"], color="red", alpha=0.1)

# Data source and update info
plt.figtext(0.5, 0.01, "Source: EPA's Climate Change Indicators in the United States (www.epa.gov/climate-indicators)\nData Source: NOAA, 2024\nWeb Update: June 2024 By Anatolie Aby", wrap=True, horizontalalignment='center', fontsize=10, bbox={"facecolor":"orange","alpha":0.5,"pad":5})

# Show plot
plt.show()
