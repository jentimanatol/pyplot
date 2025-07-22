import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk

# --- Helper for vector parsing ---
def parse_vector(text):
    try:
        vector = [float(x.strip()) for x in text.split(',')]
        if len(vector) == 0:
            raise ValueError
        return np.array(vector)
    except Exception:
        return None

# --- Main GUI Class ---
class VectorCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vectors Operations (Calculus 3 Helper)")
        self.configure(bg="#f8fcff")
        self.geometry("480x450")
        
        # Headline
        tk.Label(self, text="Vectors Calculator", font=("Lato", 19, "bold"), bg="#bee6fc", fg="#1a2340", pady=7).pack(fill="x")
        
        # Vector input fields
        f_input = tk.Frame(self, bg="#f8fcff")
        f_input.pack(pady=15)
        tk.Label(f_input, text="u =", font=("Consolas", 13), bg="#f8fcff").grid(row=0, column=0, padx=1, sticky="e")
        self.e_u = tk.Entry(f_input, font=("Consolas", 13), width=18)
        self.e_u.insert(0, "2, -3, 4")  # defaults
        self.e_u.grid(row=0, column=1, padx=8)
        tk.Label(f_input, text="v =", font=("Consolas", 13), bg="#f8fcff").grid(row=1, column=0, sticky="e")
        self.e_v = tk.Entry(f_input, font=("Consolas", 13), width=18)
        self.e_v.insert(0, "0, 6, 5")
        self.e_v.grid(row=1, column=1, padx=8)
        
        # Calculate button
        self.btn_calc = tk.Button(self, text="🧮 Calculate All", font=("Verdana", 13, "bold"),
            bg="#3bb273", fg="white", command=self.calculate)
        self.btn_calc.pack(pady=8, ipadx=8, ipady=2)

        # Results area
        tk.Label(self, text="Results:", font=("Verdana", 11, "bold"), fg="#185aba", bg="#f8fcff").pack()
        self.results = tk.Text(self, width=53, height=9, font=("Consolas", 11), bg="#f4f8fd", relief="groove")
        self.results.pack(pady=2)

        # Visualize button
        self.btn_viz = tk.Button(self, text="📊 3D Visualize All", font=("Verdana", 12, "bold"),
            bg="#1861ae", fg="white", command=self.visualize)
        self.btn_viz.pack(pady=10, ipadx=11, ipady=2)
        
        # Error label
        self.lbl_error = tk.Label(self, text="", fg="red", bg="#f8fcff", font=("Arial", 11, "bold"))
        self.lbl_error.pack()

        # Tips section
        tk.Label(self, text="• Separators: comma only (e.g., 1, 2, 3)\n• Non-3D vectors are supported!\n",
            font=("Arial",9), fg="#697882", bg="#f8fcff").pack()

    def calculate(self):
        self.lbl_error.config(text="")
        self.results.delete(1.0, "end")
        u = parse_vector(self.e_u.get())
        v = parse_vector(self.e_v.get())
        if u is None or v is None:
            self.lbl_error.config(text="Invalid input! Enter like: 5,2,1")
            return
        # Results
        lines = []
        lines.append(f"u = {u}")
        lines.append(f"v = {v}")
        lines.append(f"u · v......... = {np.dot(u, v):.4g}")
        lines.append(f"u · u......... = {np.dot(u, u):.4g}")
        lines.append(f"||v||²........ = {np.dot(v, v):.4g}")
        lines.append(f"(u · v)v...... = {np.round(np.dot(u, v) * v, 4)}")
        lines.append(f"u · (3v)...... = {np.dot(u, 3*v):.4g}")
        self.results.insert("end", "\n".join(lines))

    def visualize(self):
        self.lbl_error.config(text="")
        u = parse_vector(self.e_u.get())
        v = parse_vector(self.e_v.get())
        if u is None or v is None:
            self.lbl_error.config(text="Invalid input! Enter like: 1,0,2")
            return
        vectors = {
            "u (blue)": (u, "blue"),
            "v (green)": (v, "green"),
            "(u·v)v (purple)": (np.dot(u, v) * v, "purple"),
            "3v (orange)": (3 * v, "orange"),
        }
        fig = plt.figure(figsize=(7,5))
        ax = fig.add_subplot(111, projection="3d")
        origin = np.zeros(len(u))
        keyz = list(vectors.keys())
        for idx, (label, (vec, color)) in enumerate(vectors.items()):
            ax.quiver(*origin, *vec, color=color, label=label, arrow_length_ratio=0.13)
        maxlen = max(np.linalg.norm(u), np.linalg.norm(v), np.linalg.norm(3*v)) + 2
        for axis in "xyz":
            getattr(ax, f"set_{axis}lim")([-maxlen, maxlen])
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z" if len(u) >= 3 else "")
        ax.set_title("3D Vector Visualization", fontsize=14)
        ax.legend()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = VectorCalculator()
    app.mainloop()
