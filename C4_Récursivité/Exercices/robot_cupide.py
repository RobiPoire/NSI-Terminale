"""
La récurssivité - Robot cupide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Programme qui calcule le chemin le plus rentable pour un robot cupide.
"""

__author__ = "RobiPoire"

damier = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def robot_cupide(x, y):
    # Cas de base
    if ((x == 0) and (y == 0)):
        return damier[x][y]
    # Autres cas particuliers
    if (x == 0):
        return damier[x][y] + robot_cupide(x, y - 1)
    if (y == 0):
        return damier[x][y] + robot_cupide(x - 1, y)
    return damier[x][y] + max(robot_cupide(x - 1, y), robot_cupide(x, y - 1))


# Exemples d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté
    print(robot_cupide(3, 0))
