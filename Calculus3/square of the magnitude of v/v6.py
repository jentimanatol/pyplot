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
    # Integer if possible, else 2 decimal places
    items = []
    for x in v:
        if abs(x - int(x)) < 1e-10:
            items.append(str(int(round(x))))
        else:
            items.append(f"{x:.2f}")
    return "<" + ", ".join(items) + ">"

def visualize_vector(vec, veclabel):
    fig = plt.figure(figsize=(5,4))
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color='blue', arrow_length_ratio=0.13)
    ax.scatter([vec[0]], [vec[1]], [vec[2]], color="red", s=45)
    maxaxis = max(10, int(max(np.abs(vec))*1.2+1))
    ax.set_xlim([-maxaxis, maxaxis])
    ax.set_ylim([-maxaxis, maxaxis])
    ax.set_zlim([-maxaxis, maxaxis])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f"3D Plot: {veclabel}")
    plt.tight_layout()
    plt.show()

class VectorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calc 3 Vector Operations")
        self.geometry("420x520")
        self.resizable(False, False)
        self.configure(bg="#f7fcfd")

        # Layout
        tk.Label(self, text="Find  u·v , u·u ,  ||v||² , (u·v)v , and  u·(3v) .",
                 font=("Arial",13,"bold"), fg="#222", bg="#f7fcfd").pack(pady=(8, 2))
        
        fr = tk.Frame(self, bg="#f7fcfd")
        fr.pack()

        tk.Label(fr, text="u =", font=("Arial",11), bg="#f7fcfd").grid(row=0,column=0,sticky="e")
        self.ent_u = tk.Entry(fr, width=14, font=("Consolas",13))
        self.ent_u.insert(0, "2, -3, 4")
        self.ent_u.grid(row=0,column=1,padx=(2,8))

        tk.Label(fr, text="v =", font=("Arial",11), bg="#f7fcfd").grid(row=0,column=2,sticky="e")
        self.ent_v = tk.Entry(fr, width=14, font=("Consolas",13))
        self.ent_v.insert(0, "0, 6, 5")
        self.ent_v.grid(row=0,column=3)

        # 
        self.err_label = tk.Label(self, text="", fg="red", bg="#f7fcfd", font=("Arial",10,"bold"))
        self.err_label.pack()
        
        self.calc_btn = tk.Button(self, text="Calculate all", font=("Verdana",12,"bold"),
                                  command=self.calculate, bg="#157b26", fg="white")
        self.calc_btn.pack(pady=10)

        self.output = tk.Text(self, width=38, height=9, font=("Consolas",13), bg="#f4f9fa", borderwidth=2, relief="groove")
        self.output.pack()
        self.output.config(state=tk.DISABLED)
        
        # Visualize buttons
        visf = tk.Frame(self, bg="#f7fcfd")
        visf.pack(pady=10)
        tk.Button(visf, text="3D u",         command=self.visualize_u,   bg="#175bba", fg="white", width=7).grid(row=0,column=0,padx=3)
        tk.Button(visf, text="3D v",         command=self.visualize_v,   bg="#ba3f1c", fg="white", width=7).grid(row=0,column=1,padx=3)
        tk.Button(visf, text="3D (u·v)v",    command=self.visualize_uvv, bg="#b924ba", fg="white", width=10).grid(row=0,column=2,padx=3)
        tk.Button(visf, text="3D 3v",        command=self.visualize_3v,  bg="#b97e24", fg="white", width=7).grid(row=0,column=3,padx=3)

        tk.Label(self, text="Type values like:  2, -3, 4", fg="#7e8fa5", bg="#f7fcfd", font=("Arial",9)).pack(pady=(6,4))

        self.data = {}
    
    def calculate(self):
        self.err_label['text'] = ""
        self.output.config(state=tk.NORMAL)
        self.output.delete(1.0, "end")
        u = parse_vector(self.ent_u.get())
        v = parse_vector(self.ent_v.get())
        if u is None or len(u)!=3 or v is None or len(v)!=3:
            self.err_label['text'] = "Enter 3 values per vector, separated by commas."
            return

        a = np.dot(u,v)
        b = np.dot(u,u)
        c = np.dot(v,v)
        d = a*v
        e = np.dot(u,3*v)
        # Save for visualization
        self.data = {'u':u, 'v':v, 'udotv':a}
        table_style = [("a) u · v =", str(int(a))),
                       ("b) u · u =", str(int(b))),
                       ("c) ||v||² =", str(int(c))),
                       ("d) (u·v)v =", format_vec(d)),
                       ("e) u · (3v) =", str(int(e)))]
        # Output
        for label, result in table_style:
            self.output.insert(tk.END, f"{label:<13} {result}\n")
        self.output.config(state=tk.DISABLED)
    
    def visualize_u(self):
        u = self.data.get('u')
        if u is None:
            u = parse_vector(self.ent_u.get())
        if u is not None and len(u)==3:
            visualize_vector(u, "u")
        else:
            messagebox.showerror("Error", "Calculate results first!")

    def visualize_v(self):
        v = self.data.get('v')
        if v is None:
            v = parse_vector(self.ent_v.get())
        if v is not None and len(v)==3:
            visualize_vector(v, "v")
        else:
            messagebox.showerror("Error", "Calculate results first!")

    def visualize_uvv(self):
        a = self.data.get('udotv')
        v = self.data.get('v')
        if v is None or a is None:
            v = parse_vector(self.ent_v.get())
            a = np.dot(parse_vector(self.ent_u.get()), v) if v is not None else None
        if v is not None and a is not None and len(v)==3:
            visualize_vector(a*v, "(u·v)v")
        else:
            messagebox.showerror("Error", "Calculate results first!")

    def visualize_3v(self):
        v = self.data.get('v')
        if v is None:
            v = parse_vector(self.ent_v.get())
        if v is not None and len(v)==3:
            visualize_vector(3*v, "3v")
        else:
            messagebox.showerror("Error", "Calculate results first!")

if __name__ == "__main__":
    VectorGUI().mainloop()
