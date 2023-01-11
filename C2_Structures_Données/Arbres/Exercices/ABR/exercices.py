"""
ABR - TP
~~~~~~~~
TP sur les arbres binaires de recherche (ABR)
"""

# Exercice 1


class File:
    def __init__(self: object) -> None:
        """Constructeur de la classe File

        Args:
            self (object): Référence à l'objet courant
        """
        self.__file = []

    def enfiler(self, element: object) -> None:
        """Ajoute un élément à la fin de la file

        Args:
            element (object): Élément à ajouter
        """
        self.__file.append(element)

    def defiler(self) -> object:
        """Retire le premier élément de la file

        Returns:
            object: Élément retiré
        """
        if self.__file:
            return self.__file.pop(0)
        else:
            return None

    def est_vide(self) -> bool:
        """Vérifie si la file est vide

        Returns:
            bool: True si la file est vide, False sinon
        """
        return not self.__file

    def afficher(self) -> None:
        """Affiche la file"""
        print(self.__file)


# Exercice 2
class Arbre:
    def __init__(self, cle: int, gauche: object = None, droite: object = None) -> None:
        """Constructeur de la classe Arbre

        Args:
            cle (int): Noeud de l'arbre
            gauche (object, optional): Fils gauche. None par défaut.
            droite (object, optional): Fils droit. None par défaut.
        """
        self.cle = cle
        self.gauche = gauche
        self.droite = droite

    def __repr__(self) -> str:
        """Affichage de l'arbre

        Returns:
            str: Chaîne de caractères représentant l'arbre
        """
        return f"Arbre({self.cle}, {self.gauche}, {self.droite})"


def parcours_largeur(arbre: object) -> list:
    """Parcours en largeur d'un arbre

    Args:
        arbre (object): Arbre à parcourir

    Returns:
        list: Liste des noeuds parcourus
    """
    resultats = []
    if arbre:
        file = File()
        file.enfiler(arbre)
        while not file.est_vide():
            noeud = file.defiler()
            resultats.append(noeud.cle)
            if noeud.gauche:
                file.enfiler(noeud.gauche)
            if noeud.droite:
                file.enfiler(noeud.droite)
    return resultats

# Exercice 3
# 1


def inserer(T: object, val: int) -> None:
    """Insère une valeur dans un arbre binaire de recherche

    Args:
        T (object): Arbre binaire de recherche
        val (int): Valeur à insérer
    """
    if val < T.cle:
        if T.gauche == None:
            T.gauche = Arbre(val)
        else:
            inserer(T.gauche, val)
    else:
        if T.droite == None:
            T.droite = Arbre(val)
        else:
            inserer(T.droite, val)


# 2

def creer_abr(pl: list) -> object:
    """Crée un arbre binaire de recherche à partir d'une liste

    Args:
        pl (list): Liste de valeurs

    Returns:
        object: Arbre binaire de recherche
    """
    T = Arbre(pl[0])
    for i in range(1, len(pl)):
        inserer(T, pl[i])
    return T


# 3
def minimum_recursif(T: object) -> int:
    """Retourne la valeur minimale d'un arbre binaire de recherche

    Args:
        T (object): Arbre binaire de recherche

    Returns:
        int: Valeur minimale
    """
    if T.gauche == None:
        return T.cle
    else:
        return minimum_recursif(T.gauche)


def minimum_non_recursif(T: object) -> int:
    """Retourne la valeur minimale d'un arbre binaire de recherche

    Args:
        T (object): Arbre binaire de recherche

    Returns:
        int: Valeur minimale
    """
    while T.gauche != None:
        T = T.gauche
    return T.cle

# Exercice 4

# 1


def est_feuille(T: object) -> bool:
    """Vérifie si un noeud est une feuille

    Args:
        T (object): Noeud à vérifier

    Returns:
        bool: True si le noeud est une feuille, False sinon
    """
    return T.gauche == None and T.droite == None


# 2
def afficher_feuilles(T: object) -> None:
    """Affiche les feuilles d'un arbre binaire de recherche

    Args:
        T (object): Arbre binaire de recherche
    """
    if T:
        if est_feuille(T):
            print(T.cle)
        else:
            afficher_feuilles(T.gauche)
            afficher_feuilles(T.droite)


if __name__ == "__main__":
    T = [50, 17, 72, 12, 23, 54, 76, 9, 14, 19, 67]
    A = creer_abr(T)
    print("Parcours en largeur : ", parcours_largeur(A))
    print("Minimum : ", minimum_recursif(A))
    print("Feuilles : ")
    afficher_feuilles(A)
    # test insertion
    inserer(A, 5)
    print(A)
    print("Parcours en largeur : ", parcours_largeur(A))
    print("Minimum : ", minimum_recursif(A))
    print("Feuilles : ")
    afficher_feuilles(A)
