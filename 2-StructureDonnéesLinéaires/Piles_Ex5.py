"""
Les piles - Exercice 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
On ne considère ici que les expressions numériques contenant les quatre opérations 
élémentaires ( +, -, *, / ). 
La notation postfixée, appelée aussi Notation Polonaise Inversée (NPI), consiste à mettre les 
opérations arithmétiques après leurs arguments. 
Par exemple, l'expression 5 + 3 s'écrit :  5 3 +  en NPI. 
L'avantage, c'est que la NPI se passe complètement de parenthèses. Par exemple, l'expression 
3*((4 + 5) - 6) peut s'écrire en NPI : 3 4 5 + 6 - *. 
On se propose de se servir d'une pile pour calculer une expression arithmétique exprimée en 
NPI. 
Les données sont lues comme une suite de caractères. Chaque donnée est séparée des autres 
par un espace. La méthode consiste à utiliser une pile pour conserver les valeurs numériques 
au fur et à mesure de leur lecture (de la gauche vers la droite), et à effectuer un traitement 
quand un opérateur est lu. Ce traitement doit dépiler les deux dernières valeurs présentes 
dans la pile, effectuer l'opération, puis empiler le résultat dans la pile.  
Il faut être attentif ici à l'ordre des opérandes dans le cas des opérateurs non commutatifs ( - 
et / ). 
Le résultat final est contenu dans la pile. 
 
1. Ecrire un algorithme utilisant une pile pour effectuer un calcul en NPI. 
2. Implémenter cet algorithme en Python en définissant une fonction calcul(E) où E est 
l'expression en NPI, écrite sous forme d'une chaine de caractères dans laquelle chaque nombre 
ou symbole est séparé par un espace. 
"""

__author__ = "RobiPoire"


def calcul(E: str) -> float:
    """Calcule une expression arithmétique exprimée en NPI

    Args:
        E (str): L'expression en NPI

    Returns:
        float: Le résultat de l'expression
    """
    P = []
    for i in E.split():
        if i == "+":
            P.append(P.pop() + P.pop())
        elif i == "-":
            P.append(-P.pop() + P.pop())
        elif i == "*":
            P.append(P.pop() * P.pop())
        elif i == "/":
            P.append(1 / P.pop() * P.pop())
        else:
            P.append(float(i))
    return P[0]

#! Exemple d'utilisation


# Test 1 : 5+3 = 8
print(calcul("5 3 +"))

# Test 2 : 3*((4+5)-6) = 9
print(calcul("3 4 5 + 6 - *"))
