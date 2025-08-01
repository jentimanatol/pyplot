import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import messagebox

def parse_vector(text):
    try:
        return np.array([float(x.strip()) for x in text.split(',')])
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

def draw_shadows(ax, tip, color):
    # Draws dashed lines from (x,y,z) to (x,0,0), (0,y,0), (0,0,z)
    x, y, z = tip
    # To x-y plane (same x,y, but z=0)
    ax.plot([x, x], [y, y], [z, 0], linestyle='dashed', color=color, linewidth=1, alpha=0.6)
    # To x-z plane (y=0)
    ax.plot([x, x], [y, 0], [0, z], linestyle='dashed', color=color, linewidth=1, alpha=0.4)
    # To y-z plane (x=0)
    ax.plot([x, 0], [0, y], [0, z], linestyle='dashed', color=color, linewidth=1, alpha=0.3)

def visualize_all_with_legend_and_shadows(u, v, uvv, v3):
    fig = plt.figure(figsize=(8,7))
    ax = fig.add_subplot(111, projection='3d')

    vectors = [
        (u,     'u',      'blue',   'o'),
        (v,     'v',      'green',  's'),
        (uvv,   '(u·v)v', 'purple', '^'),
        (v3,    '3v',     'orange', 'D')
    ]

    origin = np.zeros(3)
    for vec, label, color, marker in vectors:
        ax.quiver(*origin, *vec, color=color, label=label, arrow_length_ratio=0.12, linewidth=2)
        ax.scatter([vec[0]],[vec[1]],[vec[2]], color=color, s=70, marker=marker)
        draw_shadows(ax, vec, color)

    # Set limits and labels
    allpts = np.array([u, v, uvv, v3])
    maxlim = max(10, float(np.abs(allpts).max())+2)
    ax.set_xlim([-maxlim, maxlim])
    ax.set_ylim([-maxlim, maxlim])
    ax.set_zlim([-maxlim, maxlim])
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.legend(fontsize=13, loc='upper left')
    ax.set_title("3D Plot of Vectors (with projections)", fontsize=14)

    plt.tight_layout()
    plt.show()

class VectorCalcApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vector Operations Visualizer")
        self.configure(bg="#f7fcfd")
        self.geometry('500x600')

        # -- Your preferred headline --
        tk.Label(self, text="Vectors Calculator", font=("Lato", 19, "bold"),
                bg="#bee6fc", fg="#1a2340", pady=7).pack(fill="x")
        tk.Label(self, text="Find ", font=("Arial",13,"bold"), bg="#f7fcfd"
                ).place(x=35, y=55)
        tk.Label(self, text="u · v,  u · u,  ||v||²,  (u · v)v,  u · (3v)",
                font=("Arial",13,"bold"), fg="#222", bg="#f7fcfd").place(x=85, y=55)
        
        tk.Label(self, text="u =", font=("Arial", 13), bg="#f7fcfd").place(x=40, y=90)
        self.entry_u = tk.Entry(self, font=("Consolas", 13), width=14)
        self.entry_u.insert(0, "2, -3, 4")
        self.entry_u.place(x=85, y=90)

        tk.Label(self, text="v =", font=("Arial", 13), bg="#f7fcfd").place(x=270, y=90)
        self.entry_v = tk.Entry(self, font=("Consolas", 13), width=14)
        self.entry_v.insert(0, "0, 6, 5")
        self.entry_v.place(x=315, y=90)
        
        self.err = tk.Label(self, text="", fg="red", bg="#f7fcfd", font=("Arial",10,"bold"))
        self.err.place(x=30, y=125)
        
        self.result_box = tk.Text(self, width=48, height=9, font=("Consolas",13), bg="#f8fafb", relief="groove")
        self.result_box.place(x=25, y=155)
        self.result_box.config(state=tk.DISABLED)

        tk.Button(self, text="Calculate all", font=("Verdana",12,"bold"),
                  command=self.calculate, bg="#157b26", fg="white", width=13,
                  height=1).place(x=170, y=325)

        tk.Button(self, text="3D All Vectors + Legend", command=self.visualize_all,
                  bg="#175bba", fg="white", width=23, height=2).place(x=125, y=385)

        tk.Label(self, text="Vector format:    2, -3, 4", fg="#7e8fa5", bg="#f7fcfd", font=("Arial",11)
                 ).place(x=170, y=360)
        
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
        a = int(np.dot(u, v))
        b = int(np.dot(u, u))
        c = int(np.dot(v, v))
        d = np.dot(u, v) * v
        e = int(np.dot(u, 3*v))
        self.data = {'u': u, 'v': v, 'uvv': d, 'v3': 3*v}

        # Output, matching textbook/screenshot style:
        res = []
        res.append(f"(a)   u · v      = {a}")
        res.append(f"(b)   u · u      = {b}")
        res.append(f"(c)   ||v||²     = {c}")
        res.append(f"(d)   (u·v)v     = {format_vec(d)}")
        res.append(f"(e)   u · (3v)   = {e}")
        self.result_box.insert("end", '\n'.join(res))
        self.result_box.config(state=tk.DISABLED)

    def visualize_all(self):
        # Check for None *explicitly* (no "in" with array, to avoid ambiguity)
        d = self.data
        needed = ('u', 'v', 'uvv', 'v3')
        # Recompute if missing one key
        if not all(k in d and d[k] is not None for k in needed):
            self.calculate()
        d = self.data
        # Now confirm all are numpy arrays of size 3
        if not all((k in d and isinstance(d[k], np.ndarray) and d[k].shape == (3,)) for k in needed):
            messagebox.showerror("Error", "Please calculate results first.")
            return
        visualize_all_with_legend_and_shadows(d['u'], d['v'], d['uvv'], d['v3'])

if __name__ == "__main__":
    VectorCalcApp().mainloop()
