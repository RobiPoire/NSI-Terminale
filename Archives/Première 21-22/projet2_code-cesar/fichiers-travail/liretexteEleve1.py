# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:05:11 2020

@author: jeanluc.chastel
"""

fichier="texte.txt"         #Nom du fichier traité
file = open(fichier, "r")   #Ouverture du fichier
contenu=file.read()         #Lecture du contenu du fichier
file.close()                #Fermeture du fichier
print (contenu)
print(type(contenu))        #Affiche le type de variable