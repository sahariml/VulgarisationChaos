import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_zoom(center, zoom, width=400, height=400, max_iter=100):
    """
    Génère une image de l'ensemble de Mandelbrot centrée en `center` (complexe)
    avec un facteur de zoom (plus grand = plus zoomé).
    """
    # Calcul de la région à afficher
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

    divergence = np.clip(divergence, 0, max_iter)
    divergence = divergence / max_iter
    return divergence, xmin, xmax, ymin, ymax

# Définir une séquence de zooms (centres et facteurs)
zooms = [
    (-0.5, 0.0, 1),      # vue générale
    (-0.5, 0.0, 10),     # zoom sur le bord
    (-0.5, 0.0, 50),     # zoom plus proche
    (-0.5, 0.0, 200),    # zoom très proche
]

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for i, (cx, cy, zf) in enumerate(zooms):
    center = complex(cx, cy)
    img, xmin, xmax, ymin, ymax = mandelbrot_zoom(center, zf)
    axes[i].imshow(img, extent=[xmin, xmax, ymin, ymax], cmap='hot', origin='lower')
    axes[i].set_title(f'Zoom {zf}x')
    axes[i].axis('off')
plt.tight_layout()
plt.savefig("figure_mandelbrot_zoom.png", dpi=150)
plt.close()

print("✅ figure_mandelbrot_zoom.png générée avec succès.")