# PyPlot: Data Visualization with Matplotlib

## 🌍 Global Environmental Change Data Visualizations

Welcome to the **PyPlot** repository! This project is designed to present various data visualizations related to global environmental change, climate science, and statistical analysis using Python's Matplotlib library. It showcases statistical graphs and projects that help illustrate complex environmental patterns and trends.

## 📁 Project Structure

The repository is organized into multiple directories, each representing different visualization techniques and projects:

- **Histograms** - Representation of environmental data distributions
- **Scatter Plots** - Identifying correlations in climate-related data
- **Line Graphs** - Visualizing trends in global temperatures and CO₂ levels
- **Bar Charts** - Comparing environmental statistics across regions
- **Box Plots** - Analyzing variability in climate-related datasets
- **Statistical Distributions** - Understanding data through probability distributions
- **Global Environmental Change Graphs** - Specific visualizations related to climate change impact

Each folder contains Python scripts and Jupyter notebooks demonstrating how to visualize different datasets effectively.

---

## 🔧 Installation Guide

To run this project, ensure you have Python and the necessary dependencies installed.

### 1️⃣ Install Python
First, download and install Python from the official site: [Python Downloads](https://www.python.org/downloads/)

Make sure to check the box **"Add Python to PATH"** during installation.

### 2️⃣ Install Required Libraries
This project relies on Matplotlib and other scientific computing libraries. You can install them using `pip`:

```sh
pip install matplotlib numpy pandas scipy seaborn
```

If you're using Jupyter Notebook, install it as well:

```sh
pip install notebook
```

### 3️⃣ Clone the Repository
To get a copy of the repository on your local machine, use:

```sh
git clone https://github.com/jentimanatol/pyplot.git
cd pyplot
```

---

## ▶️ How to Use

### Running Individual Scripts
Each folder contains Python scripts that generate specific visualizations. Navigate to a directory and execute the script:

```sh
cd "Histograms"
python histogram_example.py
```

Or, if using Jupyter Notebook:

```sh
jupyter notebook
```
Then open the respective `.ipynb` file.

### Example: Creating a Climate Change Line Graph
Here’s a quick example of how to generate a simple line graph representing global temperature trends:

```python
import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1880, 2025, 5)
temperatures = np.random.normal(14.0, 0.5, len(years))  # Simulated global temperature anomalies

plt.plot(years, temperatures, label='Global Temperature Anomaly', color='red')
plt.title("Global Temperature Anomalies Over Time")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.legend()
plt.show()
```

---

## 📊 Features
- Create various types of plots including histograms, scatter plots, and line graphs
- Understand global environmental trends through data visualization
- Analyze the impact of human activities on climate change
- Easily modify scripts for customized data exploration

---

## 📚 Course Context: ENV250 - Global Environmental Change
This project aligns with **Global Environmental Change (ENV250)** at Bunker Hill Community College, instructed by **Krista Reichert**. It aims to support the study of:
- Earth as a complex system
- Human influences on climate change
- Mitigation and adaptation strategies
- Data-driven decision-making in environmental sciences

For more details, refer to the **course syllabus** or contact **kreicher@bhcc.mass.edu**.

---

## ❓ Troubleshooting
If you encounter issues:
1. Ensure all dependencies are installed (`pip list` to check)
2. If using a virtual environment, activate it before running scripts
3. Check Python version (`python --version`)
4. Refer to the official Matplotlib documentation: [Matplotlib Docs](https://matplotlib.org/)


📩 **Contact:** If you have any questions, reach out via GitHub Issues.


_Not protected by copyright, may be used for its intended purpose._  
_Author: Anatolie Jentimir._
