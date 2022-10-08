# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:32:56 2020

@author: jeanluc.chastel
"""


fichier="texteEcrire2.txt"
fichier = open(fichier, "a")
fichier.write("nouveau texte 2")
fichier.close()