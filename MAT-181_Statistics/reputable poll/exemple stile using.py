import matplotlib.pyplot as plt
import seaborn as sns

# Method 1: Using seaborn's set_style (recommended)
sns.set_style("darkgrid")

# Method 2: Using matplotlib's style (if available)
# plt.style.use('seaborn-darkgrid') 

plt.plot([1,2,3], [4,5,6])
plt.title("Seaborn Darkgrid Style Example")
plt.show()


#pip uninstall matplotlib seaborn -y
#pip install --upgrade matplotlib seaborn