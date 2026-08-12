import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(order, scale=10):
    """
    Génère les points d'un flocon de Koch d'ordre donné.
    Retourne une liste de points (x, y).
    """
    # Triangle équilatéral de départ
    angles = np.array([0, 120, 240]) * np.pi / 180
    points = np.array([[np.cos(a), np.sin(a)] for a in angles])

    def koch_curve(p1, p2, order):
        if order == 0:
            return [p1, p2]
        # Vecteur de p1 à p2
        v = p2 - p1
        # Trois points de division : 1/3, 1/2 + rotation 60°, 2/3
        pA = p1 + v / 3
        pB = p1 + v / 2 + np.array([-v[1], v[0]]) * np.sqrt(3) / 6
        pC = p1 + 2 * v / 3
        # Récursion sur les segments
        pts = []
        pts.extend(koch_curve(p1, pA, order-1))
        pts.extend(koch_curve(pA, pB, order-1))
        pts.extend(koch_curve(pB, pC, order-1))
        pts.extend(koch_curve(pC, p2, order-1))
        return pts

    # Construire les trois côtés du triangle
    all_pts = []
    for i in range(3):
        segment = koch_curve(points[i], points[(i+1)%3], order)
        all_pts.extend(segment[:-1])  # éviter les doublons
    all_pts.append(all_pts[0])  # fermeture
    return np.array(all_pts)

# Tracer les flocons d'ordre 0 à 4
fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for order, ax in enumerate(axes):
    pts = koch_snowflake(order)
    ax.plot(pts[:,0], pts[:,1], 'b-', linewidth=0.8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(f'Ordre {order}')
plt.tight_layout()
plt.savefig("figure_koch.png", dpi=150)
plt.close()

print("✅ figure_koch.png générée avec succès.")