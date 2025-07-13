# 📈 Parametric Line Visualizer - Calculus 3 Toolkit

This Python GUI app helps visualize a **parametric line in 3D space** — perfect for Calculus III students learning vector equations.

## 🎓 Purpose

This tool demonstrates how a line in space can be described using a point and a direction vector:

- 📌 Given Point: \( P = (x_0, y_0, z_0) \)
- ➡️ Direction Vector: \( ec{u} = \langle a, b, c angle \)
- 📈 Parametric Equations:
  ```
  x(t) = x₀ + at  
  y(t) = y₀ + bt  
  z(t) = z₀ + ct
  ```

## 🧰 Features

- Friendly **Tkinter GUI** 🖼️
- Default data:
  - Point: **(2, 8, 5)**
  - Vector: **⟨−3, 4, −1⟩**
  - Value of t: **1**
- 🔢 Enter any value of `t` to see corresponding point
- 📄 “Print Data” displays parametric equations and key points
- 🎨 “Visualize Line” shows a 3D plot using Matplotlib

## 🖥️ Requirements

Install dependencies using:

```bash
pip install matplotlib numpy
```

## ▶️ How to Run

1. Save the Python file: `parametric_line_gui_final.py`
2. Run it:

```bash
python parametric_line_gui_final.py
```

3. Use the interface to explore different points and vectors.

## 📦 Files

- `parametric_line_gui_final.py` — the main application
- `README.md` — this documentation file

## 🧮 Example

Using default values:
- Point: \( P = (2, 8, 5) \)
- Vector: \( ec{u} = \langle -3, 4, -1 angle \)
- \( t = 1 \)

Generates:
- Another point: \( (-1, 12, 4) \)
- Line passes through both points and follows the vector direction

---

Created with ❤️ for students exploring vectors and parametric equations in Calculus 3.
