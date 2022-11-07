from tkinter import *

root = Tk()
root.title("La tour de Hanoi")
root.geometry("500x500")
root.resizable(width = True, height = True)

root.update()
# Récupére la largeur
widthRoot = root.winfo_width() 
# Récupére la hauteur
heightRoot = root.winfo_height()

# Création d'un canevas
canevas = Canvas(root, width = 500, height = 500, bg = "white")
canevas.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Quitter)
Button(root, text = "Quitter", command = root.destroy).pack(side = BOTTOM)

# Création des 3 tours
canevas.create_rectangle(10, 10, 30, 500, fill = "brown")
canevas.create_rectangle(240, 10, 260, 500, fill = "brown")
canevas.create_rectangle(470, 10, 490, 500, fill = "brown")

# Création des 3 disques
canevas.create_rectangle(10, 480, 110, 500, fill = "red")
canevas.create_rectangle(10, 460, 90, 480, fill = "blue")
canevas.create_rectangle(10, 440, 70, 460, fill = "green")


root.mainloop()