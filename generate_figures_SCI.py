import numpy as np
import matplotlib.pyplot as plt

def logistique(x, r):
    return r * x * (1 - x)

# Paramètres
r = 3.9                # régime chaotique
x0 = 0.400000          # première condition initiale
y0 = 0.400001          # seconde condition initiale (très proche)
n_iter = 50            # nombre d'itérations

# Calcul des trajectoires
x = np.zeros(n_iter)
y = np.zeros(n_iter)
x[0] = x0
y[0] = y0

for i in range(n_iter - 1):
    x[i+1] = logistique(x[i], r)
    y[i+1] = logistique(y[i], r)

# Tracé
plt.figure(figsize=(10, 5))
plt.plot(range(n_iter), x, 'b-', linewidth=1.5, label=f'$x_0 = {x0}$')
plt.plot(range(n_iter), y, 'r--', linewidth=1.5, label=f'$y_0 = {y0}$')
plt.xlabel("$n$")
plt.ylabel("$x_n$")
#plt.title(f"Sensibilité aux conditions initiales (modèle logistique, $r = {r}$)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("figure_sensibilite.png", dpi=150)
plt.show()