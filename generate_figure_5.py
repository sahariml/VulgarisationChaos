import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ---- 1. Attracteur ponctuel : oscillateur harmonique amorti ----
def damped_oscillator(state, t):
    x, y = state
    dx = y
    dy = -x - 0.1*y   # amortissement faible
    return [dx, dy]

t = np.linspace(0, 50, 2000)
state0 = [2.0, 0.0]
sol = odeint(damped_oscillator, state0, t)
x_pt, y_pt = sol[:, 0], sol[:, 1]

# ---- 2. Cycle limite : oscillateur de van der Pol ----
def vdp(state, t, mu):
    x, y = state
    dx = y
    dy = mu * (1 - x**2) * y - x
    return [dx, dy]

t_vdp = np.linspace(0, 30, 3000)
state0_vdp = [0.1, 0.1]
sol_vdp = odeint(vdp, state0_vdp, t_vdp, args=(1.0,))
x_cycle, y_cycle = sol_vdp[:, 0], sol_vdp[:, 1]

# ---- 3. Attracteur de Lorenz (étrange) ----
def lorenz(state, t, sigma, rho, beta):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

sigma, rho, beta = 10.0, 28.0, 8.0/3.0
state0_l = [1.0, 1.0, 1.0]
t_l = np.linspace(0, 40, 10000)
sol_l = odeint(lorenz, state0_l, t_l, args=(sigma, rho, beta))
x_l, y_l, z_l = sol_l[:, 0], sol_l[:, 1], sol_l[:, 2]

# ---- Création de la figure composite ----
fig = plt.figure(figsize=(12, 4))

# Panel 1 : point fixe
ax1 = fig.add_subplot(1, 3, 1)
ax1.plot(x_pt, y_pt, 'b-', linewidth=0.8)
ax1.scatter([0], [0], color='red', s=50, marker='o', label='Fixed point')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
#ax1.set_title('Attracteur ponctuel')
ax1.grid(alpha=0.3)
ax1.legend()

# Panel 2 : cycle limite
ax2 = fig.add_subplot(1, 3, 2)
ax2.plot(x_cycle, y_cycle, 'r-', linewidth=0.8)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
#ax2.set_title('Cycle limite')
ax2.grid(alpha=0.3)
ax2.axis('equal')

# Panel 3 : attracteur de Lorenz (projection x-y)
ax3 = fig.add_subplot(1, 3, 3)
ax3.plot(x_l, y_l, 'g-', linewidth=0.5, alpha=0.7)
ax3.set_xlabel('$x$')
ax3.set_ylabel('$y$')
#ax3.set_title('Attracteur étrange (Lorenz)')
ax3.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('figure_attracteurs.png', dpi=150)
plt.close()
print("✅ figure_attracteurs.png générée avec succès.")