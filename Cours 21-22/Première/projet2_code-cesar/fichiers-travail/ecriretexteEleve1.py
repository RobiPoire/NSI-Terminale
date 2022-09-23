# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:32:56 2020

@author: jeanluc.chastel
"""


fichier="texteEcrire1.txt"
fichier = open(fichier, "w")
fichier.write("nouveau texte 1")
fichier.close()