import numpy as np
import matplotlib.pyplot as plt

def logistique(x, r):
    return r * x * (1 - x)

r = 3.9
x0 = 0.400000
y0 = 0.400001
n_iter = 50

x = np.zeros(n_iter)
y = np.zeros(n_iter)
x[0] = x0
y[0] = y0

for i in range(n_iter - 1):
    x[i+1] = logistique(x[i], r)
    y[i+1] = logistique(y[i], r)

# Calcul de l'écart
ecart = np.abs(x - y)

plt.figure(figsize=(10, 5))
plt.semilogy(range(n_iter), ecart, 'g-', linewidth=1.5)
plt.xlabel("$n$")
plt.ylabel("$|x_n - y_n|$")
#plt.title("Évolution de l'écart entre deux trajectoires")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("figure_ecart.png", dpi=150)
plt.close()

print("✅ figure_ecart.png générée avec succès.")