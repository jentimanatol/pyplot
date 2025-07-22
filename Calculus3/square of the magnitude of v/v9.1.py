import numpy as np
import matplotlib.pyplot as plt
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

def draw_plane(ax, axis, size=10, alpha=0.12):
    xx = yy = np.linspace(-size, size, 2)
    if axis == "xy":
        X, Y = np.meshgrid(xx, yy)
        Z = np.zeros_like(X)
        ax.plot_surface(X, Y, Z, color="gray", alpha=alpha, linewidth=0, zorder=-1)
    elif axis == "yz":
        Y, Z = np.meshgrid(xx, yy)
        X = np.zeros_like(Y)
        ax.plot_surface(X, Y, Z, color="gray", alpha=alpha, linewidth=0, zorder=-1)
    elif axis == "xz":
        X, Z = np.meshgrid(xx, yy)
        Y = np.zeros_like(X)
        ax.plot_surface(X, Y, Z, color="gray", alpha=alpha, linewidth=0, zorder=-1)

def draw_shadows(ax, tip, color):
    x, y, z = tip
    ax.plot([x, x], [y, y], [z, 0], linestyle="dashed", color=color, linewidth=1, alpha=0.7)
    ax.plot([x, x], [y, 0], [0, 0], linestyle="dashed", color=color, linewidth=1, alpha=0.5)
    ax.plot([x, 0], [0, 0], [0, 0], linestyle="dashed", color=color, linewidth=1, alpha=0.3)

def visualize_vector(vec, label):
    fig = plt.figure(figsize=(6,5))
    ax = fig.add_subplot(111, projection='3d')
    for plane in ["xy", "xz", "yz"]:
        draw_plane(ax, plane, size=10, alpha=0.13)
    origin = np.zeros(3)
    color = 'blue'
    ax.quiver(*origin, *vec, color=color, arrow_length_ratio=0.13, linewidth=2, label=label)
    ax.scatter([vec[0]], [vec[1]], [vec[2]], color='blue', s=65)
    draw_shadows(ax, vec, color)
    maxlim = max(10, float(np.abs(vec).max())+2)
    ax.set_xlim([-maxlim, maxlim])
    ax.set_ylim([-maxlim, maxlim])
    ax.set_zlim([-maxlim, maxlim])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    ax.set_title(f"3D Plot: {label}")
    ax.grid(False)
    ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
    plt.tight_layout()
    plt.show()

def visualize_all(u, v, uvv, v3):
    fig = plt.figure(figsize=(8,7))
    ax = fig.add_subplot(111, projection='3d')
    for plane in ["xy", "xz", "yz"]:
        draw_plane(ax, plane, size=10, alpha=0.13)

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
    allpts = np.array([u, v, uvv, v3])
    maxlim = max(10, float(np.abs(allpts).max())+2)
    ax.set_xlim([-maxlim, maxlim])
    ax.set_ylim([-maxlim, maxlim])
    ax.set_zlim([-maxlim, maxlim])
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.legend(fontsize=13, loc='upper left')
    ax.set_title("3D Plot: Main Vectors")
    ax.grid(False)
    ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
    plt.tight_layout()
    plt.show()

class VectorCalcApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vectors Calculator")
        self.configure(bg="#f7fcfd")
        self.geometry('626x725')

        tk.Label(self, text="Vectors Calculator", font=("Lato", 19, "bold"),
                bg="#bee6fc", fg="#1a2340", pady=7).pack(fill="x")
        topy = 55
        tk.Label(self, text="Find ", font=("Arial",13,"bold"), bg="#f7fcfd"
                ).place(x=35, y=topy)
        tk.Label(self, text="u · v,  u · u,  ||v||²,  (u · v)v,  u · (3v)",
                font=("Arial",13,"bold"), fg="#222", bg="#f7fcfd").place(x=85, y=topy)
        
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

        # Special button group for all requested d[] keys
        visf = tk.Frame(self, bg="#f7fcfd")
        visf.place(x=8, y=430)

        self.btns = {}
        btninfo = [
            ("u",      "u",      0), ("v",      "v",      1),
            ("uv",     "u·v",    2), ("vv",     "v·v",    3),
            ("uu",     "u·u",    4), ("uvv",    "(u·v)v", 5),
            ("v3",     "3v",     6), ("d3",     "u×v",    7)
        ]
        for name, label, col in btninfo:
            b = tk.Button(visf, text=f"3D {label}", command=lambda n=name: self.visualize_component(n),
                          width=7, height=2, font=("Arial",11))
            b.grid(row=0, column=col, padx=4, pady=2)
            self.btns[name] = b

        tk.Button(self, text="3D Plot: Main Vectors", command=self.visualize_all,
                  bg="#175bba", fg="white", width=23, height=2).place(x=185, y=376)

        tk.Label(self, text="Vector format:    2, -3, 4", fg="#7e8fa5", bg="#f7fcfd", font=("Arial",11)
                 ).place(x=190, y=410)
        
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
        uv  = np.dot(u, v)
        vv  = np.dot(v, v)
        uu  = np.dot(u, u)
        uvv = uv * v
        v3  = 3 * v
        d3  = np.cross(u, v)
        self.data = {
            'u': u, 'v': v, 'uv': uv, 'vv': vv, 'uu': uu, 'uvv': uvv, 'v3': v3, 'd3': d3
        }
        res = []
        res.append(f"(a)   u · v      = {int(uv)}")
        res.append(f"(b)   u · u      = {int(uu)}")
        res.append(f"(c)   ||v||²     = {int(vv)}")
        res.append(f"(d)   (u·v)v     = {format_vec(uvv)}")
        res.append(f"(e)   u · (3v)   = {int(np.dot(u, v3))}")
        res.append(f"(f)   u × v      = {format_vec(d3)}")
        self.result_box.insert("end", '\n'.join(res))
        self.result_box.config(state=tk.DISABLED)

    def visualize_component(self, key):
        d = self.data
        if not d:
            self.calculate()
            d = self.data
        if key not in d:
            messagebox.showerror("Error", f"Please calculate results first.")
            return
        val = d[key]
        # Scalars: just show value in message; vectors: plot
        if key in ['uv','vv','uu']:
            title = {
                'uv': 'u · v',
                'vv': 'v · v',
                'uu': 'u · u',
            }[key]
            messagebox.showinfo("Scalar", f"{title} = {val}")
        else:
            label = {
                'u':'u', 'v':'v','uvv':'(u·v)v','v3':'3v','d3':'u×v'
            }[key]
            visualize_vector(val, label)

    def visualize_all(self):
        d = self.data
        keys = ['u','v','uvv','v3']
        if not all(k in d and isinstance(d[k], np.ndarray) and d[k].shape == (3,) for k in keys):
            self.calculate()
            d = self.data
        if not all(k in d and isinstance(d[k], np.ndarray) and d[k].shape == (3,) for k in keys):
            messagebox.showerror("Error", "Please calculate results first.")
            return
        visualize_all(d['u'], d['v'], d['uvv'], d['v3'])

if __name__ == "__main__":
    VectorCalcApp().mainloop()
