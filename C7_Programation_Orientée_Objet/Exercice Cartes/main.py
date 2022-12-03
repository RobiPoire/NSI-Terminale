"""
Exercice Jeu de cartes - Main (test)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Programme principal pour tester la classe JeuDeCarte et la classe Carte.
"""

__author__ = "RobiPoire"


from carte import *
from jeu_de_cartes import *



# 1 - Carte
ma_carte = Carte(11, "Trèfle")
print(ma_carte.get_figure())
if ma_carte.set_valeur(13):
    print(ma_carte.get_figure())


input("Fin de la partie 1 - Carte. Appuyez sur une touche pour continuer...")

# 2 - JeuDdeCarte
mon_jeu = JeuDeCarte(32)
print("Le jeu de cartes contient", mon_jeu.get_nombre_cartes(), "cartes")
print("Le jeu de cartes contient les cartes suivantes :")
for carte in mon_jeu.get_paquet():
    print(carte.get_figure(), "de", carte.get_couleur())
mon_jeu.melanger_paquet()
print("Le jeu de cartes contient les cartes suivantes :")
for carte in mon_jeu.get_paquet():
    print(carte.get_figure(), "de", carte.get_couleur())
