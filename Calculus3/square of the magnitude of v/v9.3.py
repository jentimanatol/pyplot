import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def parse_vec(s):
    try:
        v = np.array([float(x.strip()) for x in s.split(',')])
        if len(v) != 3:
            raise ValueError()
        return v
    except:
        return None

def pretty_vec(v):
    return "<" + ",".join(str(int(round(x))) if int(x) == x else f"{x:.2f}" for x in v) + ">"

def pop_result(title, msg):
    messagebox.showinfo(title, msg)

def show_vec_3d(vec, title="Vector", color="blue"):
    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color=color, label=title, arrow_length_ratio=0.11)
    # Projections from tip to coordinate planes
    x, y, z = vec
    ax.plot([x, x], [y, y], [z, 0], linestyle='dashed', color=color, alpha=0.7)
    ax.plot([x, x], [y, 0], [0, 0], linestyle='dashed', color=color, alpha=0.5)
    ax.plot([x, 0], [0, 0], [0, 0], linestyle='dashed', color=color, alpha=0.3)
    ax.scatter([x], [y], [z], color=color, s=75)
    ax.set_title(title)
    lim = max(10, int(max(np.abs(vec))) + 2)
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    ax.set_zlim([-lim, lim])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.tight_layout()
    plt.show()

def show_all_plot(u, v):
    uvv = np.dot(u, v)*v
    v3 = 3*v
    colors = ['blue', 'green', 'purple', 'orange']
    labels = ['u', 'v', '(u·v)v', '3v']
    vecs = [u, v, uvv, v3]
    markers = ['o', 's', '^', 'D']
    fig = plt.figure(figsize=(8,7))
    ax = fig.add_subplot(111, projection='3d')
    # Three coordinate planes (xy, xz, yz, at origin)
    for plane in ["xy", "xz", "yz"]:
        xx = yy = np.linspace(-12, 12, 2)
        if plane == "xy":
            X, Y = np.meshgrid(xx, yy)
            Z = np.zeros_like(X)
            ax.plot_surface(X, Y, Z, color="gray", alpha=0.13, zorder=-1)
        if plane == "xz":
            X, Z = np.meshgrid(xx, yy)
            Y = np.zeros_like(X)
            ax.plot_surface(X, Y, Z, color="gray", alpha=0.13, zorder=-1)
        if plane == "yz":
            Y, Z = np.meshgrid(xx, yy)
            X = np.zeros_like(Y)
            ax.plot_surface(X, Y, Z, color="gray", alpha=0.13, zorder=-1)
    for vec, label, color, marker in zip(vecs, labels, colors, markers):
        ax.quiver(0,0,0, vec[0],vec[1],vec[2], color=color, label=label, linewidth=2, arrow_length_ratio=0.13)
        ax.scatter([vec[0]],[vec[1]],[vec[2]], color=color, s=70, marker=marker)
        # Dashed drop lines
        x, y, z = vec
        ax.plot([x, x], [y, y], [z, 0], linestyle='dashed', color=color, alpha=0.7)
        ax.plot([x, x], [y, 0], [0, 0], linestyle='dashed', color=color, alpha=0.5)
        ax.plot([x, 0], [0, 0], [0, 0], linestyle='dashed', color=color, alpha=0.3)
    maxlim = max(10, float(np.abs(vecs).max())+2)
    ax.set_xlim([-maxlim, maxlim])
    ax.set_ylim([-maxlim, maxlim])
    ax.set_zlim([-maxlim, maxlim])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend(fontsize=12)
    ax.set_title('All Vectors & Planes')
    ax.grid(False)
    plt.tight_layout()
    plt.show()

def calc_all():
    ent_err['text'] = ""
    u = parse_vec(ent_u.get())
    v = parse_vec(ent_v.get())
    if u is None or v is None:
        ent_err['text'] = "Please enter two 3D vectors (comma separated)."
        return
    a = int(np.dot(u,v)) ; b = int(np.dot(u,u)) ; c = int(np.dot(v,v)) ; d = np.dot(u,v)*v ; e = int(np.dot(u,3*v))
    # Display as in screenshot
    lines = []
    lines.append(f"(a)  u · v         {a}")
    lines.append(f"(b)  u · u         {b}")
    lines.append(f"(c)  ||v||²        {c}")
    lines.append(f"(d)  (u·v)v   {pretty_vec(d)}")
    lines.append(f"(e)  u · (3v)      {e}")
    res_box.config(state=tk.NORMAL)
    res_box.delete(1.0,'end')
    res_box.insert('end', '\n\n'.join(lines))
    res_box.config(state=tk.DISABLED)

# ---- Per-operation button functions ----

def op_udotv():
    u = parse_vec(ent_u.get()); v = parse_vec(ent_v.get())
    if u is None or v is None: return
    a = int(np.dot(u,v))
    pop_result("u · v", f"u · v = {a}")
    show_vec_3d(u, "u", "blue")
    show_vec_3d(v, "v", "green")
def op_udotu():
    u = parse_vec(ent_u.get())
    if u is None: return
    a = int(np.dot(u,u))
    pop_result("u · u", f"u · u = {a}")
    show_vec_3d(u, "u", "blue")
def op_normvv():
    v = parse_vec(ent_v.get())
    if v is None: return
    a = int(np.dot(v,v))
    pop_result("||v||²", f"||v||² = {a}")
    show_vec_3d(v, "v", "green")
def op_uvv():
    u = parse_vec(ent_u.get()); v = parse_vec(ent_v.get())
    if u is None or v is None: return
    res = np.dot(u,v)*v
    pop_result("(u·v)v", f"(u·v)v = {pretty_vec(res)}")
    show_vec_3d(res, "(u·v)v", "purple")
def op_u3v():
    u = parse_vec(ent_u.get()); v = parse_vec(ent_v.get())
    if u is None or v is None: return
    res = int(np.dot(u,3*v))
    pop_result("u · (3v)", f"u · (3v) = {res}")
    show_vec_3d(3*v, "3v", "orange")
def op_allplot():
    u = parse_vec(ent_u.get()); v = parse_vec(ent_v.get())
    if u is None or v is None: return
    show_all_plot(u, v)

# --- GUI ---
root = tk.Tk()
root.title("Vectors Calculator")
root.configure(bg="#f7fcfd")
root.geometry('520x670')
tk.Label(root, text="Vectors Calculator", font=("Lato",19,"bold"), bg="#bee6fc", fg="#1a2340", pady=7).pack(fill="x")
tk.Label(root, text="Find  u · v,  u · u,  ||v||²,  (u · v)v, and  u · (3v).",
         font=("Arial",13,"bold"), fg="#222", bg="#f7fcfd").pack(pady=(10,4))

tk.Label(root, text="u =", font=("Arial",13), bg="#f7fcfd").place(x=50, y=60)
ent_u = tk.Entry(root, font=("Consolas",13), width=16)
ent_u.insert(0, "2, -3, 4")
ent_u.place(x=90, y=60)
tk.Label(root, text="v =", font=("Arial",13), bg="#f7fcfd").place(x=270, y=60)
ent_v = tk.Entry(root, font=("Consolas",13), width=16)
ent_v.insert(0, "0, 6, 5")
ent_v.place(x=310, y=60)

ent_err = tk.Label(root, fg="red", bg="#f7fcfd", font=("Arial",11,"bold")); ent_err.place(x=50, y=95)

tk.Button(root, text="Calculate all", font=("Verdana",12,"bold"), bg="#157b26", fg="white",
          width=13, command=calc_all).place(x=180, y=110)
res_box = tk.Text(root, width=45, height=10, font=("Consolas",13), bg="#f8fafb", relief="groove"); 
res_box.place(x=40, y=155)
res_box.config(state=tk.DISABLED)

btns = [
    ("Compute u · v", op_udotv, 215),
    ("Compute u · u", op_udotu, 255),
    ("Compute ||v||²", op_normvv, 295),
    ("Visualize (u·v)v", op_uvv, 335),
    ("Compute u · (3v)", op_u3v, 375),
    ("Visualize All Vectors", op_allplot, 415)
]
for label, fun, ypos in btns:
    tk.Button(root, text=label, command=fun, width=23 if "All" in label else 18,
              bg="#175bba" if "Visualize" in label else "#7fad17" if "||v||" in label else "#487993" if "u ·" in label else "#b924ba",
              fg="white", font=("Verdana",11,"bold")).place(x=143, y=ypos)

tk.Label(root,text="Example vector:   2, -3, 4", fg="#7e8fa5", bg="#f7fcfd", font=("Arial",11)).place(x=160, y=600)
root.mainloop()
