"""
On ne considère ici que les expressions numériques contenant les quatre opérations 
élémentaires ( +, -, *, / ). 
On souhaite ici convertir une expression arithmétique infixée (avec des parenthèses) en une 
expression postfixée (notation polonaise inversée (NPI), sans parenthèses). 
Par exemple, l'expression infixée : 
 7 * (((13 + 22) – 15) / 5) 
sera traduite en :   
 
  7 13 22 + 15 – 5 / * 
 
Dans l'expression infixée, chaque opération entre deux opérandes sera nécessairement mise 
entre parenthèses, car on ne tiendra pas compte ici de la priorité des opérations les unes sur les 
autres. 
Ainsi, une expression telle que :  
3 * 2 + 4  
sera écrite : (3 * 2) + 4. 
 
Le programme lit l'expression infixée comme une suite de caractères, et range le résultat de la 
conversion dans une file qui s’affichera. 
 
Ce programme utilise une pile (pile_operateurs) pour gérer les opérateurs, et une file 
(file_expression) pour conserver l’expression postfixée. 
 
Les valeurs numériques lues sont directement rangées dans la file, alors que les opérateurs 
sont traités afin d’apparaitre dans la file après leurs opérandes. Ils sont d’abord empilés (mis 
de côtés) dans pile_operateur, puis dépilés pour être rangés dans la file, après que les deux 
opérandes sont enfilées. Cela se produit quand la parenthèse fermante est rencontrée. La file 
contient les différentes valeurs et les opérateurs.  
 
Quand la fin de ligne de l'expression infixée est atteinte, tous les opérateurs qui restent encore 
dans la pile sont dépilés et rangés dans la file. 
 
Pour afficher l'expression postfixée, on défile un par un tous les éléments de la file et on les 
concatène en les séparant par un espace.
"""
__author__ = "RobiPoire"

from Piles_Ex5 import calcul


def conversion(expression: str) -> str:
    """Convertit une expression infixée en une expression postfixée

    Args:
        expression (str): L'expression infixée

    Returns:
        str: L'expression postfixée
    """
    file_expression = []
    pile_operateurs = []
    for caractere in expression:
        if caractere == "(":
            pile_operateurs.append(caractere)
        elif caractere == ")":
            while pile_operateurs[-1] != "(":
                file_expression.append(" ")
                file_expression.append(pile_operateurs.pop())
            pile_operateurs.pop()
        elif est_operateur(caractere):
            pile_operateurs.append(caractere)
        else:
            file_expression.append(caractere)
    while pile_operateurs:
        file_expression.append(" ")
        file_expression.append(pile_operateurs.pop())
    file_expression = "".join(file_expression)
    if "  " in file_expression:
        file_expression = file_expression.replace("  ", " ")
    return file_expression


def est_operateur(caractere: str) -> bool:
    """Vérifie si le caractère est un opérateur

    Args:
        caractere (str): Le caractère à vérifier

    Returns:
        bool: True si le caractère est un opérateur, False sinon
    """
    return caractere in "+-*/"


#! Exemple d'utilisation
# Se lance uniquement si le fichier est exécuté
if __name__ == "__main__":

    # L'expression infixée à convertir
    expression = "7 * (((13 + 22) - 15) / 5)"

    # Conversion de l'expression infixée en une expression postfixée
    expression_postfixee = conversion(expression)
    print(expression_postfixee)

    # Calcul de l'expression postfixée
    print(calcul(expression_postfixee))
