"""
Exercice Jeu de cartes - Classe JeuDeCarte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Objet JeuDeCarte caractérisé par son nombre de cartes et son paquet.
"""

__author__ = "RobiPoire"


from carte import *
from random import shuffle


class JeuDeCarte:
    """Classe définissant un jeu de cartes caractérisé par :
    - son nombre de cartes (un entier entre 32 et 52)
    - son paquet (une liste de cartes)
    """

    def __creer_paquet(self) -> list:
        """Méthode privée pour créer le paquet de cartes. Retourne une liste de

        Returns:
            list: Liste de cartes
        """
        mon_paquet = []
        if self.__nombre_cartes == 32:
            numero_debut = 7
        elif self.__nombre_cartes == 52:
            numero_debut = 2
        else:
            raise ValueError("Le nombre de cartes doit être égal à 32 ou 52")
        for couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:
            for valeur in range(numero_debut, 15):
                mon_paquet.append(Carte(valeur, couleur))
        return mon_paquet

    def __init__(self, nombre_cartes: int) -> None:
        """Constructeur de la classe JeuDeCarte.

        Args:
            nombre_cartes (int): Nombre de cartes du jeu de cartes (un entier entre 32 et 52)
        """
        self.__nombre_cartes = nombre_cartes
        self.__paquet = self.__creer_paquet()

    def get_nombre_cartes(self) -> int:
        """Retourne le nombre de cartes du jeu de cartes.

        Returns:
            int: Nombre de cartes du jeu de cartes (un entier entre 32 et 52)
        """
        return self.__nombre_cartes

    def get_paquet(self) -> list:
        """Retourne le paquet de cartes.

        Returns:
            list: Paquet de cartes
        """
        return self.__paquet

    def melanger_paquet(self) -> None:
        """Méthode pour mélanger le paquet de cartes."""
        shuffle(self.__paquet)
