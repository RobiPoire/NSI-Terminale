"""
Hanoi Project - Tkinter discs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fichier contenant les fonctions pour l'affichage des disques.
"""

__author__ = "HabibLebsir, devnatiofrance"

# Importation des modules
from tkinter import *
from random import randint


class Disc:

    def __init__(self, discNumber: int, name: int, rowX: int, rowY: int, size: int, Discs: list, canva: Canvas) -> None:
        """
        Cette méthode est le constructeur de la classe Disc.

        Args:
          name (int): Le numéro du disque.
          rowX (int): La tour sur laquelle se trouve le disque.
          rowY (int): La coordonnée y de la rangée sur laquelle se trouve le disque.
          size (int): La taille du disque.
          Discs (list): La liste des disques.
          canva (Canvas): La toile sur laquelle le disque sera dessiné
        """
        self.discNumber = discNumber
        self.name = name
        self.rowX = rowX
        self.rowY = rowY
        self.size = size
        self.canva = canva
        self.Discs = Discs
        self.sizeDiscWidth = 20
        self.sizeDiscHeight = 20
        self.setColor()
        self.drawDisc()

    def __fromRGB(self, color: tuple) -> str:
        """
        Cette méthode permet de convertir une couleur RGB en une couleur hexadécimale.

        Args:
          color (tuple): La couleur à convertir.

        Returns:
          Une chaîne hexadécimale.
        """
        return "#%02x%02x%02x" % color

    def setColor(self) -> None:
        """
        Cette méthode permet de définir la couleur du disque.
        """
        self.color = self.__fromRGB(
            (randint(0, 255), randint(0, 255), randint(0, 255)))

    def drawDisc(self):
        """
        Cette méthode permet de dessiner le disque.
        """
        spaceBetweenTowers = 10
        centerConstant = (self.canva.winfo_width(
        ) - (self.sizeDiscWidth * len(self.Discs) + spaceBetweenTowers) * 3) / 2
        centerDiscConstant = (self.sizeDiscWidth *
                              (self.discNumber - self.size)) / 2
        self.X = (self.sizeDiscWidth + spaceBetweenTowers) * \
            len(self.Discs) * self.rowX + centerConstant + centerDiscConstant
        self.Y = (self.rowY + len(self.Discs)) * self.sizeDiscHeight
        self.cX = self.X + self.sizeDiscWidth * self.size
        self.cY = self.Y + self.sizeDiscHeight
        self.canva.create_rectangle(
            self.X, self.Y, self.cX, self.cY, fill=self.color)

    def move(self, stemList: list, stem: str):
        """
        Cette méthode permet de déplacer le disque.

        Args:
          stemList (list): La liste des disques sur la tige.
          stem (str): La tige sur laquelle se trouve actuellement le disque.
        """
        for i in range(len(stemList)):
            if stemList[i] == self.name:  # Si le disque est sur la tige
                self.rowY = (len(self.Discs) - len(stemList)) + \
                    i  # On défini la rangée

        if stem == "A":  # Si la tige est A
            self.rowX = 0  # On défini la colonne
        elif stem == "B":  # Si la tige est B
            self.rowX = 1  # On défini la colonne
        elif stem == "C":  # Si la tige est C
            self.rowX = 2  # On défini la colonne
