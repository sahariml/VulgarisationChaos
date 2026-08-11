import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def double_pendulum(state, t, L1, L2, m1, m2, g):
    """
    Équations du mouvement pour un double pendule.
    state = [theta1, omega1, theta2, omega2]
    """
    th1, w1, th2, w2 = state
    dth1 = w1
    dth2 = w2

    delta = th2 - th1
    den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta) * np.cos(delta)
    dw1 = (m2 * L1 * w1 * w1 * np.sin(delta) * np.cos(delta) +
           m2 * g * np.sin(th2) * np.cos(delta) +
           m2 * L2 * w2 * w2 * np.sin(delta) -
           (m1 + m2) * g * np.sin(th1)) / den1

    den2 = (L2 / L1) * den1
    dw2 = (-m2 * L2 * w2 * w2 * np.sin(delta) * np.cos(delta) +
           (m1 + m2) * g * np.sin(th1) * np.cos(delta) -
           (m1 + m2) * L1 * w1 * w1 * np.sin(delta) -
           (m1 + m2) * g * np.sin(th2)) / den2

    return [dth1, dw1, dth2, dw2]

# Paramètres
L1 = L2 = 1.0
m1 = m2 = 1.0
g = 9.81

# Conditions initiales très proches
th1_0 = np.pi / 2
th2_0 = np.pi / 2
w1_0 = w2_0 = 0.0

# Légère perturbation
eps = 0.001   # 0.1% de différence sur th2
state0_1 = [th1_0, w1_0, th2_0, w2_0]
state0_2 = [th1_0, w1_0, th2_0 + eps, w2_0]

# Intégration temporelle
t = np.linspace(0, 20, 5000)
sol1 = odeint(double_pendulum, state0_1, t, args=(L1, L2, m1, m2, g))
sol2 = odeint(double_pendulum, state0_2, t, args=(L1, L2, m1, m2, g))

# Positions des masses
def positions(sol, L1, L2):
    th1 = sol[:, 0]
    th2 = sol[:, 2]
    x1 = L1 * np.sin(th1)
    y1 = -L1 * np.cos(th1)
    x2 = x1 + L2 * np.sin(th2)
    y2 = y1 - L2 * np.cos(th2)
    return x1, y1, x2, y2

x1_1, y1_1, x2_1, y2_1 = positions(sol1, L1, L2)
x1_2, y1_2, x2_2, y2_2 = positions(sol2, L1, L2)

# Tracé des trajectoires de la seconde masse (extrémité)
plt.figure(figsize=(8, 6))
plt.plot(x2_1, y2_1, 'b-', linewidth=0.8, label='$\\theta_0$')
plt.plot(x2_2, y2_2, 'r--', linewidth=0.8, label='$\\theta_{0}+0.001$ rad')
plt.xlabel("$x$")
plt.ylabel("$y$")
#plt.title("Trajectoires de l'extrémité du double pendule")
plt.legend()
plt.grid(alpha=0.3)
plt.axis('equal')
plt.tight_layout()
plt.savefig("figure_double_pendule.png", dpi=150)
plt.close()

print("✅ figure_double_pendule.png générée avec succès.")