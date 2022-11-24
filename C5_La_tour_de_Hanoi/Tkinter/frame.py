# Importation des modules
from tkinter import *
from discs import Disc


class Frame:
    # Utilisation de variables globales
    global Discs
    Discs = []

    def __init__(self, size: tuple, title: str, backgroundColor: str):
        """
        Cette méthode est le constructeur de la classe Frame.
        
        Args:
          size (tuple): La taille de la fenêtre.
          title (str): Le titre de la fenêtre.
          backgroundColor (str): La couleur du fond.
        """
        self.width = size[0]
        self.height = size[1]
        self.title = title
        self.backgroundColor = backgroundColor
        self.x = 0
        self.y = 0
        self.isRunning = True
        self.forward = True
        self.backward = True
        self.pause = True
        self.sizeItterations = 0

    def create(self):
        """
        Cette méthode permet de créer la fenêtre.
        """
        self.frame = Tk() # Création de la fenêtre
        self.frame.protocol("WM_DELETE_WINDOW", self.onClose) # Définition d'un protocole de fermeture de la fenêtre
        self.frame.title(self.title) # Définition du titre de la fenêtre
        self.frame.geometry(f"{self.width}x{self.height}") # Définition de la taille de la fenêtre
        self.frame.configure(background = self.backgroundColor) # Définition de la couleur de fond
        self.frame.update() # Mise à jour de la fenêtre
    
    def clavier_right(self, event):
        """
        Cette méthode permet de déterminer si une touche du clavier est enfoncée.
        
        Args:
          event: L'événement qui a déclenché cette fonction.
        """
        self.forward = False
        self.pause = False
    
    def clavier_left(self, event):
        """
        Cette méthode permet de déterminer si une touche du clavier est enfoncée.
        
        Args:
          event: L'événement qui a déclenché cette fonction.
        """
        self.backward = False
        self.pause = False

    def changeSize(self):
        """
        Cette méthode permet d'adapter les objets de la fenêtre en fonction de sa taille.
        """
        self.width = self.frame.winfo_width() # Récupération de la largeur de la fenêtre
        self.height = self.frame.winfo_height() # Récupération de la hauteur de la fenêtre
        self.canvas.config(width = self.width, height = self.height) # Modification de la taille du canvas
        self.paintComponent() # Mise à jour de la fenêtre

    def paintComponent(self):
        """
        Cette méthode permet de dessiner les disques sur la fenêtre.
        """
        self.canvas.delete("all") # Suppression de tout les objets du canvas
        for disc in Discs: 
            disc.sizeDiscWidth = (200 / len(Discs)) * self.width / 1280 # Définition de la taille du disque en fonction de la taille de la fenêtre
            disc.sizeDiscHeight = (200 / len(Discs)) * self.height / 720 # Définition de la taille du disque en fonction de la taille de la fenêtre
            disc.drawDisc() # Dessiner le disque

    def createCanvas(self, size: tuple, backgroundColor: str):
        """
        Cette méthode permet de créer le canvas.
        
        Args:
          size (tuple): La taille du canvas.
          backgroundColor (str): La couleur de fond de la toile.
        """
        self.canvas = Canvas(
            self.frame, width = size[0], height = size[1], bg = backgroundColor) # Création du canvas
        self.canvas.pack() # Affichage du canvas

    def onClose(self):
        """
        Cette méthode permet de déterminer si la fenêtre est fermée.
        """
        self.isRunning = False
        self.frame.destroy() # Destruction de la fenêtre
