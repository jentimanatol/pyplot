import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def parse_vec(s):
    try:
        parts = [float(x.strip()) for x in s.split(',')]
        if len(parts) != 3:
            return None
        return np.array(parts)
    except:
        return None

def pretty_vec(v):
    return "<" + ",".join(str(int(round(x))) for x in v) + ">"

class VectorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vectors Calculator")
        self.geometry("950x410")
        self.configure(bg="#f7fcfd")

        # Stylized headline
        tk.Label(self, text="Vectors Calculator", font=("Lato", 19, "bold"), bg="#bee6fc", fg="#1a2340", pady=7).grid(row=0, column=0, columnspan=3, sticky="ew")

        # --- User Input
        inpfrm = tk.Frame(self, bg="#f7fcfd")
        inpfrm.grid(row=1, column=0, sticky="nw", padx=20, pady=(18,2))

        tk.Label(inpfrm, text="u =", font=("Arial", 13), bg="#f7fcfd").grid(row=0, column=0, sticky='e')
        self.ent_u = tk.Entry(inpfrm, width=16, font=("Consolas", 13))
        self.ent_u.insert(0, "2, -3, 4")
        self.ent_u.grid(row=0, column=1)
        tk.Label(inpfrm, text="    v =", font=("Arial", 13), bg="#f7fcfd").grid(row=0, column=2)
        self.ent_v = tk.Entry(inpfrm, width=16, font=("Consolas", 13))
        self.ent_v.insert(0, "0, 6, 5")
        self.ent_v.grid(row=0, column=3)

        self.err = tk.Label(inpfrm, fg="red", bg="#f7fcfd", font=("Arial", 10, "bold"))
        self.err.grid(row=1, column=0, columnspan=4, sticky="w")

        # --- Buttons pane (vertical, small to save space)
        btnfrm = tk.Frame(self, bg="#f7fcfd")
        btnfrm.grid(row=2, column=0, sticky="nw", padx=20)
        tk.Button(btnfrm, text="u · v", width=7, command=self.show_udotv).grid(row=0, column=0, pady=1)
        tk.Button(btnfrm, text="u · u", width=7, command=self.show_udotu).grid(row=1, column=0, pady=1)
        tk.Button(btnfrm, text="||v||²", width=7, command=self.show_normv2).grid(row=2, column=0, pady=1)
        tk.Button(btnfrm, text="(u·v)v", width=7, command=self.show_uvv).grid(row=3, column=0, pady=1)
        tk.Button(btnfrm, text="u · (3v)", width=7, command=self.show_u3v).grid(row=4, column=0, pady=1)
        tk.Button(btnfrm, text="All Results", width=10, bg="#157b26", fg="white", font=("Verdana",10,"bold"), command=self.show_all).grid(row=5, column=0, pady=(8,2))

        # --- Matplotlib plot area in the MIDDLE
        plotfrm = tk.Frame(self, bg="#f7fcfd")
        plotfrm.grid(row=1, column=1, rowspan=4, padx=7, pady=8, sticky="nsw")
        self.fig = plt.figure(figsize=(5,4))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=plotfrm)
        self.plot_widget = self.canvas.get_tk_widget()
        self.plot_widget.grid(row=0, column=0)

        # --- Results (right)
        self.resfrm = tk.Frame(self, bg="#fcfbf7", bd=2, relief="groove")
        self.resfrm.grid(row=1, column=2, rowspan=4, padx=12, sticky="ne")
        self.reslabels = []
        self._build_results()

        # Example
        tk.Label(self, text="Example: u = 2, -3, 4    v = 0, 6, 5",
            fg="#7e8fa5", bg="#f7fcfd", font=("Arial",10)).grid(row=5, column=0, columnspan=3, pady=2)

        self.cur_u = None
        self.cur_v = None
        self.show_all()

    def _build_results(self):
        titles = [
            ("(a)", "u · v"),
            ("(b)", "u · u"),
            ("(c)", "||v||²"),
            ("(d)", "(u·v)v"),
            ("(e)", "u · (3v)"),
        ]
        for i,(label, title) in enumerate(titles):
            tk.Label(self.resfrm, text=f"{label}  {title}", font=("Arial",12,"bold"),
                     bg="#fcfbf7").grid(row=i*2, column=0, sticky='w', padx=12, pady=(7 if i==0 else 2,0))
            lab = tk.Label(self.resfrm, text="", font=("Consolas",14), bg="#ffffff",
                           width=17, anchor="w", relief="sunken")
            lab.grid(row=i*2+1, column=0, sticky="ew", padx=10, pady=2)
            self.reslabels.append(lab)

    def _set_results(self, vals):
        # vals: list of strings
        for lbl, val in zip(self.reslabels, vals):
            lbl.config(text=val)

    def _get_uv(self):
        u = parse_vec(self.ent_u.get())
        v = parse_vec(self.ent_v.get())
        self.cur_u, self.cur_v = u, v
        if u is None or v is None:
            self.err.config(text="Please enter two valid 3D vectors (comma separated)")
            return None, None
        self.err.config(text="")
        return u, v

    def show_udotv(self):
        u,v = self._get_uv()
        if u is not None and v is not None:
            val = int(np.dot(u,v))
            self._update_plot(vectors=[(u,"u",'blue'), (v,"v",'green')])
            self._set_results([str(val), "", "", "", ""])
    def show_udotu(self):
        u,v = self._get_uv()
        if u is not None:
            val = int(np.dot(u,u))
            self._update_plot(vectors=[(u,"u",'blue')])
            self._set_results(["", str(val), "", "", ""])
    def show_normv2(self):
        u,v = self._get_uv()
        if v is not None:
            val = int(np.dot(v,v))
            self._update_plot(vectors=[(v,"v",'green')])
            self._set_results(["", "", str(val), "", ""])
    def show_uvv(self):
        u,v = self._get_uv()
        if u is not None and v is not None:
            res = np.dot(u,v)*v
            self._update_plot(vectors=[(res,"(u·v)v",'purple')])
            self._set_results(["", "", "", pretty_vec(res), ""])
    def show_u3v(self):
        u,v = self._get_uv()
        if u is not None and v is not None:
            res = int(np.dot(u,3*v))
            self._update_plot(vectors=[(3*v,"3v",'orange')])
            self._set_results(["", "", "", "", str(res)])
    def show_all(self):
        u,v = self._get_uv()
        if u is not None and v is not None:
            a = int(np.dot(u,v))
            b = int(np.dot(u,u))
            c = int(np.dot(v,v))
            d = np.dot(u,v)*v
            e = int(np.dot(u,3*v))
            self._set_results([str(a), str(b), str(c), pretty_vec(d), str(e)])
            self._update_plot(vectors=[
                (u, "u",'blue'),
                (v, "v",'green'),
                (d, "(u·v)v", 'purple'),
                (3*v, "3v", 'orange')
            ])

    def _update_plot(self, vectors):
        self.ax.clear()
        lim = 12
        # Planes at coordinate axes
        for plane in ["xy", "xz", "yz"]:
            xx = yy = np.linspace(-lim, lim, 2)
            if plane == "xy":
                X, Y = np.meshgrid(xx, yy)
                Z = np.zeros_like(X)
                self.ax.plot_surface(X, Y, Z, color="gray", alpha=0.13, zorder=-1)
            if plane == "xz":
                X, Z = np.meshgrid(xx, yy)
                Y = np.zeros_like(X)
                self.ax.plot_surface(X, Y, Z, color="gray", alpha=0.13, zorder=-1)
            if plane == "yz":
                Y, Z = np.meshgrid(xx, yy)
                X = np.zeros_like(Y)
                self.ax.plot_surface(X, Y, Z, color="gray", alpha=0.13, zorder=-1)
        origin = np.zeros(3)
        for vec, label, color in vectors:
            self.ax.quiver(*origin, *vec, color=color, label=label, arrow_length_ratio=0.12, linewidth=2)
            self.ax.scatter([vec[0]], [vec[1]], [vec[2]], color=color, s=70)
            # Drop lines
            x,y,z = vec
            self.ax.plot([x, x], [y, y], [z, 0], linestyle='dashed', color=color, alpha=0.7)
            self.ax.plot([x, x], [y, 0], [0, 0], linestyle='dashed', color=color, alpha=0.6)
            self.ax.plot([x, 0], [0, 0], [0, 0], linestyle='dashed', color=color, alpha=0.5)
        self.ax.set_xlim([-lim,lim])
        self.ax.set_ylim([-lim,lim])
        self.ax.set_zlim([-lim,lim])
        self.ax.set_xlabel('X'); self.ax.set_ylabel('Y'); self.ax.set_zlabel('Z')
        if len(vectors)>1:
            self.ax.legend(loc='upper left')
        self.ax.set_title("3D visualization")
        self.ax.grid(False)
        self.ax.xaxis.pane.fill = False
        self.ax.yaxis.pane.fill = False
        self.ax.zaxis.pane.fill = False
        self.canvas.draw()

if __name__ == "__main__":
    VectorApp().mainloop()
