# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:05:11 2020

@author: jeanluc.chastel
"""

fichier="texte.txt"         #Nom du fichier traité
file = open(fichier, "r")   #Ouverture du fichier
for ligne in file:          #Lecture du contenu du fichier
    print(ligne)
file.close()                #Fermeture du fichier
print(type(ligne))          #Affiche le type de variable