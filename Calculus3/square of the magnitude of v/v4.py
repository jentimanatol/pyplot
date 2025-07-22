import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import messagebox

def parse_vector(text):
    try:
        v = [float(x.strip()) for x in text.split(',')]
        assert len(v) > 0
        return np.array(v)
    except Exception:
        return None

def format_vec(vec):
    return "<" + ", ".join(str(int(x)) if x == int(x) else f"{x:.2f}" for x in vec) + ">"

def visualize_vector(vec, label):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, *vec, color='blue', arrow_length_ratio=0.12, linewidth=2)
    max_axis = max(10, np.max(np.abs(vec)) + 2)
    ax.set_xlim([-max_axis, max_axis])
    ax.set_ylim([-max_axis, max_axis])
    ax.set_zlim([-max_axis, max_axis])
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.set_title(f"Visualize: {label}", fontsize=15)
    ax.scatter([vec[0]], [vec[1]], [vec[2]], color='red', s=45)
    plt.tight_layout()
    plt.show()

class VectorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vector Calculator (Calc III Student Tool)")
        self.config(bg="#eaf5fc")
        self.geometry("420x610")
        tk.Label(self, text="Enter u:", bg="#eaf5fc", font=("Tahoma",12)).pack(pady=1)
        self.in_u = tk.Entry(self, font=("Consolas",13), width=22)
        self.in_u.insert(0, "2, -3, 4")
        self.in_u.pack(pady=2)
        tk.Label(self, text="Enter v:", bg="#eaf5fc", font=("Tahoma",12)).pack(pady=1)
        self.in_v = tk.Entry(self, font=("Consolas",13), width=22)
        self.in_v.insert(0, "0, 6, 5")
        self.in_v.pack(pady=2)
        self.calc_btn = tk.Button(self, text="Calculate All", font=("Verdana", 12, "bold"),
                                  command=self.calculate, bg="#218e2a", fg="white")
        self.calc_btn.pack(pady=10)
        self.out_box = tk.Text(self, width=40, height=10, font=("Consolas",12), bg="#f9fdff")
        self.out_box.pack()
        self.err = tk.Label(self, text="", fg="red", bg="#eaf5fc", font=("Arial",10,"bold"))
        self.err.pack()

        btnframe = tk.Frame(self, bg="#eaf5fc")
        btnframe.pack(pady=12)
        tk.Button(btnframe, text="3D: u", command=self.show_u, bg="#175bba", fg="white", width=8).grid(row=0,column=0,padx=3,pady=3)
        tk.Button(btnframe, text="3D: v", command=self.show_v, bg="#175bba", fg="white", width=8).grid(row=0,column=1,padx=3,pady=3)
        tk.Button(btnframe, text="3D: (u·v)v", command=self.show_uvv, bg="#7a3b94", fg="white", width=10).grid(row=0,column=2,padx=3,pady=3)
        tk.Button(btnframe, text="3D: 3v", command=self.show_3v, bg="#ff8800", fg="white", width=8).grid(row=0,column=3,padx=3,pady=3)
        # Optionally visualize all (unified plot): 
        # tk.Button(btnframe, text="Show All", command=self.show_all_vectors).grid(row=1,columnspan=4,pady=3)

        tk.Label(self, text="\u2139\ufe0f Example: u = 2, -3, 4      v = 0, 6, 5",
                 font=("Arial",9), fg="#5d5d5d", bg="#eaf5fc").pack(pady=3)
        self.data = {}

    def calculate(self):
        self.err['text'] = ""
        self.out_box.delete(1.0, "end")
        u = parse_vector(self.in_u.get())
        v = parse_vector(self.in_v.get())
        if u is None or len(u) != 3 or v is None or len(v) != 3:
            self.err['text'] = "Input 3 values per vector, separated by commas!"
            return
        udotv = np.dot(u, v)
        udotu = np.dot(u, u)
        normv2 = np.dot(v, v)
        uvv = udotv * v
        u3v = np.dot(u, 3*v)
        self.data = {'u':u, 'v':v, 'udotv':udotv, 'udotu':udotu, 'normv2':normv2, 'uvv':uvv, 'u3v':u3v}
        results = []
        results.append(f"(a) u · v = {udotv}")
        results.append(f"(b) u · u = {udotu}")
        results.append(f"(c) ||v||² = {normv2}")
        results.append(f"(d) (u·v)v = {format_vec(uvv)}")
        results.append(f"(e) u · (3v) = {u3v}")
        self.out_box.insert("end", "\n".join(results))

    def show_u(self):
        u = self.data.get('u') or parse_vector(self.in_u.get())
        if u is None or len(u) !=3:
            messagebox.showerror("Error", "Enter valid 3D vector u.")
            return
        visualize_vector(u, "u")

    def show_v(self):
        v = self.data.get('v') or parse_vector(self.in_v.get())
        if v is None or len(v) !=3:
            messagebox.showerror("Error", "Enter valid 3D vector v.")
            return
        visualize_vector(v, "v")

    def show_uvv(self):
        udotv = self.data.get('udotv')
        v = self.data.get('v') or parse_vector(self.in_v.get())
        if udotv is None or v is None or len(v)!=3:
            messagebox.showerror("Error", "Calculate first!")
            return
        uvv = udotv * v
        visualize_vector(uvv, "(u·v)v")

    def show_3v(self):
        v = self.data.get('v') or parse_vector(self.in_v.get())
        if v is None or len(v) != 3:
            messagebox.showerror("Error", "Enter valid 3D vector v.")
            return
        visualize_vector(3*v, "3v")

if __name__ == "__main__":
    VectorApp().mainloop()
