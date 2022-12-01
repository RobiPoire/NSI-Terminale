"""
Exercice Jeu de cartes - Classe Carte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Objet carte caractérisé par sa valeur et sa couleur.
"""

__author__ = "RobiPoire"


class Carte:
    """Classe définissant une carte caractérisée par :
    - sa valeur (un entier entre 2 et 14)
    - sa couleur (un des 4 symboles suivants : "Coeur", "Carreau", "Pique", "Trèfle")
    - sa figure (un des 4 symboles suivants : "Valet", "Dame", "Roi", "As")
    """

    def __init__(self, valeur: int, couleur: str) -> None:
        """Constructeur de la classe Carte.

        Args:
            valeur (int): Valeur de la carte (un entier entre 2 et 14)
            couleur (str): Couleur de la carte (un des 4 symboles suivants : "Coeur", "Carreau", "Pique", "Trèfle")
        """
        self.__valeur = valeur
        self.__couleur = couleur
        self.__figure = None
        self.__set_figure(valeur)

    def get_valeur(self) -> int:
        """Retourne la valeur de la carte.

        Returns:
            int: Valeur de la carte (un entier entre 2 et 14)
        """
        return self.__valeur

    def get_couleur(self) -> str:
        """Retourne la couleur de la carte.

        Returns:
            str: Couleur de la carte (un des 4 symboles suivants : "Coeur", "Carreau", "Pique", "Trèfle")
        """
        return self.__couleur

    def get_figure(self) -> str:
        """Retourne la figure de la carte.

        Returns:
            str: Figure de la carte
        """
        return self.__figure

    def __set_figure(self, valeur: int) -> None:
        """Méthode privée pour définir la figure de la carte.

        Args:
            valeur (int): Valeur de la carte (un entier entre 2 et 14)
        """
        if valeur == 11:
            self.__figure = "Valet"
        elif valeur == 12:
            self.__figure = "Dame"
        elif valeur == 13:
            self.__figure = "Roi"
        elif valeur == 14:
            self.__figure = "As"
        else:
            self.__figure = str(valeur)

    def set_valeur(self, valeur: int) -> bool:
        """Définit la valeur de la carte.

        Args:
            valeur (int): Valeur de la carte (un entier entre 2 et 14)

        Returns:
            bool: True si la valeur est correcte, False sinon
        """
        if 2 <= valeur <= 14:
            self.__valeur = valeur
            self.__set_figure(valeur)
            return True
        else:
            return False

    def set_couleur(self, couleur: str) -> bool:
        """Définit la couleur de la carte.

        Args:
            couleur (str): Couleur de la carte (un des 4 symboles suivants : "Coeur", "Carreau", "Pique", "Trèfle")

        Returns:
            bool: True si la couleur est correcte, False sinon
        """
        if couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:
            self.__couleur = couleur
            return True
        else:
            return False
