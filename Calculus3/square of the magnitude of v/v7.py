import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import messagebox

def parse_vector(text):
    try:
        return np.array([float(x.strip()) for x in text.split(",")])
    except:
        return None

def format_vec(v):
    items = []
    for x in v:
        if abs(x - int(x)) < 1e-10:
            items.append(str(int(round(x))))
        else:
            items.append(f"{x:.2f}")
    return "<" + ", ".join(items) + ">"

def visualize_all_with_legend_and_shadows(u, v, uvv, v3):
    fig = plt.figure(figsize=(8,7))
    ax = fig.add_subplot(111, projection='3d')

    vectors = [
        (u, 'u', 'blue', 'o'),
        (v, 'v', 'green', 's'),
        (uvv, '(u·v)v', 'purple', '^'),
        (v3, '3v', 'orange', 'D')
    ]

    origin = np.zeros(3)
    for vec, label, color, marker in vectors:
        # Arrow
        ax.quiver(*origin, *vec, color=color, label=label, arrow_length_ratio=0.13, linewidth=2)
        # Point
        ax.scatter([vec[0]],[vec[1]],[vec[2]], color=color, s=65, marker=marker)
        # Three dashed drop lines
        ax.plot([vec[0], vec[0]], [vec[1], vec[1]], [vec[2], 0], linestyle='dashed', color=color, alpha=0.5)
        ax.plot([vec[0], vec[0]], [vec[1], 0], [0,0], linestyle='dashed', color=color, alpha=0.5)
        ax.plot([vec[0], 0], [0,0], [0,0], linestyle='dashed', color=color, alpha=0.4)

    # Set limits and labels
    allpts = np.array([u, v, uvv, v3])
    maxlim = max(10, np.abs(allpts).max()+2)
    ax.set_xlim([-maxlim, maxlim])
    ax.set_ylim([-maxlim, maxlim])
    ax.set_zlim([-maxlim, maxlim])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    ax.set_title("3D Plot of Vectors (with shadows)")

    plt.tight_layout()
    plt.show()

class VectorCalcApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vector Operations Visualizer")
        self.configure(bg="#f7fcfd")
        self.geometry('500x600')

        # Your headline, as requested
        tk.Label(self, text="Vectors Calculator", font=("Lato", 19, "bold"), bg="#bee6fc", fg="#1a2340", pady=7).pack(fill="x")

        tk.Label(self, text="u =", font=("Arial", 13), bg="#f7fcfd").place(x=40, y=70)
        self.entry_u = tk.Entry(self, font=("Consolas", 13), width=14)
        self.entry_u.insert(0, "2, -3, 4")
        self.entry_u.place(x=85, y=70)

        tk.Label(self, text="v =", font=("Arial", 13), bg="#f7fcfd").place(x=270, y=70)
        self.entry_v = tk.Entry(self, font=("Consolas", 13), width=14)
        self.entry_v.insert(0, "0, 6, 5")
        self.entry_v.place(x=315, y=70)
        
        self.err = tk.Label(self, text="", fg="red", bg="#f7fcfd", font=("Arial",10,"bold"))
        self.err.place(x=30, y=105)

        self.result_box = tk.Text(self, width=48, height=10, font=("Consolas",13), bg="#f8fafb")
        self.result_box.place(x=25, y=130)
        self.result_box.config(state=tk.DISABLED)

        tk.Button(self, text="Calculate all", font=("Verdana",12,"bold"),
                  command=self.calculate, bg="#157b26", fg="white", width=13,
                  height=1).place(x=170, y=305)

        tk.Button(self, text="3D All Vectors + Legend", command=self.visualize_all, bg="#175bba", fg="white", width=23, height=2).place(x=125, y=370)

        tk.Label(self, text="Vector format:    2, -3, 4", fg="#7e8fa5", bg="#f7fcfd", font=("Arial",11)).place(x=170, y=340)
        
        self.data = {}

    def calculate(self):
        self.err['text'] = ""
        self.result_box.config(state=tk.NORMAL)
        self.result_box.delete(1.0, "end")
        u = parse_vector(self.entry_u.get())
        v = parse_vector(self.entry_v.get())
        if u is None or v is None or len(u)!=3 or len(v)!=3:
            self.err['text'] = "Enter valid 3D vectors, separated by commas."
            return
        a = np.dot(u, v)
        b = np.dot(u, u)
        c = np.dot(v, v)
        d = a * v
        e = np.dot(u, 3*v)
        self.data = {'u': u, 'v': v, 'udotv': a, 'uvv': d, 'v3': 3*v}

        # Output, matching your screenshot
        res = []
        res.append(f"(a)   u · v      = {a}")
        res.append(f"(b)   u · u      = {b}")
        res.append(f"(c)   ||v||²     = {c}")
        res.append(f"(d)   (u·v)v     = {format_vec(d)}")
        res.append(f"(e)   u · (3v)   = {e}")
        self.result_box.insert("end", '\n'.join(res))
        self.result_box.config(state=tk.DISABLED)

    def visualize_all(self):
        # All main vectors, with legends and dashed lines for their point shadows
        d = self.data
        u = d.get('u')
        v = d.get('v')
        uvv = d.get('uvv')
        v3 = d.get('v3')
        if None in (u, v, uvv, v3):
            self.calculate()
            u = self.data.get('u')
            v = self.data.get('v')
            uvv = self.data.get('uvv')
            v3 = self.data.get('v3')
        if None in (u, v, uvv, v3):
            messagebox.showerror("Error", "Please calculate results first.")
            return
        visualize_all_with_legend_and_shadows(u, v, uvv, v3)

if __name__ == "__main__":
    VectorCalcApp().mainloop()
