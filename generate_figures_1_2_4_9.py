import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

# ---- Figure 1 : Trajectoire du modèle logistique ----
def logistique(x, r):
    return r * x * (1 - x)

r = 3.9
x0 = 0.4
n_iter = 100
x = np.zeros(n_iter)
x[0] = x0
for i in range(n_iter - 1):
    x[i+1] = logistique(x[i], r)

plt.figure(figsize=(10, 4))
plt.plot(range(n_iter), x, 'b-', linewidth=0.8)
plt.xlabel("$n$")
plt.ylabel("$x_n$")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("figure_trajectoire.png", dpi=150)
plt.close()

# ---- Figure 2 : Diagramme de bifurcation ----
r_values = np.linspace(2.8, 4.0, 1000)
x0 = 0.4
n_transient = 200
n_plot = 100

all_r = []
all_x = []

for r in r_values:
    x = x0
    for _ in range(n_transient):
        x = logistique(x, r)
    for _ in range(n_plot):
        x = logistique(x, r)
        all_r.append(r)
        all_x.append(x)

plt.figure(figsize=(10, 6))
plt.scatter(all_r, all_x, s=0.1, color='black', marker='.')
plt.xlabel("$r$")
plt.ylabel("$x$")
plt.xlim(2.8, 4.0)
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig("figure_bifurcation.png", dpi=150)
plt.close()

# ---- Figure 3 : Attracteur de Lorenz ----
def lorenz(state, t, sigma, rho, beta):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
state0 = [1.0, 1.0, 1.0]
t = np.linspace(0, 40, 10000)

sol = odeint(lorenz, state0, t, args=(sigma, rho, beta))
x, y, z = sol[:, 0], sol[:, 1], sol[:, 2]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, linewidth=0.5, color='blue')
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
plt.tight_layout()
plt.savefig("figure_lorenz.png", dpi=150)
plt.close()

# ---- Figure 4 : Exposant de Lyapunov ----
def lyapunov_logistique(r, x0, n_iter=1000):
    x = x0
    sum_lyap = 0.0
    for _ in range(n_iter):
        x = logistique(x, r)
        sum_lyap += np.log(abs(r * (1 - 2 * x)))
    return sum_lyap / n_iter

r_vals = np.linspace(2.8, 4.0, 2000)
lyap_vals = []
for r in r_vals:
    lyap_mean = 0
    for x0 in [0.2, 0.4, 0.6]:
        lyap_mean += lyapunov_logistique(r, x0, 800)
    lyap_vals.append(lyap_mean / 3)

plt.figure(figsize=(10, 5))
plt.plot(r_vals, lyap_vals, color='red', linewidth=0.8)
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.xlabel("$r$")
plt.ylabel("$\\lambda$")
plt.xlim(2.8, 4.0)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("figure_lyapunov.png", dpi=150)
plt.close()

print("✅ Figures générées avec succès.")