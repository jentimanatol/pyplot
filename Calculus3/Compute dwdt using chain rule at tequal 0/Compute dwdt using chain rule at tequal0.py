import numpy as np
import matplotlib.pyplot as plt

# Define t values
t_vals = np.linspace(-2, 2, 400)

# Define x(t) and y(t)
x = np.sin(t_vals)
y = np.exp(t_vals)

# Define w(t)
w = x**2 * y + y**2 * x + 1

# Compute dw/dt using chain rule at t = 0
t0 = 0
x0 = np.sin(t0)
y0 = np.exp(t0)
dxdt = np.cos(t0)
dydt = np.exp(t0)

# Partial derivatives
dw_dx = 2*x0*y0 + y0**2
dw_dy = x0**2 + 2*y0*x0

# Chain rule
dwdt = dw_dx * dxdt + dw_dy * dydt

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t_vals, w, label=r"$w(t) = x(t)^2 y(t) + y(t)^2 x(t) + 1$", color="blue")
plt.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
plt.scatter([t0], [x0**2 * y0 + y0**2 * x0 + 1], color='red', label=fr"$t=0$, $\frac{{dw}}{{dt}} = {dwdt:.1f}$")
plt.title(r"Visualization of $w(t) = x(t)^2 y(t) + y(t)^2 x(t) + 1$")
plt.xlabel("t")
plt.ylabel("w(t)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
