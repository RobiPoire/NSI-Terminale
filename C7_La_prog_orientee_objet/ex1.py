"""
Les classes - Exercice 1
~~~~~~~~~~~~~~~~~~~~~~~~
Création d'une classe Personne
"""

__author__ = "RobiPoire"      


class Personne:
    def __init__(self, annee: int, poids: int, taille: int) -> None:
        """Constructeur de la classe Personne

        Args:
            annee (int): année de naissance
            poids (int): poids en kg
            taille (int): taille en cm
        """
        self.annee = annee
        self.poids = poids
        self.taille = taille
        self.__set_statut()

    def __set_statut(self) -> None:
        """Méthode privée qui affecte à la variable d'instance self.__statut le 
        statut de l'objet, à savoir "Majeur" ou "Mineur" selon son année de naissance.
        """
        if 2022 - self.annee < 18:
            self.statut = "Mineur"
        else:
            self.statut = "Majeur"

    def get_statut(self: object) -> str:
        """Méthode qui renvoie le statut de l'objet.

        Returns:
            str: statut de l'objet
        """
        return self.statut

    def __str__(self) -> str:
        """Méthode qui renvoie une chaîne de caractères décrivant l'objet.

        Returns:
            str: chaîne de caractères décrivant l'objet
        """
        return f"Personne de {2022 - self.annee} ans, de {self.poids} kg et de {self.taille} cm."


# Exemple d'utilisation
if __name__ == "__main__":
    habib = Personne(2006, 50, 150)
    print(f"Habib, {habib}")
    print(f"Habib est {habib.get_statut()}.")
