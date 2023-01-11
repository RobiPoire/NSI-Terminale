import bisect
import networkx as nx
import matplotlib.pyplot as plt


class ArbreHuffman:
    def __init__(self, lettre: str = None, nbocc: int = 0, g: 'ArbreHuffman' = None, d: 'ArbreHuffman' = None) -> None:
        """ Constructeur de la classe ArbreHuffman

        Args:
            lettre (str, optional): Lettre de l'arbre. Par défaut None.
            nbocc (int, optional): Nombre d'occurences de la lettre. Par défaut 0.
            g (ArbreHuffman, optional): Arbre de gauche. Par défaut None.
            d (ArbreHuffman, optional): Arbre de droiteµ. Par défaut None.
        """
        self.lettre = lettre  # La lettre de l'arbre
        self.nbocc = nbocc  # Le nombre d'occurences de la lettre
        self.gauche = g  # L'arbre de gauche
        self.droite = d  # L'arbre de droite

    def est_feuille(self) -> bool:
        """Renvoie True si l'arbre est une feuille, False sinon

        Returns:
            bool: True si l'arbre est une feuille, False sinon
        """
        return self.gauche is None and self.droite is None

    def __lt__(self, other: 'ArbreHuffman') -> bool:
        """Permet de comparer deux arbres de Huffman

        Args:
            other (ArbreHuffman): Arbre de Huffman à comparer

        Returns:
            bool: True si l'arbre est inférieur à l'autre, False sinon
        """
        try:
            return self.nbocc > other.nbocc
        except TypeError:
            return False


def parcours(arbre: ArbreHuffman, chemin_en_cours: list, dico: dict) -> None:
    """Parcours en profondeur d'un arbre de Huffman"""
    # On vérifie que l'arbre n'est pas None
    if arbre is None:
        raise ValueError("L'arbre ne peut pas être None")
    # Si on est sur une feuille, on ajoute l'élément à notre dictionnaire
    if arbre.est_feuille():
        dico[arbre.lettre] = chemin_en_cours
    # Sinon, on parcours récursivement en allant à gauche
    else:
        parcours(arbre.gauche, chemin_en_cours + [0], dico)
        # On parcours à droite
        parcours(arbre.droite, chemin_en_cours + [1], dico)


def fusionne(gauche: ArbreHuffman, droite: ArbreHuffman) -> ArbreHuffman:
    """Fusionne deux arbres de Huffman en un seul

    Args:
        gauche (ArbreHuffman): Arbre de gauche
        droite (ArbreHuffman): Arbre de droite

    Returns:
        ArbreHuffman: Arbre fusionné
    """
    nbocc_total = gauche.nbocc + droite.nbocc
    return ArbreHuffman(None, nbocc_total, gauche, droite)


def compte_occurrences(texte: str) -> dict:
    """Compte le nombre d'occurences de chaque lettre dans un texte

    Args:
        texte (str): Texte à analyser

    Returns:
        dict: Dictionnaire contenant les lettres et leur nombre d'occurences
    """
    # Initialise le dictionnaire qui va contenir le résultat
    occ = dict()
    # Parcours le texte caractère par caractère
    for c in texte:
        # Si le caractère est déjà dans le dictionnaire
        if c in occ:
            # Incrémente le nombre d'occurences
            occ[c] += 1
        else:
            # Sinon l'ajoute avec un compteur à 1
            occ[c] = 1
    # Retourne le résultat
    return occ


def construit_liste_arbres(texte: str) -> list:
    """Construit une liste d'arbres de Huffman à partir d'un texte

    Args:
        texte (str): Texte à analyser

    Returns:
        list: Liste d'arbres de Huffman
    """
    # On compte les occurrences de chaque lettre dans le texte
    dic_occurrences = compte_occurrences(texte)
    liste_arbres = []
    # On crée un arbre de Huffman pour chaque lettre
    for lettre, nbocc in dic_occurrences.items():
        liste_arbres.append(ArbreHuffman(lettre, nbocc))
    return liste_arbres


def codage_huffman(texte: str) -> dict:
    """Codage d'un texte en utilisant l'algorithme de Huffman

    Args:
        texte (str): Texte à coder

    Returns:
        dict: Dictionnaire contenant les lettres et leur code
    """
    if not isinstance(texte, str):
        raise TypeError("Le texte doit être une chaîne de caractères")
    liste_arbres = construit_liste_arbres(texte)
    # Tri par nombres d’occurrences décroissants
    liste_arbres.sort()
    # Tant que tous les arbres n’ont pas été fusionnés
    while len(liste_arbres) > 1:
        # Les deux plus petits nombres d’occurrences
        # sont à la fin de la liste
        arbre1 = liste_arbres.pop()
        arbre2 = liste_arbres.pop()
        new_arbre = fusionne(arbre1, arbre2)
        # Le module bisect permet d’insérer le nouvel
        # arbre dans la liste, de manière à ce que la
        # liste reste triée
        bisect.insort(liste_arbres, new_arbre)
    # Il ne reste plus qu’un arbre dans la liste,
    # c’est notre arbre de Huffman
    arbre_huffman = liste_arbres.pop()
    # Parcours de l’arbre pour relever les codes
    dico = {}
    parcours(arbre_huffman, [], dico)
    return dico


def ecriture_texte_avec_huffman(texte: str, dico: dict) -> str:
    """Ecriture d'un texte en utilisant l'algorithme de Huffman

    Args:
        texte (str): Texte à coder
        dico (dict): Dictionnaire contenant les lettres et leur code

    Returns:
        str: Texte codé
    """
    texte_code = ""
    for c in texte:
        if c in dico:
            # On vérifie que la lettre est dans le dictionnaire
            # On ajoute le code correspondant au texte codé
            texte_code += "".join(str(x) for x in dico[c])
    return texte_code


def decode_huffman(texte_code: str, dico: dict) -> str:
    """Décodage d'un texte codé par huffman.

    Le texte est découpé en codes (chaînes de 0 et de 1) qui sont 
    remplacés par les caractères correspondants.

    Arguments:
        texte_code (str): texte codé par huffman
        dico (dict): dictionnaire des codes, avec comme clé les caractères
                     et comme valeur les codes correspondants

    Retourne:
        str: texte décodé
    """
    texte = ""
    # Inverse le dictionnaire de codes pour obtenir un dictionnaire
    # avec comme clé les codes et comme valeur les caractères correspondants
    dico_inverse = {"".join(str(x) for x in v): k for k, v in dico.items()}
    i = 0
    while i < len(texte_code):
        # Parcourt les codes du texte de la longueur maximale possible
        # (jusqu'à la longueur du texte) en les cherchant dans le dictionnaire
        for j in range(len(texte_code), i, -1):
            code = texte_code[i:j]
            if code in dico_inverse:
                # Si un code est trouvé, il est remplacé par le caractère
                # correspondant et on passe au code suivant
                texte += dico_inverse[code]
                i = j
                break
        else:
            # Si aucun code n'est trouvé, c'est que le texte est invalide
            raise Exception(f"Code invalide à la position {i}")
    return texte


with open("texte.txt") as f:
    texte = f.read()
code = codage_huffman(texte)

print("Texte original :")
print(texte)
print("Texte codé :")
print(ecriture_texte_avec_huffman(texte, code))
print("Texte décodé :")
print(decode_huffman(ecriture_texte_avec_huffman(texte, code), code))
