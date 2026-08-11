import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_zoom(center, zoom, width=500, height=500, max_iter=200):
    """
    Génère une sous‑image de l'ensemble de Mandelbrot centrée en `center`
    avec un facteur de zoom `zoom`. Plus `zoom` est grand, plus on grossit.
    """
    # La taille de la fenêtre est inversement proportionnelle au zoom
    taille = 3.0 / zoom
    xmin = center.real - taille/2
    xmax = center.real + taille/2
    ymin = center.imag - taille/2
    ymax = center.imag + taille/2

    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    Z = np.zeros_like(C, dtype=complex)
    divergence = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + C[mask]
        divergence[mask] += 1

    # Normalisation entre 0 et 1
    divergence = np.clip(divergence, 0, max_iter)
    divergence = divergence / max_iter
    return divergence, xmin, xmax, ymin, ymax

# Centre de la "Seahorse valley" (région très riche en détails)
center = complex(-0.75, 0.1)

# Facteurs de zoom : plus on zoom, plus on augmente le nombre d'itérations
zooms = [1, 10, 50, 200]
max_iters = [200, 200, 500, 1000]  # itérations adaptées au zoom

fig, axes = plt.subplots(1, 4, figsize=(17, 4))
for i, (zf, mi) in enumerate(zip(zooms, max_iters)):
    img, xmin, xmax, ymin, ymax = mandelbrot_zoom(center, zf, max_iter=mi)
    axes[i].imshow(img, extent=[xmin, xmax, ymin, ymax], cmap='hot', origin='lower')
    axes[i].set_title(f'Zoom {zf}×')
    axes[i].axis('off')
plt.tight_layout()
plt.savefig("figure_mandelbrot_zoom.png", dpi=150)
plt.close()

print("✅ figure_mandelbrot_zoom.png générée avec succès.")