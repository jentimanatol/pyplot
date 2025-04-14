# MAT-181: Statistical Data Visualization with Matplotlib

Welcome to the **MAT-181** repository! This project focuses on visualizing statistical data using Python's Matplotlib library. It includes various graphing techniques such as histograms, frequency distributions, and confidence intervals to aid in statistical analysis.

## 📁 Project Structure

The repository is organized into multiple directories, each representing different statistical visualization tasks:

- **90% Confidence Interval for Population Proportion**
- **Cumulative Area from the Left**
- **Frequency Distribution Graph**
- **Histogram of Days Off for Police Detectives**
- **Histogram of Heights in a Group**
- **Histogram of Heights in a Group Bins**
- **Histogram of Steps Walked**

Each folder contains Python scripts demonstrating how to visualize specific statistical concepts using Matplotlib.

---

## 🔧 Installation Guide

To run this project, ensure you have Python and the necessary dependencies installed.

### 1️⃣ Install Python
First, download and install Python from the official site: [Python Downloads](https://www.python.org/downloads/)

Make sure to check the box **"Add Python to PATH"** during installation.

### 2️⃣ Install Required Libraries
This project relies on Matplotlib and other scientific computing libraries. You can install them using `pip`:

```sh
pip install matplotlib numpy pandas scipy
```

If you're using Jupyter Notebook, install it as well:

```sh
pip install notebook
```

### 3️⃣ Clone the Repository
To get a copy of the repository on your local machine, use:

```sh
git clone https://github.com/yourusername/MAT-181.git
cd MAT-181
```

---

## ▶️ How to Use

### Running Individual Scripts
Each folder contains Python scripts that generate specific statistical graphs. Navigate to a directory and execute the script:

```sh
cd "Histogram of Steps Walked"
python histogram_steps.py
```

Or, if using Jupyter Notebook:

```sh
jupyter notebook
```
Then open the respective `.ipynb` file.

### Example: Generating a Histogram
Here’s a quick example of how to generate a histogram using Matplotlib:

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(170, 10, 250)  # Example height data
plt.hist(data, bins=10, color='blue', edgecolor='black')
plt.title("Histogram of Heights")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()
```

---

## 📊 Features
- Visualize different statistical distributions
- Analyze frequency distributions and confidence intervals
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
