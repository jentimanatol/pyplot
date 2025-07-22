import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def parse_vec(s):
    try:
        vals = [float(x) for x in s.split(',')]
        if len(vals) != 3: return None
        return np.array(vals)
    except:
        return None

def pretty_vec(v):
    return "<" + ",".join(str(int(round(x))) for x in v) + ">"

class VectorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vectors Calculator")
        # Geometry: nearly fullscreen but not maximized by default
        self.geometry(f"{min(self.winfo_screenwidth()-100,1200)}x{min(self.winfo_screenheight()-150,600)}")
        self.configure(bg="#f8fcff")

        style_label = dict(font=("Arial", 16, "bold"), bg="#f8fcff", pady=2)
        style_math = dict(font=("Arial", 17, "bold"), fg="#181822", bg="#f8fcff")
        # Headline
        tk.Label(self, text="Vectors Calculator", font=("Lato", 26, "bold"),
                 bg="#bee6fc", fg="#1a2340", pady=13).grid(row=0, column=0, columnspan=8, sticky="ew")
        tk.Label(self, text="Find ", **style_label).grid(row=1, column=0, sticky="e")
        tk.Label(self, text="u · v,  u · u,  ||v||²,  (u · v)v, and  u · (3v)", **style_label).grid(row=1, column=1, columnspan=5, sticky="w", pady=(0,6))

        # Inputs
        tk.Label(self, text="u =", font=("Arial",15), bg="#f8fcff").grid(row=2, column=0, sticky="e", padx=(14,2))
        self.ent_u = tk.Entry(self, font=("Consolas",16), width=13, justify='center')
        self.ent_u.insert(0, "2, -3, 4")
        self.ent_u.grid(row=2, column=1, sticky="w", padx=(0,18))

        tk.Label(self, text="v =", font=("Arial",15), bg="#f8fcff").grid(row=2, column=2, sticky="e")
        self.ent_v = tk.Entry(self, font=("Consolas",16), width=13, justify='center')
        self.ent_v.insert(0, "0, 6, 5")
        self.ent_v.grid(row=2, column=3, sticky="w", padx=(0,1))

        self.status = tk.Label(self, fg="red", bg="#f8fcff", font=("Arial", 13, "bold"))
        self.status.grid(row=3, column=0, columnspan=8, sticky="w", padx=19, pady=(2,4))

        # Calculation buttons - enlarged, in a single row
        calcbtn_frm = tk.Frame(self, bg="#f8fcff")
        calcbtn_frm.grid(row=4, column=0, columnspan=5, sticky="ew", pady=(8,0))
        pad_x = (7,3); pad_y=(2,2)
        button_style=dict(font=("Verdana",13,"bold"), width=11, height=1, bg="#357cda", fg='white', relief='raised')
        ttk.Style().configure("TButton", padding=6, relief="flat", font=('Arial', 12))

        btns = [
            ("u · v",        self.show_udotv, "#1a6e9e"),
            ("u · u",        self.show_udotu, "#32823f"),
            ("||v||²",       self.show_normv2, "#a87225"),
            ("(u·v)v",       self.show_uvv, "#7647a9"),
            ("u · (3v)",     self.show_u3v, "#e05c0a"),
            ("All Results",  self.show_all, "#157b26"),
        ]
        self.calcbtns=[]
        for i, (text, cmd, color) in enumerate(btns):
            b=tk.Button(calcbtn_frm, text=text, command=cmd, fg="white", bg=color,
                        font=("Verdana",13,"bold"), width=10 if i<5 else 15, height=2)
            b.grid(row=0, column=i, padx=pad_x, pady=pad_y)
            self.calcbtns.append(b)

        #  ---- Center: 3D plot area with matplotlib ----
        plot_frm = tk.Frame(self, bg="#f8fcff", highlightthickness=1)
        plot_frm.grid(row=5, column=0, columnspan=4, rowspan=7, sticky="nsew", padx=20)
        self.fig = plt.figure(figsize=(7,5))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frm)
        self.plot_widget = self.canvas.get_tk_widget()
        self.plot_widget.grid(row=0, column=0, sticky="nsew")
        plot_frm.grid_rowconfigure(0,weight=1)
        plot_frm.grid_columnconfigure(0,weight=1)

        # ---- Right: output boxes, with math-style labels ----
        ans_frame = tk.Frame(self, bg="#f8fcff")
        ans_frame.grid(row=5, column=4, rowspan=10, columnspan=3, sticky="nsw", padx=(0,18), pady=(20,0))
        al=15
        self.anslbls=[]
        # Title lines
        exprs = [
            ("(a)  ", "u · v"), ("(b)  ", "u · u"), ("(c)  ", "||v||²"),
            ("(d)  ", "(u · v)v"), ("(e)  ","u · (3v)")
        ]
        for i, (pre, expr) in enumerate(exprs):
            ypad = (11,1) if i==0 else (8,1)
            tk.Label(ans_frame, text=f"{pre}", font=("Arial", 17), bg="#f8fcff", anchor="e", width=4).grid(row=i*2, column=0, sticky='e', pady=ypad)
            tk.Label(ans_frame, text=expr, **style_math,justify='left').grid(row=i*2,column=1,sticky='w',pady=ypad)
            ans_box = tk.Entry(ans_frame, font=("Consolas",18,"bold"), width=17, bd=2, relief='solid',  justify="center", state='readonly')
            ans_box.grid(row=i*2+1, column=0, columnspan=2, padx=5, pady=(0,0))
            self.anslbls.append(ans_box)

        # Initial focus and fill
        self.show_all()

    def _get_uv(self):
        u = parse_vec(self.ent_u.get())
        v = parse_vec(self.ent_v.get())
        if u is None or v is None:
            self.status.config(text="Enter both vectors as 3 values (comma separated).")
            return None, None
        self.status.config(text="")
        return u, v

    def _set_results(self, vals):
        for box, val in zip(self.anslbls, vals):
            box.config(state='normal')
            box.delete(0, 'end')
            box.insert(0, val)
            box.config(state='readonly')

    def show_udotv(self):
        u, v = self._get_uv(); vals = [""]*5
        if u is not None and v is not None:
            vals[0]=str(int(np.dot(u,v)))
            self._set_results(vals)
            self.plot_vectors([(u, "u", "blue"), (v, "v", "green")])

    def show_udotu(self):
        u, v = self._get_uv(); vals = [""]*5
        if u is not None:
            vals[1]=str(int(np.dot(u,u)))
            self._set_results(vals)
            self.plot_vectors([(u, "u", "blue")])

    def show_normv2(self):
        u, v = self._get_uv(); vals = [""]*5
        if v is not None:
            vals[2]=str(int(np.dot(v,v)))
            self._set_results(vals)
            self.plot_vectors([(v, "v", "green")])

    def show_uvv(self):
        u, v = self._get_uv(); vals = [""]*5
        if u is not None and v is not None:
            res = np.dot(u, v) * v
            vals[3]=pretty_vec(res)
            self._set_results(vals)
            self.plot_vectors([(res, "(u·v)v", "purple")])

    def show_u3v(self):
        u, v = self._get_uv(); vals = [""]*5
        if u is not None and v is not None:
            res = int(np.dot(u,3*v))
            vals[4]=str(res)
            self._set_results(vals)
            self.plot_vectors([(3*v, "3v", "orange")])

    def show_all(self):
        u, v = self._get_uv()
        if u is None or v is None: return
        a = int(np.dot(u, v))
        b = int(np.dot(u, u))
        c = int(np.dot(v, v))
        d = np.dot(u, v) * v
        e = int(np.dot(u, 3 * v))
        answers = [str(a), str(b), str(c), pretty_vec(d), str(e)]
        self._set_results(answers)
        self.plot_vectors([
            (u, "u", "blue"),
            (v, "v", "green"),
            (d, "(u·v)v", "purple"),
            (3 * v, "3v", "orange"),
        ])

    def plot_vectors(self, vectors):
        self.ax.clear()
        lim = 12
        # Draw the three coordinate planes through origin
        xx = yy = np.linspace(-lim, lim, 2)
        for plane in ["xy", "xz", "yz"]:
            if plane=="xy":
                X,Y = np.meshgrid(xx, yy); Z=np.zeros_like(X)
                self.ax.plot_surface(X,Y,Z, color="gray", alpha=0.13, zorder=-1)
            if plane=="xz":
                X,Z = np.meshgrid(xx, yy); Y=np.zeros_like(X)
                self.ax.plot_surface(X,Y,Z, color="gray", alpha=0.13, zorder=-1)
            if plane=="yz":
                Y,Z = np.meshgrid(xx, yy); X=np.zeros_like(Y)
                self.ax.plot_surface(X,Y,Z, color="gray", alpha=0.13, zorder=-1)
        origin = np.zeros(3)
        for vec, label, color in vectors:
            self.ax.quiver(*origin, *vec, color=color, label=label, arrow_length_ratio=0.14, linewidth=2)
            self.ax.scatter([vec[0]], [vec[1]], [vec[2]], color=color, s=110)
            x, y, z = vec
            self.ax.plot([x, x], [y, y], [z, 0], linestyle='dashed', color=color, alpha=0.7)
            self.ax.plot([x, x], [y, 0], [0, 0], linestyle='dashed', color=color, alpha=0.5)
            self.ax.plot([x, 0], [0, 0], [0, 0], linestyle='dashed', color=color, alpha=0.4)
        self.ax.set_xlim([-lim, lim]); self.ax.set_ylim([-lim, lim]); self.ax.set_zlim([-lim, lim])
        self.ax.set_xlabel('X', fontsize=13); self.ax.set_ylabel('Y', fontsize=13); self.ax.set_zlabel('Z', fontsize=13)
        if len(vectors) > 1: self.ax.legend(fontsize=13, loc='upper left')
        self.ax.set_title("3D Visualization (scroll to zoom)", fontsize=15)
        self.ax.grid(False)
        self.ax.xaxis.pane.fill = False; self.ax.yaxis.pane.fill = False; self.ax.zaxis.pane.fill = False
        self.canvas.draw()

if __name__ == "__main__":
    VectorApp().mainloop()
