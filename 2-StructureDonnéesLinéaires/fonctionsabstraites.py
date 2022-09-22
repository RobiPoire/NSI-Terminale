class Lists:
    def __init__(self, size: int) -> None:
        """
        *** Cette méthode est le constructeur de la classe Lists ***

        arguments:
            size: int --> La taille de la liste
        """
        if size < 1:
            raise ValueError("n doit être supérieur à 0")
        self.size = size
        self.lists = [0] * (self.size + 1)

    def __str__(self) -> str:
        """
        *** Cette méthode est declenché au moment où l'on affiche la liste ***

        returns:
            str --> La chaîne de texte à afficher
        """
        return f"{self.lists}"

    def insert(self, element: int, index: int) -> None:
        """
        *** Cette méthode permet d'insérer un élément dans la liste à l'index choisi ***

        arguments:
            element: int --> L'élément à insérer
            index: int --> L'index choisi pour y insérer l'élément
        """
        if index == 0:
            raise IndexError(
                "L'index 0 est réservé pour la longueur de la liste")
        if self.is_full():
            raise IndexError("Liste pleine")
        self.lists[0] += 1
        self.lists[index] = element

    def delete(self, index: int) -> None:
        """
        *** Cette méthode permet de supprimer un élément dans la liste à l'index choisi ***

        arguments:
                index: int --> L'index choisi pour y supprimer l'élément
        """
        if index == 0:
            raise IndexError(
                "L'index 0 est réservé pour la longueur de la liste")
        if self.is_empty():
            raise IndexError("Liste vide")
        self.lists[0] = self.lists[0] - 1
        for a in range(index + 1, self.size + 1):
            self.lists[a-1] = self.lists[a]

    def search(self, element: int) -> int:
        """
        *** Cette méthode permet de rechercher un élément choisi ***

        arguments:
            element: int --> L'élément à rechercher

        returns:
            int --> L'index de l'élément recherché
        """
        for position in range(1, self.length()+1):
            if self.lists[position] == element:
                return position
        raise ValueError("L'élément n'est pas dans la liste")

    def read(self, index: int) -> int:
        """
        *** Cette méthode permet de lire un élément dans la liste à l'index choisi ***

        arguments:
            index: int --> L'index choisi pour y lire l'élément

        returns:
            int --> L'élément à l'index choisi
        """
        if index == 0:
            raise IndexError(
                "L'index 0 est est réservé pour la longueur de la liste")
        return self.lists[index]

    def change(self, index: int, element: int) -> None:
        """
        *** Cette méthode permet de modifier un élément dans la liste à l'index choisi ***

        arguments:
            index: int --> L'index choisi pour y modifier l'élément
            element: int --> L'élément à modifier

        returns:
            int --> L'élément à l'index choisi
        """
        if index == 0:
            raise IndexError(
                "L'index 0 est est réservé pour la longueur de la liste")
        self.lists[index] = element

    def length(self) -> int:
        """
        *** Cette méthode retourne la longueur de la liste ***

        returns:
            int --> La longueur de la liste
        """
        return self.lists[0]
    
    def is_empty(self) -> bool:
        """
        *** Cette méthode permet de savoir si la liste est vide ***

        returns:
            bool --> True si la liste est vide, False sinon
        """
        return self.length() == 0
    
    def is_full(self) -> bool:
        """
        *** Cette méthode permet de savoir si la liste est pleine ***

        returns:
            bool --> True si la liste est pleine, False sinon
        """
        return self.lists[0] == self.size

class Piles:
    def __init__(self, size: int):
        """
        *** Cette méthode est le constructeur de la classe Piles ***

        arguments:
            size: int --> La taille de la pile
        """
        self.size = size
        self.piles = [0] * (self.size + 1)
        self.piles[0] = 1
    
    def __str__(self) -> str:
        """
        *** Cette méthode est declenché au moment où l'on affiche la pile ***

        returns:
            str --> La chaîne de texte à afficher
        """
        return f"{self.piles}"
    
    def stack(self, element: int) -> None:
        """
        *** Cette méthode permet d'empiler un élément dans la pile ***

        arguments:
            element: int --> L'élément à empiler
        """
        if self.is_full():
            raise IndexError("Pile pleine")
        self.piles[self.piles[0]] = element
        self.piles[0] = self.piles[0] + 1

    def unstack(self) -> int:
        """
        *** Cette méthode permet de dépiler un élément dans la pile ***

        returns:
            int --> L'élément dépiler
        """
        if self.is_empty():
            raise IndexError("Pile vide")
        element = self.piles[self.piles[0] - 1]
        self.piles[self.piles[0] - 1] = 0
        self.piles[0] = self.piles[0] - 1
        return(element)
    
    def is_empty(self) -> bool:
        """
        *** Cette méthode permet de savoir si la pile est vide ***

        returns:
            bool --> True si la pile est vide, False sinon
        """
        return self.piles[0] == 1
    
    def is_full(self) -> bool:
        """
        *** Cette méthode permet de savoir si la pile est pleine ***

        returns:
            bool --> True si la pile est pleine, False sinon
        """
        return self.piles[0] == self.size + 1

class Files:
    def __init__(self, size: int) -> None:
        """
        *** Cette méthode est le constructeur de la classe Files ***
 
        arguments:
            size: int --> La taille de la file
        """
        self.size = size
        self.files = [0] * (self.size + 3)
        self.files[0] = 3
        self.files[1] = 3
    
    def __str__(self) -> str:
        """
        *** Cette méthode est declenché au moment où l'on affiche la file ***
 
        returns:
            str --> La chaîne de texte à afficher
        """
        return f"{self.files}"
    
    def thread(self, element: int) -> None:
        """
        *** Cette méthode permet d'enfiler un élément dans la file ***
 
        arguments:
            element: int --> L'élément à enfiler
        """
        if self.is_full():
            raise IndexError(
                f"La file est pleine, impossible d'enfiler '{element}' (taille max: {self.size})")
        file = self.files[1]
        self.files[file] = element
        self.files[2] = self.files[2] + 1
        if self.files[1] == self.size + 2:
            self.files[1] = 3
        else:
            self.files[1] = self.files[1] + 1
    
    def unthread(self) -> int:
        """
        *** Cette méthode permet de défiler un élément dans la file ***
     
        returns:
            int --> L'élément défilé
        """
        if self.is_empty():
            raise IndexError("La file est vide, impossible de défiler un élément")
        element = self.files[self.files[0]]
        self.files[self.files[0]] = 0
        self.files[2] = self.files[2] - 1
        if self.files[0] == self.size + 2:
            self.files[0] = 3
        else:
            self.files[0] = self.files[0] + 1
        return(element)

    def is_empty(self) -> bool:
        """
        *** Cette méthode permet de savoir si la file est vide ***
 
        returns:
            bool --> True si la file est vide, False sinon
        """
        return self.files[2] == 0
    
    def is_full(self) -> bool:
        """
        *** Cette méthode permet de savoir si la file est pleine ***
 
        returns:
            bool --> True si la file est pleine, False sinon
        """
        return self.files[2] == self.size
