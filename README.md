# PyPlot: Data Visualization with Matplotlib

Welcome to the **PyPlot** repository! This project showcases various data visualization techniques using Python's Matplotlib library. The repository contains scripts and notebooks for plotting histograms, scatter plots, line graphs, and statistical distributions.

## 📁 Project Structure

The repository is organized into multiple directories, each representing different visualization techniques:

- **Histograms**
- **Scatter Plots**
- **Line Graphs**
- **Bar Charts**
- **Box Plots**
- **Statistical Distributions**

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

### Example: Creating a Line Graph
Here’s a quick example of how to generate a simple line graph using Matplotlib:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='Sine Wave', color='blue')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
```

---

## 📊 Features
- Create various types of plots including histograms, scatter plots, and line graphs
- Understand data distributions using statistical visualizations
- Easily modify scripts for customized data visualization

---

## ❓ Troubleshooting
If you encounter issues:
1. Ensure all dependencies are installed (`pip list` to check)
2. If using a virtual environment, activate it before running scripts
3. Check Python version (`python --version`)
4. Refer to the official Matplotlib documentation: [Matplotlib Docs](https://matplotlib.org/)




_Not protected by copyright, may be used for its intended purpose._  
_Author: Anatolie Jentimir._
